import pyttsx3
import datetime
import os

pyttsx3.speak("Hola! I am your mini chatbot \t friend  Please enter your name")
print("Please enter your name here :", end = " ")
name = input()
x = datetime.datetime.now()
hour = int(x.strftime("%H"))
if (hour<12):
  greeting = "Good Morning !"
elif(hour<17):
  greeting = "Good AfterNoon !"
else:
  greeting = "Good Evening !"
pyttsx3.speak( greeting + name +"   How are you?")
mood = input()
if (("fine" in mood or "good" in mood or "great" in mood or "alright" in mood) and ("not" not in mood)) and ("how" in mood or "How" in mood):
    pyttsx3.speak("I am awesome Thanks!!  What you want to explore today?")
elif ("fine" in mood or "good" in mood or "great" in mood or "alright" in mood) and ("not" not in mood):
   pyttsx3.speak("Thats great!!  What you want to explore today?")
else:
    pyttsx3.speak("Exploring these activities will definitely make you happy.")
i=0
flag = True
while(i>=0):
   print()
   if flag == False:
       flag = True
       i=0
   if( i ==0 ):
     print("--------------------------------------------------------------------------------", end = "\n\n")
     print("-> Do you want to search something on chrome?")
     print("-> Do you want to watch a movie / listen a song?")
     print("-> Do you want to write something?")
     print("-> Do you want to make a presentation?")
     print("-> Do you want to paint?")
     print("-> Do you want to use calculator?")
     print("-> Do you want to open file explorer?")
     print("-> Do you want to magnify screen?")
     print("-> Do you want to know system information?")
     print("-> Do you want to exit?", end = "\n\n")
     pyttsx3.speak("  What can I help you with??")
     i=i+1
   elif flag==True:
     pyttsx3.speak("Nice choice!!" + name +"  Tell me What next you want to do?")
   
   print("Please enter your request here:" , end = " ")
   request = input()
   if ("Thank you" in request or "thank" in request):
      pyttsx3.speak("Welcome! I am happy to help you")
      print("Please enter your request here:" , end = " ")
      request = input()
   if ("exit" or "quit") in request:
       pyttsx3.speak("GoodBye!"+name+"\t\t see you soon!")
       break
   elif ("search" in request or ("open" in request or "execute" in request or "run" in request) and ("chrome" in request or "internet" in request or "search engine" in request)):
       os.system("chrome")
   elif ("listen" in request or "play" in request or "watch" in request or "hear" in request or "see" in request) and ("movie" in request or "song" in request or "music" in request):
       os.system("wmplayer")
   elif ("write" in request and ("wordpad" not in request and "notepad" not in request)):
       pyttsx3.speak("Do you want to write in Wordpad or notepad?")
       request = input()
       if("wordpad" in request):
          os.system("wordpad")
       elif("notepad" in request):
         os.system("notepad")
   elif ("run" in request or "execute" in request or "open" in request) and "wordpad" in request:
       os.system("wordpad")
   elif ("run" in request or "execute" in request or "open" in request) and ("notepad" in request or "text editor" in request ):
      os.system("notepad")
   elif ("make" in request or "open" in request or "start" in request) and ("presentation" in request or "MSPowerpoint" in request):
      os.system("POWERPNT")
   elif ("draw" in request or "paint" in request or("make" in request and ("drawing" in request or "painting" in request ))):
      os.system("mspaint")
   elif ("use" in request or "do" in request or "solve" in request or "perform" in request or "open" in request) and ("sums" in request or "problems" in request or "calculations" in request or "calculator" in request):
      os.system("calc")
   elif ("open" in request or "run" in request or "start" in request) and ("explorer" in request):
      os.system("explorer")
   elif ("magnify" in request or "zoom" in request):
      os.system("magnify")
   elif ("see" in request or "get" in request or "know" in request) and ("information" in request or "system" in request):
      os.system("msinfo32")
   else:
      pyttsx3.speak("Sorry! I can't perform that. Please tell me some other activity from the menu")
      flag = False
  

