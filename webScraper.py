#! python3
from googleapiclient.errors import HttpError
from redditScraper import getTwitchClips
from uploadToYoutube import get_authenticated_service, initialize_upload
from automateDownload import autoDownloadFile
from clearFiles import clearDirectory
from Secret.videoOptions import CATEGORY, DESCRIPTION, KEYWORDS, PRIVACYSTATUS

def runMain():
    args = {'description' : DESCRIPTION,
    'category' : CATEGORY,
    'keywords' : KEYWORDS,
    'privacyStatus' : PRIVACYSTATUS}

    youtube = get_authenticated_service()
    clip_list = getTwitchClips()
    
    for clip in clip_list:
        
        fileName = autoDownloadFile(clip_list[clip])
        print(type(fileName))
        if fileName != None:
            try:
                initialize_upload(youtube, args, clip, fileName)
            except HttpError as e:
                print ('An HTTP error %d occurred:\n%s') % (e.resp.status, e.content) 
    clearDirectory()

if __name__ == "__main__":    
    runMain()