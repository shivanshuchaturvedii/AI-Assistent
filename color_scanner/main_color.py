print("jai shri ram")

import speech_recognition as sr
import pyttsx3
import webbrowser
spre = sr.Recognizer()

def speek(command):
  engine = pyttsx3.init()
  engine.say(command)
  engine.runAndWait()

def command(c):
   if(c.lower() == "open google"):
    webbrowser.open("https://google.com")
   elif(c.lower() == "open youtube"):
    webbrowser.open("https://youtube.com")
   elif(c.lower() == "play mysic"):
    webbrowser.open("https://www.youtube.com/watch?v=kbMinfmC3E0")

if __name__== "__main__":

  speek("Initializing ram ji's assistent....") 
  while True:
    print("Recognizing...")
    try:
      with sr.Microphone() as source2:
        print("listning...")
        audio2 = spre.listen(source2)
        spre.adjust_for_ambient_noise(source2, duration=0.02)

      word = spre.recognize_google(audio2)
      myword = word.lower()

        # print('Did you say: ', myword)
        # speek(myword)
      if (myword == "test colour"):
        speek("Initializing colour picker....") 
        print('Did you say: ', myword)

      elif(myword == "new year"):
        speek("Jai shri ram...")
        with sr.Microphone() as source1:
          print("say...")
          audio1 = spre.listen(source1)
          spre.adjust_for_ambient_noise(source1, duration=2)
          Tell = spre.recognize_google(audio1)
          Tellword = Tell.lower()
          command(Tellword)
          print("your command is: ", Tellword)

    except sr.RequestError as e:
      print('could not wait result; {0}'.format(e))

    except sr.UnknownValueError:
      print('Unknown error occure!')