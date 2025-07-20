import os
import sys
import tensorflow as tf
from dataclasses import dataclass
from src.exception import CustomException
from src.component.model_definition import PCOSModel, ModelConfig 
@dataclass
class TrainerConfig:
    epochs: int = 10
    model_save_path: str = os.path.join("artifacts", "pcos_cnn_model.h5")

class PCOSModelTrainer:
    def __init__(self,
                 model_config: ModelConfig = ModelConfig(),
                 trainer_config: TrainerConfig = TrainerConfig()):
        self.model_config = model_config
        self.trainer_config = trainer_config
        self.model = None

    def train(self, train_ds: tf.data.Dataset, val_ds: tf.data.Dataset):
        try:
         
            model_builder = PCOSModel(self.model_config)
            self.model = model_builder.get_model()

      
            self.model.fit(
                train_ds,
                validation_data=val_ds,
                epochs=self.trainer_config.epochs
            )

            self._save_model()
      
        except Exception as e:
            raise CustomException(f"Error during training: {e}", sys)

    def _save_model(self):
        try:
            self.model.save(self.trainer_config.model_save_path)
            print(f"Model saved at: {self.trainer_config.model_save_path}")
        except Exception as e:
            raise CustomException(f"Error saving model: {e}", sys)
