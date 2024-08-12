# Chat with files using RAG

## Instructions
`All instructions are based on Windows machine, for other OS please refer official documentations of associated libraries`
- Install dependencies using :
    ```bash
    ./install.sh
    ```
- Store all files in a folder. Here it is `books`. In first version only markdown (.md) files are used.
- Store all access keys in a `.env` file.
- To convert files into embeddings, run :
    ```bash
    python create_database.py
    ```
- To run a rudimentary chatbot run :
    ```bash
    python query_data.py
    ```
    
## Tweakable Instructions

- The first version of bot, uses `Chroma` as Vector storage database, `HuggingFaceEmbeddings` as embedding model and `HuggingFaceEndpoint` as AI chat agent
- Their respetive access tokens are saved in `.env` file as follows :
    ```env
    HF_ACCESS_KEY=<HuggingFace access token in format hf_...>
    HUGGINGFACEHUB_API_TOKEN=<HuggingFace access token in format hf_...>
    ```
- To use other better database, embedding models and AI chat agents, click below links:
    - [Link to list of vector storage databases](https://python.langchain.com/v0.2/docs/integrations/vectorstores/)
    - [Link to list of embedding models](https://python.langchain.com/v0.2/docs/integrations/text_embedding/)
    - [Link to list of AI Chat agents](https://python.langchain.com/v0.2/docs/integrations/llms/)