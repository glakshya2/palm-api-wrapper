import google.generativeai as palm

def text(palm, model):
    print('Enter prompt:')
    prompt = input()
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # stop_sequences=['</calc>'],
        # The maximum length of the response
        max_output_tokens=800,
    )
    print(completion.result)
    
#    try:
#        response, equation = completion.result.split('<calc>', maxsplit=1)
#        print('Response:')
#        print(response)
#        print('Equation:')
#        print(equation)
#    except Exception: