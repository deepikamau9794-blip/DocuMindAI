import streamlit as st


def display_chat_history(

    messages

):

    for message in messages:

        with st.chat_message(

            message["role"]

        ):

            st.write(

                message["content"]

            )


def get_user_question():

    return st.chat_input(

        "Ask something about your document..."

    )


def display_message(

    role,

    content

):

    with st.chat_message(

        role

    ):

        st.write(

            content

        )