<h1 align="center">LangChain Modular Components - Chains</h1>

<p align="center">
A complete hands-on implementation of modular chain architectures in LangChain using 
<b>Simple Chains</b>, 
<b>Sequential Chains</b>, 
<b>Parallel Chains</b>, and 
<b>Conditional Chains</b>.
</p>

<hr>

<h2>Overview</h2>

<p>
This repository demonstrates how modern Large Language Model (LLM) applications can be designed using 
modular and reusable chain architectures provided by 
<a href="https://python.langchain.com/" target="_blank">LangChain</a>.
</p>

<p>
The project focuses on practical implementations of:
</p>

<ul>
<li>Simple Runnable Chains</li>
<li>Sequential Processing Pipelines</li>
<li>Parallel Execution using RunnableParallel</li>
<li>Conditional Routing using RunnableBranch</li>
<li>Multi-Provider LLM Integration</li>
<li>Prompt Chaining Architecture</li>
<li>Structured Workflow Design</li>
</ul>

<p>
The repository is designed for:
</p>

<ul>
<li>Students learning LangChain</li>
<li>Developers building AI applications</li>
<li>Engineers preparing for AI/LLM interviews</li>
<li>Researchers exploring modular LLM workflows</li>
<li>Professionals working with Generative AI systems</li>
</ul>

<hr>

<h2>What This Repository Covers</h2>

<table>
<tr>
<th>Component</th>
<th>Description</th>
</tr>

<tr>
<td><b>Simple Chain</b></td>
<td>Single prompt-response execution flow using LangChain runnables.</td>
</tr>

<tr>
<td><b>Sequential Chain</b></td>
<td>Output from one chain becomes input for the next chain.</td>
</tr>

<tr>
<td><b>Parallel Chain</b></td>
<td>Multiple chains execute simultaneously using RunnableParallel.</td>
</tr>

<tr>
<td><b>Conditional Chain</b></td>
<td>Dynamic branching logic using RunnableBranch based on conditions.</td>
</tr>

<tr>
<td><b>Prompt Engineering</b></td>
<td>Prompt template management and dynamic prompt execution.</td>
</tr>

<tr>
<td><b>LLM Integration</b></td>
<td>Integration with OpenAI, Groq, and Google Generative AI SDK.</td>
</tr>

</table>

<hr>

<h2>Tech Stack</h2>

<table>
<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>Python</td>
<td>Core Programming Language</td>
</tr>

<tr>
<td>LangChain</td>
<td>LLM Orchestration Framework</td>
</tr>

<tr>
<td>OpenAI API</td>
<td>GPT Model Integration</td>
</tr>

<tr>
<td>Groq API</td>
<td>High-Speed LLM Inference</td>
</tr>

<tr>
<td>Google Generative AI SDK</td>
<td>Gemini Model Integration</td>
</tr>

<tr>
<td>RunnableParallel</td>
<td>Parallel Chain Execution</td>
</tr>

<tr>
<td>RunnableBranch</td>
<td>Conditional Workflow Routing</td>
</tr>

</table>

<hr>

<h2>Repository Structure</h2>

<pre>
LangChain_Modular_Components_Chains/
│
├── simple_chain.py
├── sequential_chain.py
├── parallel_chain.py
├── conditional_chain.py
│
├── requirements.txt
├── .env
└── README.md
</pre>

<hr>

<h2>Architecture Flow</h2>

<h3>1. Simple Chain Architecture</h3>

<pre>
User Input
     │
     ▼
Prompt Template
     │
     ▼
LLM Model
     │
     ▼
Generated Response
</pre>

<hr>

<h3>2. Sequential Chain Architecture</h3>

<pre>
User Input
     │
     ▼
Chain 1
     │
     ▼
Intermediate Output
     │
     ▼
Chain 2
     │
     ▼
Final Response
</pre>

<hr>

<h3>3. Parallel Chain Architecture</h3>

<pre>
                 ┌──────────────┐
                 │ User Input   │
                 └──────┬───────┘
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
   Chain A         Chain B          Chain C
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                 Combined Output
</pre>

