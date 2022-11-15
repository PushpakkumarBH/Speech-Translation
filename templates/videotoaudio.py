import moviepy.editor as mp
from pydub import AudioSegment
def video_to_audio():
    my_clip = mp.VideoFileClip(r"videotest.mov")
    my_clip.audio.write_audiofile(r"my_result.mp3")

video_to_audio()




def mp3_to_wav():

  # files                                                                         
  src = "E:\finalproject\my_result.mp3"
  dst = "testf.wav"

  # convert wav to mp3                                                            
  sound = AudioSegment.from_mp3(r"E:\finalproject\my_result.mp3")
  sound.export(dst, format="wav")

mp3_to_wav()