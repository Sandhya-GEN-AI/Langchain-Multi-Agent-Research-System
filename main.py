from src.tools.tools import web_search
from src.tools.tools import scrape_url

results = scrape_url.run("https://www.reddit.com/r/artificial/")
print(results)