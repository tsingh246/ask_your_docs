from pathlib import Path
from typing import List
from app.models.schemas import Document

SUPPORTED_EXT = {".txt", ".md"}


def load_documents_from_folder(folder: str) -> List[Document]:
    """
    Load all .txt and .md files from a folder
    and convert them into Document objects.
    """

    base = Path(folder)

    if not base.exists():
        raise ValueError(f"Folder does not exist: {folder}")

    documents: List[Document] = []

    for file_path in base.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXT:

            text = file_path.read_text(encoding="utf-8", errors="ignore")

            doc = Document(
                text=text,
                metadata={
                    "source_path": str(file_path),
                    "source_type": file_path.suffix.replace(".", "")
                }
            )

            documents.append(doc)

    return documents