import streamlit as st

st.title("Simple Chatbot")

st.write("🤖 Greetings to you! It's pleasure to assist you today.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me something..."):
    with st.chat_message("user", avatar="🤵"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        bot_response = ""

        # Bot responses based on user input
        if prompt.lower() in ["hello", "hi"]:
            bot_response = "Hello! How can I assist you today?"
        elif "how are you" in prompt.lower():
            bot_response = "Thank you for asking! I'm just a computer, so I don't have feelings like human, but I'm here and ready to help you. How can I assist you today?"
        elif "help" in prompt.lower():
            bot_response = "Of course! I'm here to help. What do you need assistance with? Let me know if you need any further help."
        elif "thank you" in prompt.lower():
            bot_response = "You're welcome! Have a great day!"
        elif "bye" in prompt.lower():
            bot_response = "Goodbye! Have a great day."
        else:
            bot_response = "I'm sorry, I didn't understand that. Could you kindly provide complete sentence so that I may better assist you?"
        message_placeholder.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

          
