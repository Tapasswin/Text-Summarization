# Components creation validataion code will be here

import os
from TextSummerization import logger
from TextSummerization.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def data_validation(self) -> bool:
        try:

            validation_status = None

            all_req = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_req:
                if file not in self.config.All_required_files:
                    validation_status = False
                    with open(self.config.Status_file, 'w') as file:
                        file.write(f"Validation Status: {validation_status}")

                else:
                    validation_status = True
                    with open(self.config.Status_file, 'w') as file:
                        file.write(f"Validation Status: {validation_status}")
        except Exception as e:
            validation_status = "ERROR"
            with open(self.config.Status_file, 'w') as file:
                file.write(f"Validation Status: {validation_status}")
            raise e