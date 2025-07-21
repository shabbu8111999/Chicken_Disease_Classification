from CnnClassifier.components.model_evaluation_04 import Evaluation
from CnnClassifier.config.configuration import ConfigurationManager
from CnnClassifier import logger



STAGE_NAME = "Model Evaluation Stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()