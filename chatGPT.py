from openai import OpenAI
client = OpenAI(api_key="API_KEY")

messages = [
    {
        "role": "system",
        "content": "Create a concise title by summarizing the following user request. Limit the title to just a few key phrases. When no specific request provided, you may create title as 'New chat'"
    },
    {
        "role": "user",
        "content": "plan about trial"
    }
]
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=messages
)

print(completion.choices[0].message.content.replace('"', '').split(":")[-1].strip())


# engine = "text-davinci-003"

# openai.api_key = api_key
# response = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=100)

# print(response.choices[0].text.strip())
