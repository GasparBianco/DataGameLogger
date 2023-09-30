from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")