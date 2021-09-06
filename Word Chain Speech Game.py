#!/usr/bin/env python
# coding: utf-8

# In[11]:

import re
from re import sub
import matplotlib.pyplot as plt
import nltk
import random
from nltk.corpus import stopwords
from nltk.corpus import words
from tqdm.notebook import tqdm
import shutil
import os
import numpy as np
from nltk.tokenize import sent_tokenize
from datetime import datetime
import speech_recognition as sr 
import pyttsx3
import warnings
warnings.filterwarnings('ignore')

# In[12]:

nltk.download('words')
len(words.words())


# In[13]:


# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    newVoiceRate = 130
    engine.setProperty('rate',newVoiceRate)
    engine.say(command)  
    engine.runAndWait() 
    


# In[20]:


corp = [word.lower() for word in words.words()]
used = []
# x = input("Enter the Starting Word: ")
with sr.Microphone() as source2: 

    # wait for a second to let the recognizer 
    # adjust the energy threshold based on 
    # the surrounding noise level  
    r.adjust_for_ambient_noise(source2, duration=0.2) 

    #listens for the user's input 
    SpeakText("Say the Starting word")
    print("Say the Starting word: ",end="")
    audio2 = r.listen(source2) 

    # Using ggogle to recognize audio 
    MyText = r.recognize_google(audio2) 
    x = MyText.lower() 

    print(x)
end = x[0] 
while True:
    
    if len(x)>0 and x not in used:

        start = x[-1]
#         print("word -" ,x)
        if x in corp and x[0] == end:
            SpeakText("You said "+x)
            corp.remove(x)
            used.append(x)

            comp_word = random.choice([i for i in corp if i[0]==start and len(x)-3<len(i)<len(x)+2])
            clear_output(wait=True)
            
            print("Computers word :", comp_word)
            SpeakText("Computer says "+comp_word)
            
#             x = input("Enter your word: ")
            
            
            with sr.Microphone() as source2: 

                # wait for a second to let the recognizer 
                # adjust the energy threshold based on 
                # the surrounding noise level  
                r.adjust_for_ambient_noise(source2, duration=0.2) 
                
                try:
                    #listens for the user's input
                    print("Say your word: ",end="")
                    audio2 = r.listen(source2) 

                    # Using google to recognize audio 
                    MyText = r.recognize_google(audio2) 
                    x = MyText.lower() 

                    print(x)
                    SpeakText("You said "+x)
                except:
                    SpeakText("I didn't recognise that!")
                    x = "that"
            end = comp_word[-1]
            

        else:
            break
    else:
        break
    
print("\n\nYour game has ended!!")
SpeakText("Oh no!"+x+" is not a valid word, Your game has ended!")


# In[ ]:




