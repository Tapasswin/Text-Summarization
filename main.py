from TextSummerization import logger
from TextSummerization.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Staging"

try:
    logger.info(f"####################### Staring of {STAGE_NAME} #####################")
    data_ingestion = DataIngestionTrainingPipeline
    data_ingestion.run()
    logger.info(f"####################### END OF {STAGE_NAME} #####################")
except Exception as e:
    logger.exception(e)
    raise e