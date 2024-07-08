from youtube_transcript_api import YouTubeTranscriptApi
import os

# Obtain the directory where the script is
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Result.txt')

# Youtube Vid parameter
video_id = 'KRjyYh9Fd5w'

# String holder
transcript_string = ''

# Get the video transcript
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
    # print("Transcripción obtenida en español.")

except Exception as e:
    # print(f"Error al obtener la transcripción en español: {e}")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'en'])
        # print("Transcripción obtenida en inglés.")

    except Exception as e:
        print(f"Error al obtener la transcripción en inglés: {e}")
        transcript = []


# Populate the string holder with the actual video's transcript
for entry in transcript:
    transcript_string += f"{entry['start']:.0f}s: {entry['text']}\n"


# Save the file
try:    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(transcript_string)

    print(f"Transcripción guardada en {file_path}")

except Exception as e:
    print(f"Error al escribir en el archivo: {e}")