from dotenv import load_dotenv
load_dotenv()
import os
from exa_py import Exa
exa = Exa(os.environ["EXA_API_KEY"])

result = exa.search(
  "perusahaan AI consultant di Indonesia",
  num_results=10,
  type="auto",
  contents={
    "highlights": True
  }
)

for hit in result.results:
    print(hit.title, hit.url)
    print(hit.highlights)

