from src.logging.logger import logging
from src.exception_handling.exception import CustomException
from src.entity.config_entity import DataIngestionConfig, DataProcessingConfig, TrainingPipelineConfig, RecommenderTrainingConfig, RecommendationConfig
from src.entity.artifact_entity import RecomenderTrainingrArtifacts, DataProcessingArtifacts, RecoomendArtifacts
import pandas as pd
import os, sys
import pickle


class RecommenderService:
    def __init__(self, data_processing_artifacts: DataProcessingArtifacts, training_artifacts: RecomenderTrainingrArtifacts,
                 recommendation_config: RecommendationConfig):
        self.data_processing_artifacts = data_processing_artifacts
        self.training_artifacts = training_artifacts
        self.recommendation_config = recommendation_config

    def recommend_movie(self, movie: str)->RecoomendArtifacts:
        try:
            logging.info("Reading the dataframe")
            df = pd.read_csv(self.data_processing_artifacts.final_df)

            if movie not in df["title"].values:
                raise ValueError(f"{movie} not found in dataset.")
            idx = df[df["title"] == movie].index[0]

            logging.info("Loading the similarity matrix")
            with open(self.training_artifacts.similarity_matrix_path, "rb") as f:
                similarity_matrix = pickle.load(f)

            

            sim_scores = sorted(list(enumerate(similarity_matrix[idx])), key=lambda x: x[1], reverse=True)

            sim_scores = sim_scores[1:self.recommendation_config.num_recommendations+1]
            movie_indices = [i[0] for i in sim_scores]

            recommendations = df["title"].iloc[movie_indices].tolist()

            logging.info(f"Recommendations generated for '{movie}'")

            return RecoomendArtifacts(movies=recommendations)




        except Exception as e:
            logging.info(CustomException(e, sys))
            raise CustomException(e, sys)

