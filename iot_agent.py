import base64
import requests
import sys
import time
from github import Github


token = "TOKEN"

url = "http://localhost:11434/api/generate"

f = open("agent_prompt_template.txt", "r")

prompt_template = f.read()

if len(sys.argv) < 2:
    print("user prompt is required")
    exit()

user_prompt = sys.argv[1]

prompt = prompt_template.replace("{prompt}", user_prompt)

print("\n\nuser input:")
print(user_prompt)


print("\n\nmodel prompt:")
print(prompt)


data = {
    "model": "llama3.2",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=data)
model_response = response.json()["response"]
print("\n\nmodel response:")
print(model_response)


print("\n\nvisit github, the new model response should be thered")


g = Github(token)
repo = g.get_repo("ChaoyiHuang/iot_messages")
cur_time = str(time.time_ns())
upload_file = user_prompt + cur_time + ".json"
repo.create_file(upload_file, 'upload new model response' + cur_time, model_response, branch='main')
