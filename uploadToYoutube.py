import httplib2
import http.client
import time
import random
import os

# from pywinauto import Application, Desktop
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

from oauth2client import client # Added
from oauth2client import tools # Added
from oauth2client.file import Storage # Added

httplib2.RETRIES = 1

MAX_RETRIES = 10

RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, http.client.NotConnected,
http.client.IncompleteRead, http.client.ImproperConnectionState,
http.client.CannotSendRequest, http.client.CannotSendHeader,
http.client.ResponseNotReady, http.client.BadStatusLine)

RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

CLIENT_SECRETS_FILE = os.path.dirname(os.path.realpath(__file__)) + "\\Secret\\client_secrets.json"

YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")

def get_authenticated_service():
    credential_path = os.path.dirname(os.path.realpath(__file__)) + "\\Secret\\credentials.json"
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, YOUTUBE_UPLOAD_SCOPE)
        credentials = tools.run_flow(flow, store)
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=credentials)

def initialize_upload(youtube, options, name, fileName):
    tags = None
    if options['keywords']:
        tags = options['keywords'].split(',')

    body=dict(
        snippet=dict(
        title=name,
        description=options['description'],
        tags=tags,
        categoryId=options['category']
        ),
        status=dict(
        privacyStatus=options['privacyStatus']
        )
    )

    # Call the API's videos.insert method to create and upload the video.
    #videoPath = "G:\PythonFiles\AutomaticVideoUploader\RedditDownload\%s" % ('AT-cm_eu92AMT2IjQN1aDd298p2w.mp4')
    videoPath = fileName
    print(type(videoPath))
    insert_request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=MediaFileUpload(videoPath, chunksize=-1, resumable=True)
    )
    resumable_upload(insert_request, options)

def resumable_upload(request, options):
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            print('Uploading file...')
            status, response = request.next_chunk()
            if response is not None:
                if 'id' in response:
                    print ('The video with the id %s was successfully uploaded!' % response['id'])
                
                else:
                    exit('The upload failed with an unexpected response: %s' % response)
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                error = 'A retriable HTTP error %d occurred:\n%s' % (e.resp.status,
                                                                    e.content)
            else:
                raise
        except RETRIABLE_EXCEPTIONS as e:
            error = 'A retriable error occurred: %s' % e

    if error is not None:
      print (error)
      retry += 1
      if retry > MAX_RETRIES:
        exit('No longer attempting to retry.')

      max_sleep = 2 ** retry
      sleep_seconds = random.random() * max_sleep
      print ('Sleeping %f seconds and then retrying...') % sleep_seconds
      time.sleep(sleep_seconds)