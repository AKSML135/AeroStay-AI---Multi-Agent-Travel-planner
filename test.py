from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

#res = tavily_search("best hotels in rishikesh, India")
res = search_flights("give me flight between delhi and mumbai")
print(res)