"""LangChain 新架构示例：Ollama(qwen2.5:7b) + PromptTemplate + LCEL 链。"""

import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


def main() -> None:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个简洁的技术讲师。"),
            ("human", "请解释 {topic}，并给出一个 Python 示例。"),
        ]
    )

    llm = ChatOllama(
        model=os.getenv("OLLAMA_MODEL", "qwen2.5:7b"),
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0.1,
    )

    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"topic": "LangChain Runnable 接口"})
    print(result)


if __name__ == "__main__":
    main()
