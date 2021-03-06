from fastapi import FastAPI


from api import api
from api.middlewares import AuthMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from helpers import create_folder

app = FastAPI()
app.add_middleware(AuthMiddleware)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api.router)

create_folder("assets")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8003)
