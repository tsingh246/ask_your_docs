from dataclasses import dataclass


@dataclass
class Settings:
    """
    Global application configuration.
    Later we will add:
    - embedding model
    - vector store settings
    - chunk sizes
    - reranker options
    """
    app_name: str = "qlik_answers_rag"