## REAL ESTATE KENYA MARKETS
 An interactive market intelligemce dashboard covering Kenya,s real estate market across 5 major cities(Nairobi, Mombasa, Kisumu, Nakuru and Eldoret). Powereed by a local AI model that generates investment insights and answers market questions on demand.


 I will create a frontend dashaboard using streamlit and the backend will powered by Ollama AI to generate market insights based on the data insights generated.

 I created a technical article to expalin how the project works

 link: https://medium.com/@paulgikonyo100/from-rag-app-to-real-estate-dashboard-how-i-built-ai-powered-real-estate-market-intelligence-3abd54ec2b07

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
├── ai_insights.py   # Ollama AI insights & Q&A engine
├── app.py           # Streamlit dashboard
└── requirements.txt

## Author

Paul Gikonyo

Built as part of self - directed learning journey into AI engineering - combinin background in data analytics with modern AI development tools.


## License
MIT License (Anyone can use it)
