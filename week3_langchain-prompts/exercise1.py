import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5
)
from langchain.prompts import ChatPromptTemplate

# Create prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} like I'm a complete beginner."
)

# Format the prompt
formatted = prompt.format_messages(topic="Artificial Intelligence")

# Print result
print(formatted)