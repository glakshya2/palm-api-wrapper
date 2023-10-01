import google.generativeai as palm

def chat(palm, model):
    
    print('Do you wish to provide any context? [y/n]')
    choice = input()
    
    if choice == 'y':
        print('Please provide context: ')
        context = input()
        print('First message:')
        prompt = input()
        response = palm.chat(context = context, messages = prompt, temperature = 0)
    else:
        print('First message:')
        prompt = input()
        response = palm.chat(messages = prompt, temperature = 0)
    
    while(prompt != 'quit'):
        print('palmAI:\n' + response.last)
        print('You:')
        prompt = input()
        if prompt != 'quit':
            response = response.reply(prompt)
        
    print(response.messages)
        