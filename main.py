from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS for all origins and allow only GET methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# # Your student marks data as a dictionary for quick lookup
marks_data = {
    "iY7JLDu": 7, "LOzEQWK8VH": 64, "lI2F9BJBIk": 24, "C31c7": 60,
    "31x7JmPFq4": 85, "B2lCCNndM": 75, "mXgFEHtz": 73, "co": 45,
    "NrzI": 93, "f": 17, "6O8Aqz0Yy2": 76, "ZUNscPZUMu": 93,
    "t": 64, "hW": 67, "v5MN2e": 27, "c8SDOMb": 68, "gA0j": 53,
    "1y2j5H0N": 62, "dk8bce": 15, "eFIbPJR": 9, "ymDanArZI": 81,
    "lUgbwdsBy": 7, "wbTt": 18, "hul9eJ": 50, "DABkNif": 28,
    "XVoSHg": 74, "LW8NqJ": 71, "Y": 64, "9nVGd": 15, "oqhMwGBT2": 45,
    "K0n": 71, "GZPjI1v": 9, "BZncaf": 85, "D4sDX8j": 20, "7M36KTL8m": 10,
    "r9GVsVOKzo": 1, "ey": 42, "5LEWvs": 95, "6": 67, "8lnwK": 22,
    "05L3Xk9iY": 34, "kkc": 51, "tZXZOCx": 75, "2cF": 49,
    "i4nsJ4hoX6": 45, "zt": 79, "7M58FS": 43, "Whpb55w0b": 79,
    "JNb1nFGJ": 11, "RY": 99, "IY5a0Lvu": 89, "AnQ": 57, "cNHt4vc": 24,
    "JCYmRULZV": 65, "BsLSrwnY79": 10, "kd": 29, "Z": 71, "yn": 12,
    "aaeuE47yc": 46, "GR3CwC8D": 35, "At": 70, "Zs": 96, "R": 64,
    "qU": 31, "jsaJT": 74, "Z0hLgVWSF": 92, "ll6VqH": 14, "w7ppF5K": 92,
    "Niy0G2PD2": 3, "epHIZv": 43, "AUEFdtuh5": 66, "OBdJMrZng": 88,
    "aMpDHa4VU": 32, "F": 94, "DOpn": 6, "xFvbQPoYC": 28, "ieEE": 70,
    "kV": 91, "XM50N3": 34, "WGjEheD": 25, "HwOJ": 74, "2I": 18,
    "c0fo": 29, "KL5kt": 12, "A": 87, "Y3R4Rcf": 2, "lF0": 68,
    "eK5paS7Ox": 98, "OCH7SPUvJX": 88, "yVms": 46, "33uE6IN": 2,
    "pUuLr": 2, "vko2": 98, "3": 5, "19": 48, "8sb6U": 24, "Yh": 40,
    "R0Y": 49, "OGfkEi0": 71, "pRaGC": 47,
}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    # For each name requested, return their marks or None if not found
    results = [marks_data.get(n, None) for n in name]
    return {"marks": results}
# main.py



