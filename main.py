from src.logging.logger import logging
from src.exception_handling.exception import CustomException

from src.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataProcessingConfig,
    RecommenderTrainingConfig
)

from src.entity.artifact_entity import (
    DataIngestionArtifacts,
    DataProcessingArtifacts,
    RecomendeTrainingrArtifacts
)

from src.components.data_ingestion import Data_Ingestion
from src.components.data_preprocessing import DataProcessing
from src.components.RecommenderTraining import Recommender

import sys


if __name__ == "__main__":
    try:
        logging.info("========== MOVIE RECOMMENDER PIPELINE STARTED ==========")

        # CONFIGS
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_processing_config = DataProcessingConfig(training_pipeline_config)
        recommender_config = RecommenderTrainingConfig(training_pipeline_config)

        # DATA INGESTION
        ingestion = Data_Ingestion(data_ingestion_config)
        ingestion_artifacts = ingestion.initiate_data_ingestion()

        # DATA PROCESSING
        processing = DataProcessing(training_pipeline_config, ingestion_artifacts, data_processing_config)
        processing_artifacts = processing.initiate_processing()

        # MODEL RECOMMENDER TRAINING
        recommender = Recommender(training_pipeline_config, recommender_config, processing_artifacts)
        recommender_artifacts = recommender.initiate_recommendation()

        logging.info("========== PIPELINE FINISHED SUCCESSFULLY ==========")

    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
