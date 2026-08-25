from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from pgvector.sqlalchemy import Vector

from ai_legal_core.database.base import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    filename: Mapped[str] = mapped_column(
        String(255)
    )

    pages: Mapped[int] = mapped_column(
        Integer
    )

    characters: Mapped[int] = mapped_column(
        Integer
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    chunks: Mapped[list["DocumentChunk"]] = relationship(
        back_populates="document"
    )


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id")
    )

    content: Mapped[str] = mapped_column(
        Text
    )

    chunk_index: Mapped[int] = mapped_column(
        Integer
    )

    embedding: Mapped[list[float]] = mapped_column(
        Vector(1536),
        nullable=True
    )

    document: Mapped["Document"] = relationship(
        back_populates="chunks"
    )
