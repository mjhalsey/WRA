import streamlit as st
from logic import LegalReadinessQuiz

# --- Page Configuration ---
st.set_page_config(
    page_title="Warfighter Legal Readiness",
    layout="centered"
)

# --- Session State Initialization ---
# This is the most important part of a Streamlit app.
# It creates a 'memory' for the app to remember the user's progress.
# Without this, the quiz would restart every time a button is clicked.
if 'quiz' not in st.session_state:
    # If the quiz hasn't been started, create a new instance of our quiz logic
    # and store it in the session state.
    st.session_state.quiz = LegalReadinessQuiz()

# --- Main App ---

# Get the current quiz object and the current node (question/intro/etc.)
quiz = st.session_state.quiz
node = quiz.get_current_node()

if node:
    node_type = node.get('type')

    if node_type == 'section_intro':
        # --- Display a Section Introduction ---
        if node.get('title'):
            st.header(node.get('title'))

        # Replace the "\n" characters with markdown for paragraph breaks
        display_text = node['text'].replace('\n', '\n\n')
        st.write(display_text)

        # Check if there's a pop-up and display it in an expander
        if 'popup' in node:
            for term, definition in node['popup'].items():
                with st.expander(f"What is '{term}'?"):
                    st.write(definition)
        
        # A "Continue" button for section intros to move the user forward
        if st.button("Continue", type="primary"):
            quiz.current_node_id = node['next']
            st.rerun()

    elif node_type == 'question':
        # --- Display a Question with Yes/No Buttons ---
        st.subheader(node['text'])

        # Check if there's a pop-up for this question
        if 'popup' in node:
            for term, definition in node['popup'].items():
                with st.expander(f"What is '{term}'?"):
                    st.write(definition)
        
        # --- Section Footer ---
        st.divider()
        current_section_title = quiz.get_current_section_title()
        if current_section_title:
            st.caption(f"You are in: {current_section_title}")

        # Create two columns for the Yes and No buttons to appear side-by-side
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Yes", use_container_width=True):
                quiz.process_answer('yes')
                st.rerun() # Rerun the app to show the next question

        with col2:
            if st.button("No", use_container_width=True):
                quiz.process_answer('no')
                st.rerun() # Rerun the app to show the next question

    elif node_type == 'outcome':
        # This part should ideally not be reached if the logic is correct,
        # as process_answer should handle outcomes and move to the next question.
        # This is a fallback.
        st.warning("You have reached an outcome node directly. This should not happen.")
        quiz.current_node_id = node.get('next')
        st.rerun()

else:
    # --- This is the End of the Quiz ---
    st.balloons()
    st.header("You've Completed the Questionnaire!")

    if quiz.checklist:
        st.write("Based on your answers, here is your personalized legal readiness checklist. Consider taking this to your local legal assistance office.")

        # Sort checklist to show Red items first
        sorted_checklist = sorted(quiz.checklist, key=lambda x: x['level'], reverse=True)

        for item in sorted_checklist:
            if item['level'] == 'Red':
                st.error(f"**Action Strongly Advised:** {item['text']}")
            elif item['level'] == 'Yellow':
                st.warning(f"**Action Recommended:** {item['text']}")
            # Green items are not added to the checklist in our current logic
    else:
        st.success("Congratulations! Based on your answers, no immediate legal actions are recommended.")

    st.info("Disclaimer: This tool provides general information and is not a substitute for legal advice from a licensed attorney.")

    if st.button("Start Over"):
        # Clear the session state to start a new quiz
        del st.session_state.quiz
        st.rerun()
