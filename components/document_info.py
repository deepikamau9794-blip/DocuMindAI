import streamlit as st


def display_document_info(

    file_extension,

    page_count,

    document_text,

    chunk_count

):

    st.subheader(

        "Document Information"

    )


    col1, col2, col3 = st.columns(

        3

    )


    with col1:

        st.metric(

            "File Type",

            file_extension.upper()

        )


    with col2:

        if page_count:

            st.metric(

                "Pages",

                page_count

            )

        else:

            st.metric(

                "Pages",

                "N/A"

            )


    with col3:

        st.metric(

            "Words",

            len(

                document_text.split()

            )

        )


    st.write(

        f"Text chunks created: {chunk_count}"

    )