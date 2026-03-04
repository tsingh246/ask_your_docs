from dataclasses import dataclass, field
from typing import Dict, Any
import uuid


def generate_id() -> str:
    return str(uuid.uuid4())


@dataclass
class Document:
    """
    Represents a raw document loaded from a source.
    """
    doc_id: str = field(default_factory=generate_id)
    text: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Chunk:
    """
    Represents a chunk derived from a document.
    Used later for embedding and retrieval.
    """
    chunk_id: str = field(default_factory=generate_id)
    doc_id: str = ""
    text: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Query:
    """
    Represents a user query.
    Later this will include security filters.
    """
    text: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RetrievalResult:
    """
    Result returned from a retriever.
    """
    chunk: Chunk
    score: float