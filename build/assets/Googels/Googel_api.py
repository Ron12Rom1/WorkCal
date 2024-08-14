import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Scopes define the access levels your application needs
SCOPES = ['https://www.googleapis.com/auth/calendar']

def if_creds_not_valid(creds):
    if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('assets\Googels\credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('assets/Googels/token.json', 'w') as token:
        token.write(creds.to_json())

    return (flow, creds)
        
def get_credentials():
    """Get valid user credentials from storage or run the OAuth flow to get new credentials."""
    creds = None
    # Token file stores user access and refresh tokens
    if os.path.exists('assets/Googels/token.json'):
        creds = Credentials.from_authorized_user_file('assets/Googels/token.json', SCOPES)
    # If no valid credentials, run the OAuth flow
    if not creds or not creds.valid:
        flow, creds = if_creds_not_valid(creds)
    return creds


def list_upcoming_events(service):
    """Fetch and print the next 10 events from the user's primary calendar that have the name 'Bezek'."""
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # UTC time
    try:
        events_result = service.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])
        if not events:
            print('No upcoming events found.')
            return
        # Filter and print only events with the name 'Bezek'
        for event in events:
            summary = event.get('summary', '')
            if summary == 'Bezek':
                start = event['start'].get('dateTime', event['start'].get('time'))
                print(start, summary)
    except HttpError as error:
        print(f'An error occurred: {error}')

def create_event(service, summary, start_time, end_time):
    """Create a new event in the user's primary calendar."""
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'UTC',
        },
    }
    try:
        event_result = service.events().insert(
            calendarId='primary',
            body=event
        ).execute()
        print(f"Event created: {event_result.get('htmlLink')}")
    except HttpError as error:
        print(f'An error occurred: {error}')

def main():
    """Main function to authenticate, list upcoming events, and create a new event."""
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)
    
    # List upcoming events
    print("Listing upcoming events:")
    list_upcoming_events(service)

    # Create a new event
    print("\nCreating a new event:")
    summary = "Sample Event"
    start_time = '2024-08-16T10:00:00Z'  # Change to your desired start time
    end_time = '2024-08-16T11:00:00Z'    # Change to your desired end time
    create_event(service, summary, start_time, end_time)

if __name__ == '__main__':
    main()
