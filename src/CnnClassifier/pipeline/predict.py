import os
import numpy as np
import logging
from typing import List, Dict

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class PredictionPipeline:
    MODEL_PATH = os.path.join("artifacts", "training", "model.h5")
    TARGET_SIZE = (224, 224)
    LABELS = {0: "Coccidiosis", 1: "Healthy"}

    def __init__(self, filename: str):
        self.filename = filename
        self.model = self._load_model()

    def _load_model(self):
        """Load the trained Keras model from disk."""
        try:
            logging.info(f"Loading model from {self.MODEL_PATH}")
            model = load_model(self.MODEL_PATH)
            logging.info("Model loaded successfully.")
            return model
        except Exception as e:
            logging.exception("Failed to load model.")
            raise RuntimeError(f"Error loading model: {e}")

    def _preprocess_image(self) -> np.ndarray:
        """Load and preprocess the image for prediction."""
        try:
            logging.info(f"Loading and preprocessing image: {self.filename}")
            img = image.load_img(self.filename, target_size=self.TARGET_SIZE)
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0  # Normalizing pixel values
            return img_array
        except Exception as e:
            logging.exception("Image preprocessing failed.")
            raise ValueError(f"Error processing image: {e}")

    def predict(self) -> List[Dict[str, str]]:
        """Predict the class of the image and return the result."""
        try:
            processed_image = self._preprocess_image()
            prediction = self.model.predict(processed_image)
            class_index = int(np.argmax(prediction, axis=1)[0])
            predicted_label = self.LABELS.get(class_index, "Unknown")

            logging.info(f"Prediction complete. Class: {predicted_label}")
            return [{"image": predicted_label}]
        except Exception as e:
            logging.exception("Prediction failed.")
            return [{"error": str(e)}]
