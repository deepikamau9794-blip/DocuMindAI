from services.llm_service import generate_response


def analyze_medical_report(report_text):

    report_text = report_text[:12000]

    prompt = f"""
You are a medical report explanation assistant.

Explain the following medical report in simple,
easy-to-understand language.

Include:

1. General overview of the report
2. Important medical terms explained simply
3. Test values and their reference ranges, if available
4. Values that appear outside the provided reference range
5. Important observations mentioned in the report
6. Questions the patient may ask their doctor

Important safety rules:

- Do not diagnose any disease.
- Do not prescribe medicines or treatments.
- Do not tell the patient to start or stop medication.
- Do not make conclusions that are not present in the report.
- Clearly explain that this is general information and not a medical diagnosis.
- Use only the information present in the uploaded report.

Medical Report:
{report_text}
"""

    return generate_response(
        prompt,
        temperature=0.1,
        max_tokens=2200
    )