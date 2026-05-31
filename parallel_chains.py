from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# problem statemeny
# """
# user will give the input values like a detailed user text
# then we will take it and give it to model 1 for notes generation
# then to model 2 for quiz generation 
# tehn these 2 wil be given to model 3 for merging and giving the merged output
# we will develop a parallel merging chains running using runnables called RunnableParallel
# """

load_dotenv()

model1= ChatGroq(model ="llama-3.1-8b-instant", temperature=0.7)

model2 = ChatGoogleGenerativeAI(model ="gemini-3-flash-preview", temperature=0.7)

prompt1= PromptTemplate(
    template ="generate a good short points note on this text {text}",
    input_variables=["text"]
    
)
    
prompt2= PromptTemplate(
    template = "generate a good question answer for this notes {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template = "Merge the given notes and quiz into a isngle document note-> {note} and quiz-> {quiz}",
    input_variables=["notes","quiz"]
)

parser = StrOutputParser()

# chain running parallel
parallel_chain = RunnableParallel({
    'note': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

# merging chain 
merge_chain = prompt3 | model1 | parser

main_chain = parallel_chain | merge_chain

text = """ Machine learning is a transformative subfield of artificial intelligence that empowers computer systems to learn from data, identify intricate patterns, and make autonomous decisions with minimal human intervention. At its core, it functions by utilizing statistical algorithms to build mathematical models based on sample data, known as "training data," which allows the system to improve its performance on specific tasks over time. Machine learning is generally categorized into three primary types: supervised learning, where the model is trained on labeled data to predict outcomes or classify inputs; unsupervised learning, which involves training on unlabeled data to discover hidden structures, groupings, or anomalies within a dataset; and reinforcement learning, an approach where an agent learns to make optimal decisions by interacting with an environment and receiving feedback in the form of rewards or penalties. Each of these methodologies serves distinct purposes, ranging from predictive analytics and recommendation engines to complex robotics and generative modeling, effectively bridging the gap between raw information and actionable, intelligent insights."""

response = main_chain.invoke({"text":text})

print(response)

# visualizing 

main_chain.get_graph().print_ascii() 