# Introduction
Using [this scraper](https://github.com/Kraussie/WallyWeather/blob/master/scraper/scrape.py) by [Max Fan](https://github.com/InnovativeInventor), we were able to collect 7,129 days worth of hourly weather data. This data was pulled from [api.weather.com](https://www.weather.com). The contents of each hourly observation are noted below for ease of use.

# Dataset Contents
Currently, the dataset only contains one weather station located at Tweed Airport in New Haven, CT. The Folder is called ["KHVN"](https://github.com/Kraussie/WallyWeather/tree/master/dataset/khvn) and is 77.2 MB. 

# Dataset Guide
| JSON Dictionary Key | Description | Example (01/01/1950) |
| ----------- | ----------- | ----------- |
| "key" | Weather Station Symbol | "KHVN" |
| "class" | Type of Data | "observation" |
| "expire_time_gmt" | _unknown_ | -631105200 |
| "obs_id" | Weather Station Symbol | "KHVN" |
| "obs_name" | Weather Station Name | "New Haven" |
| "valid_time_gmt" | _unknown_ | -631112400 |
| "day_ind" | _unknown_ | "N" |
| "temp" | Temperature in Fahrenheit | 33 |
| "wx_icon" | _unknown_ | 33 |
| "icon_extd" | _unknown_ | 3300 |
| "wx_phrase" | _unknown_ | "Fair" |
| "pressure_tend" | _unknown_ | null |
| "pressure_desc" | _unknown_ | null |
| "dewPt" | Dew Point | 30 |
| "head_index" | Heat Index | 33 |
| "rh" | _unknown_ | 89 |
| "pressure" | Barometric Pressure | 30.47 | 
| "vis" | Visability in Miles | 5 |
| "wc" | Wind _unknown_ | 33 |
| "wdir" | Wind Direction in Degrees | 320 |
| "wdir_cardinal" | Cardinal Wind Direction | "NW" |
| "gust" | Gust | null |
| "wspd" | Wind Speed | 3 |
| "max_temp" | Max Temperature (F) | null |
| "min_temp" | Min Temperature (F) | null |
| "precip_total" | Total Preciptation | null |
| "precip_hrly" | Precipation per hour (?) | null |
| "snow_hrly" | Snowfall per hour (?) | null|
| "uv_desc" | UV Radiation Description | "Low" |
| "feels_like" | Feels Like Temperature | 33 |
| "uv_index" | UV Radiation Index | 0 |
| "qualifier" | _unknown_ | null |
| "qualifier_svrty" | _unknown_ | null |
| "blunt_phrase" | _unknown_ | null |
| "terse_phrase" | _unknown_ | null |
| "clds" | _unknown_ | "CLR" |
| "water_temp" | Water Temperature (F) | null |
| "primary_wave_period" | _unknown_ | null |
| "primary_wave_height" | Height of Waves | null |
| "primary_swell_period" | _unknown_ | null |
| "primary_swell_height" | Height of Swells | null |
| "primary_swell_direction" | Direction of Swells | null |
| "secondary_swell_period" | _unknown_ | null |
| "secondary_swell_height" | Height of Swells | null |
| "secondary_swell_direction" | Direction of Swells | null |