import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5
)
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional translator."),
    ("human", "Translate '{text}' into {language}.")
])

# French
msg1 = prompt.format_messages(
    text="Good morning, how are you?",
    language="French"
)

# Pidgin
msg2 = prompt.format_messages(
    text="Good morning, how are you?",
    language="Cameroonian Pidgin English"
)

print(msg1)
print(msg2)