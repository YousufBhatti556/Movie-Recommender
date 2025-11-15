🎬 Movie Recommender System (Content-Based)

A simple end-to-end Content-Based Movie Recommendation System built using:

Python

Flask

Scikit-Learn

Cosine Similarity

TF-IDF Vectorizer

This project recommends Top 5 most similar movies based on movie descriptions, genres, keywords, cast, and crew.
Users can type a movie name or select from a suggestion list, and the system instantly shows the best recommendations.

🚀 Features

✔ End-to-end pipeline (Ingestion → Processing → Training → Recommendation)
✔ TF-IDF vectorizer + cosine similarity
✔ Pre-trained similarity matrix stored as artifact
✔ Clean backend structure (component-based architecture)
✔ Flask web app with search + auto-suggest UI
✔ Top 5 movie recommendations
✔ Modular, scalable, production-ready code

📂 Project Structure
Movie-Recommender/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_preprocessing.py
│   │   ├── recommender_training.py
│   │   ├── recommend.py
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py
│   │
│   ├── entity/
│   │   ├── config_entity.py
│   │   ├── artifact_entity.py
│   │
│   ├── logging/
│   ├── exception_handling/
│
├── Movie_Recommender/artifacts/
│   ├── DataProcessing/final_df.csv
│   ├── Recommender/similarity.pkl
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md

🧠 How It Works
1️⃣ Data Ingestion

Loads movie metadata (title, overview, cast, crew, genres).

2️⃣ Data Preprocessing

Cleans text → combines features → builds the “final_df.csv”.

3️⃣ Training

Creates a TF-IDF matrix and computes cosine similarity.
Stores result in:

similarity.pkl

4️⃣ Recommendation

Given a movie name:

Find its index

Look up similarity scores

Sort scores

Return Top 5 similar movies

🌐 Flask Web App

UI provides:

A search bar

Auto suggestions

Top 5 recommendations displayed instantly

Simple, clean UI so you can quickly see results.

🛠 How to Run Locally
1️⃣ Clone the repo
git clone https://github.com/YOUR-USERNAME/Movie-Recommender.git
cd Movie-Recommender

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install requirements
pip install -r requirements.txt

4️⃣ Run Flask app
python -m src.pipeline.training_pipeline   # (Run only once to generate artifacts)
python app.py

5️⃣ Open in browser
http://127.0.0.1:5000

🧪 Example Recommendation

Input:

Batman


Output:

1. The Dark Knight
2. Batman Begins
3. The Dark Knight Rises
4. Batman vs Superman
5. Justice League

📌 Tech Stack

Python

Pandas

NumPy

Scikit-Learn

Flask

HTML + CSS

Pickle (model artifacts)

📜 License

This project is free to use for learning and personal projects.