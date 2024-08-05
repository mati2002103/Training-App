# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from workout_generator.generators import weekWorkoutPlanGenerator

app = FastAPI()

# Pozwala na żądania CORS z frontendu
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/generate_plan")
def generate_plan():
    #generator = weekWorkoutPlanGenerator()
    #plan = generator.generate_week_fbw_plan()
    #return plan
    return "asd"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
