# FFXIV_Profiler

## This is the basis of creating a FFXIV Profiler.
The goal is to display: 
+ [ ] Completiton rates
+ [ ] Class level totals
+ [ ] Achievements (Completed/Uncompleted)
+ [ ] Mounts
+ [ ] Minions
+ and more...
In a nice view manner or have customizable pages in the future.

## Current Status
+ The webapp can be hosted locally and is dockerized to be put onto a cloud service like AWS/Azure and have it live hosted.
+ Due to unreliability of the API library used, the project will be created anew with Golang as the base to utilize a opensourced scraper library based on Go and implement a more reliable API

# In the current version:
## HOW TO RUN:
+ Obtain an API Key:
    + Go to <https://xivapi.com/>


+ Install Dependecies:
    + pip install -r requirements.txt

    

+ HOW TO USE THIS:
    + On command line, run main.py with the python command\

    + docker run -p 80:5000 dev

## HOW TO USE:
+ On the username search bar, input a characters name you wish to find.
+ On the world search bar, input the world that character resides in.
+ A great test search would be Yoshi'p Sampo (Character name) of Aegis (World). He is the creator and developer of the game after all!
+ Enjoy the page!
