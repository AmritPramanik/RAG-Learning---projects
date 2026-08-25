from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader

# WebBaseLoader use BeautifulSoup so need to install BeautifulSoup

load_dotenv()

model = ChatMistralAI()

prompt = PromptTemplate(
    template="""
    Answer the question based on the following text.

    Text:
    {text}

    Question:
    {question}
    """,
    input_variables=["text", "question"]
)

parser = StrOutputParser()

url = 'https://www.apple.com/in/shop/buy-mac/macbook-air/15-inch-midnight-m5-chip-10-core-cpu-10-core-gpu-16gb-memory-512gb-storage?cid=aos-in-seo-pla-mac-mac'

loader = WebBaseLoader(url)
docs = loader.load()

# print(len(docs))
# print(docs[0].page_content)

chain = prompt | model | parser

answer = chain.invoke({
    "question": "What is the device name and device price?",
    "text": docs[0].page_content
})

print(answer)