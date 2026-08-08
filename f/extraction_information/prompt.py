import os
import wmill

def build_prompt(document_type: str, ocr_text: str, date_time: str) -> str:
    return f"""
            You are an expert in OCR extraction for business documents in Vietnam.

            Your task is to read the OCR input text and return a JSON object containing only the fields that are explicitly present in that OCR text.

            Important rules:
            1. Do not rely on a fixed schema for every document. The output schema must be dynamic.
            2. Only include keys that exist in the OCR text. If a field is absent, omit it entirely.
            3. Do not output null, empty strings, or placeholders such as "N/A" for missing fields.
            4. Preserve the original exact values from the OCR text as much as possible.
            5. If the OCR contains a table/list, keep repeated rows under an `items` list only when the OCR clearly shows such repeat rows.
            6. If you see extra/custom fields not in the standard template, add them with descriptive keys.
            7. Return valid JSON only. No markdown, no explanation.
            8. If OCR is Vietnamese → output keys must be Vietnamese.
            9. If OCR is English → keep English.


            Document type: {document_type}
            Current date and time: {date_time}

            Input text:
            ----------------
            {ocr_text}
            ----------------

            Your Response:
            """