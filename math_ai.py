from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama

from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
import chainlit as cl

@cl.on_chat_start
async def math_math_agent():
    llm = Ollama(model="mistral")

    problem_chain = LLMMathChain.from_llm(llm=llm)
    math_tool = Tool.from_function(
        name="Calculator",
        func=problem_chain.run,
        description="Useful for math questions only."
    )

    word_problem_template = """You are a reasoning agent tasked with solving 
    the user's logic-based math questions. Be logical in arriving at the solution...
    Question: {question}
    Answer:"""

    math_assistant_prompt = PromptTemplate(input_variables=["question"], template=word_problem_template)

    word_problem_chain = LLMChain(llm=llm, prompt=math_assistant_prompt)
    word_problem_tool = Tool.from_function(
        name="Reasoning Tool",
        func=word_problem_chain.run,
        description="Useful for reasoning or logic-based math questions."
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
