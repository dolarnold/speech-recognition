import speech_recognition as sr #imports the SR module
import time
from PyDictionary import PyDictionary #imports dictionary module to check word meanings
from googletrans import Translator #imports function to translate words to any language
translator = Translator() #assigns Translator function to var name translator
dictionary = PyDictionary() #assigns PyDictionary function to var name dictionary

#all these are lists containing words that may be said by user
said = ['hi','hello']
question = ['what time is it','what\'s the time',]
meaning = ['meaning']
ctime = time.asctime( time.localtime(time.time()) )
quit = ['stop','exit','quit']
trans = ['translate']

#main function
def rec():
     while True: #loops the code block below until the user says 'stop' or 'quit'
        r = sr.Recognizer() #assigning recognizer class to var name r
        print("Say something")
        with sr.Microphone() as source: #opens the microphone 
            r.adjust_for_ambient_noise(source) #enables code tollerate other noises captured 
            audio = r.listen(source) #listens audio from mic
            txt = r.recognize_google(audio) #recognize audio from mic
            try: #this code block is for error handling
                print(txt)
                #said.append(r.recognize_google(audio))
            except:#if an error occurs in above code block it skips and prints the below error
                print("Cannot understand audio!!Try again...")

        if  txt in said:#this code block checks if what is said by user is in any of  the lists above and executes accordingly
            print(txt +" too.")

        elif txt in question:
            print (ctime)

        elif txt in quit:
            print("Bye")
            time.sleep(1)#delays program closure by 1sec
            exit()#this exits program if user says words in list quit above
        elif txt in meaning:
            print("Say word")
            with sr.Microphone() as source:
                word = r.listen(source)
                wrd = r.recognize_google(word)
                print(wrd)
                print(dictionary.meaning(wrd)) #checks meaning of word said and prints to screen
        elif txt in trans:
            print("Say the word to translate")
            with sr.Microphone() as source:
                word1 = r.listen(source)
                word2 = r.recognize_google(word1)
                print("You have said >>"+word2)
                translated_word = translator.translate(word2)
                print(translated_word)
            #break
rec()