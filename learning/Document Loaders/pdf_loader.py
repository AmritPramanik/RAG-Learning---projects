from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

# PyPDFLoader is usefull for text type pdf but it can't read image type pdf
load_dotenv()

loader = PyPDFLoader('../dl-curriculum.pdf')
docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print("------------------------------")
print(docs[1].page_content)
print(docs[1].metadata)