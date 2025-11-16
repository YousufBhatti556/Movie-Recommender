🎬 Movie Recommender

# Movie Recommender (Content-Based)

A simple content-based movie recommender that uses Count Vectorizer(BOW) + cosine similarity.
Type or choose a movie and get top-5 similar movie recommendations.

---

## Features
- Count vectorizer on movie text (description/metadata)
- Cosine similarity based recommendations
- Artifacts (vectorizer, similarity matrix) saved as `.pkl`
- Simple Flask web UI: type movie or pick from list → get top 5

---

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

Open http://127.0.0.1:5000 in your browser.

Usage

Type a movie name or click one from the sliding list.

Click Recommend to see top 5 similar movies.

Note: Don’t commit large artifact files (similarity matrix, .pkl) to Git. Add Movie_Recommender/artifacts/ to .gitignore.

Troubleshooting

If ModuleNotFoundError: No module named 'src' occurs, run modules with -m from project root, e.g.:

python -m src.pipeline.training_pipeline


If Flask seems stuck, ensure training is finished before starting the app (or load saved artifacts instead of retraining on start).

License

Use for learning and personal projects.



