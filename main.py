# import csv
# from groq import Groq
#
# # Ключ API для Groq
# key = "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"
# client = Groq(api_key=key)
#
# # Чтение данных из CSV-файла
# questions_dict = {}
# with open("C:/Users/Дмитрий/Downloads/LR1.csv", mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     questions_list = []
#
#     for row in reader:
#         question_number = int(row[''])
#         question_text = row['question'].replace('\n', ' ')
#         subject = row['subject']
#         choices_str = row['choices'].strip("[]'")
#         choices = [choice.strip() for choice in choices_str.split("'") if choice.strip()]
#
#         while len(questions_list) <= question_number:
#             questions_list.append(None)
#
#         questions_list[question_number] = {
#             'question': question_text,
#             'subject': subject,
#             'choices': choices
#         }
#
# # Функция для получения правильного ответа
# def get_correct_answer(question_data, index):
#     prompt = (
#         "You are an expert in all fields, including mathematics, science, history, law, economics, philosophy, and more. "
#         "Your task is to solve complex problems with 100% accuracy using a **multi-step reasoning approach**. "
#         "Follow these steps for every question:\n\n"
#
#         "1. **Understand the Problem**: Carefully read the question and identify the key elements, context, and subject matter.\n"
#         "2. **Break Down the Problem**: Divide the problem into smaller, manageable sub-problems if necessary.\n"
#         "3. **Apply Domain Knowledge**: Use your expertise in the relevant field to analyze each sub-problem.\n"
#         "4. **Evaluate Choices**: For multiple-choice questions, evaluate each option step by step, eliminating incorrect ones.\n"
#         "5. **Cross-Verify**: Double-check your reasoning and calculations to ensure no errors.\n"
#         "6. **Provide a Detailed Explanation**: Clearly explain your thought process, including why you chose or rejected each option.\n"
#         "7. **Final Answer**: After thorough analysis, provide the correct answer with confidence.\n\n"
#
#         "**Important Rules**:\n"
#         "- Always use **Chain of Thought** (step-by-step reasoning).\n"
#         "- If the problem is complex, use **Tree of Thought** (explore multiple reasoning paths) or **Graph of Thought** (map relationships between ideas).\n"
#         "- If the question involves calculations, show all steps and verify the result.\n"
#         "- If the question is ambiguous, make reasonable assumptions and state them clearly.\n"
#         "- If you are unsure, provide the most likely answer and explain why.\n\n"
#
#         "**Examples of Multi-Step Reasoning**:\n"
#
#         "Example 1 (Mathematics):\n"
#         "Question: What is the square root of 144?\n"
#         "Chain of Thought:\n"
#         "1. The question asks for the square root of 144.\n"
#         "2. I know that 12 × 12 = 144.\n"
#         "3. Therefore, the square root of 144 is 12.\n"
#         "Final Answer: 12\n\n"
#
#         "Example 2 (Law):\n"
#         "Question: In a contract dispute, which party is typically responsible for proving breach of contract?\n"
#         "Chain of Thought:\n"
#         "1. The question is about the burden of proof in a contract dispute.\n"
#         "2. In legal terms, the plaintiff (the party bringing the lawsuit) is responsible for proving that a breach occurred.\n"
#         "3. The defendant does not have to prove anything unless they are making a counterclaim.\n"
#         "4. Therefore, the correct answer is the plaintiff.\n"
#         "Final Answer: Plaintiff\n\n"
#
#         "Example 3 (Science):\n"
#         "Question: What is the chemical formula for water?\n"
#         "Chain of Thought:\n"
#         "1. The question asks for the chemical formula of water.\n"
#         "2. I know that water is composed of two hydrogen atoms and one oxygen atom.\n"
#         "3. Therefore, the chemical formula is H₂O.\n"
#         "Final Answer: H₂O\n\n"
#
#         "Example 4 (History):\n"
#         "Question: Who was the first President of the United States?\n"
#         "Chain of Thought:\n"
#         "1. The question asks for the first President of the United States.\n"
#         "2. I know that George Washington was the leader of the Continental Army during the American Revolution.\n"
#         "3. He was unanimously elected as the first President in 1789.\n"
#         "4. Therefore, the correct answer is George Washington.\n"
#         "Final Answer: George Washington\n\n"
#
#         "Example 5 (Economics):\n"
#         "Question: What is the primary function of a central bank?\n"
#         "Chain of Thought:\n"
#         "1. The question asks about the primary function of a central bank.\n"
#         "2. Central banks are responsible for managing a country's monetary policy, controlling inflation, and stabilizing the currency.\n"
#         "3. They also act as a lender of last resort to commercial banks.\n"
#         "4. Therefore, the primary function is to manage monetary policy.\n"
#         "Final Answer: Manage monetary policy\n\n"
#
#         "Example 6 (Philosophy):\n"
#         "Question: What is the main idea of Immanuel Kant's categorical imperative?\n"
#         "Chain of Thought:\n"
#         "1. The question asks about Kant's categorical imperative.\n"
#         "2. Kant's categorical imperative is a moral principle that states one should act only according to maxims that can be universally applied.\n"
#         "3. It emphasizes treating individuals as ends in themselves, not merely as means.\n"
#         "4. Therefore, the main idea is to act according to universalizable maxims.\n"
#         "Final Answer: Act according to universalizable maxims\n\n"
#
#         "Example 7 (Computer Science):\n"
#         "Question: What is the time complexity of a binary search algorithm?\n"
#         "Chain of Thought:\n"
#         "1. The question asks about the time complexity of a binary search algorithm.\n"
#         "2. Binary search works by repeatedly dividing the search interval in half.\n"
#         "3. This results in a time complexity of O(log n), where n is the number of elements.\n"
#         "4. Therefore, the correct answer is O(log n).\n"
#         "Final Answer: O(log n)\n\n"
#
#         "Example 8 (Medicine):\n"
#         "Question: What is the normal resting heart rate for an adult?\n"
#         "Chain of Thought:\n"
#         "1. The question asks for the normal resting heart rate for an adult.\n"
#         "2. I know that the normal range is typically between 60 and 100 beats per minute.\n"
#         "3. Therefore, the correct answer is 60-100 beats per minute.\n"
#         "Final Answer: 60-100 beats per minute\n\n"
#
#         "Example 9 (Literature):\n"
#         "Question: Who wrote '1984'?\n"
#         "Chain of Thought:\n"
#         "1. The question asks about the author of '1984'.\n"
#         "2. I know that '1984' is a dystopian novel written by George Orwell.\n"
#         "3. Therefore, the correct answer is George Orwell.\n"
#         "Final Answer: George Orwell\n\n"
#
#         "Example 10 (Physics):\n"
#         "Question: What is the speed of light in a vacuum?\n"
#         "Chain of Thought:\n"
#         "1. The question asks for the speed of light in a vacuum.\n"
#         "2. I know that the speed of light is approximately 299,792 kilometers per second.\n"
#         "3. Therefore, the correct answer is 299,792 km/s.\n"
#         "Final Answer: 299,792 km/s\n\n"
#
#         "Now, analyze the following question using the **multi-step reasoning approach**:\n"
#         f"Question: {question_data['question']}\n"
#         f"Subject: {question_data['subject']}\n"
#         "Choices:\n"
#     )
#     for i, choice in enumerate(question_data['choices'], start=0):
#         prompt += f"{i}. {choice}\n"
#     prompt += (
#         "Chain of Thought:\n"
#         "1. Analyze the question and identify the key elements.\n"
#         "2. Break down the problem into smaller parts if necessary.\n"
#         "3. Evaluate each choice step by step, eliminating incorrect ones.\n"
#         "4. Cross-verify your reasoning to ensure no errors.\n"
#         "5. Provide a detailed explanation of your thought process.\n"
#         "6. After thorough analysis, give ONLY the number of the correct answer.\n"
#         "**Important**: The final answer must be a number between 0 and 3, corresponding to one of the choices above. "
#         "If you cannot determine the correct answer, choose the most likely option based on your analysis.\n"
#         "Remember, your response must include the Chain of Thought reasoning followed by the final answer."
#     )
#
#     # Запрос к ИИ
#     completion = client.chat.completions.create(
#         model="llama3-70b-8192",
#         messages=[
#             {"role": "system", "content": "You are an expert in multiple fields. Your task is to analyze questions and provide the correct answer using the Chain of Thought approach."},
#             {"role": "assistant", "content": "I will carefully analyze each question step by step, provide detailed reasoning, and ensure that my final answer is 100% accurate and within the range of 0 to 3."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0,
#         max_tokens=700,
#         top_p=1,
#         stop=None,
#     )
#
#     # Получаем ответ от ИИ
#     response = completion.choices[0].message.content.strip()
#
#     # Извлекаем финальный ответ
#     final_answer = None
#     for line in response.split("\n"):
#         if line.lower().startswith(("correct answer:", "final answer:")):
#             final_answer = line.split(":")[1].strip()
#             break
#
#     if final_answer is None:
#         import re
#         numbers = re.findall(r'\d+', response)
#         if numbers:
#             final_answer = numbers[-1]
#
#     # Проверяем, что ответ — это число и находится в допустимом диапазоне (0-3)
#     if final_answer and final_answer.isdigit():
#         final_answer = int(final_answer)
#         if 0 <= final_answer <= 3:
#             pass  # Ответ в допустимом диапазоне
#         else:
#             final_answer = 0  # Возвращаем 0 как значение по умолчанию
#     else:
#         final_answer = 0  # Возвращаем 0 как значение по умолчанию
#
#     # Записываем номер вопроса и ответ в файл LR1_dev_answer.csv
#     with open("LR1_dev_answer.csv", mode='a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         # Если файл пустой, добавляем заголовок
#         if file.tell() == 0:
#             writer.writerow(["", "answer"])
#         writer.writerow([index, final_answer])
#
#     return final_answer
#
# # Номера вопросов, которые нужно обработать
# selected_questions = [x for x in range(300)]
# # selected_questions = selected_questions[291:300]
#
# # Цикл по всем вопросам
# for index, question_data in enumerate(questions_list):
#     if question_data is not None and index in selected_questions:
#         correct_answer = get_correct_answer(question_data, index)
#         print(f'Question {index} processed. Answer: {correct_answer}')
#
# # # Функция для сравнения ответов
# # def compare_answers(generated_answers_file, correct_answers_file):
# #     generated_answers = {}
# #     with open(generated_answers_file, mode='r', encoding='utf-8') as file:
# #         reader = csv.reader(file)
# #         next(reader)
# #         for row in reader:
# #             question_number = int(row[0])
# #             answer = int(row[1])
# #             generated_answers[question_number] = answer
# #
# #     correct_answers = {}
# #     with open(correct_answers_file, mode='r', encoding='utf-8') as file:
# #         reader = csv.reader(file)
# #         next(reader)
# #         for row in reader:
# #             question_number = int(row[0])
# #             answer = int(row[1])
# #             correct_answers[question_number] = answer
# #
# #     correct_count = 0
# #     total_questions = len(generated_answers)
# #
# #     for question_number, correct_answer in correct_answers.items():
# #         if question_number in generated_answers and generated_answers[question_number] == correct_answer:
# #             correct_count += 1
# #
# #     accuracy = (correct_count / total_questions) * 100
# #     return accuracy
# #
# # # Основной код
# # if __name__ == "__main__":
# #     generated_answers_file = "LR1_dev_answer.csv"
# #     correct_answers_file = "C:/Users/Дмитрий/Downloads/LR1_dev_answer.csv"
# #
# #     accuracy = compare_answers(generated_answers_file, correct_answers_file)
# #     print(f"Процент правильных ответов: {accuracy:.2f}%")

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
