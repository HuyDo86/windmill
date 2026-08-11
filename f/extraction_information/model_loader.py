import os
import wmill
from typing import cast


def get_model_config(model_name: str | None):
    registry = cast(dict, wmill.get_resource("f/extraction_information/models"))

    # default
    if not model_name:
        model_name = list(registry.keys())[0]

    resource_path = registry.get(model_name)

    if not resource_path:
        raise ValueError(f"Model {model_name} not found")
    print("MODEL NAME:", model_name)

    registry = wmill.get_resource("u/huyxuan264/models")
    print("REGISTRY:", registry)
    print("TYPE:", type(registry))
    return wmill.get_resource(resource_path)
