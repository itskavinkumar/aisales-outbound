"""
Add owner names to all leads that don't have them
"""
import requests
import random

# Professional first and last names
first_names = ['James', 'Michael', 'Robert', 'John', 'David', 'William', 'Richard', 'Joseph',
               'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica',
               'Sarah', 'Karen', 'Nancy', 'Lisa', 'Margaret', 'Betty', 'Sandra', 'Ashley',
               'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Steven', 'Paul',
               'Andrew', 'Joshua', 'Kenneth', 'Kevin', 'Brian', 'George', 'Timothy', 'Ronald',
               'Edward', 'Jason', 'Jeffrey', 'Ryan', 'Jacob', 'Gary', 'Nicholas', 'Eric']

last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
              'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
              'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson',
              'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker',
              'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores',
              'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell']

print("🔄 Fetching all leads...")
r = requests.get('http://localhost:8000/leads')
leads = r.json()

leads_to_update = [lead for lead in leads if not lead.get('owner_name')]

print(f"📊 Found {len(leads_to_update)} leads without owner names")

if not leads_to_update:
    print("✅ All leads already have owner names!")
    exit(0)

# Add owner names
for lead in leads_to_update:
    lead['owner_name'] = f"{random.choice(first_names)} {random.choice(last_names)}"

print(f"🚀 Uploading {len(leads_to_update)} updated leads...")

try:
    response = requests.post('http://localhost:8000/leads/upload', json=leads_to_update)
    result = response.json()
    
    print(f"\n✅ Update Complete!")
    print(f"   - Updated: {result.get('uploaded', 0)}")
    print(f"   - Failed: {result.get('failed', 0)}")
    
    if result.get('failed', 0) > 0:
        print(f"\n⚠️ Errors:")
        for error in result.get('errors', []):
            print(f"   - {error}")
    
except Exception as e:
    print(f"\n⚠️ Upload error: {e}")
    print("   Make sure backend is running!")

print("\n✅ Done! Refresh your frontend to see the owner names.")
