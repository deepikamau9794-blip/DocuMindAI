from services.llm_service import generate_response


def analyze_book(book_text):

    book_text = book_text[:15000]

    prompt = f"""
You are an AI book analysis assistant.

Analyze the following book content and provide:

1. Book overview
2. Main themes
3. Important ideas and concepts
4. Chapter-wise insights, if chapter information is available
5. Important characters or people, if applicable
6. Key lessons and takeaways
7. A short reader-friendly summary

Use only the information available in the uploaded document.

Do not invent details.

Important:
This analysis is for a book or long-form reading document.
If the uploaded content does not appear to be a book,
say that clearly instead of pretending it is one.

Book Content:
{book_text}
"""

    return generate_response(
        prompt,
        temperature=0.2,
        max_tokens=2500
    )