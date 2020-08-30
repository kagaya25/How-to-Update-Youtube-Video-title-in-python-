import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
def changeVideoTitle(id):
    title = "This my 2019 memories picture " +  " "
    desc = "This video is about how awesome APIs are. "
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)
    
    request = youtube.videos().update(
        part="snippet", #,status
        body={
          "id": id,
          "snippet": {
            "categoryId": 27,
            # "defaultLanguage": "en",
            "description": desc,
             "tags": [
               "kagaya john","tom scott","tomscott","api","coding","application programming interface","data api"
             ],
            "title": title
          },
        }
    )
    response = request.execute()
    print(response)
    #https://www.youtube.com/watch?v=XO2fhnG61-Q 
    # The id is XO2fhnG61-Q
changeVideoTitle("XO2fhnG61-Q")