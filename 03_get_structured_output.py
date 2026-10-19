from dotenv import load_dotenv
load_dotenv()
import os
from exa_py import Exa
exa = Exa(os.environ["EXA_API_KEY"])

result = exa.search(
    "Who is Braincore Indonesia's CEO, when was the company founded, and where is it headquartered?",
    type="deep",
    output_schema={
        "type": "object",
        "required": ["company", "ceo", "founded_year", "headquarters"],
        "properties": {
            "company": {"type": "string"},
            "ceo": {"type": "string"},
            "founded_year": {"type": "number"},
            "headquarters": {"type": "string"},
        },
    },
)

print(result.output.content)
