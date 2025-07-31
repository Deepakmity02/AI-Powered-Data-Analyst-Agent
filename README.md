# AI-Powered-Data-Analyst-Agent

This project is an interactive **Streamlit web app** that acts as an AI-powered data analyst. It leverages **LLaMA-based LLMs** (via Together API) to analyze and visualize datasets through natural language queries.

## 🚀 Features

- Upload a CSV dataset and get automated insights
- Ask natural language questions about your data
- Powered by LLaMA via Together API
- Auto-generate charts and summaries
- Supports reading tables from PDFs and images using OCR
- Demo dataset: `metadata.csv` (battery test metadata)

## 🗂️ Dataset Used

The included sample dataset (`metadata.csv`) contains metadata associated with battery testing. It includes:
- Battery type
- Testing conditions
- Environmental factors

## 🏗️ Architecture

User → Streamlit App → Together LLaMA API → Model Response → Display Output  
             ↑  
    pandas / seaborn / matplotlib (Data Analysis & Visualization)

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Deepakmity02/AI-Powered-Data-Analyst-Agent.git
cd AI-Powered-Data-Analyst-Agent

**2. Install Dependencies**
pip install -r requirements.txt

###3. Set your API Key
together.api_key = "tgp_v1_OtkB6oDYcGvbnScheGQXnuALP9bklewZ4SCm5iXrOJ4"

###4. Run the Streamlit App
streamlit run app.py


📁 File Structure
📦 AI Powered Data Analyst Agent
├── app.py                  # Streamlit app
├── requirements.txt        # Python dependencies
├── metadata.csv            # Sample dataset
└── README.md               # Project documentation

🤖 Future Enhancements
Add chat history/memory for previous questions

Support multiple datasets

Export analysis as PDF/Word reports

Toggle between different LLMs (GPT, Claude, etc.)

🪪 License
This project is licensed under the MIT License.

👤 Author
Made with ❤️ by [Nalla Sai Deepak]
For AI Agent assignment / personal learning project










