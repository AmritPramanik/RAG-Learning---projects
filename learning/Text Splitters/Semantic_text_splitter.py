from langchain_experimental.text_splitter import SemanticChunker
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

#  it alwase not give a accurate result

load_dotenv()

embeddings = MistralAIEmbeddings(
    model="mistral-embed"
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

text_splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=0.5
)

# --- another way ---

# text_splitter = SemanticChunker(
#     embeddings=embeddings,
#     breakpoint_threshold_type="percentile",
#     breakpoint_threshold_amount=75
# )

chunks = text_splitter.create_documents([sample])

print(len(chunks))
for chunk in chunks:
    print(chunk.page_content,'\n')

