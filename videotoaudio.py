import moviepy.editor as mp

my_clip = mp.VideoFileClip(r"videotest.mov")
my_clip.audio.write_audiofile(r"my_result.mp3")

# import required modules
import subprocess

# convert mp3 to wav file
subprocess.call(['ffmpeg', '-i', 'my_result.mp3',
				'converted_to_wav_file.wav'])

