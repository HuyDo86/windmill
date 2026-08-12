import os
import wmill


SCHEMA_REGISTRY = {
    "phieu_chi": "f/extraction_information/schema_phieu_chi",
    "phieu_thu": "f/extraction_information/schema_phieu_thu",
    "phieu_nhap": "f/extraction_information/schema_phieu_nhap",
    "phieu_xuat": "f/extraction_information/schema_phieu_xuat",
    "chuyen_khoan": "f/extraction_information/schema_chuyen_khoan",
    "van_don": "f/extraction_information/schema_van_don",
    "thanh_toan": "f/extraction_information/schema_thanh_toan",
    "hoa_don": "f/extraction_information/schema_hoa_don",
    "bao_gia": "f/extraction_information/schema_bao_gia",
    "thue": "f/extraction_information/schema_thue",
    "bien_ban_lam_viec": "f/extraction_information/schema_bien_ban_lam_viec",
    "phieu_giao_nhan_hang_hoa": "f/extraction_information/schema_phieu_giao_nhan_hang_hoa",
    "phieu_giao_nhan_be_tong": "f/extraction_information/schema_phieu_giao_nhan_be_tong",

}


def get_schema(doc_type: str):
    path = SCHEMA_REGISTRY.get(doc_type)

    if not path:
        return None

    return wmill.get_resource(path)