import google.generativeai as palm
import text, chat
from api_key import KEY

palm.configure(api_key=KEY)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print('model = ' + model)
print('Select mode:')
print('1. Text')
print('2. Chat')
choice = int(input())

if choice == 1:
    text.text(palm, model)
else:
    chat.chat(palm, model)
