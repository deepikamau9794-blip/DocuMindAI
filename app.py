import hashlib

import streamlit as st

from components.upload_section import upload_document
from components.document_info import display_document_info
from components.chat_interface import (
    display_chat_history,
    get_user_question,
    display_message
)

from services.document_classifier import classify_document
from services.document_assistant import (
    answer_question,
    generate_summary
)
from services.resume_analyzer import analyze_resume
from services.medical_report_analyzer import analyze_medical_report
from services.book_analyzer import analyze_book
from services.study_assistant import (
    analyze_notes,
    generate_quiz,
    generate_flashcards
)
from services.government_document_analyzer import (
    analyze_government_document
)
from services.form_assistant import assist_with_form
from services.document_action_extractor import extract_actions
from services.document_translation import translate_document
from services.document_comparator import compare_documents
from services.chat_history import (
    load_chat_history,
    save_chat_session,
    delete_chat_session
)

from utils.document_loader import load_document
from utils.text_processing import create_chunks


st.set_page_config(
    page_title="DocuMind AI",
    layout="wide"
)


if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "document_name" not in st.session_state:
    st.session_state.document_name = ""

if "file_extension" not in st.session_state:
    st.session_state.file_extension = ""

if "page_count" not in st.session_state:
    st.session_state.page_count = None

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "document_type" not in st.session_state:
    st.session_state.document_type = ""

if "file_hash" not in st.session_state:
    st.session_state.file_hash = ""


st.title("DocuMind AI")

st.write(
    "Upload a document to analyze, summarize, translate, "
    "compare, or ask questions about it."
)


uploaded_file = upload_document()


if uploaded_file:

    file_bytes = uploaded_file.getvalue()

    file_extension = uploaded_file.name.split(
        "."
    )[-1].lower()

    current_file_hash = hashlib.md5(
        file_bytes
    ).hexdigest()


    if (
        st.session_state.file_hash
        != current_file_hash
    ):

        st.session_state.file_hash = current_file_hash

        st.session_state.document_name = (
            uploaded_file.name
        )

        st.session_state.file_extension = (
            file_extension
        )

        st.session_state.messages = []

        try:

            with st.spinner(
                "Reading document..."
            ):

                document_text, page_count = load_document(
                    file_bytes,
                    file_extension
                )


            if not document_text.strip():

                st.error(
                    "No readable text was found in the document."
                )

                st.stop()


            chunks = create_chunks(
                document_text
            )


            st.session_state.document_text = (
                document_text
            )

            st.session_state.page_count = (
                page_count
            )

            st.session_state.chunks = (
                chunks
            )


            with st.spinner(
                "Identifying document type..."
            ):

                st.session_state.document_type = (
                    classify_document(
                        document_text
                    )
                )


        except Exception as error:

            st.error(
                f"Could not process the document: {error}"
            )

            st.stop()


document_text = st.session_state.document_text

document_type = st.session_state.document_type

chunks = st.session_state.chunks


