import datetime
import tqdm
import os
import requests

def daterange(start_date = None, end_date = None):
    """
    Loops over date range
    """
    if not start_date:
        start_date = datetime.datetime(day=1, month=1,year=1950)
    if not end_date:
        end_date = datetime.datetime.now()

    cursor_date = start_date

    while cursor_date < end_date:
        yield cursor_date
        cursor_date += datetime.timedelta(days=1)

def fetch_weather(url = None, save=True, location="dataset/khvn/", verbose=True):
    """
    Fetches weather for all days given the proper URL
    """
    if not url:
        url = "https://api.weather.com/v1/location/KHVN:9:US/observations/historical.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&units=e&startDate="

    for each_date in tqdm.tqdm(daterange()):
        date = each_date.strftime("%Y%m%d")
        if not os.path.isfile(location + date + ".json"):
            r = requests.get(url + date)
            if r.status_code == 200 and save and location:
                with open(location + date + ".json", "wb") as f:
                    f.write(r.content)
                if verbose:
                    print("Fetched and saved", url + date, "to", location + date + ".json")
            else:
                if verbose:
                    print("Had trouble fetching", url + date, "Status Code:", r.status_code)
        # break
        

if __name__ == "__main__":
    fetch_weather()
