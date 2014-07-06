from scrape import TrackListScrapeHandler
from splinter import Browser


class OpenDownloadLinks(object):

    def __init__(self, artists, year):
        self.artists = artists
        self.year = year
        self.handler = TrackListScrapeHandler(self.artists, self.year)

    def open_all_tabs(self):
        artists_list = self.handler.execute_scrape()
        for artist in artists_list:
            tab = DownloadLinkTab()
            tab.open_download_tab(artists_list[artist])


class DownloadLinkTab(object):

    def open_download_tab(self, track_list):
        for track in track_list:
            try:
                browser = Browser('chrome')
                browser.visit('http://google.com')
                print track
                browser.fill('q', track[0] + ' ' + track[1] + ' download free')
                browser.find_by_name('btnG').first.click()
            except Exception:
                pass
