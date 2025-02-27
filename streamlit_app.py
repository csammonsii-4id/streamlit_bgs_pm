import streamlit as st

def main():
    st.title("Agentic BGS PM")

    # Initialize login state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    # Login form
    if not st.session_state['logged_in']:
        with st.form(key='login_form', clear_on_submit=True):  # Use st.form to group elements
            st.subheader("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")  # Use st.form_submit_button

            if login_button:
                if username == "demo" and password == "test":
                    st.session_state['logged_in'] = True
                    st.success("Logged in successfully!")
                else:
                    st.error("Invalid username or password")

    # Main app content (shown after successful login)
    else:
        st.subheader("Welcome, Agentic PM")
        logout_button = st.button("Logout")

        if logout_button:
            st.session_state['logged_in'] = False

        # Add your main app content here (the LlamaIndex-powered conversation)
        st.write("Ask me questions about our product roadmap to help gain insights, and make decisions about timelines and strategies.")

        query = st.text_area("Enter your question:", height=100)

        if query:
            st.write(f"Question for the model: {query}")
            # Replace this placeholder with your actual LlamaIndex query engine
            # response = query_engine.query(query)
            # st.write(response.response)
            st.write("Response from the agent (replace with actual response)")

if __name__ == "__main__":
    main()