import os
import gradio as gr
from dotenv import load_dotenv
from langchain.llms import OpenAI


load_dotenv()


def process(info):
    my_key = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(
        temperature=1, 
        openai_api_key=my_key)
    return llm(info)

demo = gr.Interface(
    fn=process, 
    inputs="text", 
    outputs="text")

demo.launch()  