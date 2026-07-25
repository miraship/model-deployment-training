from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/")
def health_check():
    return {"status": "Healthy"}
