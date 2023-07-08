# -*- coding: utf-8 -*-

"""
Created on Wed Mar 31 16:59:29 2021

@author: Ahmet Onur Akman
"""

#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import librosa
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout
import numpy
from pickle import dump

#%%

data=pd.read_csv('C:/Users/asus/Desktop/Projects/Yarasa/Dataset/train.csv')

#%%

mfc=[]
chr=[]
me=[]
ton=[]
lab=[]

#%%

for i in tqdm(range(len(data))):
    f_name='C:/Users/asus/Desktop/Projects/Yarasa/Dataset/Train/'+str(data.ID[i])+'.wav'
    X, s_rate = librosa.load(f_name, res_type='kaiser_fast')
    try:
        t = np.mean(librosa.feature.tonnetz( y=librosa.effects.harmonic(X), sr=s_rate).T,axis=0)
        ton.append(t)
        mf = np.mean(librosa.feature.mfcc(y=X, sr=s_rate).T,axis=0)
        mfc.append(mf)
        l=data.Class[i]
        lab.append(l)
        m = np.mean(librosa.feature.melspectrogram(X, sr=s_rate).T,axis=0)
        me.append(m)
        s = np.abs(librosa.stft(X))
        c = np.mean(librosa.feature.chroma_stft(S=s, sr=s_rate).T,axis=0)
        chr.append(c)   
    except:
        print("[ERROR] ", f_name)  

print("Completed successfully for ", len(ton), " samples.")  
  
#%%
    
mfcc = pd.DataFrame(mfc)
mfcc.to_csv('C:/Users/asus/Desktop/Projects/Yarasa/Dataset/mfc.csv', index=False)
chrr = pd.DataFrame(chr)
chrr.to_csv('C:/Users/asus/Desktop/Projects/Yarasa/Dataset/chr.csv', index=False)
mee = pd.DataFrame(me)
mee.to_csv('C:/Users/asus/Desktop/Projects/Yarasa/Dataset/me.csv', index=False)
tonn = pd.DataFrame(ton)
tonn.to_csv('C:/Users/asus/Desktop/Projects/Yarasa/Dataset/ton.csv', index=False)
la = pd.DataFrame(lab)
la.to_csv('C:/Users/asus/Desktop/Projects/Yarasa/Dataset/labels.csv', index=False)

#%%

features = []
for i in range(len(ton)):
    features.append(np.concatenate((me[i], mfc[i], ton[i], chr[i]), axis=0))
    
#%%
    
la = pd.get_dummies(lab)
label_columns=la.columns #To get the classes
target = la.to_numpy() #Convert labels to numpy array
    
#%%

tran = StandardScaler()
features_train = tran.fit_transform(features) 

#%%

feat_train=features_train[:4285]
target_train=target[:4285]
y_train=features_train[4285:5285]
y_val=target[4285:5285]
test_data=features_train[5285:]
test_label=target[5285:]
len(features)
print("Training",feat_train.shape)
print(target_train.shape)
print("Validation",y_train.shape)
print(y_val.shape)
print("Test",test_data.shape)
print(len(test_label))

#%%
    
model = Sequential()

model.add(Dense(512, input_shape=(166,), activation = 'relu'))
model.add(Dropout(0.3))

model.add(Dense(512, activation = 'relu'))
model.add(Dropout(0.3))

model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.3))

model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.3))

model.add(Dense(10, activation = 'softmax'))

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='Adam')

model.summary() 
   
#%%

history = model.fit(feat_train, target_train, batch_size=64, epochs=50, validation_data=(y_train, y_val))

#%%

print(history.history.keys())

# accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='lower right')
plt.show()

# loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper right')
plt.show()

#%%

model.evaluate(x=test_data, y=test_label, batch_size=64)
prediction = model.predict_classes(test_data)
classes = ["air_conditioner", "car_horn", "children_playing", "dog_bark", "drilling", "engine_idling", "gun_shot", "jackhammer", "siren", "street_music"]
for x in prediction:
    print(classes[x])
    
#%%
    
model.save_weights('classifier_weights')
model.save('classifier.h5')
dump(tran, open('tran.pkl', 'wb'))
print("Saving the model as classifier.h5")