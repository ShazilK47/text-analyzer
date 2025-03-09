import streamlit as st

def analyze_text(text):
    if not text:
        st.error("Please enter a paragraph to analyze.")
        return
    
    # Word and character count
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    
    # Vowel count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    
    # Search and replace
    search_word = st.text_input("Enter a word to search for:")
    replace_word = st.text_input("Enter a word to replace it with:")
    modified_text = text.replace(search_word, replace_word) if search_word else text
    
    # Uppercase and Lowercase Conversion
    uppercase_text = text.upper()
    lowercase_text = text.lower()
    
    # Type Casting
    word_count_str = str(word_count)
    vowel_count_str = str(vowel_count)
    
    # Operators
    contains_python = "Python" in text
    avg_word_length = char_count / word_count if word_count else 0
    
    # Display Results
    st.subheader("Text Analysis Results:")
    st.write(f"Total Words: {word_count_str}")
    st.write(f"Total Characters (including spaces): {char_count}")
    st.write(f"Total Vowels: {vowel_count_str}")
    st.write(f"Contains 'Python': {contains_python}")
    st.write(f"Average Word Length: {avg_word_length:.2f}")
    
    st.subheader("Modified Text:")
    st.write(modified_text)
    
    st.subheader("Text Transformations:")
    st.write("Uppercase:")
    st.write(uppercase_text)
    st.write("Lowercase:")
    st.write(lowercase_text)

# Streamlit UI
st.title("Text Analyzer")
text_input = st.text_area("Enter your paragraph:")
analyze_text(text_input)
