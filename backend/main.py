from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "This is home page added  "

@app.get("/payment")
def payment():
    return "This is payment page "


@app.post("/calculation")
def calculation(a,b):
    return a+b

@app.get("/health")
def health():
    return {"status": "ok"}



