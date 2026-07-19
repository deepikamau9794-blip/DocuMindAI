from services.llm_service import generate_response


def analyze_notes(notes_text):

    notes_text = notes_text[:12000]

    prompt = f"""
You are an AI study assistant.

Analyze the following study notes and help the student
understand them better.

Provide:

1. A simple overview of the topic
2. Important concepts
3. Key definitions
4. Important points to remember
5. Difficult concepts explained simply
6. A short revision summary

Use only the information present in the notes.

Do not invent facts that are not present in the notes.

Study Notes:
{notes_text}
"""

    return generate_response(
        prompt,
        temperature=0.2,
        max_tokens=2000
    )


def generate_quiz(notes_text):

    notes_text = notes_text[:10000]

    prompt = f"""
You are an AI study assistant.

Create a quiz from the following study notes.

Create:

- 5 multiple-choice questions
- 5 short-answer questions

For each question, provide the correct answer.

Use only information from the notes.

Study Notes:
{notes_text}
"""

    return generate_response(
        prompt,
        temperature=0.3,
        max_tokens=2000
    )


def generate_flashcards(notes_text):

    notes_text = notes_text[:10000]

    prompt = f"""
You are an AI study assistant.

Create useful flashcards from the following study notes.

Format each flashcard as:

Question:
Answer:

Create at least 10 flashcards.

Use only information present in the notes.

Study Notes:
{notes_text}
"""

    return generate_response(
        prompt,
        temperature=0.2,
        max_tokens=2000
    )