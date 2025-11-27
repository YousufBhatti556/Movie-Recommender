
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

🚀 App Usage & Quick Access<br><br>
Your MovieFlix application should be running at the following address:

🌐 Open in Browser: http://127.0.0.1:5000

####How to Get Recommendations:<br><br>
Input: Type your favorite movie's name into the search bar (or select it from the list).<br><br>
Output: Click Recommend button to instantly view the Top 5 similar movie suggestions with posters.<br><br><br><br>

<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr style="background-color: #333; color: white;">
            <th style="padding: 10px; border: 1px solid #555; text-align: left;">Category</th>
            <th style="padding: 10px; border: 1px solid #555; text-align: left;">Issue</th>
            <th style="padding: 10px; border: 1px solid #555; text-align: left;">Solution / Best Practice</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 10px; border: 1px solid #555;">🚨 **Module Error**</td>
            <td style="padding: 10px; border: 1px solid #555;"><code>ModuleNotFoundError: No module named 'src'</code></td>
            <td style="padding: 10px; border: 1px solid #555;">Run modules using the **<code>-m</code> flag** from the root directory:<br><code>python -m src.pipeline.training_pipeline</code></td>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #555;">⏱️ **Performance**</td>
            <td style="padding: 10px; border: 1px solid #555;">Flask app takes **too long** to start.</td>
            <td style="padding: 10px; border: 1px solid #555;">Ensure the **training pipeline** (which generates artifacts) has been completed before starting <code>app.py</code>.</td>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #555;">🔒 **Git Security**</td>
            <td style="padding: 10px; border: 1px solid #555;">Committing large artifacts (e.g., <code>similarity.pkl</code>).</td>
            <td style="padding: 10px; border: 1px solid #555;">Do not commit artifact files. Ensure the <code>Movie_Recommender/artifacts/</code> folder is added to **<code>.gitignore</code>**.</td>
        </tr>
    </tbody>
</table><br><br>
### ⚖️ License<br>
This project is provided for Learning, Exploration, and Personal Projects only. Feel free to explore and modify the code!

```
<img width="1415" height="591" alt="image" src="https://github.com/user-attachments/assets/185dfc69-52af-4617-9bfe-37e912741980" />
