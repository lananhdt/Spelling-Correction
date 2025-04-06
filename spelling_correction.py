# Basic Spell Check App
import streamlit as st
import spacy
import contextualSpellCheck

# Load spaCy model
nlp = spacy.load('en_core_web_md')
contextualSpellCheck.add_to_pipe(nlp)

# Spelling Correction function
def spell_corrector(sentence):
    doc = nlp(sentence)
    return {
        'original': sentence,
        'corrected': doc._.outcome_spellCheck,
        'performed': doc._.performed_spellCheck,
        'suggestions': doc._.suggestions_spellCheck,
        'words': [token.text for token in doc]
    }
    # return doc._.performed_spellCheck, doc._.outcome_spellCheck
    # return (2 index) index 0: T/F có cần sửa lỗi hay không, index 1: Trả về câu đúng

# Streamlit app
def main():
    st.title('Contextual Spell Correction')
    st.write('Correct English sentences using Spacy + contextualSpellCheck')

    sentence = st.text_input("Enter a sentence: ")

    if sentence:
        result = spell_corrector(sentence)
        if result['performed']:
            st.success(f'Corrected sentence: {result['corrected']}')
        else:
            st.success(f'No spelling issues detected: {result['original']}')

        with st.expander("Show analysis"):
            st.write("**Tokens:**", result['words'])
            st.write("**Suggestions:**", result['suggestions'])

if __name__ == '__main__':
     main()