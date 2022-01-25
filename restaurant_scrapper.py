# -*- coding: utf-8 -*-
"""Restaurant_Scrapper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Oks4Gmu2tdzbKCxK7eL1rJLHtwI-HpbT

# Libraries
---
"""

!pip install python-google-places

from googleplaces import GooglePlaces, types, lang
import time
import pandas as pd

"""# Location Dataset 
---
This dataset contains the list of Upazilla/Thana for Different Districts of Bangladesh.

Credit : [Mobile network coverage in Bangladeshi Upazila or Thana - kaggle](https://www.kaggle.com/mushfiqurrobin/network-coverage)
"""

!mkdir ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d mushfiqurrobin/network-coverage

!mkdir network-coverage
!unzip network-coverage.zip -d network-coverage

df = pd.read_csv("/content/network-coverage/Coverage.csv")

df_area = df[['Upazila_or_Thana', 'District']]

# Checking For Missing Values
total = df_area.isnull().sum().sort_values(ascending=False)
percent = (df_area.isnull().sum()/df_area.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent*100], axis=1, keys=['Total', 'Percent'])
display(missing_data.head(5))

# Checking for Duplicate Rows 
df_area.duplicated().sum()

# Dropping Duplicates
df_area.drop_duplicates(keep="first", inplace=True)
df_area.reset_index(drop=True, inplace=True)

df_area.to_csv("locations.csv", index=False)

"""# Initialization
---
Here, I am combining the Upazilla/Thana and its dedicated District into a string and storing them into ``` locations``` list. Later I will use this list for the searching query.

I have also intialized the searching ``` radius ``` to 2000 Meter or 2 KM. 

Finally, I will store the Restaurants' information into ```restaurant_data``` 


"""

API_KEY = "YOUR API KEY"

google_places = GooglePlaces(API_KEY)

restaurant_data = []
radius = 2000

# Converting the list of Upazilla/Thana and District into a combined string
locations = []
list_areas = df_area.values.tolist()

for area in list_areas:
  location_name = ', '.join([str(item) for item in area])
  locations.append(location_name)

print(locations)

"""# Restaurant Scraper 

---


"""

for location in locations:
  print("---------------------", location, "-----------------------")
  query_result = google_places.nearby_search(
          location=location, keyword='Restaurant',
          radius=radius) 

  if query_result:
  
    for place in query_result.places:
      place.get_details()

      place_id = place.details.get('place_id')
      name = place.name
      latitude = place.geo_location.get('lat')
      longitude = place.geo_location.get('lng')
      rating = place.rating
      number_of_reviews = place.details.get('user_ratings_total')
      affluence = place.details.get('price_level')
      address = place.formatted_address

      restaurant_data.append([place_id, name, latitude, longitude, rating, number_of_reviews, affluence, address])
      # print(place.details)

    # print(restaurant_data)
    print("--------------------- Scrapped Restaurants: ", len(restaurant_data))
    time.sleep(5) 

    while query_result.has_next_page_token:
        query_result = google_places.nearby_search(location=location, keyword='Restaurant',
            radius=radius, pagetoken=query_result.next_page_token)
        
        for place in query_result.places:
          place.get_details()

          place_id = place.details.get('place_id')
          name = place.name
          latitude = place.geo_location.get('lat')
          longitude = place.geo_location.get('lng')
          rating = place.rating
          number_of_reviews = place.details.get('user_ratings_total')
          affluence = place.details.get('price_level')
          address = place.formatted_address

          restaurant_data.append([place_id, name, latitude, longitude, rating, number_of_reviews, affluence, address])
          # print(place.details)
        # print(restaurant_data)  
        print("--------------------- Scrapped Restaurants: ", len(restaurant_data))
        time.sleep(5) 

  time.sleep(5)

# Dumping the data into a DataFrame
df_restaurant = pd.DataFrame(restaurant_data, columns=['place_id', 'name', 'latitude', 'longitude', 'rating', 'number_of_reviews', 'affluence', 'address'])

df_restaurant.to_csv("restaurants.csv", index=False, encoding='utf-8')

"""# Data Preparation

---

"""

restaurant_df = pd.read_csv("/content/restaurants.csv", encoding='utf-8')

display(restaurant_df.duplicated().sum())

"""**There are 1945 Duplicate Data present in the dataframe.**"""

restaurant_df.drop_duplicates(keep="first", inplace=True)

"""**Here, I kept the address of each restaurant to check whether they are in Bangladeh or Not. As we can see below, 62 restaurants are in India.**"""

res_not_bangladesh = restaurant_df[restaurant_df['address'].str.contains('Bangladesh')==False]
res_not_bangladesh

restaurant_df = restaurant_df[restaurant_df['address'].str.contains('Bangladesh')==True]
restaurant_df.reset_index(drop=True, inplace=True)

"""**Now the dataframe ```restaurant_df``` contains only Bangladeshi restaurants.**"""

def missing_value_describe(data):
    # check missing values in the data
    total = data.isna().sum().sort_values(ascending=False)
    missing_value_pct_stats = (data.isnull().sum() / len(data)*100)
    missing_value_col_count = sum(missing_value_pct_stats > 0)

    # missing_value_stats = missing_value_pct_stats.sort_values(ascending=False)[:missing_value_col_count]
    missing_data = pd.concat([total, missing_value_pct_stats], axis=1, keys=['Total', 'Percent'])

    print("Number of rows with at least 1 missing values:", data.isna().any(axis = 1).sum())
    print("Number of columns with missing values:", missing_value_col_count)

    if missing_value_col_count != 0:
        # print out column names with missing value percentage
        print("\nMissing percentage (desceding):")
        display(missing_data[:missing_value_col_count])

        # plot missing values
        missing = data.isnull().sum()
        missing = missing[missing > 0]
        missing.sort_values(inplace=True)
        missing.plot.bar()
    else:
        print("No missing data!!!")

# pass a dataframe to the function
missing_value_describe(restaurant_df)

"""**Converting the Affluence Level ```1.0, 2.0, 3.0...``` to ```$, $$, $$$...```**"""

restaurant_df['affluence'] = restaurant_df['affluence'].replace([1.0, 2.0, 3.0, 4.0],['$', '$$', '$$$', '$$$$'])
restaurant_df[restaurant_df['affluence'].notna()==True]

"""**Saving the final dataframe into CSV**"""

final_df = restaurant_df[['name',	'latitude',	'longitude',	'rating',	'number_of_reviews',	'affluence']]

final_df.to_csv("bangladesh_restaurants.csv", index=False, encoding='utf-8')

"""# Remarks


---

**The dataset may contain some anomalies such as Tea Stores or Food Stores that are also registered under Restaurant keyword. More extensive cleaning can be done to handle such issues in the future.**

"""