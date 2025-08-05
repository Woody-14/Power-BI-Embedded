# app.py Function Walkthrough

This document explains the purpose and logic of each function in `app.py` for the Power BI Embedded project.

---

## Overview

`app.py` is a Flask web application that:
- Loads Azure AD and Power BI settings from a `config.ini` file using Python's `configparser`.
- Authenticates with Azure AD using client credentials.
- Requests Power BI embed tokens and URLs for a specific report.
- Serves a static HTML file and a JSON API endpoint for embedding Power BI reports securely.
---

## Configuration Loading

- At startup, `app.py` loads configuration values (tenant ID, client ID, client secret, workspace ID, report ID) from a `config.ini` file using the `configparser` module. This keeps secrets and environment-specific values out of the codebase.

**Example portion of the config.ini:**
```ini
[POWERBI]
WORKSPACE_ID = your-workspace-id
REPORT_ID = your-report-id
```

**Note:** The real `config.ini` should not be committed to version control. Use `config_template.ini` as a template for sharing.

---

## Function-by-Function Explanation

### 1. `get_access_token()`
- **Purpose:**
  - Authenticates with Azure Active Directory (Azure AD) using the OAuth2 client credentials flow.
  - Retrieves an access token for the Power BI REST API.
- **How it works:**
  - Sends a POST request to the Azure AD token endpoint with the app's client ID, client secret, and required scope (all loaded from `config.ini`).
  - Returns the access token from the response.

### 2. `get_embed_token(access_token)`
- **Purpose:**
  - Requests a Power BI embed token for the specified report.
- **How it works:**
  - Sends a POST request to the Power BI REST API `/GenerateToken` endpoint for the report (report and workspace IDs from `config.ini`).
  - Uses the Azure AD access token for authentication.
  - Requests `view` access level.
  - Returns the embed token from the response.

### 3. `get_embed_url(access_token)`
- **Purpose:**
  - Retrieves the embed URL for the specified Power BI report.
- **How it works:**
  - Sends a GET request to the Power BI REST API for the report details (report and workspace IDs from `config.ini`).
  - Uses the Azure AD access token for authentication.
  - Returns the `embedUrl` from the response.

### 4. `index()`
- **Purpose:**
  - Serves the static HTML file (`embed_powerbi_report.html`) when the root URL (`/`) is accessed.
- **How it works:**
  - Uses Flask's `send_from_directory` to send the HTML file from the current directory.

### 5. `get_embed_info()`
- **Purpose:**
  - API endpoint that provides the frontend with all necessary information to embed the Power BI report.
- **How it works:**
  - Calls `get_access_token()` to get an Azure AD token.
  - Calls `get_embed_token()` and `get_embed_url()` to get the embed token and URL.
  - Returns a JSON object with the embed URL, embed token, and report ID.

### 6. `if __name__ == "__main__": ...`
- **Purpose:**
  - Starts the Flask development server when the script is run directly.
- **How it works:**
  - Runs the app in debug mode on the default port (5000).

---

## Summary
- The backend handles all authentication and token management securely.
- The frontend only needs to call `/getEmbedInfo` to get everything it needs to embed the Power BI report.
- This separation keeps secrets safe and makes embedding easy for the frontend.
