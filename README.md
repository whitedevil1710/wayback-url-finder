# Wayback URL Finder

Welcome to the **Wayback URL Finder**, a powerful script that lets you travel back in time and explore the archives of the internet using the Wayback Machine API. 🚀

## Requirements

To embark on this time-traveling adventure, make sure you have the following prerequisites:

- Python 3.x
- `requests` library
- `colorama` library
- `readline` module
- `prompt_toolkit` library
## Installation
```
git clone https://github.com/whitedevil1710/wayback-url-finder.git
cd wayback-url-finder
pip3 install -r requirements.txt
python3 wdfinder.py
```

## How to Use

Prepare yourself for an exciting journey through time with these simple steps:

1. **Set Your Destination**: Use the `seturl` command to set the URL you want to search for. Choose wisely! ⚡️
```
seturl <url>
```
2. **Choose Your Starting Year**: Set the beginning timestamp (year) using the `setbeg` command. Where do you want to begin your search? 📅
```
setbeg <yyyy>
```

3. **Decide Your Final Year**: Set the end timestamp (year) using the `setend` command. Determine when your exploration should end. 🏁
```
setend <yyyy>
```

4. **Initiate Time Travel**: Perform the search and retrieve the data using the `find` command. Brace yourself for an adventure into the past! ⏰
```
find
```

5. **Extract the Time Stamps**: Extract the timestamps from the retrieved data using the `findts` command. Unveil the hidden records of time! 📜
```
findts
```
6. **Witness the Time Unfold**: Print the extracted timestamps using the `printts` command. Marvel at the historical moments you've discovered! 🕰️
```
printts
```
7. **Unveil Ancient URLs**: Display the URLs with their corresponding timestamps using the `showurls` command. Revisit the websites of the past! 🔗
```
showurls
```
8. **Document Your Journey**: Save the URLs and timestamps to a text file using the `save` command. Share your findings with fellow adventurers! 📝
```
save <filename>
```
9. **Need Assistance?**: Don't worry if you lose your way. Use the `help` command to see available commands and their descriptions. Our guide is always here to help! ℹ️
```
help
```
10. **End Your Expedition**: When you're ready to return to the present, gracefully exit the program using the `exit` command. Until next time, time traveler! 👋
 ```
 exit
 ```

## Author
- **Coded by** - [White Devil](https://github.com/whitedevil1710)
