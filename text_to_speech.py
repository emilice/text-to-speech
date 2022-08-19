from gtts import gTTS
import os

language = input('Dil listesi: \n\n en: İngilizce \n tr: Türkçe \n\nMetni seslendirmek istediğiniz dil kısaltmasını yazınız: ')
myText=input("Metin giriniz: ")
audioInfo = gTTS(text=myText, lang=language, slow=True)
audioInfo.save("record.mp3")
os.system("mpg321 record.mp3")
