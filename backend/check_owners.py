import requests

r = requests.get('http://localhost:8000/leads')
leads = r.json()

print(f'Total leads: {len(leads)}')

with_owner = [l for l in leads if l.get('owner_name')]
without_owner = [l for l in leads if not l.get('owner_name')]

print(f'Leads with owner_name: {len(with_owner)}')
print(f'Leads without owner_name: {len(without_owner)}')

if with_owner:
    print(f'\nSample lead WITH owner:')
    print(f"  Company: {with_owner[0].get('company_name')}")
    print(f"  Owner: {with_owner[0].get('owner_name')}")

if without_owner:
    print(f'\nSample lead WITHOUT owner:')
    print(f"  Company: {without_owner[0].get('company_name')}")
    print(f"  Fields: {list(without_owner[0].keys())}")
