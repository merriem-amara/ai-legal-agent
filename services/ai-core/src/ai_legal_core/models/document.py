from pydantic import BaseModel


class DocumentMetadata(BaseModel):
    filename: str
    pages: int
    characters: int


class DocumentChunk(BaseModel):
    content: str
    index: int


class ProcessedDocument(BaseModel):
    metadata: DocumentMetadata
    chunks: list[DocumentChunk]
