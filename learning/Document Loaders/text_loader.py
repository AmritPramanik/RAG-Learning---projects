from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatMistralAI()

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader("../cricket.txt",encoding='utf-8')
docs = loader.load()

# print(type(docs))
# print(len(docs))
# print(docs[0])
# print(type(docs[0]))

# every docs have two things : page_content and metadata

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

summary = chain.invoke({"poem" : docs[0].page_content})
print(summary)
