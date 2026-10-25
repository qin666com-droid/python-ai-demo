"""调用 DeepSeek 的命令行问答脚本。

用法：
    python main.py 什么是RAG
没配 API Key 时会自动进入离线演示模式，照样能跑。
"""
import os
import sys

MODEL = "deepseek-chat"
BASE_URL = "https://api.deepseek.com"


def load_env(path=".env"):
    """把 .env 里的 KEY=VALUE 读进环境变量（免装 python-dotenv）。"""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def ask(question: str) -> None:
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("[离线模式] 没有检测到 DEEPSEEK_API_KEY。")
        print("把 .env.example 复制成 .env 填上 key，再运行一次就会真的调用模型。\n")
        print(f"你问的是：{question}")
        return

    from openai import OpenAI

    client = OpenAI(api_key=api_key, base_url=BASE_URL)
    stream = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": question}],
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()


def main() -> None:
    load_env()
    question = " ".join(sys.argv[1:]) or "用一句话解释什么是 RAG"
    print(f"你问：{question}\n")
    ask(question)


if __name__ == "__main__":
    main()
