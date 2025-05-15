from openai import OpenAI

def call_gpt_review(code: str):
    prompt = f"""다음 코드를 읽고 개선할 수 있는 부분을 제안해줘:\n\n{code}"""
    
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
