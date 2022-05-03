# Vimeo API Functions

## Work Process
1. Created a gmail account
2. Created a vimeo account using the gmail account I created
3. Followed the steps to create the app on https://developer.vimeo.com/api/guides/start
4. Chose python as language to write in - most experience of languages provided
5. Following https://github.com/vimeo/vimeo.py guide, understood how to operate functions through the api.
6. Made a connection using the 'getting started' instructions on vimeo
7. Using the json() function and debugger(pycharm), found the likes and views of a video.
8. Following a tutorial on the website https://developer.vimeo.com/api/reference/videos/3.4#create_comment, commented on a video
9. Added assert statements to functions for each function, following the connection function example
10. Added documentation to functions
11. Added parser to implement arguments using cmd, using the id, secret, and token as arguments
12. Added video-id as argument, so other videos can be accessed


## Usage
```
usage: main.py [-h] [--video-id VIDEO_ID] --token TOKEN --key KEY --secret SECRET [--comment COMMENT]
Perform Tasks on Vimeo API

optional arguments:
  -h, --help           show this help message and exit
  --video-id VIDEO_ID  A video ID
  --token TOKEN        Vimeo API Token
  --key KEY            Vimeo API Key
  --secret SECRET      Vimeo API Secret
  --comment COMMENT    Comment content to post on the video
```

## Requirements
* Python 3
* install PyVimeo python package