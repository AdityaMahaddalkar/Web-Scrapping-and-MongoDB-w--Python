from scrapper import Scraps
from data.connect import global_init
from data.weather import Weather
import mongoengine
import time


def main():
    # Connect to database

    global_init('Weather_Database')

    while (True):

        # Scrap the web page
        # Warning : Donot issue huge amount of requests in small time
        # This is called spamming
        sc = Scraps()
        sc.extract()

        # Assign document paramenters
        w = Weather()
        w.temperature = sc.temperature
        w.precipitation = sc.precipitation
        w.humidity = sc.humidity
        w.wind = sc.wind

        # save in database

        w.save()

        # wait for 15 minutes
        time.sleep(900)


if __name__ == '__main__':
    main()
