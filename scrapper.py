import urllib.request
from bs4 import BeautifulSoup

class Scraps(object):
    
    def __init__(self):
        self.temperature = 0
        self.precipitation = 0
        self.humidity = 0
        self.wind = 0

    def extract(self):

        # Extract html web page

        url = 'https://www.google.co.in/search?rlz=1C1OKWM_enIN791IN791&ei=Ff-DW_3xJsS9rQHlvrGQDQ&q=weather+in+pune&oq=weather+&gs_l=psy-ab.3.2.0j0i67k1j0l3j0i131k1j0l4.592054.592054.0.594459.1.1.0.0.0.0.375.375.3-1.1.0....0...1.1.64.psy-ab..0.1.374....0.3s0q9_lFJZ0'
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

        resp = urllib.request.Request(url=url, headers=headers)
        try:
            soup = BeautifulSoup(urllib.request.urlopen(resp).read(), 'lxml')
            self.temperature = int(soup.find_all('span', {'class':'wob_t', 'id':'wob_tm'})[0].string)
            self.precipitation = int(soup.find_all('span', {'id':'wob_pp'})[0].string[:-1])
            self.humidity = int(soup.find_all('span', {'id':'wob_hm'})[0].string[:-1])
            self.wind = int(soup.find_all('span', {'class':'wob_t', 'id':'wob_ws'})[0].string[:-4])
        except Exception as e:
            print(e)

        ''' Test 
        print("Temp : {}".format(self.temperature))
        print("Precipitation : {}".format(self.precipitation))
        print("Humidity : {}".format(self.humidity))
        print("Wind : {}".format(self.wind))
        '''

''' Driver        
def main():
    sc = Scraps()
    sc.extract()

if __name__ == '__main__':
    main()
'''