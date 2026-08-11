import os
import wmill
from typing import Optional, List
from pydantic import BaseModel, ConfigDict

# vận đơn
class CargoItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    stt: Optional[int] = None
    name: Optional[str] = None
    unit: Optional[str] = None
    quantity: Optional[float] = None
    weight_kg: Optional[float] = None
    volume_m3: Optional[float] = None
    declared_value: Optional[float] = None


class Waybill(BaseModel):
    model_config = ConfigDict(extra="allow")
    waybill_number: Optional[str] = None
    order_code: Optional[str] = None
    internal_code: Optional[str] = None
    date: Optional[str] = None
    carrier_name: Optional[str] = None
    driver_name: Optional[str] = None
    driver_phone: Optional[str] = None
    vehicle_number: Optional[str] = None
    transport_route: Optional[str] = None
    sender_organization: Optional[str] = None
    sender_name: Optional[str] = None
    sender_phone: Optional[str] = None
    sender_address: Optional[str] = None
    receiver_organization: Optional[str] = None
    receiver_name: Optional[str] = None
    receiver_phone: Optional[str] = None
    receiver_address: Optional[str] = None
    items: Optional[List[CargoItem]] = None
    freight_charge: Optional[float] = None
    surcharges: Optional[float] = None
    total_charge: Optional[float] = None
    currency: Optional[str] = None
    cod_amount: Optional[float] = None
    note: Optional[str] = None


# Báo giá
class QuotationItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    code: Optional[str] = None
    name: Optional[str] = None
    specification: Optional[str] = None
    unit: Optional[str] = None
    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    amount: Optional[float] = None


class Quotation(BaseModel):
    model_config = ConfigDict(extra="allow")
    quotation_number: Optional[str] = None
    date: Optional[str] = None
    validity_period: Optional[str] = None
    supplier_name: Optional[str] = None
    supplier_address: Optional[str] = None
    supplier_contact: Optional[str] = None
    supplier_phone: Optional[str] = None
    supplier_email: Optional[str] = None
    customer_name: Optional[str] = None
    customer_address: Optional[str] = None
    customer_contact: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_email: Optional[str] = None
    items: Optional[List[QuotationItem]] = None
    subtotal_amount: Optional[float] = None
    vat_tax: Optional[float] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    amount_in_words: Optional[str] = None
    payment_terms: Optional[str] = None
    delivery_terms: Optional[str] = None
    warranty_terms: Optional[str] = None
    project: Optional[str] = None
    note: Optional[str] = None

#Phiếu nhập
class StockReceiptItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    code: Optional[str] = None
    name: Optional[str] = None
    unit: Optional[str] = None
    quantity_doc: Optional[float] = None
    quantity_real: Optional[float] = None
    unit_price: Optional[float] = None
    amount: Optional[float] = None


class StockReceiptNote(BaseModel):
    model_config = ConfigDict(extra="allow")
    document_number: Optional[str] = None
    date: Optional[str] = None
    debit_account: Optional[str] = None
    credit_account: Optional[str] = None
    supplier: Optional[str] = None
    supplier_representative: Optional[str] = None
    supplier_email: Optional[str] = None
    supplier_phone: Optional[str] = None
    supplier_address: Optional[str] = None
    receiver: Optional[str] = None
    receiver_representative: Optional[str] = None
    receiver_email: Optional[str] = None
    receiver_phone: Optional[str] = None
    creator_name: Optional[str] = None
    approver_name: Optional[str] = None
    contract: Optional[str] = None
    invoice: Optional[str] = None
    delivery_location: Optional[str] = None
    issued_from: Optional[str] = None
    reason: Optional[str] = None
    items: Optional[List[StockReceiptItem]] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    total_amount_in_words: Optional[str] = None
    note: Optional[str] = None
    project: Optional[str] = None
    attached_documents: Optional[str] = None

#Phiếu chi
class ExpenseItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    stt: Optional[int] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    note: Optional[str] = None


