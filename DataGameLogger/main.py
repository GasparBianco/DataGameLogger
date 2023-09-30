from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routers import userRouter, boardGameRouter, authRouter, friendsRouter

app = FastAPI()

app.include_router(userRouter.router)
app.include_router(boardGameRouter.router)
app.include_router(authRouter.router)
app.include_router(friendsRouter.router)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")