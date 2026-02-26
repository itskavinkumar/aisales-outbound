"""
Auto-generate and upload 200 realistic B2B leads
"""
import pandas as pd
import numpy as np
import requests

# Generate realistic B2B dataset
def generate_leads(num_leads=200):
    industries = {
        'Technology': 0.30,
        'Healthcare': 0.15,
        'Finance': 0.15,
        'Manufacturing': 0.15,
        'Retail': 0.10,
        'Education': 0.10,
        'Other': 0.05
    }
    
    job_roles = {
        'Chief Technology Officer': 0.15,
        'Chief Information Officer': 0.12,
        'Chief Executive Officer': 0.10,
        'Chief Financial Officer': 0.08,
        'VP Engineering': 0.12,
        'VP Sales': 0.10,
        'VP Operations': 0.10,
        'Director IT': 0.10,
        'Manager': 0.10,
        'Procurement': 0.03
    }
    
    company_prefixes = {
        'Technology': ['Tech', 'Cloud', 'Data', 'Cyber', 'Smart', 'Digital', 'AI', 'Quantum'],
        'Healthcare': ['Health', 'Medi', 'Care', 'Pharma', 'Bio', 'Medical'],
        'Finance': ['Fin', 'Capital', 'Invest', 'Bank', 'Trading', 'Wealth'],
        'Manufacturing': ['Precision', 'Auto', 'Industrial', 'Robo', 'Advanced'],
        'Retail': ['Retail', 'Shop', 'Commerce', 'Fashion', 'Mega', 'Smart'],
        'Education': ['Edu', 'Learn', 'Academy', 'University', 'Online'],
        'Other': ['Global', 'Premier', 'Elite', 'Dynamic']
    }
    
    company_suffixes = ['Corp', 'Inc', 'Solutions', 'Systems', 'Group', 'Partners', 
                        'Industries', 'Technologies', 'Services', 'Labs']
    
    # Professional first and last names for owner generation
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
    
    leads = []
    np.random.seed(42)
    
    for i in range(num_leads):
        industry = np.random.choice(list(industries.keys()), p=list(industries.values()))
        
        prefix = np.random.choice(company_prefixes[industry])
        suffix = np.random.choice(company_suffixes)
        company_name = f"{prefix}{np.random.choice(['Tech', 'Soft', 'Pro', 'Plus', 'Max', 'Star', ''])}{suffix}"
        
        domain = company_name.lower().replace(' ', '').replace('corp', '').replace('inc', '')
        job_role = np.random.choice(list(job_roles.keys()), p=list(job_roles.values()))
        email_prefix = job_role.split()[0].lower()
        email = f"{email_prefix}@{domain}.com"
        
        base_value = {
            'Technology': (50000, 500000),
            'Healthcare': (75000, 400000),
            'Finance': (100000, 600000),
            'Manufacturing': (150000, 800000),
            'Retail': (20000, 150000),
            'Education': (30000, 200000),
            'Other': (40000, 250000)
        }
        min_val, max_val = base_value[industry]
        
        if any(role in job_role for role in ['Chief', 'CEO', 'CTO', 'CIO', 'CFO']):
            quote_value = np.random.randint(int(max_val * 0.6), max_val)
        else:
            quote_value = np.random.randint(min_val, int(max_val * 0.6))
        
        item_count = int((quote_value / 1000) * np.random.uniform(0.5, 2))
        item_count = max(10, min(item_count, 1000))
        
        conversion_days = np.random.randint(15, 90)
        
        if quote_value > 300000:
            past_engagements = np.random.randint(5, 15)
        elif quote_value > 100000:
            past_engagements = np.random.randint(2, 8)
        else:
            past_engagements = np.random.randint(0, 4)
        
        # Generate owner name
        owner_name = f"{np.random.choice(first_names)} {np.random.choice(last_names)}"
        
        lead = {
            'company_name': company_name,
            'email': email,
            'owner_name': owner_name,
            'job_role': job_role,
            'quote_value': quote_value,
            'item_count': item_count,
            'conversion_days': conversion_days,
            'past_engagements': past_engagements,
            'industry': industry
        }
        
        leads.append(lead)
    
    return pd.DataFrame(leads)


if __name__ == "__main__":
    print("="*60)
    print("  GENERATING REALISTIC B2B LEADS")
    print("="*60)
    
    print("\n🔄 Generating 200 realistic leads...")
    df = generate_leads(200)
    
    print(f"✅ Generated {len(df)} leads")
    
    # Save to CSV
    df.to_csv('data/generated_leads.csv', index=False)
    print("\n💾 Saved to: data/generated_leads.csv")
    
    # Show stats
    print("\n📊 Dataset Statistics:")
    print(f"   - Industries: {df['industry'].value_counts().to_dict()}")
    print(f"   - Avg Quote Value: ${df['quote_value'].mean():,.0f}")
    print(f"   - Total Revenue Potential: ${df['quote_value'].sum():,.0f}")
    
    # Upload to system
    print("\n🚀 Uploading to MongoDB...")
    leads = df.to_dict(orient='records')
    
    try:
        response = requests.post('http://localhost:8000/leads/upload', json=leads)
        result = response.json()
        
        print(f"\n✅ Upload Complete!")
        print(f"   - Uploaded: {result.get('uploaded', 0)}")
        print(f"   - Failed: {result.get('failed', 0)}")
        
        print("\n🎉 Success! Check analytics:")
        print("   curl http://localhost:8000/analytics/segments")
        
    except Exception as e:
        print(f"\n⚠️ Upload error: {e}")
        print("   Make sure backend is running!")
    
    print("\n" + "="*60)
