from src.tools.tools import scrape_url, web_search


r = web_search.invoke({"query" : "what is the latest research on  using AI for climate change mitigation"})


print(r)