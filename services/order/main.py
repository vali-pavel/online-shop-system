from fastapi import FastAPI


from api import api
from api.middlewares import AuthMiddleware

app = FastAPI()
app.add_middleware(AuthMiddleware)
app.include_router(api.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8004)
