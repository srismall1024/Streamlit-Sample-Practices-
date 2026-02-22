import streamlit as st

# Initialize expression
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Function to add values
def add_to_expression(value):
    st.session_state.expression += str(value)

st.title("Sample Page 3")
st.header("Sample Calculator")

# Display expression
st.text_input("Expression", st.session_state.expression)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("1"):
        add_to_expression(1)
    if st.button("4"):
        add_to_expression(4)
    if st.button("7"):
        add_to_expression(7)
    if st.button("+"):
        add_to_expression("+")
    if st.button("/"):
        add_to_expression("/")

with col2:
    if st.button("2"):
        add_to_expression(2)
    if st.button("5"):
        add_to_expression(5)
    if st.button("8"):
        add_to_expression(8)
    if st.button("0"):
        add_to_expression(0)
    if st.button("*"):
        add_to_expression("*")

with col3:
    if st.button("3"):
        add_to_expression(3)
    if st.button("6"):
        add_to_expression(6)
    if st.button("9"):
        add_to_expression(9)
    if st.button("-"):
        add_to_expression("-")
    if st.button("C"):
        st.session_state.expression = ""

# Evaluate
if st.button("="):
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except:
        st.session_state.expression = "Error"
