# Scraping Bangladeshi Restaurants from GoogleMaps
---

[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?logo=Jupyter)](https://jupyter.org/try) [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/tanjimanasreen/GoogleMaps-Restaurant-Scraper/blob/main/Restaurant_Scrapper.ipynb)

## Summary

In this project I created a scraper in python using Google Places API to scrap Restaurants' information from all over Bangladesh.

## About Dataset
The restaurant dataset contains name, logitude, latitude, ratings, number of reviews and price level of each restaurant.
You will find the raw dataset [here](https://github.com/tanjimanasreen/GoogleMaps-Restaurant-Scraper/tree/main/Dataset/Restaurant-Raw) and final cleaned version [here](https://github.com/tanjimanasreen/GoogleMaps-Restaurant-Scraper/tree/main/Dataset/Restaurant-FInal)

## Prerequisite
- A Google API key with Google Places API Web Service and Google Maps Geocoding API activated against it. Check [Google Places API](https://developers.google.com/maps/documentation/places/web-service/overview) for more details

- A location list of every Upazilla/Thana along with its District of Bangladesh. In my case I used [Mobile network coverage in Bangladeshi Upazila or Thana](https://www.kaggle.com/mushfiqurrobin/network-coverage) from kaggle to collect the locations around Bangladesh. Here you can see my collected [location](https://github.com/tanjimanasreen/GoogleMaps-Restaurant-Scraper/blob/main/Dataset/locations.csv) list.  

## Built With
```
python 3.7.12
python-google-places
```
