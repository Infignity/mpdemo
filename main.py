from fastapi import FastAPI
from apollo import Apollo
import json, csv, io
import requests

app = FastAPI()

spice_pro_sh = 'https://docs.google.com/spreadsheets/d/1oycHxgxnStCDT39_7rLP3IwlVpfXxO41vdvbdYe9ees/gviz/tq?tqx=out:csv'

@app.get("/apollo")
def random_apollo(q="spice"):
    "Return 25 random data points from Apollo."
    if q.lower() == 'spice':
        res = requests.get(spice_pro_sh)
        return list(csv.DictReader(io.StringIO(res.text)))


@app.get("/icp")
def icp(q="spice"):
    "Return preset icp if query matches the input."
    icp_files = ['spice_icp']
    for f in icp_files:
        if q in f:
            with open(f'icps/{f}.json') as fp:
                return json.load(fp)
    return []