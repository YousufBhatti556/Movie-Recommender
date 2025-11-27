from flask import Flask, render_template, request
from src.utils.utils import fetch_posters_for_movies  # utils.py se import
from src.pipeline.training import TrainingPipeline
from src.components.recommend import RecommenderService
from src.entity.config_entity import RecommendationConfig
import pandas as pd

pipeline = TrainingPipeline()
ingestion_artifact = pipeline.start_data_ingestion()
processing_artifact = pipeline.start_data_processing(ingestion_artifact)
training_artifact = pipeline.start_recommender_training(processing_artifact)
df = pd.read_csv(processing_artifact.final_df)
all_movies = sorted(df["title"].tolist())

app = Flask(__name__)

NUM_DISPLAY_MOVIES = 10 

@app.route("/", methods=["GET"])
def home():
    # Home page par top N movies display karein
    sample_movies = all_movies[:NUM_DISPLAY_MOVIES] 
    sample_posters = fetch_posters_for_movies(sample_movies) 
    
    return render_template("index.html", 
                           movies=all_movies,
                           display_movies=sample_movies, 
                           movie_posters=sample_posters)

@app.route("/recommend", methods=["POST"])
def recommend():
    movie_name = request.form.get("movie")

    try:
        config = RecommendationConfig(num_recommendations=5)

        service = RecommenderService(
            data_processing_artifacts=processing_artifact,
            training_artifacts=training_artifact,
            recommendation_config=config
        )

        result = service.recommend_movie(movie_name)
        recommended_movies = result.movies
        
        recommended_posters = fetch_posters_for_movies(recommended_movies)

        sample_movies = all_movies[:NUM_DISPLAY_MOVIES]
        sample_posters = fetch_posters_for_movies(sample_movies)
        
        return render_template("index.html",
                               movies=all_movies,
                               display_movies=sample_movies,
                               movie_posters=sample_posters,
                               movie=movie_name,
                               recommendations=recommended_movies,
                               recommended_posters=recommended_posters)

    except Exception as e:
        sample_movies = all_movies[:NUM_DISPLAY_MOVIES]
        sample_posters = fetch_posters_for_movies(sample_movies)
        
        return render_template("index.html",
                               movies=all_movies,
                               display_movies=sample_movies,
                               movie_posters=sample_posters,
                               error=str(e))

if __name__ == "__main__":
    app.run(debug=True)