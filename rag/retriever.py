def retrieve_docs(vectorstore, query):
    results = vectorstore.similarity_search(query, k=3)

    return results