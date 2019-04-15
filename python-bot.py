# - *- coding: utf- 8 - *-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '*****************************(telegram-bot-token)'

def start(bot, update):
  update.message.reply_text("Hello! I'm a News Summarizer bot. Nice to meet you!")
  update.message.reply_text("To get news articles summarized, type /news <category_name>")

def news(bot, update):
  words = update.message.text.split(" ")
  category_name = words[1]
  update.message.reply_text(category_name)

def send_invalid_message(bot, update):
  update.message.reply_text("Invalid text : " + update.message.text)

def unknown(bot, update):
  update.message.reply_text("Sorry, I didn't understand that command.")

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater(TOKEN)
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