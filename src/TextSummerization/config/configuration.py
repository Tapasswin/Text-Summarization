from TextSummerization.constants import *
from TextSummerization.utils.common import read_yaml, create_directories
from TextSummerization.entity.config_entity import (DataIngestionConfig,
                                                    DataValidationConfig)

class configurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
    
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL= config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation = DataValidationConfig(
            root_dir= config.root_dir,
            Status_file=config.Status_file,
            All_required_files=config.All_required_files
        )

        return data_validation