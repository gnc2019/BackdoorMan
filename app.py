import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página do navegador
st.set_page_config(page_title="Painel de Monitoramento de Pacientes", layout="wide")

# Título do Painel
st.title("🏥 Painel de Informações dos Pacientes")
st.markdown("---")

# Inicializa um banco de dados temporário na memória se ele não existir
if 'pacientes' not in st.session_state:
    st.session_state.pacientes = pd.DataFrame(columns=["Nome do Paciente", "Data de Nascimento", "Localização Atual"])

# --- Formulário para Adicionar Novo Paciente ---
st.sidebar.header("📝 Cadastrar Novo Paciente")
with st.sidebar.form(key='cadastro_form', clear_on_submit=True):
    nome = st.text_input("Nome do Paciente:")
    data_nasc = st.date_input("Data de Nascimento:", min_value=datetime(1900, 1, 1))
    
    # Lista suspensa solicitada
    opcoes_localizacao = ["RECEPÇÃO", "SALA DE OPERAÇÃO", "RPA", "ENCAMINHADO PARA O LEITO"]
    localizacao_inicial = st.selectbox("Localização Inicial:", opcoes_localizacao)
    
    botao_enviar = st.form_submit_button(label="Cadastrar")

# Lógica para adicionar o paciente à tabela
if botao_enviar:
    if nome:
        data_formatada = data_nasc.strftime("%d/%m/%Y")
        novo_paciente = pd.DataFrame([{
            "Nome do Paciente": nome, 
            "Data de Nascimento": data_formatada, 
            "Localização Atual": localizacao_inicial
        }])
        # Adiciona ao estado da sessão
        st.session_state.pacientes = pd.concat([st.session_state.pacientes, novo_paciente], ignore_index=True)
        st.sidebar.success(f"Paciente {nome} cadastrado com sucesso!")
    else:
        st.sidebar.error("Por favor, preencha o nome do paciente.")

# --- Painel de Visualização e Atualização ---
st.subheader("📋 Status dos Pacientes em Tempo Real")

if st.session_state.pacientes.empty:
    st.info("Nenhum paciente cadastrado no momento. Use a barra lateral para adicionar.")
else:
    # Cria uma lista de opções para a dropdown de atualização
    opcoes_localizacao = ["RECEPÇÃO", "SALA DE OPERAÇÃO", "RPA", "ENCAMINHADO PARA O LEITO"]
    
    # Exibe os pacientes em formato de "cards" ou linhas interativas
    for idx, row in st.session_state.pacientes.iterrows():
        col1, col2, col3, col4 = st.columns([3, 2, 3, 1])
        
        with col1:
            st.markdown(f"**Paciente:** {row['Nome do Paciente']}")
        with col2:
            st.markdown(f"**Nascimento:** {row['Data de Nascimento']}")
        with col3:
            # Encontra o índice atual para deixar marcado na dropdown
            idx_atual = opcoes_localizacao.index(row['Localização Atual'])
            novo_local = st.selectbox(
                f"Alterar local de {row['Nome do Paciente']}:", 
                opcoes_localizacao, 
                index=idx_atual,
                key=f"sel_{idx}",
                label_visibility="collapsed" # Esconde o texto para ficar visualmente limpo
            )
            # Atualiza o banco de dados se mudar a opção
            if novo_local != row['Localização Atual']:
                st.session_state.pacientes.at[idx, 'Localização Atual'] = novo_local
                st.rerun() # Atualiza a tela imediatamente
                
        with col4:
            # Botão para dar alta / remover do painel
            if st.button("❌ Alta", key=f"btn_{idx}"):
                st.session_state.pacientes = st.session_state.pacientes.drop(idx).reset_index(drop=True)
                st.rerun()
                
        st.markdown("---")