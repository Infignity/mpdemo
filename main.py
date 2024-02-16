from fastapi import FastAPI
from apollo import Apollo
import json, csv, io
import requests
from pydantic import BaseModel
from typing import Union

app = FastAPI()

spice_pro_sh = 'https://docs.google.com/spreadsheets/d/1oycHxgxnStCDT39_7rLP3IwlVpfXxO41vdvbdYe9ees/gviz/tq?tqx=out:csv&sheet=prospects'
spice_con_sh = 'https://docs.google.com/spreadsheets/d/1oycHxgxnStCDT39_7rLP3IwlVpfXxO41vdvbdYe9ees/gviz/tq?tqx=out:csv&sheet=content'
spice1_pro_sh = 'https://docs.google.com/spreadsheets/d/1BFKGwGdp_DKYf2liUr3uzR46P53pt8hA0x5W6EXqQSc/gviz/tq?tqx=out:csv&sheet=prospects'
spice1_con_sh = 'https://docs.google.com/spreadsheets/d/1BFKGwGdp_DKYf2liUr3uzR46P53pt8hA0x5W6EXqQSc/gviz/tq?tqx=out:csv&sheet=content'
alex_pro_sh = 'https://docs.google.com/spreadsheets/d/1qJtjXjLgmIjzQ7uRAsMGmWfVDMMg-_YQtrthApFxEO0/gviz/tq?tqx=out:csv&sheet=prospects'
alex_con_sh = 'https://docs.google.com/spreadsheets/d/1qJtjXjLgmIjzQ7uRAsMGmWfVDMMg-_YQtrthApFxEO0/gviz/tq?tqx=out:csv&sheet=content'
alex1_pro_sh = 'https://docs.google.com/spreadsheets/d/1DZSct8JCUAX1qFyLg9Y7HlBZrUlTOsfl-rvI5Gd_HLs/gviz/tq?tqx=out:csv&sheet=prospects'
alex1_con_sh = 'https://docs.google.com/spreadsheets/d/1DZSct8JCUAX1qFyLg9Y7HlBZrUlTOsfl-rvI5Gd_HLs/gviz/tq?tqx=out:csv&sheet=content'

@app.get("/sheet_data")
def random_apollo(q="spice", type="prospect"):
    "Return sheet data as json."
    if 'spice' in q.lower() and '1' in q.lower():
        if type == "prospect":
            res = requests.get(spice1_pro_sh)
            return list(csv.DictReader(io.StringIO(res.text)))
        else:
            res = requests.get(spice1_con_sh)
            return list(csv.DictReader(io.StringIO(res.text)))
    if 'spice' in q.lower():
        if type == "prospect":
            res = requests.get(spice_pro_sh)
            return list(csv.DictReader(io.StringIO(res.text)))
        else:
            res = requests.get(spice_con_sh)
            return list(csv.DictReader(io.StringIO(res.text)))
        
    if 'alex' in q.lower() and '1' in q.lower():
        if type == "prospect":
            res = requests.get(alex1_pro_sh)
            return list(csv.DictReader(io.StringIO(res.text)))
        else:
            res = requests.get(alex1_con_sh)
            return list(csv.DictReader(io.StringIO(res.text)))
    if 'alex' in q.lower():
        if type == "prospect":
            res = requests.get(alex_pro_sh)
            return list(csv.DictReader(io.StringIO(res.text)))
        else:
            res = requests.get(alex_con_sh)
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


apollo_gateway = Apollo()
class RequestInput(BaseModel):
    url: str
    method: str = 'post'
    params: Union[dict, None] = None
    body: Union[dict, None] = None

@app.post("/apollo_gateway")
def apollo(req: RequestInput):
    return apollo_gateway.req(req.url,
                              json_data=req.body,
                              params=req.params,
                              method=req.method)