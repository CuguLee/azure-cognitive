import os
import azure.cognitiveservices.speech as speechsdk
import tkinter as tk

def recognize_from_microphone():
    # credientials
    KEY_1='SUBS_KEY_'
    loc_reg='REGION'
    speech_config = speechsdk.SpeechConfig(subscription=KEY_1, region=loc_reg)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone!")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Recognized: {speech_recognition_result.text}")
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print(f"No speech could be recognized: {speech_recognition_result.no_match_details}")
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print(f"Speech Recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")
            print("Did you set the speech resource key and region values?")

#recognize_from_microphone()

# creating the GUI window
window = tk.Tk()
window.title("Speech to Text")
window.geometry("400x200")

# create a label for the result
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack(pady=20)

# create a button to trigger speech recognition
recognize_button = tk.Button(window, text="Recognize Speech", command=recognize_from_microphone)
recognize_button.pack()

window.mainloop()       # start the GUI event loop