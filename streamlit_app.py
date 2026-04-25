import streamlit as st
from docloader import load_pdf, load_documents_from_folder

st.title("Mój pierwszy projekt AI 🚀")
name = st.text_input("Jak się nazywasz?")
if name:

    st.write(f"Cześć {name}! Zaraz uruchomimy tu model LLM.")



# --- Upload pliku PDF lub folderu w sidebarze ---
with st.sidebar:
    st.header("Wczytaj plik PDF lub folder")
    uploaded_file = st.file_uploader("Wybierz plik PDF", type=["pdf"])
    st.markdown("---")
    st.write("Lub podaj ścieżkę do folderu z PDF-ami:")
    folder_path = st.text_input("Ścieżka do folderu")
    load_folder = st.button("Wczytaj wszystkie PDF-y z folderu")

# --- Wyświetlanie tekstu PDF w głównej części ---
if uploaded_file is not None:
    with open("temp_uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())
    text = load_pdf("temp_uploaded.pdf")
    st.subheader("Zawartość pliku PDF:")
    st.text_area("Tekst z PDF", text, height=300)

# --- Wyświetlanie tekstów z folderu PDF-ów ---
if load_folder and folder_path:
    documents = load_documents_from_folder(folder_path)
    if documents:
        st.subheader("Zawartość wszystkich PDF-ów z folderu:")
        for filename, text in documents.items():
            st.markdown(f"**{filename}**")
            st.text_area(f"Tekst z {filename}", text, height=200)
    else:
        st.warning("Nie znaleziono plików PDF w podanym folderze lub folder nie istnieje.")