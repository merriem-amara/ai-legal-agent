import pymupdf


def extract_text(file_path: str) -> tuple[str, int]:
    """
    Extract text from PDF.

    Returns:
        text, number_of_pages
    """

    document = pymupdf.open(file_path)

    pages = []

    for page in document:
        pages.append(page.get_text())

    document.close()

    return "\n".join(pages), len(pages)
