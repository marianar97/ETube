from django.shortcuts import render
from googleapiclient.discovery import build
import json

home_playlists = []
api_key="AIzaSyDO8BUfyrgBrVvH31BTMdnZKy9QNVYut48"

# Create your views here.
def home(request):
    topics1 = ['computer science', 'algorithms', 'web development', 'python']
    topics2 = ['compilers', 'java', 'javascript', 'numpy', 'sklearn']
    topics3 = ['Machine Learning', 'Large Lenguage Models', 'Data Structures'] 
    topics4 = ['React', 'Django', 'CSS', 'Javascript']
    home_playlists = get_all_playlists(topics1, topics2, topics3, topics4)
    context = {'items': home_playlists}
    print(context)
    return render(request, 'socialnetwork/home.html', context)

def login(request):
    return render(request, 'socialnetwork/login.html')


def get_query(keywords: list):
    query = ""
    for topic in keywords[:-2]:
        query += topic + " | "
    query += keywords[-1]
    print("query: " + query)
    return query

def get_playlists_items(topics):
    youtube = build('youtube', 'v3', developerKey=api_key)
    query = get_query(topics)
    request = youtube.search().list(
        part="snippet",
        maxResults=6,
        order="viewCount",
        q=query,
        type="playlist"
    )
    return request.execute()['items']

def get_playlist(items):
    playlists = []
    for item in items:
        playlist = {}
        playlist['playlistId'] = item['id']['playlistId']
        playlist['channelId'] = item['snippet']['channelId']
        playlist['title'] = item['snippet']['title']
        playlist['thumbnail'] = item['snippet']['thumbnails']['medium']['url']
        playlists.append(playlist)
    
    return playlists

def get_all_playlists(*args):
    items = []
    for keywords in args:
        ans = get_playlists_items(keywords)
        playlist = get_playlist(ans)
        items.extend(playlist)
    print("output", items)
    return items


    