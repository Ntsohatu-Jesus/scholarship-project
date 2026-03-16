from fastapi import FastAPI

app = FastAPI()

# Returns welcome message
@app.get("/")
def welcome():
    return {"message": "Welcome to my FastAPI backend - Irene"}

# Returns course information
@app.get("/info")
def info():
    return {
        "course": "Backend Development",
        "instructor": "HonraTech",
        "weeks": 6
    }

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "OK"}