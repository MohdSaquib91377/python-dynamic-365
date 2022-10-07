import imp
import adal
import requests
import json



# Global configs.
CLIENT_ID = '5a9190dd-4134-4402-8930-6a4fbc5c2812'
RESOURCE_URI = 'https://kaya-sandbox.crm8.dynamics.com'
AUTHORITY_URI = 'https://login.microsoftonline.com/8e681491-9aa1-454e-b90c-c39afa008e79'
CLIENT_SECRET = 's~2OjgBdAizMwmb60-rAMoki-kBM1TM_KT'
ENTITY = 'contact'
 
# Get an access token.
context = adal.AuthenticationContext(AUTHORITY_URI, api_version=None)
token = context.acquire_token_with_client_credentials(RESOURCE_URI, CLIENT_ID, CLIENT_SECRET)
session = requests.Session()
session.headers.update(dict(Authorization='Bearer {}'.format(token.get('accessToken'))))
 
# Request image.
request_uri = 'https://kaya-sandbox.crm8.dynamics.com/api/data/v8.2/contacts?$select=fullname,contactid,mobilephone,gendercode,firstname,emailaddress1,yomifullname,lastname,kay_contactid,birthdate,aging90_base,aging60_base,aging30_base,middlename,_kaya_preferredclinic_value,createdon'
r = session.get(request_uri)
rawJson = r.content.decode('utf-8')

with open('contacts.json','w') as f:
    f.write(rawJson)