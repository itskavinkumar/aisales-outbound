"""
Directly update MongoDB to add owner names to leads without them
"""
import asyncio
import random
from app.database import db

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

async def add_owner_names():
    # Connect to database
    db.connect()
    
    print("🔄 Fetching all leads from MongoDB...")
    all_leads = await db.get_all_leads(limit=1000)
    
    leads_without_owner = [lead for lead in all_leads if not lead.get('owner_name')]
    
    print(f"📊 Found {len(leads_without_owner)} leads without owner names")
    
    if not leads_without_owner:
        print("✅ All leads already have owner names!")
        db.close()
        return
    
    print(f"🚀 Adding owner names...")
    updated = 0
    
    for lead in leads_without_owner:
        owner_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        
        # Update directly in MongoDB
        await db.db["leads"].update_one(
            {"_id": lead["_id"]},
            {"$set": {"owner_name": owner_name}}
        )
        updated += 1
        
        if updated % 50 == 0:
            print(f"   Updated {updated}/{len(leads_without_owner)}...")
    
    print(f"\n✅ Successfully added owner names to {updated} leads!")
    
    # Verify
    all_leads_after = await db.get_all_leads(limit=1000)
    leads_with_owner = [lead for lead in all_leads_after if lead.get('owner_name')]
    print(f"✅ Verification: {len(leads_with_owner)}/{len(all_leads_after)} leads now have owner names")
    
    db.close()

if __name__ == "__main__":
    asyncio.run(add_owner_names())
