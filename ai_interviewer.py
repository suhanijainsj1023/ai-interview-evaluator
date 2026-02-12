from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
api_key=os.getenv("GOOGLE_API_KEY")

# ---------- ENV ----------
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4
)

# ---------- USER SETUP ----------
role = input("Enter role (Python Developer / Data Analyst): ")
level = input("Enter level (easy / medium / hard): ")

print("\nInterview Started...\n")

# ---------- INTERVIEW LOOP ----------
for i in range(1, 6):   # 5 questions
    print(f"\nQuestion {i}:")
    
    question = llm.invoke(
        f"Ask one {level} interview question for a {role}. Only ask the question."
    ).content
    
    print(question)

    answer = input("\nYour Answer: ")

    evaluation = llm.invoke(
        f"""
        Question: {question}
        Answer: {answer}

        Give score out of 10 and short feedback.
        """
    ).content

    print("\nAI Feedback:")
    print(evaluation)

print("\nInterview Finished ✅")