class PhieuChi(BaseModel):
    model_config = ConfigDict(extra="allow")
    code: Optional[str] = None
    date: Optional[str] = None
    payer_organization: Optional[str] = None
    payer_name: Optional[str] = None
    payer_phone: Optional[str] = None
    payer_address: Optional[str] = None
    receiver_organization: Optional[str] = None
    receiver_name: Optional[str] = None
    receiver_phone: Optional[str] = None
    receiver_address: Optional[str] = None
    approver_organization: Optional[str] = None
    approver_name: Optional[str] = None
    approver_phone: Optional[str] = None
    creator_name: Optional[str] = None
    debit_account: Optional[str] = None
    credit_account: Optional[str] = None
    expense_type: Optional[str] = None
    expense_category: Optional[str] = None
    reason: Optional[str] = None
    amount: Optional[float] = None
    amount_in_words: Optional[str] = None
    currency: Optional[str] = None
    payment_method: Optional[str] = None
    bank_account: Optional[str] = None
    contract: Optional[str] = None
    invoice: Optional[str] = None
    project: Optional[str] = None
    fund: Optional[str] = None
    attached_documents: Optional[str] = None
    items: Optional[List[ExpenseItem]] = None
    note: Optional[str] = None

# Phiếu xuất
class StockIssueItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    code: Optional[str] = None
    name: Optional[str] = None
    unit: Optional[str] = None
    quantity_requested: Optional[float] = None
    quantity_real: Optional[float] = None
    unit_price: Optional[float] = None
    amount: Optional[float] = None


class StockIssueNote(BaseModel):
    model_config = ConfigDict(extra="allow")
    document_number: Optional[str] = None
    date: Optional[str] = None
    debit_account: Optional[str] = None
    credit_account: Optional[str] = None
    issuer_organization: Optional[str] = None
    issuer_representative: Optional[str] = None
    issuer_phone: Optional[str] = None
    receiver: Optional[str] = None
    receiver_representative: Optional[str] = None
    receiver_phone: Optional[str] = None
    creator_name: Optional[str] = None
    approver_name: Optional[str] = None
    contract: Optional[str] = None
    invoice: Optional[str] = None
    delivery_location: Optional[str] = None
    issued_from: Optional[str] = None
    reason: Optional[str] = None
    items: Optional[List[StockIssueItem]] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    total_amount_in_words: Optional[str] = None
    note: Optional[str] = None
    project: Optional[str] = None
    attached_documents: Optional[str] = None

#Phiếu thu
class PhieuThuItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    stt: Optional[int] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    note: Optional[str] = None


class PhieuThu(BaseModel):
    model_config = ConfigDict(extra="allow")
    code: Optional[str] = None
    date: Optional[str] = None
    receiver_organization: Optional[str] = None
    receiver_name: Optional[str] = None
    receiver_phone: Optional[str] = None
    receiver_address: Optional[str] = None
    payer_organization: Optional[str] = None
    payer_name: Optional[str] = None
    payer_phone: Optional[str] = None
    payer_address: Optional[str] = None
    approver_organization: Optional[str] = None
    approver_name: Optional[str] = None
    approver_phone: Optional[str] = None
    creator_name: Optional[str] = None
    debit_account: Optional[str] = None
    credit_account: Optional[str] = None
    receipt_type: Optional[str] = None
    reason: Optional[str] = None
    amount: Optional[float] = None
    amount_in_words: Optional[str] = None
    currency: Optional[str] = None
    payment_method: Optional[str] = None
    bank_account: Optional[str] = None
    contract: Optional[str] = None
    invoice: Optional[str] = None
    task: Optional[str] = None
    project: Optional[str] = None
    fund: Optional[str] = None
    attached_documents: Optional[str] = None
    items: Optional[List[PhieuThuItem]] = None
    note: Optional[str] = None

#Phiếu thuế
class TaxItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    stt: Optional[int] = None
    tax_content: Optional[str] = None
    tax_period: Optional[str] = None
    subgroup_code: Optional[str] = None
    chapter_code: Optional[str] = None
    economic_content_code: Optional[str] = None
    amount: Optional[float] = None


