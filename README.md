# Tech4Germany Coding Challenge: Passau's water levels

A little web app that helps citizens of a city to quickly get information about the current water levels of their river(s).
It shows you Passau's water level per default but you can also look at other available cities.
The app uses data from the REST-API [PegelOnline](https://www.pegelonline.wsv.de/webservice/guideRestapi).

## Installations

To install the necessary libraries, run "pip install -r requirements.txt", ideally in a Python virtual environment.

## Usage
Simply run app.py (e.g. command "python3 app.py").
Click the local host address which will show you the current water levels of Passau.
If you want to see e.g. Deggendorf's water levels, exchange 'passau' with 'deggendorf' in the URL.

## Structure
Some basic settings can be changed in config.py, e.g. if a city wants to redefine their critical warning levels.
The data is retrieved from PegelOnline in access_api.py.
Ultimately, if the core app structure needs to be changed, it can be done in app.py.
