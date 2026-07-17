from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

#res = tavily_search("best hotels in rishikesh, India")
#res = search_flights("give me flight between delhi and mumbai")

res = run_travel_agent("Create me a budget itenary plan for 6 days 7 nights from India to London")
print(res)