class PhieuNopThue(BaseModel):
    model_config = ConfigDict(extra="allow")
    document_number: Optional[str] = None
    date: Optional[str] = None
    taxpayer_name: Optional[str] = None
    taxpayer_code: Optional[str] = None
    taxpayer_address: Optional[str] = None
    declarant_name: Optional[str] = None
    collecting_authority: Optional[str] = None
    treasury_account: Optional[str] = None
    treasury_name: Optional[str] = None
    district_province: Optional[str] = None
    items: Optional[List[TaxItem]] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    total_amount_in_words: Optional[str] = None
    payment_method: Optional[str] = None
    bank_account_debited: Optional[str] = None
    project: Optional[str] = None
    note: Optional[str] = None

#yêu cầu thanh toán
class PaymentRequestItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    code: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    attached_doc: Optional[str] = None


class PaymentRequest(BaseModel):
    model_config = ConfigDict(extra="allow")
    request_number: Optional[str] = None
    date: Optional[str] = None
    requester_name: Optional[str] = None
    requester_department: Optional[str] = None
    requester_organization: Optional[str] = None
    requester_phone: Optional[str] = None
    beneficiary_name: Optional[str] = None
    beneficiary_account: Optional[str] = None
    beneficiary_bank: Optional[str] = None
    reason: Optional[str] = None
    expense_category: Optional[str] = None
    project: Optional[str] = None
    contract: Optional[str] = None
    invoice: Optional[str] = None
    items: Optional[List[PaymentRequestItem]] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    total_amount_in_words: Optional[str] = None
    advance_amount: Optional[float] = None
    remaining_amount: Optional[float] = None
    approver_name: Optional[str] = None
    attached_documents: Optional[str] = None
    note: Optional[str] = None

#Phiếu giao nhận hàng hóa
class DeliveryItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    code: Optional[str] = None
    name: Optional[str] = None
    unit: Optional[str] = None
    quantity_sent: Optional[float] = None
    quantity_received: Optional[float] = None
    unit_price: Optional[float] = None
    amount: Optional[float] = None
    status_note: Optional[str] = None


class PhieuGiaoNhanHangHoa(BaseModel):
    model_config = ConfigDict(extra="allow")
    document_number: Optional[str] = None
    date: Optional[str] = None
    deliverer_organization: Optional[str] = None
    deliverer_name: Optional[str] = None
    deliverer_phone: Optional[str] = None
    deliverer_address: Optional[str] = None
    vehicle_number: Optional[str] = None
    receiver_organization: Optional[str] = None
    receiver_name: Optional[str] = None
    receiver_phone: Optional[str] = None
    delivery_location: Optional[str] = None
    contract: Optional[str] = None
    project: Optional[str] = None
    items: Optional[List[DeliveryItem]] = None
    total_amount: Optional[float] = None
    currency: Optional[str] = None
    total_amount_in_words: Optional[str] = None
    note: Optional[str] = None
    deliverer_signature_name: Optional[str] = None
    receiver_signature_name: Optional[str] = None

#Phiếu giao nhận bê tông
class PhieuGiaoNhanBeTong(BaseModel):
    model_config = ConfigDict(extra="allow")
    document_number: Optional[str] = None
    date: Optional[str] = None
    supplier: Optional[str] = None
    plant_location: Optional[str] = None
    customer: Optional[str] = None
    project: Optional[str] = None
    construction_item: Optional[str] = None
    delivery_location: Optional[str] = None
    concrete_grade: Optional[str] = None
    slump: Optional[str] = None
    additive: Optional[str] = None
    stone_size: Optional[str] = None
    volume_m3: Optional[float] = None
    accumulated_volume_m3: Optional[float] = None
    batch_number: Optional[str] = None
    driver_name: Optional[str] = None
    truck_number: Optional[str] = None
    pump_type: Optional[str] = None
    pump_code: Optional[str] = None
    time_leaving_plant: Optional[str] = None
    time_arriving_site: Optional[str] = None
    time_starting_pour: Optional[str] = None
    time_finishing_pour: Optional[str] = None
    receiver_signature_name: Optional[str] = None
    driver_signature_name: Optional[str] = None
    note: Optional[str] = None

