from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://b3openai26.openai.azure.com/",
    api_key="99rhZPQ356tKQnu3IOtAwk49HeWD3eSL10DyYkKcTmMxQqyG0kQdJQQJ99CCACL93NaXJ3w3AAABACOGC05k",
)

def summarize(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a legal assistant."},
            {"role": "user", "content": f"Summarize this legal document:\n{text}"}
        ]
    )
    return response.choices[0].message.content

def extract_clauses(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Extract important legal clauses."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

def check_compliance(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Check compliance issues in legal document."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content