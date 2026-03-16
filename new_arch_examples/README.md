# LangChain 新架构双版本示例

本目录中的每个可运行示例都提供两份：
- `*_deepseek.py`：调用 DeepSeek（OpenAI 兼容接口）
- `*_ollama.py`：调用本地 Ollama `qwen2.5:7b`

## 文件说明

1. `01_basic_chat_deepseek.py` / `01_basic_chat_ollama.py`
   - 基础 `llm.invoke(...)` 对话调用
2. `02_prompt_chain_deepseek.py` / `02_prompt_chain_ollama.py`
   - 使用 `ChatPromptTemplate | model | StrOutputParser` 的 LCEL 链式写法

## 依赖

建议安装（新架构最小依赖）：

```bash
pip install -U langchain langchain-core langchain-openai langchain-ollama
```

## 运行

### DeepSeek

```bash
export DEEPSEEK_API_KEY="your_deepseek_key"
python new_arch_examples/01_basic_chat_deepseek.py
python new_arch_examples/02_prompt_chain_deepseek.py
```

### Ollama

```bash
ollama pull qwen2.5:7b
python new_arch_examples/01_basic_chat_ollama.py
python new_arch_examples/02_prompt_chain_ollama.py
```
