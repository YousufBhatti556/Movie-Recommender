from src.logging.logger import logging
from src.exception_handling.exception import CustomException
from constants import training_pipeline
from src.entity.artifact_entity import DataIngestionArtifacts, DataProcessingArtifacts, RecomendeTrainingrArtifacts
from src.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataProcessingConfig, RecommenderTrainingConfig
import pandas as pd
import os, sys
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
nltk.download('wordnet')
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pickle

class Recommender:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig,
                 recommender_config: RecommenderTrainingConfig,
                 data_processing_artifacts: DataProcessingArtifacts):

        self.training_pipeline_config = training_pipeline_config
        self.recommender_config = recommender_config
        self.data_processing_artifacts = data_processing_artifacts

    def initiate_recommendation(self):
        try:
            logging.info("Reading the processed dataframe")
            df = pd.read_csv(self.data_processing_artifacts.final_df)

            logging.info("Vectorizing tags using CountVectorizer")
            cv = CountVectorizer(max_features=5000, stop_words="english")
            vectors = cv.fit_transform(df["tags"])

            logging.info("Calculating cosine similarity matrix")
            similarity = cosine_similarity(vectors)


            os.makedirs(self.recommender_config.recommender_dir, exist_ok=True)

            logging.info("Saving vectorizer.pkl")
            pickle.dump(cv, open(self.recommender_config.vectorizer_path, "wb"))

            # Save similarity matrix
            logging.info("Saving similarity.pkl")
            pickle.dump(similarity, open(self.recommender_config.similarity_matrix_path, "wb"))

            logging.info("=== MODEL TRAINING COMPLETED SUCCESSFULLY ===")

            # Return artifacts object
            return RecomendeTrainingrArtifacts(
                vectorizer_path=self.recommender_config.vectorizer_path,
                similarity_matrix_path=self.recommender_config.similarity_matrix_path,
            )
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e, sys)