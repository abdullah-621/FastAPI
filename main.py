from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
  return {"massage" : "Hello world!"}

@app.get("/about")
def about():
  return {"massage":"campusX is an education platform where you can learn ai"}