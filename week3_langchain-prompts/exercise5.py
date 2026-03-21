import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5
)
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import HumanMessage, AIMessage
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful study assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm | parser

# Simulated conversation
history = []

# Turn 1
response1 = chain.invoke({
    "history": history,
    "input": "What is Python?"
})
history.append(HumanMessage(content="What is Python?"))
history.append(AIMessage(content=response1))
print(response1)

# Turn 2
response2 = chain.invoke({
    "history": history,
    "input": "Why is it popular?"
})
history.append(HumanMessage(content="Why is it popular?"))
history.append(AIMessage(content=response2))
print(response2)

# Turn 3
response3 = chain.invoke({
    "history": history,
    "input": "Give examples of its use."
})
print(response3)