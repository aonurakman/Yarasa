# Yarasa
# Visual Alert System for Drivers with Hearing Loss

Samsung Innovation Campus: Final Project\
Source Code File w/o Sound Source Localization Function

This project aims to gather and classify the traffic sounds with Raspberry Pi, and later display visually from mobile app to the driver with hearing loss. I hope this will be beneficial for the future works for providing a safe driving for everyone.

Technical Presentation (TR): [Drive Link](drive.google.com/file/d/1MsnYL0TvRR0PxL0HOKPzIwFXduhnYWt8/view?usp=sharing)

URBANSOUND8K DATASET: [Link to Dataset](urbansounddataset.weebly.com/urbansound8k.html)

## File Placement

[Yarasa - Android.rar](https://github.com/aonurakman/Yarasa/blob/main/Yarasa%20-%20Android.rar) may be reviewed on Android Studio, to-be-created .apk file may be installed on an Android device.

[Yarasa-Pi.py](https://github.com/aonurakman/Yarasa/blob/main/Yarasa-Pi.py) file should be located on your Raspberry Pi.

[classifier.h5](https://github.com/aonurakman/Yarasa/blob/main/classifier.h5) , [classifier_weights.data-00000-of-00001](https://github.com/aonurakman/Yarasa/blob/main/classifier_weights.data-00000-of-00001) , [classifier_weights.index](https://github.com/aonurakman/Yarasa/blob/main/classifier_weights.index) , [tran.pkl](https://github.com/aonurakman/Yarasa/blob/main/tran.pkl) shall be placed on the same directory with [Yarasa-Pi.py](https://github.com/aonurakman/Yarasa/blob/main/Yarasa-Pi.py).

## Usage

This project elements are yet to be set for an automatic connection. Following steps shall be followed for a smooth operation.

You need a Raspberry Pi 3+, a ReSpeaker 4-Mic Array for Raspberry Pi and Android smartphone for this system.

Firstly, your Raspberry needs to know how to operate a ReSpeaker. Simply follow the instructions on [ReSpeaker Wiki](https://wiki.seeedstudio.com/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/).\
*Hint*: This process might be a little challenging, but remember that instead of using "sudo ./install.sh", using the following can save your life:\
`sudo ./install.sh --compat-kernel`\
Not my favorite solution, but gets the things done.

On your Raspberry Pi, you should follow instructions given on [Yurockkk's Repistory](https://github.com/Yurockkk/Bluetooth-RPi-Python) to obtain a sucessfull Bluetooth connection between Android & Raspberry Pi. Shout-out to them for the help of their project for establishing the Bluetooth connection between these parts.

Simply run [Yarasa-Pi.py](https://github.com/aonurakman/Yarasa/blob/main/Yarasa-Pi.py) on your Raspberry Pi. If this is your first time running such program on your Pi, you might struggle with libraries for some time, thanks to the limited resources of the Rasbian environment.

The Android device that has the [Yarasa - Android.rar](https://github.com/aonurakman/Yarasa/blob/main/Yarasa%20-%20Android.rar) on it should be connected to your Pi via Bluetooth.

And that should do it. This project is open for improvements, especially for the sound source localization. Together we can build an equally safe, easy, and enjoyable living for everyone.

### Onur

## Major Shout-Outs To

For this incredible dataset, [URBANSOUND8K](https://urbansounddataset.weebly.com/urbansound8k.html)\
Bluetooth connection, Pi side: [Yurockkk's Bluetooth-RPi-Python](https://github.com/Yurockkk/Bluetooth-RPi-Python)\
Bluetooth connection, Android side: [Yurockkk's Bluetooth-RPi](https://github.com/Yurockkk/Bluetooth-RPi)\
Data preprocessing: [Shubham Gupta's work](https://towardsdatascience.com/urban-sound-classification-using-neural-networks-9b6fcd8a9150)


