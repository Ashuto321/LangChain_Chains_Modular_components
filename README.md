<h1 align="center">LangChain Modular Components - Chains</h1>

<p align="center">
  A comprehensive repository demonstrating the architecture, implementation, and execution flow of 
  <strong>LangChain Chains</strong> using modern runnable components such as 
  <strong>RunnableSequence</strong>, <strong>RunnableParallel</strong>, and <strong>RunnableBranch</strong>.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This repository is designed to provide a deep understanding of how modular chain architectures work in 
<a href="https://python.langchain.com/" target="_blank">LangChain</a>. 
The project focuses on building scalable and reusable AI workflows by demonstrating different types of chains 
used in modern LLM applications.
</p>

<p>
The repository covers:
</p>

<ul>
  <li>Simple Chains</li>
  <li>Sequential Chains</li>
  <li>Parallel Chains</li>
  <li>Conditional Chains</li>
  <li>Runnable Architecture</li>
  <li>Branching Logic using RunnableBranch</li>
  <li>Concurrent Execution using RunnableParallel</li>
  <li>Prompt Chaining Workflows</li>
  <li>Reusable Modular AI Components</li>
</ul>

<hr>

<h2>🎯 Objectives of This Repository</h2>

<ul>
  <li>Understand the architecture of LangChain chains</li>
  <li>Learn how modular AI workflows are designed</li>
  <li>Implement scalable chain execution patterns</li>
  <li>Explore sequential and parallel execution pipelines</li>
  <li>Build condition-based LLM routing systems</li>
  <li>Understand Runnable interfaces introduced in LangChain</li>
  <li>Improve prompt orchestration skills</li>
</ul>

<hr>

<h2>🧠 Why Chains Matter in LangChain</h2>

<p>
Large Language Models become significantly more powerful when multiple operations are connected together.
Chains help developers:
</p>

<ul>
  <li>Break complex workflows into smaller reusable components</li>
  <li>Control execution flow dynamically</li>
  <li>Build production-ready AI pipelines</li>
  <li>Route tasks intelligently based on conditions</li>
  <li>Execute tasks simultaneously for performance optimization</li>
</ul>

<p>
This repository demonstrates how those workflows are created using modern LangChain runnable components.
</p>

<hr>

<h2>🏗️ Repository Architecture</h2>

<pre>
Langchain_Modular_Components_Chains/
│
├── simple_chain.py
├── sequential_chain.py
├── parallel_chain.py
├── conditional_chain.py
│
├── prompts/
│   ├── summarization_prompt.py
│   ├── translation_prompt.py
│   └── classification_prompt.py
│
├── outputs/
│   └── sample_outputs/
│
├── requirements.txt
├── README.md
└── .env
</pre>

<hr>

<h2>⚙️ Technologies Used</h2>

<table>
  <tr>
    <th>Technology</th>
    <th>Purpose</th>
  </tr>

  <tr>
    <td>Python</td>
    <td>Core programming language</td>
  </tr>

  <tr>
    <td>LangChain</td>
    <td>LLM orchestration framework</td>
  </tr>

  <tr>
    <td>RunnableSequence</td>
    <td>Sequential execution pipeline</td>
  </tr>

  <tr>
    <td>RunnableParallel</td>
    <td>Concurrent chain execution</td>
  </tr>

  <tr>
    <td>RunnableBranch</td>
    <td>Conditional routing logic</td>
  </tr>

  <tr>
    <td>LLMs</td>
    <td>Text generation and processing</td>
  </tr>
</table>

<hr>

<h2>🚀 Installation</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone https://github.com/your-username/langchain-modular-components-chains.git

cd langchain-modular-components-chains
</pre>

<h3>2. Create Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

<h3>3. Activate Virtual Environment</h3>

<h4>Windows</h4>

<pre>
venv\Scripts\activate
</pre>

<h4>Linux / MacOS</h4>

<pre>
source venv/bin/activate
</pre>

<h3>4. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>🔑 Environment Variables</h2>

