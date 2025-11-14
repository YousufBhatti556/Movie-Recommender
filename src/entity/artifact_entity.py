from dataclasses import dataclass


@dataclass
class DataIngestionArtifacts:
    movies_file_path: str
    credits_file_path: str
    final_data_path: str


@dataclass
class DataProcessingArtifacts:
    final_df: str

@dataclass
class RecomendeTrainingrArtifacts:
    similarity_matrix_dir_path : str
    vectors_dir_path : str