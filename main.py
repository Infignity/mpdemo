from fastapi import FastAPI
from apollo import Apollo
import json

app = FastAPI()

@app.get("/apollo")
def random_apollo(q="test"):
    "Return 25 random data points from Apollo."
    prospect_files = ['test']
    for f in prospect_files:
        if q in f:
            with open(f'prospects/{f}.jsonl') as f:
                return [json.loads(p) for p in f.readlines()]

@app.get("/icp")
def icp(q="spice"):
    "Return preset icp if query matches the input."
    icp_files = ['spice_icp']
    for f in icp_files:
        if q in f:
            with open(f'icps/{f}.json') as fp:
                return json.load(fp)
    return []