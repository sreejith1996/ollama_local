import requests
import json

url = "http://localhost:11434/api/generate"
body = {
    "model": "llama3.2",
    "prompt":"Why is the sky blue?",
}

with requests.post(url, json = body, stream=True) as r:
    if r.status_code == 200:
        for line in r.iter_lines():
            if line:
                json_obj = json.loads(line.decode("utf-8"))
                print(json_obj["response"], end='', flush=True)
