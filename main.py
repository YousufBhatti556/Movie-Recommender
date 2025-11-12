from src.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from src.components.data_ingestion import Data_Ingestion

if __name__ == "__main__":
    # Step 1: Create pipeline config
    training_pipeline_config = TrainingPipelineConfig()

    # Step 2: Create data ingestion config
    data_ingestion_config = DataIngestionConfig(training_pipeline_config)

    # Step 3: Run data ingestion
    ingestion = Data_Ingestion(data_ingestion_config)
    artifacts = ingestion.initiate_data_ingestion()

    print("\n✅ Data Ingestion Completed Successfully!")
    print("Movies File:", artifacts.movies_file_path)
    print("Credits File:", artifacts.credits_file_path)
    print("Final Data:", artifacts.final_data_path)
