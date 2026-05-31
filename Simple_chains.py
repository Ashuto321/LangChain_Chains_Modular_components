from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-safeguard-20b", temperature=0.7)

prompt = PromptTemplate(
    template = "generate 5 interesting facts about the topic {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chains = prompt | model | parser

response = chains.invoke({'topic':'Japan'})

print(response)

# visualize your chain

chains.get_graph().print_ascii()