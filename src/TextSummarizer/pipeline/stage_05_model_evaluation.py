from TextSummarizer.components.model_evaluation import Model_Evaluation
from TextSummarizer.config.configuration import ConfigurationManager

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        model_evaluation_config=config.model_evaluation_config()
        model_evaluation=Model_Evaluation(config=model_evaluation_config)
        model_evaluation.evaluate()
        