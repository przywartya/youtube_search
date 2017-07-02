from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyAordadII2JP-hFzI0VQcfh8yeFEmkH0dc"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class Video(object):
    def __init__(self, title, link):
      self.title = title
      self.id = link

def youtube_search(q, max_results):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(q=q, part="id,snippet", maxResults=max_results).execute()

  videos = list()

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(Video(search_result["snippet"]["title"], 
                search_result["id"]["videoId"]))
  return videos

