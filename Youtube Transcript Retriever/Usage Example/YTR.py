from youtube_transcript_api import YouTubeTranscriptApi
import os
import requests
from decouple import config
from PVR import get_playlist_video_ids


# Enviromental Variables setting
YOUR_YOUTUBE_API_KEY = config("YOUR_YOUTUBE_API_KEY")

# Function Version
def process_vid(video_id: str) -> None:

    """Processes a YouTube video by retrieving its transcript and saving it as a text file named after the video's title."""


    def get_video_title() -> str:

        """Retrieve the title of a YouTube video using YouTube API."""

        api_key = YOUR_YOUTUBE_API_KEY
        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            if "items" in data and len(data["items"]) > 0:
                return data["items"][0]["snippet"]["title"]
            
            else:
                raise ValueError("Video not found or invalid video ID.")
            
        else:
            raise Exception(f"Failed to retrieve video title. Status code: {response.status_code}")
        

    def get_transcript(video_title: str) -> None:

        """Retrieve and save the transcript of a YouTube video."""

        # Ensure valid filename
        safe_title = "".join(c for c in video_title if c.isalnum() or c in (' ', '.', '_')).rstrip()

        # Obtain the directory where the script is
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir+"\\output\\", f"{safe_title}.txt")  # Use video title for file name

        # String holder
        transcript_string = ""

        # Get the video transcript
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
            print("English transcript retrieved.")

        except Exception as e:
            print(f"Error when trying to retrieve English transcript: {e}")
            transcript = []


        # Populate the string holder with the actual video's transcript
        for entry in transcript:
            transcript_string += f"{entry['start']:.0f}s: {entry['text']}\n"


        # Save the file
        try:

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(transcript_string)

            print(f"Transcript saved in: {file_path}")

        except Exception as e:
            print(f"Error writing to the file: {e}")


    # Main process logic
    try:
        video_title = get_video_title()
        get_transcript(video_title)

    except Exception as e:
        print(f"Error processing video {video_id}: {e}")
    

# Safeguard clause
if __name__ == "__main__":

    # Corey's Schafer Django Tutorial Playlist
    pl_id = 'PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p'

    # PL vids ids retrival
    vid_list = get_playlist_video_ids(api_key=YOUR_YOUTUBE_API_KEY, playlist_id=pl_id)
    
    # PL loop processing
    for vid in vid_list:
        process_vid(vid)

