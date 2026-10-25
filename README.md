# python-ai-demo

一个调用 DeepSeek 的命令行问答脚本，支持环境变量管理密钥和流式输出。

## 技术栈

Python 3.14 · OpenAI SDK · DeepSeek API

## 怎么跑

1. `pip install -r requirements.txt`
2. 复制 `.env.example` 为 `.env`，填入你的 `DEEPSEEK_API_KEY`
3. `python main.py 什么是RAG`

没配 key 时会自动进入离线演示模式，不会报错。

## 效果

```
> python main.py 什么是RAG

你问：什么是RAG

RAG（检索增强生成）……
```

## 我踩过的坑

- 流式输出要 `stream=True`，然后逐块读 `chunk.choices[0].delta.content`，不能用 `message.content`。
- `.env` 必须写进 `.gitignore`，否则密钥会跟着提交一起公开。
- Windows 下 `python` 可能是 3.14，`py` 也可以；两个都试一下。
