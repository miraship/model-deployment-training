from fastapi import APIRouter

router = APIRouter(tags=["AI"], prefix="/ai")


@router.get("/")
def ai_health_check():
    return {"status", "healthy"}
