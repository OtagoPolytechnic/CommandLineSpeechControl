import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:              
     audio = r.listen(source)
      	
x = 1

while True:	                  
    try:  
        print(r.recognize_google(audio) + "\n") 
        x += 1
        break
        
    except LookupError:                           	
        print("Could not understand audio")