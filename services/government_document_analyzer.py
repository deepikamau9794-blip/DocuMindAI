from services.llm_service import generate_response


def analyze_government_document(document_text):

    document_text = document_text[:15000]

    prompt = f"""
You are a government document explanation assistant.

Analyze the following government document and explain it
in simple and clear language.

Include:

1. What this document is about
2. Main purpose of the document
3. Important rules, policies, or guidelines
4. Eligibility criteria, if mentioned
5. Important dates or deadlines, if mentioned
6. Required documents or steps, if mentioned
7. Important benefits, restrictions, or conditions
8. A simple summary for an ordinary citizen

Important rules:

- Use only information present in the uploaded document.
- Do not invent government schemes, rules, dates, or eligibility criteria.
- If any information is not present, clearly say that it was not found.
- Do not treat this as legal advice.
- Mention important conditions clearly.

Government Document:
{document_text}
"""

    return generate_response(
        prompt,
        temperature=0.1,
        max_tokens=2500
    )