import praw
from Secret.redditSecret import *

def getTwitchClips():
    clip_dict = {}
    reddit = praw.Reddit(client_id=CLIENT_ID, \
                        client_secret=CLIENT_SECRET, \
                        user_agent=USER_AGENT, \
                        username=USERNAME, \
                        password=PASSWORD)

    subreddit = reddit.subreddit(SUBREDDIT)
    topThree = subreddit.top('day', limit=3)
    for key in topThree:
        if 'clips.twitch.tv' in key.url:
            clip_dict.update({key.title : key.url})
    return clip_dict