<hr>

<h3>4. Conditional Chain Architecture</h3>

<pre>
                 User Input
                      │
                      ▼
              RunnableBranch
               /          \
              /            \
             ▼              ▼
       Condition A     Condition B
             │              │
             ▼              ▼
        Chain A         Chain B
</pre>

<hr>

<h2>Detailed Explanation of Chains</h2>

<h3>Simple Chain</h3>

<p>
A Simple Chain is the most fundamental building block in LangChain.
It follows a direct flow where:
</p>

<ul>
<li>User input is passed into a prompt template</li>
<li>The prompt is sent to the LLM</li>
<li>The LLM generates the output</li>
</ul>

<p>
This approach is ideal for:
</p>

<ul>
<li>Question answering</li>
<li>Text summarization</li>
<li>Basic chatbot workflows</li>
<li>Single-step reasoning tasks</li>
</ul>

<hr>

<h3>Sequential Chain</h3>

<p>
Sequential Chains allow chaining multiple LLM operations together.
The output of one chain becomes the input for the next chain.
</p>

<p>
This architecture is useful for:
</p>

<ul>
<li>Multi-step reasoning</li>
<li>Content generation pipelines</li>
<li>Data transformation workflows</li>
<li>AI automation systems</li>
</ul>

<p>
Example Workflow:
</p>

<pre>
Topic → Generate Blog → Summarize Blog → Create LinkedIn Post
</pre>

<hr>

<h3>Parallel Chain using RunnableParallel</h3>

<p>
RunnableParallel executes multiple chains simultaneously.
This significantly improves performance and allows multi-perspective outputs.
</p>

<p>
Advantages:
</p>

<ul>
<li>Reduced execution time</li>
<li>Concurrent task execution</li>
<li>Better scalability</li>
<li>Multi-output generation</li>
</ul>

<p>
Example Use Cases:
</p>

<ul>
<li>Generate summary + keywords + hashtags together</li>
<li>Perform sentiment and classification simultaneously</li>
<li>Run multiple prompts on the same input</li>
</ul>

<hr>

<h3>Conditional Chain using RunnableBranch</h3>

<p>
RunnableBranch enables intelligent routing inside LLM workflows.
Different chains are executed depending on conditions.
</p>

<p>
This introduces decision-making capability into AI applications.
</p>

<p>
Example:
</p>

<ul>
<li>If input is technical → send to technical chain</li>
<li>If input is casual → send to conversational chain</li>
<li>If input is code-related → send to coding chain</li>
</ul>

<p>
This pattern is heavily used in:
</p>

<ul>
<li>AI Agents</li>
<li>Dynamic Chatbots</li>
<li>Customer Support Systems</li>
<li>Multi-domain AI Applications</li>
</ul>

<hr>

<h2>Installation</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone https://github.com/your-username/langchain-modular-components-chains.git

cd langchain-modular-components-chains
</pre>

<hr>

<h3>2. Create Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

<hr>

<h3>3. Activate Virtual Environment</h3>

<h4>Windows</h4>

<pre>
venv\Scripts\activate
</pre>

<h4>Mac/Linux</h4>

<pre>
source venv/bin/activate
</pre>

<hr>

<h3>4. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>Environment Variables</h2>

<p>
Create a <b>.env</b> file in the root directory and add the following API keys:
</p>

<pre>
OPENAI_API_KEY=your_openai_api_key

GROQ_API_KEY=your_groq_api_key

GOOGLE_API_KEY=your_google_generative_ai_key
</pre>

<hr>

<h2>Required Packages</h2>

<pre>
langchain
langchain-openai
langchain-google-genai
langchain-groq
python-dotenv
</pre>

<hr>

<h2>How to Run</h2>

<h3>Run Simple Chain</h3>

<pre>
python simple_chain.py
</pre>

<hr>

<h3>Run Sequential Chain</h3>

<pre>
python sequential_chain.py
</pre>

<hr>

<h3>Run Parallel Chain</h3>

<pre>
python parallel_chain.py
</pre>

<hr>

