from gtts import gTTS
import os
from playsound import playsound
myText="i love you manali"

language='en'

output=gTTS(text=myText,lang=language,slow=False)

output.save("test.mp3")

# os.system("start test.mp3")
playsound('test.mp3')