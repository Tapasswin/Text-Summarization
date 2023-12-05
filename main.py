from TextSummerization import logger
from TextSummerization.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from TextSummerization.pipeline.stage02_data_validation import DataValidationTrainingPipeline


STAGE_NAME = "Data Ingestion Staging"

try:
    logger.info(f"####################### Staring of {STAGE_NAME} #####################")
    data_ingestion = DataIngestionTrainingPipeline
    data_ingestion.run()
    logger.info(f"####################### END OF {STAGE_NAME} #####################")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"

try:
    logger.info(f"####################### Staring of {STAGE_NAME} #####################")
    data_validation = DataValidationTrainingPipeline
    data_validation.validate()
    logger.info(f"####################### END OF {STAGE_NAME} #####################")
except Exception as e:
    logger.exception(e)
    raise e