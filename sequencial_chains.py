from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# our pipeline will go like
# 1:- prompt is given by user
# 2:- we will give this to a LLM
# 3:- LLM will generate a detailed report
# 4:- willl give this report the LLM again for summary
# 5:- llm will generate a 5 points summary for this 

load_dotenv()

model = ChatGroq(model ="llama-3.1-8b-instant", temperature=0.7)

prompt_1 = PromptTemplate(
    template = "generate a detailed report for the topic {topic}",
    input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template = "generate a 5 short point summary for the report {report}",
    input_variables=["report"]
)

parser = StrOutputParser()

chain = prompt_1 | model | parser | prompt_2 | model | parser

response = chain.invoke({"topic": "japan"})

print(response)

# visualize your chain

chain.get_graph().print_ascii()