from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from apiclient.discovery import build

scopes = ['https://www.googleapis.com/auth/calendar']
calendar_id = '9brb7n3ddbdu37frgn4rhpd2r4@group.calendar.google.com'
channel_id = '47321391915f41149d9da679b4d11c27'


def get_api(keyfile):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'keyfile.json', scopes
    )

    http_auth = credentials.authorize(Http())

    calendar_api = build('calendar', 'v3', http=http_auth)

    return calendar_api


def subscribe_for_events(api, link):
    # return 'https://alexbalagura.pythonanywhere.com/{}'.format(link)
    return api.events().watch(
        calendarId=calendar_id,
        body={
            'address': 'https://alexbalagura.pythonanywhere.com/{}'.format(link),
            'type': 'web_hook',
            'id': channel_id
        }).execute()
