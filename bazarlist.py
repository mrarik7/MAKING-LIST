import streamlit as st

col1,col2,col3 = st.columns(3)
with col1:
    st.header('Make Your List📙')
with col3:
    if st.button('ℹ️ info'):
        st.text('1.write one by one\n2.write "end"when you finish\n3.take a screanshot for later usage')
if 'msg' not in st.session_state:
    st.session_state.msg = []

msg = st.chat_input('write here...')
if msg:
    st.session_state.msg.append(msg)

for i in st.session_state.msg:
    with st.chat_message('ai'):
        st.write(i)


if msg == 'end':
    st.subheader('your list is ready💁')
    st.write(st.session_state.msg)
    st.write ('⚠️take a screanshot so that you have a copy for later uses:)')
    st.markdown('[about Arik](https://profilepy-3t8ez4hcjvvmwsczqmxnbz.streamlit.app/)')












