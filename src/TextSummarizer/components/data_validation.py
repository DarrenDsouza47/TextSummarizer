import os
from TextSummarizer.logging import logger
from TextSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config=config
    
    def validate_all_files(self)->bool:
        try:
            validation=None
            all_files=os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation=False
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Validation Status: {validation}")   
                else:
                    validation=True
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Validation Status: {validation}")
            
            return validation

        except Exception as e:
            raise e
              


