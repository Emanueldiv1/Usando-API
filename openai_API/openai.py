import openai

openai.api_key = "SUA CHAVE DA API"


def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2080,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()


prompt = input('Digite sua pergunta para o ChatGPT: \n')
print(generate_text(prompt))
