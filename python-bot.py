# - *- coding: utf- 8 - *-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from article_list import create_categorized_list
from ts import generate_summary
import pickle

BOT_TOKEN = '*********************************************'
category_list = ["finance", "sports", "politics", "tech", "entertainment"]

def start(bot, update):
  update.message.reply_text("Hello! I'm a News Summarizer bot. Nice to meet you!")
  update.message.reply_text("Preparing news articles... Please wait")
  news_list = create_categorized_list()
  with open('news_list.pkl', 'wb') as f:
    pickle.dump(news_list, f)
  update.message.reply_text("To get news articles summarized, type /news <category_name>")

def news(bot, update):
  words = update.message.text.split(" ")
  category_name = words[1].lower()
  if category_name not in category_list:
    update.message.reply_text("Not in list")
  else:  
    update.message.reply_text("Summarizing articles ... ")
    with open('news_list.pkl', 'rb') as f:
      news_list = pickle.load(f)
      specific_list = []
      for i in range(len(news_list)):
        if(news_list[i]['scores']['taxonomy'][0]['tag'] == category_name):
          specific_list.append({
            'summary': generate_summary(news_list[i]['article'], 2),
            'category': category_name
            })

      for i in range(len(specific_list)):
        update.message.reply_text(specific_list[i]['summary'])

def send_invalid_message(bot, update):
  update.message.reply_text("Invalid text : " + update.message.text)

def unknown(bot, update):
  update.message.reply_text("Sorry, I didn't understand that command.")

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater(BOT_TOKEN)
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  news_handler = CommandHandler('news', news)
  invalid_handler = MessageHandler(Filters.text, send_invalid_message)
  unknown_handler = MessageHandler(Filters.command, unknown)
  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(news_handler)
  dispatcher.add_handler(invalid_handler)
  dispatcher.add_handler(unknown_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()