import random
import streamlit as st

st.set_page_config(page_title="Adivinha o número", page_icon="🎯")
st.title("🎯 Adivinha o número")
st.write("Estou a pensar num número entre 1 e 100.")

# Estado do jogo (guardado entre cliques)
if "numero" not in st.session_state:
    st.session_state.numero = random.randint(1, 100)
    st.session_state.tentativas = 0
    st.session_state.mensagem = ""
    st.session_state.terminou = False


def novo_jogo():
    st.session_state.numero = random.randint(1, 100)
    st.session_state.tentativas = 0
    st.session_state.mensagem = ""
    st.session_state.terminou = False


palpite = st.number_input(
    "O teu palpite:",
    min_value=1,
    max_value=100,
    value=50,
    step=1,
    disabled=st.session_state.terminou,
)

if st.button("Tentar", disabled=st.session_state.terminou):
    st.session_state.tentativas += 1
    if palpite < st.session_state.numero:
        st.session_state.mensagem = "Mais alto ⬆️"
    elif palpite > st.session_state.numero:
        st.session_state.mensagem = "Mais baixo ⬇️"
    else:
        st.session_state.mensagem = (
            f"Acertaste em {st.session_state.tentativas} tentativas! 🎉"
        )
        st.session_state.terminou = True
        st.rerun()

if st.session_state.mensagem:
    if st.session_state.terminou:
        st.success(st.session_state.mensagem)
    else:
        st.info(st.session_state.mensagem)

st.caption(f"Tentativas: {st.session_state.tentativas}")

st.button("Novo jogo", on_click=novo_jogo)