# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# # The text that you want to convert to audio 
# mytext = 'How to Make Your Crush Fall in Love with You in 30 Seconds'
# output_path = 'welcome.mp3'

def google_tts(mytext, output_path):

    # Language in which you want to convert 
    language = 'id'

    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named 
    # welcome 
    myobj.save(output_path)

# google_tts(mytext, output_path)