from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
  with open("patients.json", 'r') as f:
    data = json.load(f)
  return data

@app.get("/")
def hello(): 
  return {"massage":"Hello, I'm Abdullah Al Masum"}

@app.get("/about")
def about():
  return {"massage":"This is a project for doctor and patients"}

@app.get("/views")
def views():
  return load_data()
