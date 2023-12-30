from moviepy.editor import *
from mutagen.mp3 import MP3
from get_videos import *
import time

def make_vid(niche):
    id_videos = download_videos(8, niche)
    resized_clips = {}

    for video_id in id_videos:
        clip = VideoFileClip(f'{video_id}.mp4')
        resized_clip = clip.fx(vfx.resize, width=1080)
        resized_clips[video_id] = resized_clip

    final_clip = concatenate_videoclips([resized_clips[video_id] for video_id in id_videos], method="compose")

    audioclip = AudioFileClip('voice_over.mp3')
    voice_over = MP3('voice_over.mp3')
    durvid = final_clip.duration
    durvoice = voice_over.info.length
    if durvid >= durvoice:
        halfdiff = (durvid - durvoice) / 2
        final_clip = final_clip.subclip(halfdiff, durvid - halfdiff)
        final_clip = final_clip.set_audio(audioclip)
    else:
        id = download_videos(1, niche)
        clip_id = VideoFileClip(f'{id[0]}.mp4')
        final_clip = concatenate_videoclips([final_clip, clip_id])
        duration_new = final_clip.duration
        new_halfdiff = (duration_new - durvoice) / 2
        final_clip = final_clip.subclip(new_halfdiff, duration_new - new_halfdiff)
        final_clip = final_clip.set_audio(audioclip)
        
    final_clip.write_videofile('final.mp4')

