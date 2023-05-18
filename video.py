from moviepy.editor import *
import glob
import subprocess
import os
from datetime import datetime
import random

# take all pngs in a folder and creates a video object
def make_video(folder, clip_duration):
    images = glob.glob(f'{folder}/*.png')
    clips = []
    for img in images:
        image = ImageClip(img).set_duration(clip_duration).resize(width=1024, height=1024)
        clips.append(image)

    video = concatenate_videoclips(clips, method='compose')
    return video

def set_audio(final_video, music, total_duration):
    audio = AudioFileClip(music)
    audio = audio.subclip(0, total_duration)
    audio = audio.volumex(0.6)
    final_video = final_video.set_audio(audio)

    return final_video
today_date = datetime.today().strftime('%Y-%m-%d')

video = make_video(folder= f'C:\\nang\\stable-diffusion-webui\\outputs\\txt2img-images\\{today_date}', clip_duration = 0.3)
# random song
songs = os.listdir('songs')
random_song = random.choice(songs)

video = set_audio(video, music= f'songs\\{random_song}', total_duration= 16)
video.write_videofile(f'vids\\{today_date}_video.mp4', fps=24)

# subprocess.run([f'ffmpeg', '-i', f'vids\\{today_date}_video.mp4', '-vf', 'crop=720:1280', f'vids\\{today_date}_SHORT.mp4'])
# os.remove(f'vids\\{today_date}_video.mp4')