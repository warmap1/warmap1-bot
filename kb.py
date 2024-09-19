from telebot import types

texts = ['📝About me', "✉️Contact me", "🔗Links", "📰Bot's news"]

menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
about_me = types.KeyboardButton('📝About me')
contacts = types.KeyboardButton("✉️Contact me")
links = types.KeyboardButton("🔗Links")
news = types.KeyboardButton("📰Bot's news")
menu.add(about_me, contacts, links, news)