if document_text:

    display_document_info(
        st.session_state.file_extension,
        st.session_state.page_count,
        document_text,
        len(chunks)
    )


    st.write(
        "Document Type: "
        + document_type.replace(
            "_",
            " "
        ).title()
    )


    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Chat",
            "Analysis",
            "Actions",
            "Translation",
            "Compare Documents"
        ]
    )


    with tab1:

        display_chat_history(
            st.session_state.messages
        )


        question = get_user_question()


        if question:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )


            display_message(
                "user",
                question
            )


            with st.spinner(
                "Generating answer..."
            ):

                answer = answer_question(
                    question,
                    document_text[:15000]
                )


            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )


            display_message(
                "assistant",
                answer
            )


    with tab2:

        if st.button(
            "Generate Summary"
        ):

            with st.spinner(
                "Generating summary..."
            ):

                summary = generate_summary(
                    document_text
                )


            st.write(
                summary
            )


        if document_type == "resume":

            if st.button(
                "Analyze Resume"
            ):

                with st.spinner(
                    "Analyzing resume..."
                ):

                    result = analyze_resume(
                        document_text
                    )


                st.write(
                    result
                )


        elif document_type == "medical_report":

            if st.button(
                "Analyze Medical Report"
            ):

                with st.spinner(
                    "Analyzing medical report..."
                ):

                    result = analyze_medical_report(
                        document_text
                    )


                st.write(
                    result
                )


        elif document_type == "book":

            if st.button(
                "Analyze Book"
            ):

                with st.spinner(
                    "Analyzing book..."
                ):

                    result = analyze_book(
                        document_text
                    )


                st.write(
                    result
                )


        elif document_type == "notes":

            if st.button(
                "Analyze Study Notes"
            ):

                with st.spinner(
                    "Analyzing study notes..."
                ):

                    result = analyze_notes(
                        document_text
                    )


                st.write(
                    result
                )


            if st.button(
                "Generate Quiz"
            ):

                with st.spinner(
                    "Generating quiz..."
                ):

                    quiz = generate_quiz(
                        document_text
                    )


                st.write(
                    quiz
                )


            if st.button(
                "Generate Flashcards"
            ):

                with st.spinner(
                    "Generating flashcards..."
                ):

                    flashcards = generate_flashcards(
                        document_text
                    )


                st.write(
                    flashcards
                )


        elif document_type == "government_document":

            if st.button(
                "Analyze Government Document"
            ):

                with st.spinner(
                    "Analyzing government document..."
                ):

                    result = analyze_government_document(
                        document_text
                    )


                st.write(
                    result
                )


        elif document_type == "form":

            if st.button(
                "Understand This Form"
            ):

                with st.spinner(
                    "Analyzing form..."
                ):

                    result = assist_with_form(
                        document_text
                    )


                st.write(
                    result
                )


    with tab3:

        if st.button(
            "Extract Important Actions"
        ):

            with st.spinner(
                "Extracting important information..."
            ):

                actions = extract_actions(
                    document_text
                )


            st.write(
                actions
            )


    with tab4:

        target_language = st.selectbox(
            "Choose target language",
            [
                "Hindi",
                "English",
                "French",
                "German",
                "Spanish"
            ]
        )


        if st.button(
            "Translate Document"
        ):

            with st.spinner(
                "Translating document..."
            ):

                translated_text = translate_document(
                    document_text,
                    target_language
                )


            st.write(
                translated_text
            )


    with tab5:

        st.write(
            "Upload another document to compare it with the current document."
        )


        second_file = st.file_uploader(
            "Upload second document",
            type=[
                "pdf",
                "docx",
                "txt",
                "png",
                "jpg",
                "jpeg"
            ],
            key="second_document"
        )


        if second_file:

            second_file_bytes = (
                second_file.getvalue()
            )

            second_extension = (
                second_file.name.split(
                    "."
                )[-1].lower()
            )


            if st.button(
                "Compare Documents"
            ):

                try:

                    with st.spinner(
                        "Reading second document..."
                    ):

                        second_text, _ = load_document(
                            second_file_bytes,
                            second_extension
                        )


                    if not second_text.strip():

                        st.error(
                            "No readable text was found in the second document."
                        )

                    else:

                        with st.spinner(
                            "Comparing documents..."
                        ):

                            comparison = compare_documents(
                                document_text,
                                second_text
                            )


                        st.write(
                            comparison
                        )


                except Exception as error:

                    st.error(
                        f"Could not compare documents: {error}"
                    )


    st.divider()

    st.subheader(
        "Chat History"
    )


    if st.session_state.messages:

        if st.button(
            "Save Current Chat"
        ):

            first_message = (
                st.session_state.messages[0]
            )

            title = first_message[
                "content"
            ][:50]


            save_chat_session(
                title,
                st.session_state.document_name,
                st.session_state.messages
            )


            st.success(
                "Chat saved successfully."
            )


    history = load_chat_history()


    if history:

        for session in history:

            with st.expander(
                session["title"]
            ):

                st.write(
                    "Document: "
                    + session["document_name"]
                )

                st.write(
                    "Created: "
                    + session["created_at"]
                )


                for message in session[
                    "messages"
                ]:

                    st.write(
                        message["role"].title()
                        + ": "
                        + message["content"]
                    )


                if st.button(
                    "Delete",
                    key=session["id"]
                ):

                    delete_chat_session(
                        session["id"]
                    )

                    st.rerun()


else:

    st.info(
        "Upload a PDF, DOCX, TXT, PNG, JPG, or JPEG file to get started."
    )