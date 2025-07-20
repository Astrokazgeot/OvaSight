import sys
from src.component.dataingestion import DataIngestion
from src.pipeline.predict_pipeline import PCOSModelTrainer
from src.exception import CustomException

def run_training_pipeline():
    try:
        ingestion = DataIngestion()
        train_ds = ingestion.get_train_dataset()
        val_ds = ingestion.get_test_dataset()

        trainer = PCOSModelTrainer()
        trainer.train(train_ds, val_ds)

        print(" Model training completed successfully.")

    except Exception as e:
        raise CustomException(f"[Pipeline Error] {e}", sys)

if __name__ == "__main__":
    run_training_pipeline()
