import telebot
from telebot import types

TOKEN = '7182329668:AAFyuv79NfJTFivXp8TOfFKeTGfP6X8nEq0'
bot = telebot.TeleBot(TOKEN)
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False)
start_keyboard.add(types.KeyboardButton(text="Начать"))
options_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=False)
options_keyboard.add(types.KeyboardButton(text="Option 1"))
options_keyboard.add(types.KeyboardButton(text="Option 2"))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы начать.", reply_markup=start_keyboard)


@bot.message_handler(func=lambda message: message.text == "Начать")
def handle_start(message):
    bot.send_message(message.chat.id, "Выбери опцию:", reply_markup=options_keyboard)


@bot.message_handler(func=lambda message: message.text in ["Option 1", "Option 2"])
def handle_option(message):
    option = message.text
    bot.send_message(message.chat.id, f"Ты выбрал {option}. Теперь напиши свое сообщение.")
    bot.register_next_step_handler(message, handle_message, option)


def handle_message(message, option):
    with open(f'{option}.txt', 'w', encoding="utf-8") as file:
        file.write(message.text + '\n')
    bot.send_message(message.chat.id, "Сообщение записано!")


bot.polling()