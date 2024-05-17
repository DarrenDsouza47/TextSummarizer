from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config=ConfigurationManager()
        data_transformation_config=config.data_transformation_config()
        data_transformation=DataTransformation(data_transformation_config)
        data_transformation.convert()