<p>
Create a <strong>.env</strong> file in the root directory.
</p>

<pre>
OPENAI_API_KEY=your_api_key
</pre>

<hr>

<h2>📘 Understanding the Implemented Chains</h2>

<hr>

<h2>1️⃣ Simple Chain</h2>

<p>
A Simple Chain represents the most basic execution pipeline in LangChain.
It takes an input, sends it to a prompt template, forwards it to the model,
and generates the final output.
</p>

<h3>Workflow</h3>

<pre>
User Input
    ↓
Prompt Template
    ↓
Language Model
    ↓
Generated Output
</pre>

<h3>Purpose</h3>

<ul>
  <li>Basic prompt execution</li>
  <li>Single-step processing</li>
  <li>Introduction to runnable architecture</li>
</ul>

<h3>Concepts Covered</h3>

<ul>
  <li>PromptTemplate</li>
  <li>LLM invocation</li>
  <li>Output parsing</li>
  <li>Runnable pipeline basics</li>
</ul>

<hr>

<h2>2️⃣ Sequential Chain</h2>

<p>
Sequential Chains execute multiple operations one after another.
The output of one chain becomes the input of the next chain.
</p>

<h3>Workflow</h3>

<pre>
Input
  ↓
Chain 1
  ↓
Chain 2
  ↓
Chain 3
  ↓
Final Output
</pre>

<h3>Example Use Cases</h3>

<ul>
  <li>Text Summarization → Translation</li>
  <li>Question → Answer → Explanation</li>
  <li>Topic Generation → Blog Creation</li>
</ul>

<h3>Concepts Covered</h3>

<ul>
  <li>RunnableSequence</li>
  <li>Data flow between chains</li>
  <li>Pipeline orchestration</li>
  <li>Modular execution</li>
</ul>

<hr>

<h2>3️⃣ Parallel Chain using RunnableParallel</h2>

<p>
Parallel Chains execute multiple tasks simultaneously.
This architecture is useful for reducing latency and improving efficiency.
</p>

<h3>Workflow</h3>

<pre>
                 ┌──────────────┐
                 │    Input     │
                 └──────┬───────┘
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ↓               ↓                ↓
   Chain A         Chain B          Chain C
        │               │                │
        └───────────────┼────────────────┘
                        ↓
                 Combined Output
</pre>

<h3>Why RunnableParallel?</h3>

<ul>
  <li>Faster execution</li>
  <li>Concurrent processing</li>
  <li>Multiple output generation</li>
  <li>Efficient workflow design</li>
</ul>

<h3>Example Use Cases</h3>

<ul>
  <li>Sentiment Analysis + Translation + Summarization</li>
  <li>Generating multiple content formats simultaneously</li>
  <li>Multi-agent task execution</li>
</ul>

<h3>Concepts Covered</h3>

<ul>
  <li>RunnableParallel</li>
  <li>Concurrent execution pipelines</li>
  <li>Task aggregation</li>
  <li>Performance optimization</li>
</ul>

<hr>

<h2>4️⃣ Conditional Chain using RunnableBranch</h2>

<p>
Conditional Chains dynamically decide which execution path to follow
based on user input or conditions.
</p>

<h3>Workflow</h3>

<pre>
                User Input
                     ↓
             Condition Evaluation
                     ↓
      ┌──────────────┼──────────────┐
      │                             │
      ↓                             ↓
 Positive Route              Negative Route
      │                             │
      └──────────────┬──────────────┘
                     ↓
                Final Response
</pre>

<h3>Why RunnableBranch?</h3>

<ul>
  <li>Dynamic AI routing</li>
  <li>Intelligent workflow selection</li>
  <li>Adaptive chain execution</li>
  <li>Context-aware processing</li>
</ul>

<h3>Example Use Cases</h3>

<ul>
  <li>Customer Support Routing</li>
  <li>Intent Classification</li>
  <li>AI Decision Systems</li>
  <li>Query Categorization</li>
</ul>

<h3>Concepts Covered</h3>

