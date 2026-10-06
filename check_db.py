import requests
import json
import time

SUPABASE_URL = 'https://gpxllxfyaayyohszhrgj.supabase.co'
SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdweGxseGZ5YWF5eW9oc3pocmdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTA1NjMzMjEsImV4cCI6MjEwNjEzOTMyMX0.WOdr0CLPqb7jdow4JTTPDDyIqOt7_mwFKQB4HcUcpcM'

headers = {
    'apikey': SUPABASE_ANON_KEY,
    'Authorization': f'Bearer {SUPABASE_ANON_KEY}'
}

def get_enquiries():
    response = requests.get(f'{SUPABASE_URL}/rest/v1/enquiries?select=*', headers=headers)
    print("Database contents (enquiries table):")
    print(json.dumps(response.json(), indent=2))

if __name__ == '__main__':
    get_enquiries()
