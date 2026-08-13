import wmill

MODEL_REGISTRY_PATH = "f/extraction_information/models"


def get_model_config(model_path: str | None = None):
    registry = wmill.get_resource(MODEL_REGISTRY_PATH)

    models = registry.get("models", {})
    default_model_name = registry.get("default")

    # CASE 1: không truyền → lấy default
    if not model_path:
        model_path = models.get(default_model_name)

    # CASE 2: user truyền full path
    elif model_path.startswith("f/"):
        return wmill.get_resource(model_path)

    # CASE 3: user truyền tên model
    else:
        model_path = models.get(model_path)

    if not model_path:
        raise ValueError("Model not found")

    return wmill.get_resource(model_path)