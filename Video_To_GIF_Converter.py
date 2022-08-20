# 1 Import statements

from moviepy.editor import *

# 2 Getting the Video

video = VideoFileClip("Video_Name.mp4")

# 3 Converting video into gif
video.write_gif("My_Video.gif")