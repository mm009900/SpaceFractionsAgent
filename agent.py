import os
import json

def generate_space_fractions_project():
    # Verify input file exists
    if not os.path.exists("architecture_input.json"):
        print("Error: architecture_input.json not found! Run parser.py first.")
        return

    output_dir = "generated_project"
    public_dir = os.path.join(output_dir, "public")
    os.makedirs(public_dir, exist_ok=True)

    print("Generating Space Fractions Desktop Project Files...")

    # 1. Write package.json configured for Electron
    package_data = {
        "name": "space-fractions",
        "version": "1.0.0",
        "main": "main.js",
        "scripts": {
            "start": "electron ."
        },
        "devDependencies": {
            "electron": "^28.0.0"
        }
    }

    with open(os.path.join(output_dir, "package.json"), "w", encoding="utf-8") as f:
        json.dump(package_data, f, indent=2)

    # 2. Write main.js to launch Electron desktop window
    electron_main = """const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    title: "Space Fractions",
    autoHideMenuBar: true,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  win.loadFile(path.join(__dirname, 'public', 'index.html'));
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
"""
    with open(os.path.join(output_dir, "main.js"), "w", encoding="utf-8") as f:
        f.write(electron_main)

    # 3. Write public/index.html (Game UI)
    html_lines = """<!DOCTYPE html>
<html>
<head>
    <title>Space Fractions</title>
    <style>
        body { background: #0b0d1b; color: white; font-family: sans-serif; text-align: center; padding: 50px; }
        .box { background: #161b33; border: 2px solid #4a4e69; padding: 30px; border-radius: 10px; display: inline-block; }
        button { background: #3f37c9; color: white; border: none; padding: 12px 24px; font-size: 18px; margin: 8px; cursor: pointer; border-radius: 5px; }
        button:hover { background: #4895ef; }
    </style>
</head>
<body>
    <div class="box">
        <h1>Space Fractions</h1>
        <p><strong>Mission Question: Solve 1/4 + 2/4 = ?</strong></p>
        <div>
            <button onclick="alert('Correct! High score achieved!')">3/4</button>
            <button onclick="alert('Incorrect! Try again.')">2/4</button>
            <button onclick="alert('Incorrect! Try again.')">1/2</button>
        </div>
    </div>
</body>
</html>
"""
    with open(os.path.join(public_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_lines)

    print("Success! Created 'generated_project' folder with local desktop app files.")

if __name__ == "__main__":
    generate_space_fractions_project()