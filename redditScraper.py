import imp
import praw
from Secret.redditSecret import *

def getTwitchClips():
    clip_array = []
    reddit = praw.Reddit(client_id=CLIENT_ID, \
                        client_secret=CLIENT_SECRET, \
                        user_agent=USER_AGENT, \
                        username=USERNAME, \
                        password=PASSWORD)

    subreddit = reddit.subreddit('LivestreamFail')
    top_sub = subreddit.top('day')

    for sub in subreddit.top('day', limit=2):
        if 'clips.twitch.tv' in sub.url:
            clipString = sub.url.split("tv/")[1]
            clipString = clipString.split("?")[0]
            clip_array.append(clipString)
    return clip_array