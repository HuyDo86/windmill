import os
import wmill


SCHEMA_REGISTRY = {
    "phieu_chi": "f/extraction_information/phieu_chi",
    "phieu_thu": "f/extraction_information/schema/phieu_thu",
    "phieu_nhap": "f/extraction_information/schema/phieu_nhap",
    "phieu_xuat": "f/extraction_information/schema/phieu_xuat",
}


def get_schema(doc_type: str):
    path = SCHEMA_REGISTRY.get(doc_type)

    if not path:
        return None

    return wmill.get_resource(path)