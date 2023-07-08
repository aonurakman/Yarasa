# Yarasa
# Visual Alert System for Drivers with Hearing Loss

Samsung Innovation Campus: Final Project\
Source Code File w/o Sound Source Localization Function

![Overview](https://i.hizliresim.com/a3xxtnz.PNG)

This project aims to gather and classify the traffic sounds with Raspberry Pi, and later display them visually from a mobile app to the driver with hearing loss. I hope this will be beneficial for future work for providing safe driving for everyone.

URBANSOUND8K DATASET: [Link to Dataset](https://urbansounddataset.weebly.com/urbansound8k.html)

## What's included?

[Yarasa - Android.zip](https://github.com/aonurakman/Yarasa/blob/876aeb5e36355f34804774808dd330efb2b052db/Yarasa%20-%20Android.zip) is to-be-created .apk file may be installed on an Android device.

Contents of [Yarasa - Pi](https://github.com/aonurakman/Yarasa/tree/876aeb5e36355f34804774808dd330efb2b052db/Yarasa%20-%20Pi) should be placed on a directory of your choice on your Raspberry Pi.

## Usage

These project elements are yet to be set for an automatic connection. Following steps shall be followed for a smooth operation.

You need a Raspberry Pi 3+, a ReSpeaker 4-Mic Array for Raspberry Pi, and an Android smartphone for this system.

Firstly, your Raspberry needs to know how to operate a ReSpeaker. Simply follow the instructions on [ReSpeaker Wiki](https://wiki.seeedstudio.com/ReSpeaker_4_Mic_Array_for_Raspberry_Pi/).\
*Hint*: This process might be a little challenging, but remember that instead of using "sudo ./install.sh", using the following can save your life:\
`sudo ./install.sh --compat-kernel`\
Not my favorite solution, but gets things done.

On your Raspberry Pi, you should follow the instructions given on [Yurockkk's Repistory](https://github.com/Yurockkk/Bluetooth-RPi-Python) to obtain a successful Bluetooth connection between Android & Raspberry Pi. Shout-out to them for the help of their project for establishing the Bluetooth connection between these parts.

Simply run [Yarasa-Pi.py](https://github.com/aonurakman/Yarasa/blob/main/Yarasa-Pi.py) on your Raspberry Pi. If this is your first time running such a program on your Pi, you might struggle with libraries for some time, thanks to the limited resources of the Rasbian environment.

The Android device that has the [Yarasa - Android.rar](https://github.com/aonurakman/Yarasa/blob/main/Yarasa%20-%20Android.rar) on it should be connected to your Pi via Bluetooth.

And that should do it. This project is a very basic first step, and certainly open for improvements, especially for sound source localization. Together we can build an equally safe, easy, and enjoyable living for **everyone**.

### Onur

## Major Shout-Outs To

For this great dataset, [URBANSOUND8K](https://urbansounddataset.weebly.com/urbansound8k.html)\
Bluetooth connection, Pi side: [Yurockkk's Bluetooth-RPi-Python](https://github.com/Yurockkk/Bluetooth-RPi-Python)\
Bluetooth connection, Android side: [Yurockkk's Bluetooth-RPi](https://github.com/Yurockkk/Bluetooth-RPi)\
Signal processing: [Shubham Gupta's work](https://towardsdatascience.com/urban-sound-classification-using-neural-networks-9b6fcd8a9150)


