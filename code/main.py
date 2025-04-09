from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import os

app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/api", tags=["base link"]):
def root():
	return {"status" : "Ok"}
