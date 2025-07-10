from openai import OpenAI
import json
import re
client = OpenAI()

def ideafy():
    with open('./backend/messages.json', 'r', encoding='utf-8') as f:
        prompt = json.load(f)

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=prompt
    )

    clean = re.sub(r"^```(?:json)?\s*|\s*```$", "", response.choices[0].message.content, flags=re.MULTILINE)
    data = json.loads(clean)

    with open('./backend/ideas.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
