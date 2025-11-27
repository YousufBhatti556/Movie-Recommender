
# 🎬 Movie Recommender

# Movie Recommender (Content-Based)

A simple content-based movie recommender that uses Count Vectorizer(BOW) + cosine similarity.
Type or choose a movie and get top-5 similar movie recommendations.


## Features
- Count vectorizer on movie text (description/metadata)
- Cosine similarity based recommendations
- Artifacts (vectorizer, similarity matrix) saved as `.pkl`
- Simple Flask web UI: type movie or pick from list → get top 5


## Quick Start

1. Clone repo:
```bash
git clone https://github.com/YOUR-USERNAME/Movie-Recommender.git
cd Movie-Recommender
```


Create & activate virtualenv:
```bash
python -m venv venv
```
# Windows
```bash
venv\Scripts\activate
```
# macOS / Linux
```bash
source venv/bin/activate
```


Install dependencies:
```bash
pip install -r requirements.txt
```

(One-time) Run training pipeline to generate artifacts:

# run training pipeline script (adjust path if different)
```bash
python -m src.pipeline.training_pipeline
```

This creates artifacts like similarity.pkl and final_df.csv under Movie_Recommender/artifacts/.

Run Flask app:

```bash
python app.py
```

🚀 App Usage & Quick Access
Your MovieFlix application should be running at the following address:

🌐 Open in Browser: http://127.0.0.1:5000

How to Get Recommendations:
Input: Type your favorite movie's name into the search bar (or select it from the list).
Output: Click Recommend button to instantly view the Top 5 similar movie suggestions with posters.

⚙️ Essential Best Practices & Troubleshooting
Category	Issue	Solution / Best Practice
🚨 Module Error	ModuleNotFoundError: Run modules using the -m flag from the root directory: python -m src.pipeline.training_pipeline
⏱️ Performance	Flask app takes too long to start:	Ensure the training pipeline (which generates artifacts) has been completed before starting app.py.
🔒 Git Security	Committing large artifacts (e.g., similarity.pkl).	Do not commit artifact files (similarity matrix, vectorizers). Ensure the Movie_Recommender/artifacts/ folder is added to .gitignore.

⚖️ License
This project is provided for Learning, Exploration, and Personal Projects only. Feel free to explore and modify the code!

```
<img width="1415" height="591" alt="image" src="https://github.com/user-attachments/assets/185dfc69-52af-4617-9bfe-37e912741980" />
