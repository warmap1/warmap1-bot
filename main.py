import cfg
import kb
import telebot as tb

bot = tb.TeleBot(cfg.TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Hi! Here you can learn more about me, get in touch, find useful links, and stay updated with the latest news. Choose an option below! Also, check out [source code on github](https://github.com/warmap1/warmap1-bot)', reply_markup=kb.menu, parse_mode='Markdown', disable_web_page_preview=True)

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def text(m):
    if m.text in kb.texts:
        if m.text == '📝About me':
            bot.send_message(m.chat.id, "I'm a Python bot developer. I live in Russia. I love playing games. I use ArchLinux (btw) (if someone needs - you can contact me for any help with Linux).")
        elif m.text == '✉️Contact me':
            bot.send_message(m.chat.id, 'Discord: warmap1\nMatrix: @warmap1:matrix.org')
        elif m.text == '🔗Links':
            bot.send_message(m.chat.id, 'My [GitHub](https://github.com/warmap1)', parse_mode='Markdown', disable_web_page_preview=True)
        elif m.text == "📰Bot's news":
            bot.send_photo(m.chat.id, 'https://media.discordapp.net/stickers/1101215267763277844.webp?size=160&quality=lossless')

# Запуск бота
bot.polling(none_stop=True)
