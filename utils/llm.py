# utils/llm.py
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 전역 LLM 인스턴스 (deepseek-coder-v2:16b 사용)
llm = Ollama(model="deepseek-coder-v2:16b")

def call_llm(prompt: str) -> str:
    template = PromptTemplate(
        input_variables=["input"],
        template="{input}"
    )
    chain = LLMChain(llm=llm, prompt=template)
    return chain.invoke({"input": prompt})
