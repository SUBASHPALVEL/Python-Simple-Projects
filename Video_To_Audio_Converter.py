# 1 Importing statement

import moviepy.editor as mp

# 2 Getting the video file

Clip = mp.VideoFileClip("Variables.mp4")

# 3 Producing the audio

Clip.audio.write_audiofile("my Audio.mp3")