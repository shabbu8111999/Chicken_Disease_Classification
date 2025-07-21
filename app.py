from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import logging

from CnnClassifier.utils.common import decodeImage
from CnnClassifier.pipeline.predict import PredictionPipeline

# Set environment variables for language settings
os.environ['LANG'] = 'en_US.UTF-8'
os.environ['LC_ALL'] = 'en_US.UTF-8'

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


# Initialize ClientApp once when the server starts
clApp = ClientApp()


@app.route("/", methods=["GET"])
def home():
    """Render the home page with upload form"""
    logging.info("Serving Home Page")
    return render_template("index.html")


@app.route("/train", methods=["GET", "POST"])
def train_route():
    """Trigger model training"""
    try:
        logging.info("Training initiated...")
        os.system("python main.py")
        logging.info("Training completed successfully.")
        return "✅ Training has been completed successfully!"
    except Exception as e:
        logging.exception("Error during training:")
        return f"❌ Training failed: {str(e)}", 500


@app.route("/predict", methods=["POST"])
def predict_route():
    """Handle prediction requests"""
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({"error": "No image provided"}), 400

        image_base64 = data['image']
        decodeImage(image_base64, clApp.filename)

        result = clApp.classifier.predict()
        logging.info(f"Prediction result: {result}")
        return jsonify(result)

    except Exception as e:
        logging.exception("Error during prediction:")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    logging.info("Starting Flask server...")
    app.run(host="0.0.0.0", port=8080, debug=True)
