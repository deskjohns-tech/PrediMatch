import os

folders = [
    "app",
    "data"
]

files = {
    "README.md": "# PrediMatch\n\nSoccer prediction demo app.",
    "requirements.txt": "streamlit\npandas\nscikit-learn\nlightgbm",
    ".gitignore": "*.pyc\n__pycache__/\ndata/*.csv",
    "data/sample_matches.csv": "team_a,team_b,date,score_a,score_b\nArsenal,Chelsea,2023-08-01,2,1",
    "app/main.py": "# Streamlit entry point\nimport streamlit as st\nst.title('PrediMatch Demo')",
    "app/match_predictor.py": "# Match prediction logic",
    "app/data_loader.py": "# Data loading functions",
    "app/rating_models.py": "# TrueSkill and Glicko models",
    "app/simulation.py": "# Match simulation logic",
    "app/utils.py": "# Helper functions"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ PrediMatch folder scaffolded successfully.")
