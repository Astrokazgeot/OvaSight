from src.component.model_definition import PCOSModel, ModelConfig


if __name__ == "__main__":
    
    config = ModelConfig()
    model_builder = PCOSModel(config)
    model = model_builder.get_model()
    model.summary() 