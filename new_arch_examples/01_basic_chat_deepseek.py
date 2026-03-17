"""LangChain 新架构示例：DeepSeek 基础对话。

运行前请设置：
- DEEPSEEK_API_KEY
可选：
- DEEPSEEK_BASE_URL（默认 https://api.deepseek.com）
- DEEPSEEK_MODEL（默认 deepseek-chat）
"""

import os

from langchain_openai import ChatOpenAI


def main() -> None:
    openai_api_key = os.getenv("DEEPSEEK_API_KEY")

    llm = ChatOpenAI(
        model="deepseek-chat",
        api_key=openai_api_key,
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        temperature=0.2,
    )

    response = llm.invoke("请用三句话介绍 LangChain 的 LCEL。")
    print(response.content)


if __name__ == "__main__":
    main()
