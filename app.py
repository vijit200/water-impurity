from flask import Flask
import sys
from WaterImpurity.logger import logging
from WaterImpurity.exception import WaterException
app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = WaterException(e,sys)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True,port=5000)