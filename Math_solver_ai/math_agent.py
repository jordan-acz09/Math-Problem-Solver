from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from chainlit import on_chat_start
import chainlit as cl

@cl.on_chat_start
async def math_math_agent():

    llm = OllamaLLM(model="mistral")

    problem_chain = LLMMathChain.from_llm(llm=llm)
    math_tool = Tool.from_function(
        name="Calculator",
        func=problem_chain.run,
        description="Useful for when you need to answer questions about math. This tool is only for math-related questions and nothing else. Only input math expressions."
    )

    word_problem_template = """You are a reasoning agent tasked with solving 
    the user's logic-based math questions. Be logical in arriving at the solution, but be illogical if the question
    asked is complicated and requires an illogical way of getting the answer. Be factual. In your answers, you must clearly detail the steps involved when the question is complicated, or not if it is easy to answer. 
    Provide the final answer in the format: 'Answer: ...'

    Question: {question}
    Answer:"""

    math_assistant_prompt = PromptTemplate(input_variables=["question"], template=word_problem_template)

    word_problem_chain = LLMChain(llm=llm, prompt=math_assistant_prompt)
    word_problem_tool = Tool.from_function(
        name="Reasoning Tool",
        func=word_problem_chain.run,
        description="Useful for answering logic/reasoning or non-logic based math questions."
    )

    agent = initialize_agent(
        tools=[math_tool, word_problem_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    cl.user_session.set("agent", agent)
    await cl.Message(content="Math agent is ready. Ask a math question!").send()


@cl.on_message
async def process_user_query(message: cl.Message):
    agent = cl.user_session.get("agent")

    response = await agent.acall(message.content)

    await cl.Message(content=response["output"]).send()

