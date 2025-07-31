from fastapi import FastAPI

app = FastAPI()

@app.get("/ping", status_code=200)
def ping():
   return print("pong")
