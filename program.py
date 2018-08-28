from scrapper import Scraps
from data.connect import global_init
from data.weather import Weather
import mongoengine
import time
import threading


def store_data():
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
        time.sleep(90)


def query():
    menu = ''' [q]uery | [f]ind '''
    while True:
        print('--------------------------')
        print(menu)
        print('--------------------------')
        print('Current stats')
        print('Total reports {}'.format(Weather.countReport()))

        user_input = str(input('>'))

if __name__ == '__main__':
    thread1 = threading.Thread(target=store_data)
    thread2 = threading.Thread(target=query)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
