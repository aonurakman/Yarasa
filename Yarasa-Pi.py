# -*- coding: utf-8 -*-
from tensorflow.keras.models import load_model
import numpy as np
import librosa
from pickle import load
import pyaudio
import wave
import serial
import time
import threading

#%%
 
RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 4 
RESPEAKER_WIDTH = 2
RESPEAKER_INDEX = 0  # refer to input device id
CHUNK = 1024
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"

model = load_model('classifier.h5', compile = False)
model.load_weights('classifier_weights')
tran = load(open('tran.pkl', 'rb'))
classes = ["air_conditioner", "car_horn", "children_playing", "dog_bark", "drilling", "engine_idling", "gun_shot", "jackhammer", "siren", "street_music"]

ble_comm = None
 
#%%

class SerialComm:
    def __init__(self):
        self.port = serial.Serial("/dev/rfcomm0", baudrate=9600, timeout=1)
 
    def send_serial(self, text):
        self.port.write(text.encode())
		
#%%

def inToSend(msg):
	global ble_comm
	try:
		ble_comm = SerialComm()
		ble_comm.send_serial(msg) 
	except serial.SerialException:
		print("Waiting for connection")
	
#%%
def main():
	global ble_comm
	connected = False
	while(connected == False):
		try:
			ble_comm = SerialComm()
			connected = True
		except serial.SerialException:
			print("Waiting for connection")
			time.sleep(1)
		
	print("Connected!")
			
	while(True):
		p = pyaudio.PyAudio()
		 
		stream = p.open(
					rate=RESPEAKER_RATE,
					format=p.get_format_from_width(RESPEAKER_WIDTH),
					channels=RESPEAKER_CHANNELS,
					input=True,
					input_device_index=RESPEAKER_INDEX,)
		
		print("*****RECORDING******")
		 
		frames = []
		 
		for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)
		
		print("******DONE RECORDING******")
		 
		stream.stop_stream()
		stream.close()
		p.terminate()
		 
		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(RESPEAKER_CHANNELS)
		wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
		wf.setframerate(RESPEAKER_RATE)
		wf.writeframes(b''.join(frames))
		wf.close()
		
		
		f_name='output.wav'
		X, s_rate = librosa.load(f_name, res_type='kaiser_fast')
		mf = np.mean(librosa.feature.mfcc(y=X, sr=s_rate).T,axis=0)
		try:
			t = np.mean(librosa.feature.tonnetz(
						   y=librosa.effects.harmonic(X),
						   sr=s_rate).T,axis=0)
		except:
			print(f_name)  
		m = np.mean(librosa.feature.melspectrogram(X, sr=s_rate).T,axis=0)
		s = np.abs(librosa.stft(X))
		c = np.mean(librosa.feature.chroma_stft(S=s, sr=s_rate).T,axis=0)
		
		feature = [np.concatenate((m, mf, t, c), axis=0) ]
		feat = tran.transform(feature) 
		
		prediction = model.predict(feat)[0]
		print("This is predicted to be ", classes[np.where(prediction == max(prediction))[0][0]], " with the possibility of ", max(prediction))
		
		msg = "0:none" 
		if (max(prediction)>0.9):
			msg = "1:" + classes[np.where(prediction == max(prediction))[0][0]]			
			
		thread = threading.Thread(target = inToSend, args = (msg,))
		thread.start()
	
#%%
if __name__ == "__main__":
    main()


