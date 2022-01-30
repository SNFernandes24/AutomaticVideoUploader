#! python3

import os

from googleapiclient.errors import HttpError
from redditScraper import getTwitchClips
from uploadToYoutube import get_authenticated_service, initialize_upload
from setVideoOptions import VideoOptions



if __name__ == "__main__":
    args = VideoOptions()
    youtube = get_authenticated_service()
    clip_list = getTwitchClips()

    for clip in clip_list:
        # downloadClip(clip)
        try:
          initialize_upload(youtube, args)
        except HttpError as e:
          print ('An HTTP error %d occurred:\n%s') % (e.resp.status, e.content) 
    #print(clip_list)

    pass