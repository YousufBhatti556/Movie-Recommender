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
class RecomenderTrainingrArtifacts:
    similarity_matrix_path : str
    vectorizer_path : str

@dataclass
class RecoomendArtifacts:
    movies : list