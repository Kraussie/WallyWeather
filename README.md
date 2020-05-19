# WallyWeather
## Introduction
This is the final project in Choate Rosemary Hall's Machine Learning class (CS580-HO). Individually or in groups, we were supposed to use "interesting and open datasets" and "models using algorithms we can undersand and neural network architectures that we can study." As a team (Ian Haile, Nate Krauss, and Max Fan), we created our own weather dataset and model.

## Dataset
Using [this scraper](https://github.com/Kraussie/WallyWeather/blob/master/scraper/scrape.py) by [Max Fan](https://github.com/InnovativeInventor), we were able to collect 7,129 days worth of hourly weather data. This data was pulled from [api.weather.com](https://www.weather.com). 

\* More information about the dataset can be found [here](https://github.com/Kraussie/WallyWeather/blob/master/dataset/dataset_guide.md).

## Model
The model was created in the Google Colab Notebook development enviornment and was trained over an X hour period. 

\* More information about the model and its training can be found [here (not working yet)]().

## User-Interface
The culimination of this project comes together at https://natekrauss.me/WallyWeather. The website pulls the current weather data of Wallingford, CT and inputs that into the pre-trained model. Then, the model outputs a three-day prediction which is displayed to the user.

The website uses the [Materialize CSS Framework](https://materializecss.com/) that allowed for fast UI development. The website is hosted on Github Pages and pulls the current predictions from ???.