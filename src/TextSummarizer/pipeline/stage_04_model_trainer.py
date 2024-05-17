from TextSummarizer.components.model_trainer import ModelTrainer
from TextSummarizer.config.configuration import ConfigurationManager
class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        model_trainer_config=config.model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.trainer()