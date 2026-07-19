from services.llm_service import generate_response


def extract_actions(document_text):

    document_text = document_text[:15000]

    prompt = f"""
You are an intelligent document action extractor.

Analyze the following document and extract all useful,
actionable information.

Find:

1. Important dates and deadlines
2. Tasks or actions that need to be completed
3. Requirements
4. Required documents
5. Important numbers, amounts, or limits
6. Contact information
7. Important warnings or conditions
8. A final "What should I do next?" section

Use only information present in the document.

Do not invent dates, tasks, requirements, or contact details.

If a category has no relevant information, write:
"Not found in the document."

Document:
{document_text}
"""

    return generate_response(
        prompt,
        temperature=0.1,
        max_tokens=2200
    )