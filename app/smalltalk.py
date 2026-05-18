import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_client = Groq()

def small_talk_chain(query):
    load_dotenv()
    groq_client = Groq()
    prompt = f'''You are a helpful and friendly assistant for an e-commerce website. 
    Answer the user's question in a concise and clear manner. If you don't know the answer, say "I don't know". Don't try to make up an answer.
    
    User's question: {query}
    
    Assistant's answer:'''
    response = groq_client.chat.completions.create(
        model=os.getenv("GROQ_MODEL"),
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()



if __name__ == '__main__':
    query = "How are you?"
    print(small_talk_chain(query))