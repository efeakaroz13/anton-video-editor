import os
import wave
import matplotlib.pyplot as plt
import numpy as np

filenamemp3 = input("Enter a mp3 file:")
try:
	os.system(f"rm {filenamemp3.replace('.mp3','wav')}")
except:
	pass

os.system(f"ffmpeg -i {filenamemp3} -acodec pcm_u8 -ar 22050 {filenamemp3.replace('.mp3','')}.wav")

thefile = wave.open(f"{filenamemp3.replace('.mp3','.wav')}","rb")
n_samples = thefile.getnframes()
signal_wave = thefile.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
l_channel = signal_array[0::2]
n_channels = thefile.getnchannels()
sample_freq = thefile.getframerate()
t_audio = n_samples/sample_freq
times = np.linspace(0, n_samples/sample_freq, num=n_samples)
plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Left Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()


