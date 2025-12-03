from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def aiquest():
  return {"Django": "API"}

@app.get("/course")
def course():
  return {"course":"Machine Learning"}

@app.get("/course/python")
def python():
  return {"python":"ML with Python", "Instractor":"Abdullah Al Masum", "Duration":"3 Months"}