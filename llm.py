import os
from dotenv import load_dotenv
import openai
import langchain
from langchain.llms import OpenAI


load_dotenv()

my_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=1, openai_api_key=my_key)
text = "What is ASR?"
print(llm(text))

