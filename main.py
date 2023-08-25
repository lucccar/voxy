import logging, os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Voxy Word Counter",
    redoc_url=None,
    version="1",
)

origins = [
    "*",
    "http://localhost",
    "http://localhost:7070",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(routes.router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")

logger = logging.getLogger(os.getenv("LOGGER_NAME"))
logger.setLevel(logging.INFO)

voxy_logger = logging.StreamHandler()
voxy_logger.setLevel(logging.INFO)

logger.addHandler(voxy_logger)

formatter = logging.Formatter(
    "%(levelname)s:    %(asctime)s  |  %(message)s  |  %(name)s"
)
voxy_logger.setFormatter(formatter)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=7070)
