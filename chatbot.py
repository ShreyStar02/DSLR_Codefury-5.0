import requests

key = "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"
context = text = "The following is a conversation with Fred. Fred is an intelligent AI Chatbot for a website named Codefury. Fred was developed by Team DSLR. Codefury is a website used by Startups or Individuals to post their works so that, investors may have a look and provide funding based on the idea. Fred can be used to learn about the website and can also give tips to users based on their interest as on what can they learn or do further to improve their resume or to gain investors' attraction. Fred should introduce itself at the beginning of the conversation \n\nAI: "

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + key
}


def dermatologist(text, context):
    json_data = {
        'model': 'text-davinci-002',
        'prompt': context + text,
        'temperature': 0.9,
        'max_tokens': 250,
        'stop': ["Human: ", "AI: "],
    }
    response = requests.post('https://api.openai.com/v1/completions', auth=(
        '', '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'), json=json_data, headers=headers)
    response = response.json()
    return response['choices'][0]['text']


while text != "bye":
    reply = dermatologist(text, context)
    context = context + "\n" + reply
    print(reply)
    text = input("You: ")
    context = context + "\nHuman: " + text + "\nAI: "

# print("\n\n")
# print(context)
