from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

import os

app = FastAPI()

app.mount("/api/static", StaticFiles(directory="static"))

@app.get("/api/", tags=["base link"], response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Сайт седьмого стёта проектировщиков</title>
        </head>
        <body>
            <h1>На данный момент сайт находится в разработке</h1>
        </body>
    </html>
    """

@app.get("/api/video/{name}", tags=["video"])
async def stream_video(name : str):
    path = f"/app/static/{name}"
    file_like  = open(path, mode="rb")

    return StreamingResponse(file_like, media_type="video/mp4")

# @app.get("/api/static_video/{name}", tags=["video"])
# async def stream_video(name : str):
#     path = f"/app/static/{name}"
#     file_like  = open(path, mode="rb")

#     return StreamingResponse(file_like, media_type="video/mp4")