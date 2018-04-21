#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBIWZnbxikuiEExiq79iEPF0GmkgdiBRqI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword , np=""):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  print 'np==' + np
  NEXT_PAGE = np
  params = {
    'q': keyword,
    'part': 'id, snippet',
	'type':'video',
    'maxResults': 10,
	'pageToken': np
}

  #search_response = youtube.search(params).execute()
  search_response = youtube.search().list(q=keyword,part="id,snippet",maxResults=10,pageToken = np).execute()
  
  
  '''list(
    q=keyword,
    part="id,snippet",
    maxResults=25
  ).execute()'''

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    #print search_result["snippet"]["description"]
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s|kobe|%s|kobe|%s|kobe|%s" % (search_result["snippet"]["title"], search_result["id"]["videoId"],search_result["snippet"]["thumbnails"]["high"]["url"],search_result["snippet"]["description"]))

  if search_response['nextPageToken']:
    videos.append("|np|%s"%search_response['nextPageToken'])
    #print "Videos:\n", "\n".join(videos), "\n"
  return videos

if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