<h3>Run Conditional Chain</h3>

<pre>
python conditional_chain.py
</pre>

<hr>

<h2>Core Concepts Learned</h2>

<ul>
<li>LangChain Runnable Architecture</li>
<li>Composable AI Pipelines</li>
<li>LLM Workflow Engineering</li>
<li>Prompt Chaining</li>
<li>Parallel Execution in LangChain</li>
<li>Conditional Routing Logic</li>
<li>Modular AI Design</li>
<li>Scalable Chain Architectures</li>
<li>Multi-LLM Integration</li>
</ul>

<hr>

<h2>Real-World Applications</h2>

<table>
<tr>
<th>Use Case</th>
<th>Implementation</th>
</tr>

<tr>
<td>AI Chatbots</td>
<td>Conditional + Sequential Chains</td>
</tr>

<tr>
<td>Content Generation</td>
<td>Sequential Chains</td>
</tr>

<tr>
<td>Multi-Agent Systems</td>
<td>Parallel Chains</td>
</tr>

<tr>
<td>Customer Support Bots</td>
<td>RunnableBranch Routing</td>
</tr>

<tr>
<td>Research Assistants</td>
<td>Sequential + Parallel Pipelines</td>
</tr>

<tr>
<td>AI Automation</td>
<td>Modular Chain Architecture</td>
</tr>

</table>

<hr>

<h2>Why This Project Matters</h2>

<p>
Modern AI systems are no longer built using a single prompt.
Production-grade LLM applications require:
</p>

<ul>
<li>Modularity</li>
<li>Scalability</li>
<li>Conditional Logic</li>
<li>Workflow Orchestration</li>
<li>Multi-step Reasoning</li>
</ul>

<p>
This repository demonstrates those concepts practically using LangChain’s latest runnable architecture.
</p>

<hr>

<h2>Key Highlights</h2>

<ul>
<li>Clean modular implementations</li>
<li>Industry-relevant LangChain concepts</li>
<li>RunnableParallel implementation</li>
<li>RunnableBranch conditional routing</li>
<li>Multi-provider LLM support</li>
<li>Beginner-friendly architecture</li>
<li>Interview-oriented project structure</li>
<li>Production-level workflow understanding</li>
</ul>

<hr>

<h2>Interview Preparation Value</h2>

<p>
This repository helps in understanding:
</p>

<ul>
<li>How LangChain workflows are structured</li>
<li>Difference between sequential and parallel execution</li>
<li>How conditional routing works in LLM pipelines</li>
<li>How modular AI systems are designed</li>
<li>How to build scalable Generative AI applications</li>
</ul>

<p>
These are frequently discussed topics in:
</p>

<ul>
<li>Generative AI Interviews</li>
<li>LLM Engineer Roles</li>
<li>AI Application Development Interviews</li>
<li>LangChain-Based Project Discussions</li>
</ul>

<hr>

<h2>Future Improvements</h2>

<ul>
<li>Add LangGraph workflows</li>
<li>Integrate Memory Components</li>
<li>Add RAG Pipelines</li>
<li>Implement AI Agents</li>
<li>Add Streaming Responses</li>
<li>Deploy using FastAPI or Streamlit</li>
<li>Add Vector Database Integration</li>
<li>Introduce Observability with LangSmith</li>
</ul>

<hr>

<h2>Author</h2>

<p>
<b>Ashutosh Pandey</b>
</p>

<p>
Generative AI Research Analyst | LangChain Developer | Machine Learning Enthusiast
</p>

<hr>

<h2>Conclusion</h2>

<p>
This repository provides a strong foundation for understanding modular chain architectures in LangChain.
It demonstrates how modern AI workflows can be structured using simple, sequential, parallel, and conditional execution pipelines.
</p>

<p>
The project is designed not only for learning but also for showcasing practical implementation skills in Generative AI engineering.
</p>

<hr>

<h2>License</h2>

<p>
This project is licensed under the MIT License.
</p>

<hr>

<h2>Support</h2>

<p>
If you found this repository useful, consider giving it a star on GitHub.
</p>
