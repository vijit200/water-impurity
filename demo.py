from WaterImpurity.pipeline.pipeline import pipeline
from WaterImpurity.exception import WaterException
from WaterImpurity.logger import logging
def main():
    try:
        pipe = pipeline()
        pipe.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()