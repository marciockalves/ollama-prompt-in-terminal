## 🧠 About the Application

The `main.py` script is a specialized AI Assistant built with **LangChain**. Here is how it works:

* **Config Driven**: It reads settings from environment variables (`.env`) for easy switching between models.
* **Persona-Based**: Uses a custom `ChatPromptTemplate` to focus the AI's expertise on Python and Machine Learning.
* **Chain Execution**: Implements a LangChain pipeline (`prompt | llm`) to process user queries efficiently.
* **Resilient**: Includes basic error handling and an interactive CLI loop for real-time testing.


## 🛠️ Makefile Commands

This project uses a `Makefile` to automate the setup and management of the Ollama container and AI models.

### Available Commands

| Command | Description |
| :--- | :--- |
| `make setup` | **Initial Setup**: Starts the Docker containers in detached mode, waits for the service to stabilize, and pulls all required models. |
| `make stop-setup` | **Teardown**: Stops and removes the Docker containers. |
| `make pull-all` | **Download All Models**: Executes the pull command for both DeepSeek and Llama models inside the container. |
| `make pull-deepseek` | **Download DeepSeek**: Specifically pulls the `deepseek-r1:8b` model. |
| `make pull-llama` | **Download Llama**: Specifically pulls the `llama3.1` model. |
| `make status` | **Check Models**: Lists all models currently available and downloaded in the Ollama container. |
| `make run` | **Execute App**: Runs the `main.py` script using the `uv` Python package manager. |

---

### 🚀 How to Use

1. **First time setup**:
   ```bash
   make setup