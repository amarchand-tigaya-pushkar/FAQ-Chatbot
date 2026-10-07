# Simple FAQ Chatbot for Beginners
# FAQ data stored in dictionary
faq = {
    "what is brainwave ai": "Brainwave AI is an AI and Data Science training institute.",
    "what courses do you offer": "We offer Python, Data Science, Machine Learning, Deep Learning, NLP, Generative AI and Agentic AI.",
    "what is agentic ai": "Agentic AI is an AI system that can plan, use tools, make decisions and complete tasks.",
    "do you provide internship": "Yes, we provide training with internship and live projects.",
    "how can i contact you": "You can contact us at 9828919909."
}

print("Welcome to Brainwave AI FAQ Chatbot")
print("Type 'exit' to stop the chatbot")

while True:
    # Take user input
    user_question = input("\nAsk your question: ")

    # Convert input into lowercase
    user_question = user_question.lower()

    # Stop chatbot
    if user_question == "exit":
        print("Thank you for chatting with us!")
        break

    # Check question in FAQ dictionary
    if user_question in faq:
        print("Bot:", faq[user_question])
    else:
        print("Bot: Sorry, I do not know the answer. Please contact 9828919909.")