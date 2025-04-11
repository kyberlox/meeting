from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse

import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", tags=["base link"])
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
