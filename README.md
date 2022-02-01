# AutomaticVideoUploader

## Fetches videos from your personal subreddit and uploads to youtube(**Twitch Clips Only**)

# How to use
  Create a folder named 'Secret' inside 'AutomaticVideoUploader'
  
## API

  You will need API for Youtube, Reddit, Gmail
  
  ### Youtube
    
  Copy the 'client_secret.json' file inside the 'Secret' folder and rename it to 'YoutubeSecrets.json'
  
  ### Reddit
  
  Get the reddit client_id, client_secret, user_agent, username, password, subreddit in one file and name it RedditSecret.py insert this file into the 'Secret' folder.
  It should look like:
  
    CLIENT_ID = 'client_id here'
    CLIENT_SECRET = 'client_secret here'
    USER_AGENT = 'user_agent here'
    USERNAME = 'username here'
    PASSWORD = 'password here'
    SUBREDDIT = 'subreddit here'

  ### GMAIL
    
  Similar to Youtube you will need to copy the 'client_secret.json' in 'Secret' Folder and rename it to 'EmailSecret.json' you may be able to just use the same one as youtube     if you enable GMAIL API on it
    
## Other files in 'Secret' Folder
  
  ### emailInfo.py
  
  ```
  SENDER = 'email registered for API, you will need to tick 'Allow email to be sent' when it opens in browser the first time'
  TO_EMAIL = 'Target for email'
  ```
  
  ### videoOptions.py
  
  ```
  DESCRIPTION = "Default description here"
  CATEGORY = "Youtube category default(20 is for gaming)"
  KEYWORDS = "Tags to upload with(game)"
  PRIVACYSTATUS = "Status uploaded with(private, public, unlisted)"
  ```
## Chromedriver

  Download chromedriver.exe for the version your chrome browser runs on here: https://chromedriver.chromium.org/downloads
  Copy it into 'AutomaticVideoUploader' directory
  
## redditFetch.py

  By default the code fetches top three post from 'day' and makes sure they are Twitch clips.
  It is possible to change from 'day' to other criteria and the amount of posts to fetch, but it will not check until it gets the required amount of clips.
  Make sure this is directed at a subreddit with only Twitch clips uploaded to get the best results.
