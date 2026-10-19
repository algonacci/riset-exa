from dotenv import load_dotenv
load_dotenv()
import os
from exa_py import Exa
from openai import OpenAI
exa = Exa(os.environ["EXA_API_KEY"])
openai = OpenAI(
    base_url=os.environ["LLM_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
)


messages = [{"role": "user", "content": "What's the latest on AI chips?"}]

completion = openai.chat.completions.create(
    model=os.environ["LLM_MODEL"],
    messages=messages,
    tools=[exa.openai.web_search(), exa.openai.get_contents()],
)

message = completion.choices[0].message
messages.append(message)
messages += exa.openai.handle_tool_calls(message)

completion = openai.chat.completions.create(model=os.environ["LLM_MODEL"], messages=messages)

print(completion.choices[0].message.content)
