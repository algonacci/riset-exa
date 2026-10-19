import json
from dotenv import load_dotenv
load_dotenv()
import os
from exa_py import Exa
exa = Exa(os.environ["EXA_API_KEY"])

run = exa.agent.runs.create(
    query="Find 10 AI consultant companies in Indonesia.",
    output_schema={
        "type": "object",
        "required": ["companies"],
        "properties": {
            "companies": {
                "type": "array",
                "maxItems": 10,
                "items": {
                    "type": "object",
                    "required": ["name", "website"],
                    "properties": {
                        "name": {"type": "string"},
                        "website": {"type": "string", "format": "uri"},
                    },
                },
            }
        },
    },
    effort="auto",
)

run = exa.agent.runs.poll_until_finished(run.id)

print(json.dumps(run.output.structured if run.output else None, indent=2))
