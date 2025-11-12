from dataclasses import dataclass


@dataclass
class DataIngestionArtifacts:
    movies_file_path: str
    credits_file_path: str
    final_data_path: str