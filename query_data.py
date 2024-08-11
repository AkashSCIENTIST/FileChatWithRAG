import warnings
warnings.filterwarnings("ignore")

from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from llm_utils import get_embeddings, get_agent

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():

    # Prepare the DB.
    embedding_function = get_embeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    model = get_agent()

    while True:
        query_text = input("Enter query: ")

        # Search the DB.
        results = db.similarity_search_with_relevance_scores(query_text, k=5)
        if len(results) == 0:
            print(f"Unable to find matching results. Next question please")
            continue

        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)
        # print(prompt)
        
        response_text = model.invoke(prompt)

        sources = [doc.metadata.get("source", None) for doc, _score in results]
        formatted_response = f"Response: \n{response_text.content}\nSources: \n{sources}\n\n"
        print(formatted_response)


if __name__ == "__main__":
    main()
