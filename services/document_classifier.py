from services.llm_service import generate_response


def classify_document(text):
    sample_text = text[:8000]

    prompt = f"""
You are a document classification system.

Classify the uploaded document into exactly one of these categories:

1. resume
2. medical_report
3. book
4. notes
5. government_document
6. form
7. general_document

Return only the category name.

Do not explain your answer.

Document:
{sample_text}
"""

    result = generate_response(
        prompt,
        temperature=0,
        max_tokens=20
    )

    result = result.strip().lower()

    valid_categories = [
        "resume",
        "medical_report",
        "book",
        "notes",
        "government_document",
        "form",
        "general_document"
    ]

    for category in valid_categories:
        if category in result:
            return category

    return "general_document"