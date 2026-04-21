## Kenya Real Estate Market Dashboard
 An interactive market intelligence dashboard covering Kenya,s real estate market across 5 major cities(Nairobi, Mombasa, Kisumu, Nakuru and Eldoret). Powereed by a local AI model that generates investment insights and answers market questions on demand.


"Understanding where prices are moving, where yields are strongest and where opportunities exist, that is the first step forward smarter property investment in Kenya."

 I created a technical article to explain how the project works

 link: https://medium.com/@paulgikonyo100/from-rag-app-to-real-estate-dashboard-how-i-built-ai-powered-real-estate-market-intelligence-3abd54ec2b07

 ## What It Does
 An intercative dashboard that tracks Kenya's property market across 5 Major Cities from Quarter-1 2022 to Quarter-4 2024. Powered by TinyLlama running locxally via Ollama, no API key, no cloud costs and your data never leaves your machine.

# Key Capabilities
1. Track price trends across cities and property types over 12 quarters.

2. Compare current prices across all markets side by side

3. Identify the best rental yield opportunities via a colour-code heatmap

4. Generate AI Investment insights at the clickof a button

5. Ask any market question in plain English and get a data-backed answer.

6. Explore the raw data behind every chart with dynamic filters
## How It Works

 ## Tech Stack
 Python - Core Programming Language
 FastAPI - Backend REST API
 Streamlit - Frontend Web Interface
 LangChain - RAG pipeline orchestration
 Ollama - Local AI model runner
 TinyLlama - Free Local AI model
 Plotly - Interactive data visualisations
 Pandas and Numpy - Data Processing and Generation

 ## Prerequisites and Installation
 1. Install Python
 Download from python.org (Python 3.10 + recommended)

 2. Install Ollama
 Download from ollama.com and install it

 3. Pull the TinyLlama model
     ollama pull tinyllama

 4. Start Ollama
     ollama serve 

 5. Create a virtual environment
    python -m venv venv

 6. Install Libraries
   pip install requirements.txt

 7. Run the app
    streamlit run app.py

## How it Works
1. data.py generates 144 rows of Kenya market data.

2. app.py loads data inot memory with @st.cache_data

3. User selects city and property type from sidebar

4. Charts, metrics and AI all update automatically.

5. AI generates insights via TinyLlama running locally

## Project Structure

kenya-realestate-project/

├── data.py          # Market data generation & helper functions
|
├── ai_insights.py   # Ollama AI insights & Q&A engine
|
├── app.py           # Streamlit dashboard
|
└── requirements.txt

## Author

Paul Gikonyo

Built as part of self - directed learning journey into AI engineering - combinin background in data analytics with modern AI development tools.


## License
MIT License (Anyone can use it)
