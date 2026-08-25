from fastapi import APIRouter, UploadFile, File

from ai_legal_core.services import DocumentService


router = APIRouter(
    prefix="/documents",
    tags=["documents"]
)


service = DocumentService()


@router.post("/process")
async def process_document(
    file: UploadFile = File(...)
):
    content = await file.read()

    temp_path = f"/tmp/{file.filename}"

    with open(temp_path, "wb") as document:
        document.write(content)

    result = service.process_pdf(
        temp_path,
        file.filename
    )

    return result
