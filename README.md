
## Step-by-Step Setup Instructions

1. **Clone or download this repository to your local machine.**

2. **Install Python 3.7+ if you don't have it already.**

3. **Setup your virtual environment:**
   - Open a terminal in the project directory and run:
     ```powershell
         python3 -m venv .venv
     ```

4. **Activate your new virtual environment:**
   - Open a terminal in the project directory and run:
     ```powershell
         source .venv/bin/activate
     ```

5. **Install required Python packages:**
   - Open a terminal in the project directory and run:
     ```powershell
     pip install Flask flask-cors requests
     ```


6. **Configure your Power BI and Azure AD credentials:**
   - Copy `config_template.ini` to `config.ini` in the project directory.
   - Edit `config.ini` and fill in your real values for:
     - `TENANT_ID`, `CLIENT_ID`, `CLIENT_SECRET`, `WORKSPACE_ID`, `REPORT_ID`
   - **(since `config.ini` is in the .gitignore, it will not commit to version control.)**
---

## Configuration Files

- `config_template.ini`: Example config file with placeholder values. Copy this to `config.ini` and fill in your real credentials.
- `config.ini`: Your actual secrets and IDs. **This file is ignored by git and should not be shared.**

The app will not run unless `config.ini` is present and filled out.

7. **Start the Flask backend (port 5000):**
   - In your terminal, run:
     ```powershell
     python3 app.py
     ```
8. **Start a new terminal window:**
   - In VS Code, go to "Terminal" then select "New Terminal"
     
9. **Start the static HTTP server (port 8000):**
   - In a new terminal window, run:
     ```powershell
     python3 -m http.server 8000
     ```
   - Make sure you are in the directory containing `embed_powerbi_report.html`.

10. **Open the app in your browser:**
   - Go to: [http://localhost:8000/embed_powerbi_report.html](http://localhost:8000/embed_powerbi_report.html)

11. **You should see your embedded Power BI report!**

---

If you run into issues, check the terminal output for errors