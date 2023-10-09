from dataclasses import dataclass # define the variable instead of using "self" for classes
from pathlib import Path


@dataclass(frozen=True) # not a python class, but a data class (entity): class variable to access the variable from other files
class DataIngestionConfig: # entity names
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True) #frozen=True, it only accepts the parameters defined in the beginning
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int