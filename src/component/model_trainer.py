from tensorflow.keras import layers, models
from dataclasses import dataclass

@dataclass
class ModelConfig:
    input_shape: tuple = (180, 180, 3)
    num_classes: int = 2  
    dropout_rate: float = 0.5

class PCOSModel:
    def __init__(self, config: ModelConfig = ModelConfig()):
        self.config = config

    def get_model(self):
        model = models.Sequential([
            layers.Input(shape=self.config.input_shape),
            layers.Conv2D(32, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dropout(self.config.dropout_rate),
            layers.Dense(128, activation='relu'),
            layers.Dense(self.config.num_classes, activation='sigmoid')
        ])

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        return model