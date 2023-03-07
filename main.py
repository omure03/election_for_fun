import streamlit as st

st.set_page_config(layout="wide")

st.header("cumhurbaşkanı kim olamlı?")

col1, col2, col3, col4 = st.columns([4,4,3,3])

values = [0, 0, 0, 0]

with col1:
    st.image("rte.jpg")
    st.checkbox("RECEP TAYİP ERDOĞAN", key="0")

with col2:
    st.image("kk.jpg")
    st.checkbox("KEMAL KILIÇDAROĞLU", key="1")

with col3:
    st.image("mi.jpg", width=265)
    st.checkbox("MUHARREM İNCE", key="2")

with col4:
    st.image("kocmann.jpeg", width=250)
    st.checkbox("MUSTAFA KOÇMAN", key="3")

button = st.button("BAS MÜHRÜ", key="ok")

for idx,i in enumerate(range(4)):
    if st.session_state[str(i)]:
        values[idx] = 1
if button:
    if values.count(1) >= 2:
        st.info("GEÇERSİZ OY")
        st.subheader("YARRAĞI YEDİN")
    elif values.count(1) == 0:
        st.info("BOŞ OY")
        st.subheader("YARRAĞI YEDİN")
    else:
        if values[3] == 1:
            st.info("GÜZEL SEÇİM")
            st.subheader("ÜLKE KURTULDU")
            st.write("NOT: Gayler idam edildi...")
        else:
            st.info("KÖTÜ SEÇİM")
            st.subheader("ÜLKE BATTI, YARRAĞI YEDİN")