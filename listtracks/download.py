import scrape
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist

class OpenDownloadLinks(object):

    def __init__(self):
        self.browser = Browser()