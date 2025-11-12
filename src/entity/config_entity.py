from constants import training_pipeline
from datetime import datetime
import os


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        self.timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE
        self.artifact_name = training_pipeline.ARTIFACT_DIR_NAME
        self.artifact_dir = os.path.join(self.pipeline_name, self.artifact_name)



class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME)
        self.movies_data_path = os.path.join(self.data_ingestion_dir, "movies.csv")
        self.credits_data_path = os.path.join(self.data_ingestion_dir, "credits.csv")
        self.final_data_path = os.path.join(self.data_ingestion_dir, "final_data.csv")

        