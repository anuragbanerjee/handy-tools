#!/usr/bin/env python

'''
Quick Add
Created by Anurag Banerjee.
Copyright 2016. All rights reserved.

You may need to get your client_secret.json from console.developers.google.com.

USAGE `python quick-add.py -q <EVENT DETAILS>`

-q <EVENT DETAILS>: sets the Quick Add message/query to send to Google Calendar
'''

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
import sys

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser])
    flags.add_argument("-q", action="store", dest="query")
    flags = flags.parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/quick-add.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Quick Add'


def get_credentials():
    """
    Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'quick-add.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """
    Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object, logs the query from the arguments, and creates an event with Quick Add.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    if len(sys.argv) > 1:
        with open("log.txt", "a") as logfile:
            logfile.write(flags.query + "\n")
        created_event = service.events().quickAdd(
            calendarId='primary',
            text=flags.query
        ).execute()


if __name__ == '__main__':
    main()
