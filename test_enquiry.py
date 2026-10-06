import requests
import json

SUPABASE_URL = 'https://gpxllxfyaayyohszhrgj.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdweGxseGZ5YWF5eW9oc3pocmdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTA1NjMzMjEsImV4cCI6MjEwNjEzOTMyMX0.WOdr0CLPqb7jdow4JTTPDDyIqOt7_mwFKQB4HcUcpcM'

headers = {
    'apikey': SUPABASE_ANON_KEY,
    'Authorization': f'Bearer {SUPABASE_ANON_KEY}',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

# Step 1: Insert (same way the JS client does it)
print("STEP 1: Inserting test enquiry (with return=representation like JS client)...")
resp = requests.post(
    f'{SUPABASE_URL}/rest/v1/enquiries',
    headers=headers,
    json=[{
        'name': 'Pre-flight Test',
        'contact': 'preflight@mozhi.com',
        'requirement': 'Automated verification before manual testing.'
    }]
)
print(f"  Status: {resp.status_code}")
print(f"  Response: {resp.text}")

if resp.status_code in (200, 201):
    print("  >>> INSERT + READ-BACK: WORKING ✅")
else:
    print("  >>> FAILED ❌")

# Step 2: Read all rows
print("\nSTEP 2: Reading all enquiries...")
resp2 = requests.get(
    f'{SUPABASE_URL}/rest/v1/enquiries?select=*&order=created_at.desc',
    headers={
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f'Bearer {SUPABASE_ANON_KEY}'
    }
)
print(f"  Status: {resp2.status_code}")
data = resp2.json()
print(f"  Total rows: {len(data)}")
for row in data:
    print(f"  - [{row.get('created_at','?')}] {row.get('name')} | {row.get('contact')} | {row.get('requirement','')[:50]}...")

if resp2.status_code == 200:
    print("  >>> SELECT: WORKING ✅")
else:
    print("  >>> SELECT FAILED ❌")

# Step 3: Clean up test rows
print("\nSTEP 3: Cleaning up test rows...")
del_resp = requests.delete(
    f'{SUPABASE_URL}/rest/v1/enquiries?contact=eq.preflight@mozhi.com',
    headers={
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f'Bearer {SUPABASE_ANON_KEY}'
    }
)
# Also clean the earlier minimal test
del_resp2 = requests.delete(
    f'{SUPABASE_URL}/rest/v1/enquiries?contact=eq.x@x.com',
    headers={
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': f'Bearer {SUPABASE_ANON_KEY}'
    }
)
print(f"  Cleanup status: {del_resp.status_code}, {del_resp2.status_code}")

print("\n" + "=" * 50)
print("ALL CHECKS PASSED — You're good to test manually!" if resp.status_code in (200,201) and resp2.status_code == 200 else "ISSUES REMAIN — see above")
print("=" * 50)
