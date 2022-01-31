# Scraping Bangladeshi Restaurants from GoogleMaps
---

[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?logo=Jupyter)](https://jupyter.org/try) [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/tanjimanasreen/GoogleMaps-Restaurant-Scraper/blob/main/Restaurant_Scrapper.ipynb) [![Open in HTML](https://img.shields.io/badge/Html-Open%20Notebook-blue?logo=HTML5)](https://nbviewer.org/github/tanjimanasreen/GoogleMaps-Restaurant-Scraper/blob/main/Restaurant_Scrapper.html)

## Summary

In this project I created a scraper in python using Google Places API to scrap Restaurants' information from all over Bangladesh. Moreover added some visualizations according to their ratings, reviews and price level.

## About Dataset
There are two versions of Dataset here
- [Raw Restaurant Dataset](https://github.com/tanjimanasreen/GoogleMaps-Restaurant-Scraper/tree/main/Dataset/Restaurant-Raw) : This contains the place ID, name logitude, latitude, ratings, number of reviews and price level and address of each restaurant. Some of the restaurants may not be in Bangladeshi borders.
- [Final Bangladeshi Restaurant Dataset](https://github.com/tanjimanasreen/GoogleMaps-Restaurant-Scraper/tree/main/Dataset/Restaurant-FInal) : This contains name, logitude, latitude, ratings, number of reviews and price level of each restaurant. All of the restaurants are inside Bangladesh.


## Prerequisite
- A Google API key with Google Places API Web Service and Google Maps Geocoding API activated against it. Check [Google Places API](https://developers.google.com/maps/documentation/places/web-service/overview) for more details

- A location list of every Upazilla/Thana along with its District of Bangladesh. In my case I used [Mobile network coverage in Bangladeshi Upazila or Thana](https://www.kaggle.com/mushfiqurrobin/network-coverage) from kaggle to collect the locations around Bangladesh. Here you can see my collected [location](https://github.com/tanjimanasreen/GoogleMaps-Restaurant-Scraper/blob/main/Dataset/locations.csv) list.  

## Preview 
### Most Popular Restaurant Names
![](https://github.com/tanjimanasreen/GoogleMaps-Restaurant-Scraper/blob/main/files/English_word_cloud.png)

### Restaurant Heat Map
![](https://github.com/tanjimanasreen/GoogleMaps-Restaurant-Scraper/blob/main/files/heatmap.png)

### Mostly Reviewed Restaurants' Area
![](https://github.com/tanjimanasreen/GoogleMaps-Restaurant-Scraper/blob/main/files/circlemap.png)

### Expensive Restaurants' Area
![](https://github.com/tanjimanasreen/GoogleMaps-Restaurant-Scraper/blob/main/files/expensivemap.png)

## Built With
```
python 3.7.12
python-google-places 1.4.2
folium 0.8.3
geopandas 0.10.2
wordcloud 1.5.0

```
