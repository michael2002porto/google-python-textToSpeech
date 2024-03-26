import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 220)     # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
# for voice in voices: 
    # print(voice)
    # to get the info. about various voices in our PC  
    # print("Voice:") 
    # print("ID: %s" %voice.id) 
    # print("Name: %s" %voice.name) 
    # print("Age: %s" %voice.age) 
    # print("Gender: %s" %voice.gender) 
    # print("Languages Known: %s" %voice.languages) 

"""GENDER"""
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

"""LANGUAGE"""
# engine.setProperty('voice', voices[0].id)

engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('JAKARTA, KOMPAS.com - Gempa bumi magnitudo 6,5 terjadi di Tuban, Jawa Timur, Jumat (22/3/2024) pukul 15.52 WIB. Tepatnya di 130 kilometer timur laut Tuban. Berdasarkan data Badan Meteorologi, Klimatologi, dan Geofisika (BMKG), kedalaman gempa mencapai 10 kilometer. Getarannya terasa hingga wilayah Jakarta, salah satunya di Menara Kompas, Palmerah Selatan, Jakarta Pusat. Baca juga: Gempa M 6,5 Guncang Tuban, Getaran Terasa sampai Solo 'Iya lagi di kantor, lagi kerja di depan meja, tiba-tiba terasa seperti diayun-ayun,' ujar seorang karyawan bernama Sakina (34) kepada Kompas.com, Jumat. 'Di sekitar juga langsung ramai, 'Gempa, gempa', gitu,' imbuh dia. Dalam akun X BMKG, disebutkan bahwa gempa ini tidak berpotensi tsunami. 'Hati-hati terhadap gempa bumi susulan yang mungkin terjadi,' bunyi peringatan BMKG di situs webnya.', 'test.mp3')
engine.runAndWait()