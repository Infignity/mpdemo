import json
import csv

with open('prospects/test.jsonl') as f:
    with open('prospects/testdb.csv', 'a+') as op:
        writer = csv.DictWriter(op, fieldnames=['name', 'job_title', 'company', 'score',
                                                'email', 'score', 'state', 'city', 'country', 'linkedin_url',
                                                'company_website', 'photo_url', 'logo_url'])
        for l in f.readlines():
            p = json.loads(l)
            out = {
                'name': p['name'],
                'job_title': p['title'],
                'company': p['organization']['name'],
                'score': '',
                'email': p['email'],
                'score': 'good',
                'city': p['city'],
                'state': p['state'],
                'country': p['country'],
                'linkedin_url': p['linkedin_url'],
                'company_website': p['organization']['website_url'],
                'photo_url': p['photo_url'],
                'logo_url': p['organization']['logo_url']
            }
            writer.writerow(out)