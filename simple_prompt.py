import streamlit as st

template = """

Stage 1 (Absorption): Prompts to get basic understanding and spark curiosity
 - Can you explain {topic} to a 10 year old?
 - Give 2 questions which will make me curious about {topic} \n
Stage 2 (Consolidation): Prompts to foster deeper understanding
 - Describe a real-world scenario where {topic} is applied, and explain the key concepts involved in solving the problem or addressing the challenge.
 - Break down the main principles of {topic} and explain how they relate to each other in a simplified manner. \n
Stage 3 (Re-expression): Prompts that enable practice/self-assessment
 - Ask me some basic questions to check if I have rudimentary understanding of {topic}
 - Provide a brief, hypothetical scenario related to {topic} and ask me to identify the relevant principles or concepts at play.

"""

st.title("Generate prompts to learn a new topic!")

topic_name = st.text_input("Which topic do you want to learn?")

if topic_name:
    answer = template.format(topic = topic_name)
    st.write(f"""
    Here are your prompts:
    {answer}
    """)


