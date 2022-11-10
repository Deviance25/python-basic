from fastapi import APIRouter

router = APIRouter(
    prefix="/ping",
)


@router.get("")
def ping_con():
    return {"message": "pong"}

