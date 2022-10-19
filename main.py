from fastapi import FastAPI
from router.router import user

app = FastAPI()

# un recorador..
app.include_router(user)

