from services.llm_service import generate_response


def assist_with_form(form_text):

    form_text = form_text[:12000]

    prompt = f"""
You are DocuMind AI, a form-filling assistant.

Analyze the following form and help the user understand
how to fill it.

Provide:

1. Form name or purpose, if available
2. List of all fields that need to be filled
3. What information should be entered in each field
4. Required documents or attachments, if mentioned
5. Important instructions, conditions, or warnings
6. A simple step-by-step guide for filling the form

Important rules:

- Use only the information visible in the uploaded form.
- Do not invent field meanings.
- If a field is unclear, clearly say that it needs verification.
- Do not fill in personal information automatically.
- Never guess sensitive information such as Aadhaar number,
  bank details, passwords, or other personal data.

Form Content:
{form_text}
"""

    return generate_response(
        prompt,
        temperature=0.1,
        max_tokens=2200
    )