<ul>
  <li>RunnableBranch</li>
  <li>Conditional execution</li>
  <li>Routing logic</li>
  <li>Dynamic chain selection</li>
</ul>

<hr>

<h2>🔄 End-to-End Chain Execution Lifecycle</h2>

<pre>
User Query
    ↓
Prompt Formatting
    ↓
Runnable Execution
    ↓
Model Processing
    ↓
Chain Routing
    ↓
Output Parsing
    ↓
Final Response
</pre>

<hr>

<h2>🧩 Modular Design Philosophy</h2>

<p>
This repository follows a modular architecture approach where every component is reusable.
Instead of building monolithic AI workflows, each chain is designed independently
and can be connected dynamically.
</p>

<h3>Advantages</h3>

<ul>
  <li>Easy debugging</li>
  <li>Reusable components</li>
  <li>Scalable architecture</li>
  <li>Better maintainability</li>
  <li>Production-ready design</li>
</ul>

<hr>

<h2>📊 Runnable Components Used</h2>

<table>
  <tr>
    <th>Component</th>
    <th>Purpose</th>
  </tr>

  <tr>
    <td>RunnableSequence</td>
    <td>Sequential task execution</td>
  </tr>

  <tr>
    <td>RunnableParallel</td>
    <td>Parallel concurrent execution</td>
  </tr>

  <tr>
    <td>RunnableBranch</td>
    <td>Condition-based routing</td>
  </tr>

  <tr>
    <td>PromptTemplate</td>
    <td>Input formatting</td>
  </tr>

  <tr>
    <td>OutputParser</td>
    <td>Structured response extraction</td>
  </tr>
</table>

<hr>

<h2>💡 Real-World Applications</h2>

<ul>
  <li>AI Chatbots</li>
  <li>Customer Support Automation</li>
  <li>Document Processing Pipelines</li>
  <li>AI Workflow Orchestration</li>
  <li>Multi-Agent Systems</li>
  <li>Research Assistants</li>
  <li>Intelligent Routing Systems</li>
  <li>Content Generation Platforms</li>
</ul>

<hr>

<h2>📈 Learning Outcomes</h2>

<p>
After exploring this repository, developers will understand:
</p>

<ul>
  <li>How LangChain runnable architecture works</li>
  <li>How sequential workflows are designed</li>
  <li>How parallel processing improves performance</li>
  <li>How conditional routing is implemented</li>
  <li>How modular AI systems are built</li>
  <li>How production-ready LLM pipelines are structured</li>
</ul>

<hr>

<h2>🛠️ Future Improvements</h2>

<ul>
  <li>Integration with Memory Components</li>
  <li>LangGraph Implementation</li>
  <li>Agentic Workflows</li>
  <li>Streaming Responses</li>
  <li>Async Execution Pipelines</li>
  <li>Tool Calling Integration</li>
  <li>RAG-based Chains</li>
  <li>Multi-Agent Coordination</li>
</ul>

<hr>

<h2>📚 References</h2>

<ul>
  <li>
    <a href="https://python.langchain.com/docs/introduction/" target="_blank">
      LangChain Official Documentation
    </a>
  </li>

  <li>
    <a href="https://github.com/langchain-ai/langchain" target="_blank">
      LangChain GitHub Repository
    </a>
  </li>
</ul>

<hr>

<h2>🤝 Contribution</h2>

<p>
Contributions are welcome.
Feel free to fork the repository, improve workflows, optimize chains,
or add advanced runnable components.
</p>

<hr>

<h2>⭐ Support</h2>

<p>
If you found this repository helpful, consider giving it a star on GitHub.
It helps support the project and encourages future development.
</p>

<hr>

<h2>👨‍💻 Author</h2>

<p>
Ashutosh Pandey
</p>

<p>
Generative AI Research Analyst | Machine Learning Enthusiast | LangChain Developer
</p>

<hr>

<h2>📜 License</h2>

<p>
This project is licensed under the MIT License.
</p>

<hr>

<h2 align="center">
Building Modular AI Workflows with LangChain Runnable Components
</h2>
