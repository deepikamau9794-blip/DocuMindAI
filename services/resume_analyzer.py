from services.llm_service import generate_response


def analyze_resume(resume_text):

    resume_text = resume_text[:12000]

    prompt = f"""
You are an expert resume and ATS analyzer.

Analyze the following resume and provide a practical,
honest, and structured review.

Your analysis must include:

1. ATS Compatibility Score (0-100)
2. Overall Impression
3. Key Strengths
4. Weak Areas
5. Technical Skills Analysis
6. Project Analysis
7. Experience and Achievement Analysis
8. Specific Resume Improvements
9. Suitable Entry-Level Job Roles

Important rules:

- Use only information present in the resume.
- Do not invent experience, skills, projects, or achievements.
- Do not recommend adding a skill unless clearly label it as a suggestion.
- Do not claim that the ATS score is an exact score.
- Clearly mention that the ATS score is an estimated evaluation.
- Keep the analysis practical and useful.

Resume:
{resume_text}
"""

    return generate_response(
        prompt,
        temperature=0.2,
        max_tokens=2000
    )