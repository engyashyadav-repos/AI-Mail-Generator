from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate 


load_dotenv()

model = ChatGroq(
    model = "openai/gpt-oss-120b"
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a professional Email Generator.
            
            Rules:
            - Preserve the original meaning.
            - Email tone should be Professional.
            - Email length is medium
            - Include an appropriate subject line.
            - Address the recipient by name.
            - End the email with the sender's name."""
    ),
    (
        "human",
        """
            Subject of the Email: {topic}
            Name of the Email Recipient: {recipient_name}
            The purpose of the Email: {details}
            The sender name is: {sender_name}
        """
    )
   
])

chain = prompt | model
topic = input("Enter the topic of email: ")
recipient_name = input("Enter recipient's Name: ")
purpose = input("What is the purpose of the email? \nWhat information should be included? ")
sender_name = input("Enter the sender name: ")

response = chain.invoke({"topic":topic,"recipient_name":recipient_name,"details":purpose,"sender_name":sender_name})

print(response.content) 