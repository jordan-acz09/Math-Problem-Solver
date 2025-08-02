# Math Solver AI

A conversational math agent built using [LangChain](https://python.langchain.com/) and [Chainlit](https://www.chainlit.io/). This app leverages powerful language models and math reasoning chains to solve and explain mathematical problems interactively.

## Features

- **Conversational Math Agent:** Chat interface for asking math questions and receiving detailed, step-by-step solutions.
- **Hybrid Reasoning:** Handles both direct math computations and logic-based word problems using custom tools and chains.
- **Ollama Model Integration:** Uses the Mistral model via Ollama for language understanding and generation.
- **Extensible:** Easily extend with new tools or LLMs.

## Getting Started

### Prerequisites

- Python 3.8+
- [Chainlit](https://docs.chainlit.io/latest/installation.html)
- [LangChain](https://python.langchain.com/)
- [Ollama](https://ollama.com/) (for local LLM model inference)

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/math-solver-ai.git
   cd math-solver-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Ollama and download the Mistral model**
   ```bash
   ollama pull mistral
   ollama serve
   ```

4. **Run the Chainlit app**
   ```bash
   chainlit run math_agent.py
   ```

5. **Open your browser**
   Visit [http://localhost:8000](http://localhost:8000) to interact with your math agent.

## Usage

- Type any math question (e.g., "What is the derivative of x^2?", "If a train leaves at 3pm...").
- The agent will choose the appropriate reasoning tool (calculator or word problem solver) and reply with a step-by-step answer.

## Example Questions

- What is 17 * (3 + 5)?
- Solve for x: 2x + 3 = 11
- If a rectangle has sides 5 and 12, what is its area?
- Explain the Pythagorean theorem.

## Project Structure

```
math_agent.py        # Main Chainlit app with agent setup and message handlers
requirements.txt     # Python dependencies
README.md            # Project documentation
```

## License

MIT License

## Acknowledgements

- [LangChain](https://python.langchain.com/)
- [Chainlit](https://www.chainlit.io/)
- [Ollama](https://ollama.com/)
