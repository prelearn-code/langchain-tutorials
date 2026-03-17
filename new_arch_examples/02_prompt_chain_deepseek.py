"""LangChain 新架构示例：DeepSeek + PromptTemplate + LCEL 链。

运行前请设置：
- DEEPSEEK_API_KEY
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

from langchain_openai import ChatOpenAI


def main() -> None:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个简洁的技术讲师。"),
            ("human", "请解释 {topic}，并给出一个 Python 示例。"),
        ]
    )

    openai_api_key = os.getenv("DEEPSEEK_API_KEY")

    llm = ChatOpenAI(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
        api_key=openai_api_key,
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        temperature=0.1,
    )

    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"topic": "LangChain Runnable 接口"})
    print(result)


if __name__ == "__main__":
    main()
