import streamlit as st


# here all the session_state variables.. you know so that no unsual reload effect
if "text" not in st.session_state:
    st.session_state.text = ""
if "modified_text" not in st.session_state:
    st.session_state.modified_text = ""
if "transformed_text" not in st.session_state:
    st.session_state.transformed_text = ""
if "word_count" not in st.session_state:
    st.session_state.word_count = 0
if "char_count" not in st.session_state:
    st.session_state.char_count = 0
if "vowel_count" not in st.session_state:
    st.session_state.vowel_count = 0
if "contains_python" not in st.session_state:
    st.session_state.contains_python = False
if "avg_word_length" not in st.session_state:
    st.session_state.avg_word_length = 0.0

def analyze_text():
    text = st.session_state.text.strip()
    if not text:
        st.error("Please enter a paragraph to analyze.")
        return
    
    # -> Word and character count
    words = text.split()
    st.session_state.word_count = len(words)
    st.session_state.char_count = len(text)
    
    # -> Vowel count
    vowels = "aeiouAEIOU"
    st.session_state.vowel_count = sum(1 for char in text if char in vowels)
    
    # -> Operators
    st.session_state.contains_python = "Python" in text
    st.session_state.avg_word_length = st.session_state.char_count / st.session_state.word_count if st.session_state.word_count else 0
    
# Streamlit UI
st.title("Professional Text Analyzer")
st.text_area("Enter your paragraph:", value=st.session_state.text, height=200, key="text")

if st.button("Analyze Text", key="analyze_button"):
    analyze_text()


st.subheader("Analysis Results")
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Total Words", value=st.session_state.word_count)
    st.metric(label="Total Characters", value=st.session_state.char_count)
    st.metric(label="Total Vowels", value=st.session_state.vowel_count)

with col2:
    st.metric(label="Contains 'Python'", value=str(st.session_state.contains_python))
    st.metric(label="Average Word Length", value=f"{st.session_state.avg_word_length:.2f}")

st.divider()

# here -> Search and Replace
st.subheader("Search and Replace")
search_word = st.text_input("Enter a word to search for:")
replace_word = st.text_input("Enter a word to replace it with:")

if st.button("Replace Text", key="replace_button"):
    st.session_state.modified_text = st.session_state.text.replace(search_word, replace_word) if search_word else st.session_state.text

st.text_area("Modified Text:", value=st.session_state.modified_text, height=150)

st.divider()

# here -> Text Transformations
st.subheader("Text Transformations")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Convert to Uppercase", key="uppercase_button"):
        st.session_state.transformed_text = st.session_state.text.upper()
with col2:
    if st.button("Convert to Lowercase", key="lowercase_button"):
        st.session_state.transformed_text = st.session_state.text.lower()
with col3:
    if st.button("Convert to Title Case", key="titlecase_button"):
        st.session_state.transformed_text = st.session_state.text.title()

st.text_area("Transformed Text:", value=st.session_state.transformed_text, height=150)
