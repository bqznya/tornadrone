import g4f
from g4f.Provider import (
    GeekGpt,
    Liaobots,
    Phind,
    Raycast,
    RetryProvider)
from g4f.client import Client
import nest_asyncio
nest_asyncio.apply()

client = Client(
    provider = RetryProvider([
            g4f.Provider.Liaobots,
            g4f.Provider.GeekGpt,
            g4f.Provider.Phind,
            g4f.Provider.Raycast
    ])
  )
chat_history = [{"role": "user", "content": 'Отвечай на русском языке'}]


def send_request(message):
    global chat_history
    chat_history[0]["content"] += message + " "

    try:
        response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=chat_history
    )
    except Exception as err:
        print("Все провайдеры не отвечают, попробуйте позже")
    print(response)
    chat_history[0]["content"] += response + " "
    return response

while True:
    user_input = input("\n You: ")
    if user_input.lower() == 'exit':
        break
    else:
        send_request(user_input)