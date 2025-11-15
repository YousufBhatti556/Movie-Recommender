from flask import Flask, render_template, request
from src.pipeline.training import TrainingPipeline
from src.components.recommend import RecommenderService
from src.entity.config_entity import RecommendationConfig

pipeline = TrainingPipeline()

# Run ingestion + processing only ONCE
ingestion_artifact = pipeline.start_data_ingestion()
processing_artifact = pipeline.start_data_processing(ingestion_artifact)
training_artifact = pipeline.start_recommender_training(processing_artifact)

# Load movies for frontend scroll list
import pandas as pd
df = pd.read_csv(processing_artifact.final_df)
all_movies = sorted(df["title"].tolist())

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", movies=all_movies)

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

        return render_template("index.html",
                               movies=all_movies,
                               movie=movie_name,
                               recommendations=result.movies)

    except Exception as e:
        return render_template("index.html",
                               movies=all_movies,
                               error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
