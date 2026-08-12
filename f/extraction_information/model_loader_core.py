import os
import wmill

import wmill

MODEL_REGISTRY_PATH = "f/extraction_information/models"


def get_model_config(model_path: str | None = None):
    registry = wmill.get_resource(MODEL_REGISTRY_PATH)

    models = registry.get("models", {})
    default_model_name = registry.get("default")

    # nếu user không truyền → lấy default
    if not model_path:
        model_path = models.get(default_model_name)

    # nếu user truyền full resource path
    elif model_path.startswith("f/"):
        return wmill.get_resource(model_path)

    # nếu user truyền tên model
    else:
        model_path = models.get(model_path)

    if not model_path:
        raise ValueError("Model not found")

    return wmill.get_resource(model_path)