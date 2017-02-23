# Conky dashboard for potato

I use my potato as a fancy dashboard to display various data such as weather, appointments and the next bus connections from my local station.

I use conky to display this dashboard, and a collection of scripts to refresh the data.

## Screenshot

![Screenshot](https://github.com/jereviendrai/potato/raw/master/conky/example.png "Screenshot")

## Accuweather

This is a script to gather data from accuweather. It works anywhere in the world, but I found the forecast to be rather imprecise.

Documented in 1d_accuweather_rss. Example in conkyrc_accuweather.

Requires:

* wget
* Conkyweather font

## Meteo

This script gathers weather data (temperature and precipitation) from Meteoswiss. It only works in switzerland, but I find it to be more precise than accuweather.

The script gets the weather data and generates a picture using python matplotlib. The picture is then included in conky (see conkyrc for example). I recommend calling the script periodically from a cronjob.

Requires:

* python3
* python numpy
* python matplotlib
* curl
* jshon
* cronie or similar

## ZVV

This script can get traffic data for public transport in switzerland. It generates data for a "stationboard" that displays the next few departing busses/trains from a specific station. The station is determined through a station ID which is provided by the API. To find out what ID your station has, try:

     curl http://transport.opendata.ch/v1/locations?query=STATIONNAME | jshon

jshon is optional and pretty-prints the output.

Documentation for the entire API can be found at http://transport.opendata.ch/docs.html

The id is then put in the getdata script. The script is executed periodically directly from within conky. The stationboard data is stored into three different files, which then are included in conky.

Example can be found in conkyrc. Note that this script is not perfect. Sometimes, the line numbers, targets, and times don't align properly due to race condition (e.g. line 32 is said to go to Holzerhurd even though it actually goes to Schwamendingerplatz). This happens when conky updates the text while at the same time the data files are being updated.

Requires:

* curl
* jshon
* jsawk

## Calendar

This script gets all the appointments for the next two days from the local calcurse database. 

Calcurse is a minimal ncurses based CLI calendar and happens to support caldav. This means you can synchronize pretty much any online calendar to your local calcurse and then display it. It also supports todo lists in a similar fashion. 

To use it, install calcurse and synchronize it with your calendar of choice using the calcurse-caldav script (that is included in the newest version of calcurse).

You can set up a cronjob to regularly synchronize your calendar and keep your appointments up to date.

The timespan for which events are shown can be altered in the getcal script. It's also possible to show todo items. See the documentation of calcurse for further reference.

http://freecode.com/projects/calcurse


Requires:

* calcurse
* cronie or similar

## Calendar - version 2

A second approach to the calendar uses khal and vdirsyncer, the former to display appointments, the latter to synchronize with the caldav server. I had some issues with calcurse-caldav, so eventually switched to this approach. See example in conkyrc_khal file.

To use it, install khal and vdirsyncer. Set up vdirsyncer to synchronize your caldav calendar(s) to a local directory, then set up khal to display those.

Set up a cronjob to regularly synchronize your calendar using vdirsyncer.

khal can be directly called from your conkyrc. No need for an extra script.
