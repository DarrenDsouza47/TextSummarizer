from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainer
from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from TextSummarizer.logging import logger

STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>stage {STAGE_NAME} started<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>stage {STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation stage"
try:
    logger.info(f">>>stage {STAGE_NAME} started<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>stage {STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f">>>stage {STAGE_NAME} started<<<<<")
    data_transformation=DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>stage {STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training Stage"
try:
    logger.info(f">>>stage {STAGE_NAME} started<<<<<")
    Model_Trainer=ModelTrainer()
    Model_Trainer.main()
    logger.info(f">>>stage {STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Evaluation Stage"
try:
    logger.info(f">>>stage {STAGE_NAME} started<<<<<")
    Model_Evaluation=ModelEvaluationPipeline()
    Model_Evaluation.main()
    logger.info(f">>>stage {STAGE_NAME} completed<<<<<")
except Exception as e:
    logger.exception(e)
    raise e