#Phiếu chuyển khoản
class ChuyenKhoanNganHang(BaseModel):
    model_config = ConfigDict(extra="allow")
    transaction_code: Optional[str] = None
    transaction_type: Optional[str] = None
    date: Optional[str] = None
    remitter_name: Optional[str] = None
    remitter_account: Optional[str] = None
    remitter_bank: Optional[str] = None
    remitter_address: Optional[str] = None
    beneficiary_name: Optional[str] = None
    beneficiary_account: Optional[str] = None
    beneficiary_bank: Optional[str] = None
    beneficiary_address: Optional[str] = None
    amount: Optional[float] = None
    amount_in_words: Optional[str] = None
    currency: Optional[str] = None
    fee_amount: Optional[float] = None
    fee_bearer: Optional[str] = None
    reason: Optional[str] = None
    contract: Optional[str] = None
    invoice: Optional[str] = None
    project: Optional[str] = None
    bank_seal_status: Optional[str] = None
    note: Optional[str] = None

#Biên bản làm việc
class Participant(BaseModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = None
    position: Optional[str] = None
    organization: Optional[str] = None
    role: Optional[str] = None


class BienBanLamViec(BaseModel):
    model_config = ConfigDict(extra="allow")
    document_title: Optional[str] = None
    document_number: Optional[str] = None
    date: Optional[str] = None
    location: Optional[str] = None
    project: Optional[str] = None
    participants: Optional[List[Participant]] = None
    purpose: Optional[str] = None
    discussion_content: Optional[str] = None
    agreed_conclusions: Optional[str] = None
    action_items: Optional[str] = None
    attached_documents: Optional[str] = None
    signatures_note: Optional[str] = None
    note: Optional[str] = None

#Hóa đơn
class InvoiceItem(BaseModel):
    model_config = ConfigDict(extra="allow")
    code: Optional[str] = None
    name: Optional[str] = None
    unit: Optional[str] = None
    quantity: Optional[float] = None
    unit_price: Optional[float] = None
    tax_rate: Optional[str] = None
    tax_amount: Optional[float] = None
    amount: Optional[float] = None


class Invoice(BaseModel):
    model_config = ConfigDict(extra="allow")
    invoice_form_symbol: Optional[str] = None
    invoice_symbol: Optional[str] = None
    invoice_number: Optional[str] = None
    date: Optional[str] = None
    seller_name: Optional[str] = None
    seller_tax_code: Optional[str] = None
    seller_address: Optional[str] = None
    seller_phone: Optional[str] = None
    seller_bank_account: Optional[str] = None
    buyer_name: Optional[str] = None
    buyer_person: Optional[str] = None
    buyer_tax_code: Optional[str] = None
    buyer_address: Optional[str] = None
    buyer_phone: Optional[str] = None
    buyer_bank_account: Optional[str] = None
    payment_method: Optional[str] = None
    currency: Optional[str] = None
    items: Optional[List[InvoiceItem]] = None
    subtotal_amount: Optional[float] = None
    total_tax_amount: Optional[float] = None
    total_amount: Optional[float] = None
    amount_in_words: Optional[str] = None
    lookup_code: Optional[str] = None
    contract: Optional[str] = None
    project: Optional[str] = None
    note: Optional[str] = None


SCHEMA_REGISTRY = {
    "phieu_chi": PhieuChi,
    "phieu_thu": PhieuThu,
    "van_don": Waybill,
    "hoa_don": Invoice,
    "chuyen_khoan": ChuyenKhoanNganHang,
    "bien_ban_lam_viec": BienBanLamViec,
    "phieu_nhap_hang": StockReceiptNote,
    "phieu_xuat_hang": StockIssueNote,
    "yeu_cau_thanh_toan": PaymentRequest,
    "bao_gia": Quotation,
    "giao_nhan_hang_hoa": PhieuGiaoNhanHangHoa,
    "giao_nhan_be_tong": PhieuGiaoNhanBeTong,
    "phieu_thue": PhieuNopThue
}