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

prompt = ChatPromptTemplate.from_template(
    "Answer this question in one paragraph: {question}"
)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke({
    "question": "What is a large language model?"
})

print(response)