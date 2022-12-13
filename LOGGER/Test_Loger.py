from flask import Flask
import json
from flask_cors import CORS
from flask import request
from Logger_ import LoggerManager

app = Flask(__name__)
CORS(app)

logger = LoggerManager()

@app.route("/")
def hello_world():
    logger.debug("Starting method")
    try:
        logger.info("Starting the operation ")
        number = 5 / 0
        # force an error to go to the exception
        logger.debug("End Method")
        return str(number)
    except:
        logger.error("We have an exception")
        return "test"
    