import os
import requests
import logging
import pandas as pd
from msal import ConfidentialClientApplication
from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

print("TENANT_ID:", os.getenv("TENANT_ID"))
print("CLIENT_ID:", os.getenv("CLIENT_ID"))

# -----------------------------
# Setup logging
# -----------------------------
logging.basicConfig(
    filename="lifecycle.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# MSAL Client Credentials Setup
# -----------------------------
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

app = ConfidentialClientApplication(
    client_id=CLIENT_ID,
    client_credential=CLIENT_SECRET,
    authority=AUTHORITY
)

def get_access_token():
    """
    Acquire a token using client credentials
    for Microsoft Graph API.
    """
    result = app.acquire_token_for_client(scopes=SCOPE)
    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception(f"Token error: {result.get('error_description')}")

# -----------------------------
# Azure AD Operations
# -----------------------------
def list_users():
    """
    Lists all users in the tenant.
    """
    token = get_access_token()
    url = "https://graph.microsoft.com/v1.0/users"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    users = response.json().get("value", [])
    for user in users:
        print(f"{user['displayName']} | {user['userPrincipalName']} | {user.get('department', 'N/A')}")

def create_user(display_name, upn, dept):
    """
    Create a new user in Azure AD with a temporary password
    and assign to a department.
    """
    token = get_access_token()
    url = "https://graph.microsoft.com/v1.0/users"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "accountEnabled": True,
        "displayName": display_name,
        "mailNickname": upn.split("@")[0],
        "userPrincipalName": upn,
        "passwordProfile": {
            "forceChangePasswordNextSignIn": True,
            "password": "TempP@ssword123"
        },
        "department": dept
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    print(f"[CREATE] User {display_name} ({upn}) created.")
    logging.info(f"Created user {display_name} | {upn}")

def disable_user(upn):
    """
    Disable (deprovision) a user account.
    """
    token = get_access_token()
    url = f"https://graph.microsoft.com/v1.0/users/{upn}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {"accountEnabled": False}
    response = requests.patch(url, headers=headers, json=payload)
    response.raise_for_status()
    print(f"[DISABLE] User {upn} disabled.")
    logging.info(f"Disabled user {upn}")

# -----------------------------
# CSV-Driven Automation
# -----------------------------
def process_csv(file_path):
    """
    Reads a CSV of user actions and applies
    provisioning/deprovisioning.
    """
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        action = row['action'].strip().lower()
        display_name = row['displayName']
        upn = row['upn']
        dept = row['department']

        try:
            if action == "create":
                create_user(display_name, upn, dept)
            elif action == "disable":
                disable_user(upn)
            else:
                print(f"[SKIP] Unknown action {action} for {upn}")
        except Exception as e:
            print(f"[ERROR] Action {action} for {upn} failed: {e}")
            logging.error(f"Action {action} for {upn} failed: {e}")

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    print("Starting Identity Lifecycle Automation Lab...")
    process_csv("users.csv")
    print("Done.")