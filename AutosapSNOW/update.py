import requests

# Constants
url = "https://gskdev.service-now.com/api/gskgs/service_catalog_task/Update_Task"
task_id = "SCTASK2906031"
client_id = "61dddd006c38a210b4fcfe3348a76489"
client_secret = "GR!Q84VQ-8"
username = "event_int_nexthink_dev"
password = "Opend00r1nexthink!"

# Get the access token
token_url = "https://gskdev.service-now.com/oauth_token.do"
token_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
}

response = requests.post(token_url, data=token_data)
access_token = response.json().get("access_token")

# Check if the token was retrieved successfully
if access_token:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "task_id": task_id,
        "Content-Type": "application/json",
    }
    
    # Body of the PATCH request
    body = {
        "work_notes": "test update 123"
    }
    
    # Make the PATCH request
    patch_response = requests.patch(url, headers=headers, json=body)
    
    # Print the response
    if patch_response.status_code == 200:
        print("Task updated successfully:", patch_response.json())
    else:
        print("Error updating task:", patch_response.status_code, patch_response.text)
else:
    print("Failed to retrieve access token.")
