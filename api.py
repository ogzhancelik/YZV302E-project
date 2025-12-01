import os
from openai import AzureOpenAI
from typing import List, Dict
from pprint import pprint
from time import time
import json
import pandas as pd

def connect_azure_gpt():
    azure_endpoint = "https://pengineering.openai.azure.com/"
    #deleted for security reasons
    api_key = ""
    api_version = "" 

    client = AzureOpenAI(
        azure_endpoint=azure_endpoint,
        api_key=api_key,
        api_version=api_version
    )

    return client

def get_resp(client, messages: List[Dict[str, str]]) -> str:
    """The input is a list of dictionaries."""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.8
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error getting response: {e}")
        return None

def generate_answer(client: AzureOpenAI, text_fragment: str, question: str) -> str:
    messages = [
        {
            'role': 'system',
            'content': (
                "Sen yardımcı bir asistansın. Görevin, soruyu doğru ve tam olarak yanıtlamaktır."
            )
        },
        {
            'role': 'user',
            'content': f"Context: {text_fragment}\n\nSoru: {question}"
        }
    ]
    answer = get_resp(client, messages)
    return answer

