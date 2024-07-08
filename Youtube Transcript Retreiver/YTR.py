from youtube_transcript_api import YouTubeTranscriptApi

JSON_PATH = r'C:\Users\USUARIO\GR\Software Development\Misc Scripts\Youtube Transcript Retreiver\Result.txt'

video_id = 'JSehk8lKkYs'
transcript_string = ''

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
except:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'en'])

for entry in transcript:
   transcript_string += f"{entry['start']:.0f}s: {entry['text']}\n"


with open(JSON_PATH, 'w') as file:
    file.write(transcript_string)
