import os
import wmill
from typing import cast



def get_model_config(model_name: str | None):
    registry = cast(dict, wmill.get_resource("f/extraction_information/models"))

    models = registry.get("models", {})

    # default
    if not model_name:
        model_name = registry.get("default") or list(models.keys())[0]

    resource_path = models.get(model_name)

    if not resource_path:
        raise ValueError(f"Model {model_name} not found in {models}")

    model_cfg = wmill.get_resource(resource_path)

    if not model_cfg:
        raise ValueError(f"Resource {resource_path} returned None")

    return model_cfg