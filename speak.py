import pyttsx3
engine = pyttsx3.init() # object creation
def speaker(d):
 rate = engine.getProperty('rate')   # getting details of current speaking rate
 print (rate)                        #printing current voice rate
 engine.setProperty('rate', 135)     # setting up new voice rate

 voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
 engine.setProperty('voice', voices[14].id)   #changing index, changes voices. 1 for female


 engine.say(d)
 engine.runAndWait()
 engine.stop()
