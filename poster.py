import telebot
import sys
import os

try:
  
  chat_id = int(sys.argv[1])
  file = str(chat_id)+'.png'
  ربات   =   تله  ربات . TeleBot ( "6289066233:AAHibW5dbPYnvcopqlOWDHE7uOTN3XifNoo" )
  img = open(file, 'rb')
  bot.send_photo(chat_id, img)
  os.remove(file)

except:
  pass
