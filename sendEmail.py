from email.mime.text import MIMEText
import base64
import os
import pickle
import datetime

from Secret.emailInfo import *

# from pywinauto import Application, Desktop
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.readonly']

def auth():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "\\Secret\\token.pickle"):
        with open(os.path.dirname(os.path.realpath(__file__)) + "\\Secret\\token.pickle", 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.dirname(os.path.realpath(__file__)) + "\\Secret\\EmailJson.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(os.path.dirname(os.path.realpath(__file__)) + "\\Secret\\token.pickle", 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

    Returns:
        An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
    b64_string = b64_bytes.decode()
    return {'raw': b64_string}

def create_message_string(clips):
    message = ''
    for clip in clips:
        message += f'\nSuccessfully uploaded file with tite: {clip} found at: {clips[clip]} from Twitch clips.\n'
    return message
    
def sendEmail(clips):
    try:
        # Call the Gmail API
        subject = 'Uploaded files at: {}'.format(datetime.datetime.now())
        message_text = create_message_string(clips)
        message = create_message(SENDER, TO_EMAIL, subject, message_text)

        authunt = auth()
        service = build('gmail', 'v1', credentials=authunt)
        results = (service.users().messages().send(userId='me', body=message).execute())
        print(results)


    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')