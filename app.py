from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import requests
import configparser
import os

app = Flask(__name__)
CORS(app)

# Load config from config.ini
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "config.ini"))

TENANT_ID = config.get("AZURE", "TENANT_ID")
CLIENT_ID = config.get("AZURE", "CLIENT_ID")
CLIENT_SECRET = config.get("AZURE", "CLIENT_SECRET")

WORKSPACE_ID = config.get("POWERBI", "WORKSPACE_ID")
REPORT_ID = config.get("POWERBI", "REPORT_ID")


def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://analysis.windows.net/powerbi/api/.default",
    }
    resp = requests.post(url, data=data)
    resp.raise_for_status()
    return resp.json()["access_token"]


def get_embed_token(access_token):
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{WORKSPACE_ID}/reports/{REPORT_ID}/GenerateToken"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    body = {"accessLevel": "view"}
    resp = requests.post(url, headers=headers, json=body)
    resp.raise_for_status()
    return resp.json()["token"]


def get_embed_url(access_token):
    url = (
        f"https://api.powerbi.com/v1.0/myorg/groups/{WORKSPACE_ID}/reports/{REPORT_ID}"
    )
    headers = {"Authorization": f"Bearer {access_token}"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()["embedUrl"]


@app.route("/")
def index():
    return send_from_directory(".", "embed_powerbi_report.html")


@app.route("/getEmbedInfo")
def get_embed_info():
    access_token = get_access_token()
    embed_token = get_embed_token(access_token)
    embed_url = get_embed_url(access_token)
    return jsonify(
        {
            "embedUrl": embed_url,
            "embedToken": embed_token,
            "reportId": REPORT_ID,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
