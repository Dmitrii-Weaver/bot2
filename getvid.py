import requests
import google_token

URL = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId=UCyl1z3jo3XHR1riLFKG5UAg&maxResults=1&order=date&key=" + google_token.GTOKEN

def getvid():

    response = requests.get(URL)
    response_json = response.json()
    id = response_json["items"][0]["id"]["videoId"]
    vidUrl = "https://www.youtube.com/embed/" + id
    return vidUrl
