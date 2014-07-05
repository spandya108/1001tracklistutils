1001 TrackList Utils
==================

The **1001 Tracklist Website Utils** repository contains different utility methods in order to traverse and scrape [1001TrackLists](http://1001tracklists.com). Each directory within the repository contains the necessary packages in order to execute a specific purpose of scraping the wwebsite, listed below. 

The different utilities currently created include:

1. `listtracks`: takes in the specified artist and year as parameters and searches for 'artist edc year' in order to get the tracklist for their set in the specified `year`. It then places the name of all the tracks in the specified set into the file named `tracklist-[artist]-edc[year]`.
