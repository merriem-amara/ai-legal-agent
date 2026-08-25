from ai_legal_core.documents.parser import extract_text
from ai_legal_core.documents.chunker import chunk_text
from ai_legal_core.models.document import (
    DocumentMetadata,
    DocumentChunk,
    ProcessedDocument,
)


class DocumentService:

    def process_pdf(
        self,
        file_path: str,
        filename: str
    ) -> ProcessedDocument:

        text, pages = extract_text(file_path)

        chunks = chunk_text(text)

        return ProcessedDocument(
            metadata=DocumentMetadata(
                filename=filename,
                pages=pages,
                characters=len(text),
            ),
            chunks=[
                DocumentChunk(
                    content=chunk,
                    index=index,
                )
                for index, chunk in enumerate(chunks)
            ],
        )
