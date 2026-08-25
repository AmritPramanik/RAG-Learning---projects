from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('../Social_Network_Ads.csv')
docs = loader.lazy_load()

# for csv file each row consider as a pagge
for documents in docs :
    print(documents.page_content)