from services.llm_service import generate_response


def answer_question(question, context):

    prompt = f"""
You are DocuMind AI, a helpful document assistant.

Answer the user's question using only the information
provided in the document context.

If the answer is not available in the context,
clearly say that the information was not found
in the uploaded document.

Do not invent facts.

Document Context:
{context}

User Question:
{question}

Answer:
"""

    return generate_response(
        prompt,
        temperature=0.2,
        max_tokens=1500
    )


def generate_summary(text):

    summary_text = text[:12000]

    prompt = f"""
You are DocuMind AI.

Summarize the following uploaded document in a clear
and easy-to-understand way.

Include:

1. A short overview
2. Main points
3. Important details
4. Key takeaways

Use only the information present in the document.

Document:
{summary_text}
"""

    return generate_response(
        prompt,
        temperature=0.2,
        max_tokens=1500
    )