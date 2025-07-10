from googleapiclient.discovery import build
import json
from dotenv import load_dotenv
import os
from .manage_messages import add_to_messages, reset_messages
from .get_ideas import ideafy

load_dotenv(override=True) 
api_key = os.getenv("YT_API_KEY")
print(api_key)


youtube = build("youtube", "v3", developerKey=api_key)

def generate_vids(query):

    reset_messages()
    add_to_messages(query)
    ideafy()

    with open('./backend/ideas.json', 'r', encoding='utf-8') as f:
        datas = json.load(f)

    response_data = []

    for data in datas:
        request = youtube.search().list(
            part=data["part"],
            q=data["q"],
            type=data["type"],
            maxResults=5,
            order=data["order"],
            # videoDuration=data["videoDuration"],
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
