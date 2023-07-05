import pyttsx3
text_speech=pyttsx3.init()
while True:
    text=input("write your text")
    if text=="q":
        print("thanks for using")
        break

    text_speech.say(text)
    text_speech.runAndWait()
