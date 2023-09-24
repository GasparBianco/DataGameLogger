from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routers import userRouter

app = FastAPI()

app.include_router(userRouter)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")