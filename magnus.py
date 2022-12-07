import speech_recognition as sr
import time
import importlib
import os
import sys
# Komut dosyalarını taramak için commands klasörüne erişim sağlıyoruz
sys.path.append("./commands")
mic = sr.Microphone() 
r = sr.Recognizer()
komutlar = {}

for dosya in os.listdir("commands"):
  # Dosyanın bir Python dosyası olup olmadığını kontrol edin
  if dosya.endswith(".py"):
    # Dosyayı içe aktarın
    modul = importlib.import_module(dosya[:-3])
    # Dosyadaki verileri bir sözlük içine toplayın
    komutlar.update(modul.exec)

def callback(recognizer, audio):
    r.adjust_for_ambient_noise(mic)
    try:
        yazi = r.recognize_google(audio, language="tr-tr")
        yazi = yazi.lower()
        command = " ".join(yazi.split()[1:]).lower()
        
        if yazi.split()[0] == "magnus" or "magnoz" or "magnos": 
          if command in komutlar:
              komutlar[command]["exec"](command.split()[1:])      
          elif command.split()[0] in komutlar:
              komutlar[command.split()[0]]["exec"](" ".join(command.split()[1:]))      


    except sr.WaitTimeoutError:
        print("Dinleme zaman aşımına uğradı")

    except sr.UnknownValueError:
        print("Ne dediğini anlayamadım")

    except sr.RequestError:
        print("İnternete bağlanamıyorum")

r.listen_in_background(mic, callback)
while True: time.sleep(0.1)
