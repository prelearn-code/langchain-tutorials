"""LangChain 新架构示例：Ollama(qwen2.5:7b) 基础对话。

运行前请确保本地 Ollama 可用，并已拉取模型：
  ollama pull qwen2.5:7b
可选环境变量：
- OLLAMA_BASE_URL（默认 http://localhost:11434）
- OLLAMA_MODEL（默认 qwen2.5:7b）
"""

import os

from langchain_ollama import ChatOllama


def main() -> None:
    llm = ChatOllama(
        model=os.getenv("OLLAMA_MODEL", "qwen2.5:7b"),
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0.2,
    )

    response = llm.invoke("请用三句话介绍 LangChain 的 LCEL。")
    print(response.content)


if __name__ == "__main__":
    main()
