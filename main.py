# import json
# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# from typing import List
# from mangum import Mangum

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["GET"],
#     allow_headers=["*"],
# )

# marks_data = {}

# @app.on_event("startup")
# def load_data():
#     global marks_data
#     with open("marks.json", "r") as f:
#         data = json.load(f)
#     marks_data = {entry["name"]: entry["marks"] for entry in data}

# @app.get("/api")
# # async def get_marks(name: List[str] = Query(...)):
# #     results = [marks_data.get(n, None) for n in name]
# #     return {"marks": results}
# def read_api(name: str = "World"):
#     return {"message": f"Hello, {name}!"}

# handler = Mangum(app)
# @app.get("/")
# def root():
#     return {"message": "Welcome to the API"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}