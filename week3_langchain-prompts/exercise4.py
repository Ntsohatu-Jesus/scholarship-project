import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5
)
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

def ask_ai(role, question):

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a professional {role}."),
        ("human", "{question}")
    ])

    chain = prompt | llm | parser

    return chain.invoke({"question": question})

# Test calls
print(ask_ai("doctor", "What causes headaches?"))
print(ask_ai("teacher", "Explain gravity simply"))
print(ask_ai("lawyer", "What is a contract?"))