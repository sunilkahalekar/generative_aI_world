from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["OPEN_API"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

prompt = ChatPromptTemplate.from_messages(
[
("system","you are a helpful assistant"),
("user","Question:{question}\nContext:{context}")
])

model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt|model|output_parser

question="summerize the article given"
context=""" The way mid-cap stocks have performed in the last two trading sessions. The biggest question would be whether this is another short term correction or a beginning of a long phase of underperformance and the answer would be in the market breadth of the midcap segment. Also one would have"""

print(chain.invoke({"question":question,"context":context}))

