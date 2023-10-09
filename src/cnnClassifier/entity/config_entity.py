from dataclasses import dataclass # define the variable instead of using "self" for classes
from pathlib import Path


@dataclass(frozen=True) # not a python class, but a data class (entity): class variable to access the variable from other files
class DataIngestionConfig: # entity names
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path