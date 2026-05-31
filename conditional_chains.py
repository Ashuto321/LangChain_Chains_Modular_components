from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda

load_dotenv()

model= ChatGroq(model="openai/gpt-oss-safeguard-20b", temperature=0.7)
parser = StrOutputParser()

class feedback(BaseModel):
    
    sentiment : Literal['positive','negative'] = Field(discription="give me the sentiment of the feedback as positive or negative") 
    
parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template = "classsify the feedback as positive or negative only {feedback} {format_instrcution}",
    input_variables=["feedback"],
    partial_variables={'format_instrcution': parser2.get_format_instructions()}
)

classification_chain = prompt1 | model | parser2

# response = classification_chain.invoke({'feedback': "This is very good in hardware"})

# print(response)
# for now we dont need the above since out chain is classifying properly.

# in the runnablebranch we pass multiple tupple as
# (condition, if true then chain)
# (condition2, if true then chain)
# default chain

# before this we neeed prompts for procesing the positive and negative feedback

prompt2 = PromptTemplate(
    template = "generate a appropriate response for the positive feedback {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template ="generate a appropriate response for the negative feedback {feedback}",
    input_variables=["feedback"]
)

branch_chain= RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model| parser),
    RunnableLambda(lambda x: "could not found the sentiment")
)

# combining the final chains together

main_chain = classification_chain | branch_chain

response1 = main_chain.invoke({'feedback':'this phone is terrible in use, i want a refund'})

response2 = main_chain.invoke({'feedback': 'this is a very good product amazing'})


print(response2)

# lets visualize it 
main_chain.get_graph().print_ascii()


