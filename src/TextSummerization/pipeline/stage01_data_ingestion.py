from TextSummerization.config.configuration import configurationManager
from TextSummerization.components.data_ingestion import DataIngestion
from TextSummerization import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def run():
        config = configurationManager()
        data_ingestion_config = config.get_data_ingestion()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_file()
