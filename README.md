# ✈️ AeroStay-AI: Multi-Agent Travel Planner 🏨

[![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](#)

AeroStay-AI is an intelligent, multi-agent travel planning platform that automates the orchestration of flight discovery, hotel options, and dynamic itinerary creation. Powered by Agentic AI (utilizing LangGraph/ReAct patterns) and built with a fast Python backend, it breaks down complex travel logistics into collaborative tasks handled by specialized AI agents.

The application is fully **containerized** via Docker and natively deployed as a live **web service on the Render platform**.

---

## 🚀 Features
*   **Multi-Agent Orchestration:** Specialized AI agents collaborate to handle distinct tasks (Flight analysis, Hotel curation, and Itinerary scheduling).
*   **Comprehensive Trip Planning:** Generates fully tailored end-to-end travel plans based on user preferences, budget, and destination.
*   **Production Ready & Cloud-Deployed:** Fully containerized with Docker and hosted on Render as a scalable web service.
*   **Modern Web UI:** A clean, intuitive frontend built to display rich, step-by-step travel plans.

---

## 🛠️ Tech Stack & Tools
*   **Backend:** FastAPI (Python 3.10+)
*   **AI Architecture:** Agentic Framework (LangGraph / ReAct pattern)
*   **LLM Integration:** Grok / External APIs
*   **Frontend:** HTML5, CSS3, JavaScript (Async Fetch API)
*   **Infrastructure:** Docker, Render (Web Service), PostgreSQL

---

## 📁 Project Folder Structure
```text
├── images/               # UI snapshots and demonstration assets
├── static/               # CSS, JS, and client-side assets
├── templates/            # HTML templates for the frontend UI
├── tools/                # Custom agent tools (APIs, web scrapers, data fetchers)
├── .dockerignore         # Docker build exclusions
├── .env.example          # Template for environment variables
├── .gitignore            # Git exclusion file
├── app.py                # Main application entry point (FastAPI)
├── backend.py            # Core Multi-Agent orchestration and LLM logic
├── Dockerfile            # Container build configuration
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── test.py               # Test suites for agents and tool execution
```

---

## ⚙️ Environment Configuration
Before running the project locally, you need to configure your environment variables.

Create a `.env` file in the root directory:
```bash
touch .env
```
Open the `.env` file and add your required API keys and endpoints:
```env
# LLM & Agent APIs
grok_api_key=your_grok_api_key_here
AVIATIONSTACK_API_KEY=your_aviationstack_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

# Database Configuration
DATABASE_URL= postgres database url from render

# LangSmith Tracing
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=AeroStay
```


> **💡 VS Code Tip:** If you see a warning stating "Terminal environment injection is disabled", open your VS Code settings (Ctrl + `,` or Cmd + `,`), search for `python.terminal.useEnvFile`, and check the box to enable automatic terminal environment loading.

---

## 🏃 How to Run the Application
You can spin up the application locally using Python or Docker.

### Option 1: Running Locally (Standard)
Install dependencies:
```bash
pip install -r requirements.txt
```
Launch the FastAPI server:
```bash
python app.py
```
Open your browser and navigate to `http://localhost:8000`.

### Option 2: Running via Docker 🐳
Because the application is containerized, you can run it identically to the production environment:

Build the Docker image:
```bash
docker build -t aerostay-ai .
```
Run the container:
```bash
docker run -p 8000:8000 --env-file .env aerostay-ai
```
Access the application at `http://localhost:8000`.

---

## ☁️ Deployment (Render Web Service)
This project is configured for seamless deployment on Render. It runs as a containerized Web Service.

1. Connect your GitHub repository to Render.
2. Create a new Web Service.
3. Select **Docker** as the runtime environment.
4. Render will automatically detect the `Dockerfile` and build the container.
5. Add your `.env` variables to the Render Environment Variables dashboard.
6. Deploy and access the live application via the provided Render URL.

---

## 📸 Output Snapshots
Here is a visual breakdown of the application interfaces generated during planning phases:

### User Interface Dashboard
The central hub where users input travel parameters, destination, and budget constraints.
*![images/frontend.png](<images/render hosted UI.png>)*



### Multi-Agent Itinerary Output
The final, systematically compiled flight schedules, hotel choices, and day-by-day itineraries.
*![Itinerary Output](<images/frontend.png>)*
*![Itinerary Output](<images/frontend2.png>)*

*![Langsmith Tracing](<images/langsmith_trace.png>)*
*![Langsmith Tracing](<images/langsmith_trace2.png>)*
