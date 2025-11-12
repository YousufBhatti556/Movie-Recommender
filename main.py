from src.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataProcessingConfig
from src.components.data_ingestion import Data_Ingestion
from src.components.data_preprocessing import DataProcessing
from src.logging.logger import logging  # make sure logger object exists
import os

def run_pipeline():
    try:
        # Step 1: Pipeline configuration
        training_pipeline_config = TrainingPipelineConfig()

        # ---------------------- Data Ingestion ----------------------
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        ingestion = Data_Ingestion(data_ingestion_config)
        ingestion_artifacts = ingestion.initiate_data_ingestion()
        logging.info("✅ Data Ingestion completed successfully")

        # ---------------------- Data Processing ----------------------
        data_processing_config = DataProcessingConfig(training_pipeline_config)
        processor = DataProcessing(
            training_pipeline_config=training_pipeline_config,
            data_ingestion_artifacts=ingestion_artifacts,
            data_processing_config=data_processing_config
        )

        processing_artifacts = processor.initiate_processing()
        logging.info("✅ Data Processing completed successfully")
        logging.info(f"Final processed CSV: {processing_artifacts.final_df}")

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        raise e


if __name__ == "__main__":
    run_pipeline()
