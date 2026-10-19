from dotenv import load_dotenv
load_dotenv()
import os
from exa_py import Exa
exa = Exa(os.environ["EXA_API_KEY"])

result = exa.get_contents(
    ["https://braincore.id/publication"],
    highlights={"query": "IEEE papers"},
)

print(result.results[0].highlights)
