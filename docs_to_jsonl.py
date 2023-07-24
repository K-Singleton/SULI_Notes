# Here is an example of a line in the jsonl file
# {"text": "### Human: Hola### Assistant: \u00a1Hola! \u00bfEn qu\u00e9 puedo ayudarte hoy?"}
import json

def main():
    with open("../kb_sdk_docs/source/howtos/add_ui_elements.rst") as f:
        answer = f.read()
    question = "How do I add ui elements to KBase modules?"
    text = f'### Human: {question}### Assistant: {answer}'
    # dict(foo=100, bar=200)
    line = json.dumps(dict(text=text))
    print(line)
    with open("data.jsonl","w") as f:
        f.write(line)

if __name__ == "__main__":
    main()