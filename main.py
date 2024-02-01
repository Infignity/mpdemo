from fastapi import FastAPI
from apollo import Apollo

app = FastAPI()

@app.get("/random_apollo_search")
def random_apollo(q="john"):
    "Return 25 random data points from Apollo."
    apollo = Apollo()
    payload = {
        'finder_view_id': '5b6dfc5a73f47568b2e5f11c',
        'q_keywords': q,
        'page': 1,
        'display_mode': 'explorer_mode',
        'per_page': 25,
        'open_factor_names': [],
        'num_fetch_result': 1,
        'context': 'people-index-page',
        'show_suggestions': False,
        'ui_finder_random_seed': '2fw3w6c21zm',
        'cacheKey': 1706784155092,
    }

    return apollo.search(payload=payload)