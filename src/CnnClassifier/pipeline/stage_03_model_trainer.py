from CnnClassifier.config.configuration import ConfigurationManager
from CnnClassifier.components.model_trainer_03 import Training
from CnnClassifier import logger


STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config = training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()