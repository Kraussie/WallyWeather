import datetime
import tqdm
import os
import requests
from multiprocessing import Pool

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

def fetch_weather(station="KHVN:9:US", url = None, save=True, location="dataset/", verbose=True, check=True):
    """
    Fetches weather for all days given the proper URL
    """
    location += station.split(":")[0].lower() + "/"

    if not url:
        url = "https://api.weather.com/v1/location/{station}/observations/historical.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&units=e&startDate=".format(station=station)

    seen = []
    if check and os.path.isfile("unknown.txt"):
        with open("unknown.txt") as f:
            for each_row in f:
                seen.append(each_row.rstrip())
                # print(each_row.rstrip())

    for each_date in tqdm.tqdm(daterange()):
        date = each_date.strftime("%Y%m%d")
        if (not os.path.isfile(location + date + ".json")) and (not station.rstrip() + date.rstrip() in seen):
            r = requests.get(url + date)
            if r.status_code == 200 and save and location:
                with open(location + date + ".json", "wb") as f:
                    f.write(r.content)
                if verbose:
                    print("Fetched and saved", url + date, "to", location + date + ".json")
            elif r.status_code == 400:
                with open("unknown.txt", "a") as f:
                    f.write(station.rstrip() + date.rstrip() + "\n")
                if verbose:
                    print("Had trouble fetching", url + date, "Status Code:", r.status_code)
            else:
                if verbose:
                    print("Had trouble fetching", url + date, "Status Code:", r.status_code)
        elif station + date in seen:
            if verbose:
                print("Seen", date)
        # break
        

if __name__ == "__main__":
    with open("locations.txt") as f:
        # with Pool(8) as p:
            # stations = []
            # for each_station in f:
                # stations.append(each_station)
            # p.map(fetch_weather, stations)
        for each_station in f:
            fetch_weather(each_station)
