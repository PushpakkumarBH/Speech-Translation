#Removing audio from video 

from moviepy.editor import VideoFileClip
final_video= VideoFileClip("video.mp4").without_audio()
final_video.write_videofile("output.mp4",fps=60)