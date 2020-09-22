from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import speech_recognition as sr
import pyaudio
import datetime
import pyttsx3
import pytz
from gtts import gTTS
import wordtodigits
#changing some contents on manoj
MONTHS=['january','february','march','april','may','june','july','august','september','october','november','december']
words={'event','events','task','tasks','programme','programmes','plan','plans'}
def speak(text):
    print(text)
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def get_audio():
    print("listening......")
    r=sr.Recognizer()
    service=main()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        sil=""
        month=''
        day=0
        try :
            said=r.recognize_google(audio)
            st=set(said.split())
            if 'hello' in said:
                speak("'hello, how are you doing?")
            elif 'what is your name' in said:
                speak('my name is manoj')
            elif "time" in said:
                sa=str(datetime.datetime.now().time().strftime('%I:%M:%p'))
                speak(sa)
            elif len(words.intersection(st))>0:
                today=str(datetime.date.today())
                sil=wordtodigits.convert(said)
                for wor in st:
                    if wor.lower() in MONTHS:
                        month=MONTHS.index(wor.lower())+1
                for wory in sil:
                    if wory.isdigit():
                        day=int(wory)
                dat=datetime.date(month=month,day=day,year=int(today[:4]))
                ser(dat,service)
            else:
                speak(said)
        except Exception as e:
            print('problem :'+str(e))
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service
def ser(n,service):
    date=datetime.datetime.combine(n,datetime.datetime.min.time())
    endate=datetime.datetime.combine(n,datetime.datetime.max.time())
    utc=pytz.UTC
    date=date.astimezone(utc)
    endate=endate.astimezone(utc)
    print(f'Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(),
                                        timeMax=endate.isoformat(),
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    s=''
    if not events:
        print('No events found.')
        speak('No events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        speak(str(event["summary"]))
get_audio()
