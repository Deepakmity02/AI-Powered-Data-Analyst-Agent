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
git clone https://github.com/your-username/ai-data-analyst-agent.git
cd ai-data-analyst-agent
