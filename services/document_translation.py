from services.llm_service import generate_response


def translate_document(document_text, target_language):

    document_text = document_text[:15000]

    prompt = f"""
You are a professional document translation assistant.

Translate the following document into:
{target_language}

Important rules:

- Preserve the original meaning.
- Do not add information.
- Do not remove important information.
- Keep names, dates, numbers, amounts, and official terms accurate.
- Maintain the structure as much as possible.
- If a technical or legal term should remain in English,
  include the original term in brackets when helpful.

Document:
{document_text}
"""

    return generate_response(
        prompt,
        temperature=0.1,
        max_tokens=3000
    )