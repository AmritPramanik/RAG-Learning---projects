from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='../books',
    glob="*.pdf",
    loader_cls = PyPDFLoader
)

# docs = loader.load()  ---> Here whole data load at a time, this method is usefull for small document, but for large or huge no of documment it is very time consuming and heavy process

# so we use 
docs = loader.lazy_load() # ---> it create genarator of each page and load one by one

# print(len(docs))
# print(docs[10].page_content)
# print(docs[10].metadata)

for documents in docs :
    print(documents.metadata)