from dotenv import load_dotenv
load_dotenv()
import os
from exa_py import Exa
exa = Exa(os.environ["EXA_API_KEY"])

run = exa.agent.runs.create(
    query=(
        "Analyze how the EU AI Act affects startups selling AI products in Europe. "
        "Cover key dates, obligations, and practical risks, citing official sources."
    ),
    effort="medium",
)

run = exa.agent.runs.poll_until_finished(run.id)

print(run.output.text if run.output else None)
