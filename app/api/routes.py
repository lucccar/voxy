import logging, os
from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
from ..data.models import Body
from ..services.words import Words

router = APIRouter()

logger = logging.getLogger(os.getenv("LOGGER_NAME"))


@router.post("/count")
def word_count(data: Body):
    try:
        count = Words.count(data.word, data.delimiters)

        return JSONResponse(content=count, status_code=200)

    except Exception as e:
        logger.error(e)

        return Response(status_code=400)
