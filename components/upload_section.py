import streamlit as st


def upload_document():

    uploaded_file = st.file_uploader(

        "Upload your document",

        type=[

            "pdf",

            "docx",

            "txt",

            "png",

            "jpg",

            "jpeg"

        ]

    )

    return uploaded_file