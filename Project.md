
# Power BI Embedded Project

## The Big Idea

This project lets you securely embed a Power BI report in a web page. It uses:
- A Python Flask backend (on port 5000) to handle authentication with Azure AD and Power BI, and to generate secure embed tokens.
- A static HTML frontend (served on port 8000) that displays the Power BI report using the Power BI JavaScript SDK and fetches tokens from the backend.

---

## Required Elements

### 1. Flask Backend (`app.py`)
- Runs on port 5000.
- Handles authentication with Azure AD and Power BI REST API.
- Exposes:
  - `/getEmbedInfo`: Returns the embed URL, token, and report ID as JSON.
  - `/`: Serves the HTML file (optional, if you want to serve HTML from Flask).

**Start the backend:**
```powershell
python app.py
```

### 2. Static HTTP Server (for HTML, port 8000)
- Serves `embed_powerbi_report.html` so it can be loaded in the browser.
- You can use Python’s built-in HTTP server:

**Start the static server:**
```powershell
python -m http.server 8000
```
- Run this in the directory containing `embed_powerbi_report.html`.

### 3. HTML Frontend (`embed_powerbi_report.html`)
- Loads the Power BI JS SDK.
- Fetches embed info from the backend at `http://localhost:5000/getEmbedInfo`.
- Embeds the report in a div.
- Periodically refreshes the embed token in the background.

**Access the app:**
- Open `http://localhost:8000/embed_powerbi_report.html` in your browser.

---

## How It Works

1. User opens the HTML page in their browser (served from port 8000).
2. The page fetches embed info from the Flask backend (`http://localhost:5000/getEmbedInfo`).
3. The backend authenticates with Azure AD and Power BI, then returns the embed URL and token.
4. The frontend uses the Power BI JS SDK to display the report.
5. The frontend refreshes the token in the background so the report stays active.

---

## Summary

- **Backend:** Flask app on port 5000, handles authentication and token generation.
- **Frontend:** Static HTML on port 8000, fetches tokens and displays the report.
- **No Docker or containers required.** Just run the two Python commands above and open the HTML page in your browser.

---
## Setup

- **README:** Refer to the README.md for step by step setup instructions.

---
