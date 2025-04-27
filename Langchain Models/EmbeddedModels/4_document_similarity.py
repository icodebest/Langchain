from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents = [
    "The sky is clear and blue today.",
    "I love eating fresh mangoes in summer.",
    "My cat sleeps all day on the couch.",
    "Books are a window to endless knowledge.",
    "The mountains look beautiful during sunset.",
    "He enjoys playing football with his friends.",
    "A warm cup of coffee makes mornings better."
]

# Query sentence to check similarity
query = "I like to drink coffee in the morning."

doc_embeddings=embedding.embed_documents(documents)

query_embedding=embedding.embed_query(query)

#cousine similarity
scores=cosine_similarity([query_embedding], doc_embeddings)[0]
index, score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score is ",score)