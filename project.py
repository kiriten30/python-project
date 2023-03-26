import speech_recognition as sr
import webbrowser as wb
import os
import cv2
import numpy as np
kernal = np.ones((5,5),np.uint8)
webcam= cv2.VideoCapture(0)
webcam.set(3,640)
webcam.set(4,480)
webcam.set(10,100)

# obtain audio from the microphone  
r = sr.Recognizer()  
with sr.Microphone() as mic:  
   print("Please wait. Calibrating microphone...")
   # listen for 2 seconds and create the ambient noise energy level  
   r.adjust_for_ambient_noise(mic, duration=2)  
   print("Say something!")  
   audio = r.listen(mic)  

# recognize speech 
try:
    # Using Google 
    text = r.recognize_google(audio)
    print("I think you said '" + text + "'")
    text="".join(text).lower()
   

# if speech==1-9 or"one"-"nine" then open file which you want to open
    if text=="play music":
        os.startfile(r"F:\music\Daru Badnam Kardi.mp3")
    elif text=="open calculator":
        os.startfile(r"C:\Windows\System32\calc.exe")
    elif text=="open youtube":
        wb.open_new("www.youtube.com")
    elif text=="prettiest person in the world":
        while True:
            success,img= webcam.read()
            flip = cv2.flip(img,1)
            cv2.imshow("Webcam",flip)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    elif text=="play stand up comedy":
        wb.open_new("https://youtu.be/KBZfnt80s54")
    elif text=="open whatsapp":
        wb.open_new("https://web.whatsapp.com/")
    elif text=="7":
        os.startfile(r"")
    elif text=="8":
        os.startfile(r"")
    elif text=="9":
        os.startfile(r"")    
    #else Search it on google
    else:
        f_text='https://www.google.co.in/search?q=' + text
        wb.open_new(f_text)    
        
        
except sr.UnknownValueError:  
   print("I could not understand audio")  
except sr.RequestError as e:  
   print(f"error; {e}")

except Exception as e:
   print (e)