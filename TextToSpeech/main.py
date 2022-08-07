import pyttsx3
you = input("Your Name : ")
bot = pyttsx3.init()                    # object creation
speech_rate = 180
""" RATE"""
rate = bot.getProperty('rate')          # getting details of current speaking rate
print (rate)                            # printing current voice rate
bot.setProperty('rate', speech_rate)            # setting up new voice rate

"""VOLUME"""
volume = bot.getProperty('volume')      # getting to know current volume level (min=0 and max=1)
print (volume)                          # printing current volume level
bot.setProperty('volume',1.0)           # setting up volume level  between 0 and 1

"""VOICE"""
voices = bot.getProperty('voices')      #getting details of current voice
#bot.setProperty('voice', voices[0].id) #changing index, changes voices. o for male
bot.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female


bot.say("Hello "+ you)
bot.say("I am your personal assistant")
bot.say("I can do anything for you")
bot.say('My current speaking rate is ' + str(rate) + "But you configured my speech as " + str(speech_rate))
bot.say("I can speak in male voice as well as female voice")
bot.say("This is a sample speech in female voice")
bot.setProperty('voice', voices[0].id) #changing index, changes voices. o for male
bot.say("This is a sample speech in male voice")
bot.say("Thank you "+ you)
bot.say("Will meet you again")
bot.runAndWait()
bot.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
bot.save_to_file('Hello '+you+ ' I am you virtual Assistant', 'test.mp3')
bot.runAndWait()
