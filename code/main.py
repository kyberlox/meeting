from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/api", tags=["base link"])
def root():
	return {"status" : "Ok"}
