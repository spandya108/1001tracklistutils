from bs4 import BeautifulSoup
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist


class TrackListScrapeHandler(object):

    def __init__(self, artists, year):
        self.artists = artists
        self.year = year

    def execute_scrape(self):
        scraper = TrackListScraper(self.artists, self.year)
        full_list = scraper.execute_full_scrape()
        return full_list


class TrackListScraper(object):

    def __init__(self, artists, year):
        self.browser = Browser('chrome')
        self.artists = artists
        self.year = year
        self.browser.visit('http://1001tracklists.com')

    def execute_full_scrape(self):
        artist_tracklists = {}
        for artist in self.artists:
            artist_tracklists[artist] = self.scrape_per_artist(artist)
        self.browser.quit()
        return artist_tracklists

    def scrape_per_artist(self, artist):
        """Execute the same scrape but instead using the python splinter library
        """

        self.browser.fill('main_search', artist + ' edc ' + self.year)

        self.browser.find_by_id('btn_search').first.click()

        try:
            self.browser.click_link_by_partial_text('2014-06-')
            track_strings = self.get_track_list_for_set(artist)
            return track_strings
        except ElementDoesNotExist:
            pass

    def get_track_list_for_set(self, artist):
        soup = BeautifulSoup(self.browser.html)
        track_values = soup.find_all('div', class_='trackValue')

        track_strings = []
        file = open('tracklist-' + artist + '-edc' + self.year, 'w')
        for track in track_values:
            if track.a:
                track_string = track.a.string
                file.write(track_string)
                # track details in format [artist, trackname]
                track_details = self.parse_track_string(track_string)
                track_strings.append(track_details)
        file.close()
        return track_strings

    def parse_track_string(self, track_string):
        track_info = track_string.strip().split('-')
        for i in range(len(track_info)):
            track_info[i] = track_info[i].strip()
        return track_info
