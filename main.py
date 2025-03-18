import streamlit as st
import re
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
import langchain_groq

model = langchain_groq.ChatGroq(
    model_name='deepseek-r1-distill-llama-70b',
    api_key='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',
)


def response_generator(prompt):  # генерация ответов
    messages = [
        SystemMessage("""Ты эксперт в сфере математического анализа. Я задам тебе вопрос и ты на него ответишь, пользуясь стандартными теоремами и определениями.
                      ВСЕ ФУНКЦИИ И ФОРМУЛЫ ПРОПИСЫВАЙ С ПОМОЩЬЮ MARKDOWN так, чтобы это было понятно интерпретатору st.markdown"""),
        HumanMessage(prompt),
    ]

    response = model.invoke(messages).content
    return response


def preprocess_think_tags(text):  # обработка текста, чтобы были разные цвета у размышлений и ответа
    # Заменяем <think>...</think> на HTML с CSS-стилизацией
    if '</think>' in text:
        processed_text = text.replace("<think>",
                                      '<div style="color:red;">Размышления: </div><div style="font-size: 0.8em; opacity: 0.5;">')
        processed_text = processed_text.replace("</think>",
                                                '</div><div style="color:red;">Ответ: </div>\n<div style="font-size: 1em;">')
        processed_text += '\n</div>'
    else:
        processed_text = text.replace("<think>", '')
        processed_text = '<span style="color: yellow; font-style: Roboto;">' + processed_text
        processed_text += '</span>'
    return processed_text


def model_answer(prompt):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message['content'])

    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message('assistant'):
        messages = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        prompt = ''
        for i in range(len(messages)):
            prompt += str(messages[i])
        ans = response_generator(prompt)

        ans_with_html = preprocess_think_tags(ans)

        st.markdown(ans_with_html, unsafe_allow_html=True)
        print(ans)
        ans = ans.split('</think>')[1]
    st.session_state.messages.append({'role': 'assistant', 'content': ans})
    return ans


def reset_conversation():
    st.session_state.conversation = None
    st.session_state.chat_history = None


st.button('Reset Chat', on_click=reset_conversation)
