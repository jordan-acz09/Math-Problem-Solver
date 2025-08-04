from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import chainlit as cl

HUGGINGFACEHUB_API_TOKEN = "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"

llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",
    model_kwargs={"temperature": 0.5, "max_length": 256},
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
)

math_assistant_prompt = PromptTemplate(
    input_variables=["question"],
    template="Solve this math problem step by step: {question}",
)

word_problem_chain = LLMChain(llm=llm, prompt=math_assistant_prompt)

@cl.on_message
async def process_user_query(message: cl.Message):
    response = await word_problem_chain.ainvoke({"question": message.content})
    await cl.Message(content=response).send()
