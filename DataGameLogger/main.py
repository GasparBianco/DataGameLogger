from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routers import userRouter, boardGameRouter

app = FastAPI()

app.include_router(userRouter.router)
app.include_router(boardGameRouter.router)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")