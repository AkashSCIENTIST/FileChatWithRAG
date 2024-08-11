# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.evaluation import load_evaluator
from langchain.evaluation.embedding_distance.base import EmbeddingDistanceEvalChain
from langchain.evaluation.embedding_distance.base import EmbeddingDistance
from dotenv import load_dotenv
from llm_utils import get_embeddings
import openai
import os

def main():
    # Get embedding for a word.
    embedding_function = get_embeddings()

    words = ("apple", "iphone")
    chain = EmbeddingDistanceEvalChain(embeddings=embedding_function, distance_metric=EmbeddingDistance.COSINE)
    x = chain.evaluate_strings(prediction=words[0], reference=words[1])

    print(f"Comparing ({words[0]}, {words[1]}): {x}")


if __name__ == "__main__":
    main()
