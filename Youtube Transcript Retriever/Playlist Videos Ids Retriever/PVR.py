import requests
from decouple import config


def get_playlist_video_ids(api_key: str, playlist_id: str) -> list:
    
    """
    Retrieve all video IDs from a given YouTube playlist.
    
    Args:
        api_key (str): Your YouTube Data API key.
        playlist_id (str): The ID of the YouTube playlist.
    
    Returns:
        list: A list of video IDs present in the playlist.
    """

    endpoint = "https://www.googleapis.com/youtube/v3/playlistItems"
    video_ids = []
    next_page_token = None


    while True:

        # Set up the request parameters
        params = {
            "part": "contentDetails",
            "playlistId": playlist_id,
            "maxResults": 50,  # Maximum allowed by the API
            "pageToken": next_page_token,
            "key": api_key,
        }

        # Make the API request
        response = requests.get(endpoint, params=params)

        # Check response
        if response.status_code != 200:
            raise Exception(f"API request failed: {response.status_code}, {response.text}")

        # Define the data variable
        data = response.json()

        # Extract video IDs from the current page of results
        video_ids.extend(item["contentDetails"]["videoId"] for item in data["items"])

        # Check if there's another page of results
        next_page_token = data.get("nextPageToken")

        if not next_page_token:
            break

    return video_ids


# Safeguard Clause
if __name__ == "__main__":

    API_KEY = config("YOUR_YOUTUBE_API_KEY")
    PLAYLIST_ID = "PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p"

    try:
        video_ids = get_playlist_video_ids(API_KEY, PLAYLIST_ID)
        print(f"Retrieved {len(video_ids)} video IDs:")
        print(video_ids)
        
    except Exception as e:
        print(f"An error occurred: {e}")