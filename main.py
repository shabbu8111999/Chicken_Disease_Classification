from CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from CnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
from CnnClassifier import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx-----------x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx-----------x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx-----------x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
    model_eval = ModelEvaluationPipeline()
    model_eval.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx-----------x")
except Exception as e:
    logger.exception(e)
    raise e