from googleapiclient.discovery import build
import json

api_key = "AIzaSyCaIbuMru2i2_2zPRjeitBM-ODReG241NQ"

youtube = build("youtube", "v3", developerKey=api_key)

def generate_vids():

    with open('./backend/ideas.json', 'r', encoding='utf-8') as f:
        datas = json.load(f)

    response_data = []

    for data in datas:
        request = youtube.search().list(
            part=data["part"],
            q=data["q"],
            type=data["type"],
            maxResults=1,
            order=data["order"],
            videoDuration=data["videoDuration"],
            videoDefinition=data["videoDefinition"],
            safeSearch=data["safeSearch"],
            relevanceLanguage=data["relevanceLanguage"]
        )

        response = request.execute()

        for item in response['items']:
            json_item = {}
            json_item['title'] = item['snippet']['title']
            json_item['thumbnail'] = item['snippet']['thumbnails']['high']['url']
            json_item['url'] = f"http://www.youtube.com/embed/{item['id']['videoId']}"
            response_data.append(json_item)
    return response_data


