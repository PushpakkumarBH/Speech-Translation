import wave
from pydub import AudioSegment
from pydub.playback import play
# obj_new=wave.open('hitesh.wav','wb')
# obj_new.setnchannels(1)
# obj_new.setsampwidth(2)
# obj_new.setframerate(22050)
# obj_new.setnframes(1000)
# obj_new.writeframes(b'ab')
# obj_new.close()


sound = AudioSegment.from_file('/Users/pushpak/Downloads/fn1.wav', format="wav")
sound = sound.set_frame_rate(22050)
sound = sound.set_channels(1)
sound = sound.set_sample_width(2)

sound.export(out_f = "train.wav",format = "wav")
obj=wave.open('testvoice.wav','rb')
print(obj.getframerate())
print(obj.getnframes())
t_audio=obj.getnframes()/obj.getframerate()
print('audio duration',t_audio)
obj.close()