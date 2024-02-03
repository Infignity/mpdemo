from fastapi import FastAPI
from apollo import Apollo
import json

app = FastAPI()

@app.get("/random_apollo_search")
def random_apollo(q="john"):
    "Return 25 random data points from Apollo."
    return

@app.get("/icp")
def icp(q="spice"):
    "Return preset icp if query matches the input."
    icp_files = ['spice_icp']
    for f in icp_files:
        if q in f:
            with open(f'icps/{f}.json') as fp:
                return json.load(fp)
    return []