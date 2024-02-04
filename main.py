from fastapi import FastAPI
from apollo import Apollo
import json, csv, io
import requests

app = FastAPI()

spice_pro_sh = 'https://docs.google.com/spreadsheets/d/1oycHxgxnStCDT39_7rLP3IwlVpfXxO41vdvbdYe9ees/gviz/tq?tqx=out:csv'
spice_con_sh = 'https://docs.google.com/spreadsheets/d/1oycHxgxnStCDT39_7rLP3IwlVpfXxO41vdvbdYe9ees/gviz/tq?tqx=out:csv&sheet=content'

@app.get("/sheet_data")
def random_apollo(q="spice", type="prospect"):
    "Return sheet data as json."
    if q.lower() == 'spice':
        if type == "prospect":
            res = requests.get(spice_pro_sh)
            return list(csv.DictReader(io.StringIO(res.text)))
        else:
            res = requests.get(spice_con_sh)
            return list(csv.DictReader(io.StringIO(res.text)))
    

@app.get("/icp")
def icp(q="spice"):
    "Return preset icp if query matches the input."
    icp_files = ['spice', 'assist', 'alex', 'jordan']
    for f in icp_files:
        if f in q.lower():
            with open(f'icps/{f}.json') as fp:
                return json.load(fp)
    return []