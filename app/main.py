from fastapi import FastAPI
from fastapi.responses import JSONResponse


# Init the entry point of the app
app = FastAPI()


@app.get("/")
def entry_point():
    return JSONResponse(status_code=200, content={"status": "working..."})
