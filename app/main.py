from __future__ import annotations
import argparse
from app.config import Settings
from app.connectors.local_files import load_documents_from_folder


def cmd_ingest(args: argparse.Namespace) -> int:
    docs = load_documents_from_folder(args.folder)
    print(f"Ingested {len(docs)} document(s) from: {args.folder}")
    for d in docs[: min(3, len(docs))]:
        preview = d.text[:120].replace("\n", " ")
        print(
            f"- doc_id={d.doc_id} "
            f"source={d.metadata.get('source_path')} "
            f"preview={preview!r}"
        )
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="qlik-answers-rag",
        description="Modular RAG (CLI)",
    )
    p.add_argument("--version", action="version", version="0.1.0")

    sub = p.add_subparsers(dest="cmd", required=True)

    ingest = sub.add_parser(
        "ingest",
        help="Load raw documents from a folder (.txt/.md for now)",
    )
    ingest.add_argument("folder", help="Path to folder containing .txt/.md files")
    ingest.set_defaults(func=cmd_ingest)

    return p


def main() -> int:
    _settings = Settings()
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())