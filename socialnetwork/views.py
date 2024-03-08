from django.shortcuts import render
from googleapiclient.discovery import build
import json

home_playlists = []
api_key="AIzaSyDO8BUfyrgBrVvH31BTMdnZKy9QNVYut48"

# Create your views here.
def home(request):
    home_playlists = get_home_playlists()
    context = {'items': home_playlists}
    print(context)
    return render(request, 'socialnetwork/home.html', context)

def login(request):
    return render(request, 'socialnetwork/login.html')


def get_home_playlists():
    youtube = build('youtube', 'v3', developerKey=api_key)
    topics = ['computer science', 'algorithms', 'web development', 'python'] #, 'Machine Learning', 'Large Lenguage Models', 'React', 'Django', 'Data Structures', 
                # 'compilers', 'java', 'javascript', 'numpy', 'sklearn']

    query = ""
    for topic in topics[:-2]:
        query += topic + " | "
    query += topics[-1]
    print("query: " + query)

    request = youtube.search().list(
        part="snippet",
        maxResults=24,
        order="viewCount",
        q=query,
        type="playlist"
    )

    response = request.execute()
    print(f"response: {response}")
    print("\n" * 10)
    items = response['items']

    
    playlists = []
    for item in items:
        playlist = {}
        playlist['playlistId'] = item['id']['playlistId']
        playlist['channelId'] = item['snippet']['channelId']
        playlist['title'] = item['snippet']['title']
        playlist['thumbnail'] = item['snippet']['thumbnails']['medium']['url']
        playlists.append(playlist)
    
    home_playlists = playlists
