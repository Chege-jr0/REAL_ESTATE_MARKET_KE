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

 ## Tech Stack
 Python - Core Programming Language
 FastAPI - Backend REST API
 Streamlit - Frontend Web Interface
 LangChain - RAG pipeline orchestration
 Ollama - Local AI model runner
 TinyLlama - Free Local AI model
 Plotly - Interactive data visualisations
 Pandas and Numpy - Data Processing and Generation


## How it Works
<img width="694" height="611" alt="Screenshot 2026-04-04 214856" src="https://github.com/user-attachments/assets/f756dd22-3453-4cb1-bd7f-a5f6b00656ee" />

1. data.py generates 144 rows of Kenya market data.

2. app.py loads data inot memory with @st.cache_data

3. User selects city and property type from sidebar

4. Charts, metrics and AI all update automatically.

5. AI generates insights via TinyLlama running locally

## The Three Charts
Every Chart waas chose to answer a specific investment question:
1. Price Trend Line: Shows Market trajectory and momentum

2. City Comparison: Enables direct city-by-cuty comparison

3. Rental Yield HeatMap - Identifies optimal city and propert type combinations.

## How the AI works
The dashboard builds a clean context dictionary from the current filtered state and passes it to TinyLlama

```python
context = {
     "avg_price": 15_234_500,
    "avg_rental_yield": 7.52,
    "avg_occupancy": 82.3,
    "total_transactions": 1842,
    "top_city": "Nairobi",
    "selected_city": "Mombasa",
    "selected_property": "Residential"
}
```

Important: All values are explicitly converted to plain Python Types float(), int(), str() before beingg passed to the AI. This prevents pandas dtype conflict that cause silent errors.

## What the AI Does
# Auto-generates investment insights:
"Commercial properties in Nairobi show the strongest price apprecation at 22% over the 3 year period, while Kisumu residential properties offer the highest rental yields at 8.9%, presenting an attractive income-focused investment opportunity"

## Project Structure
```markdown
kenya-realestate-dashboard/
├── data.py          # Market data generation & helper functions
├── ai_insights.py   # Ollama AI insights & Q&A engine
├── app.py           # Streamlit dashboard (charts + AI + filters)
└── requirements.txt
```

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

## Key Technical Concepts
@st.cache_data on data loading.

Without caching, generate_market_data() in data.py reruns every time a user changes a filter. Caching stores DataFrame in memory so filter changes are instant, no regeneration delay.

Direct prompting instead of RAG

Unlike a RAG app which uses vector search for large unstrucutured datasets, this dashboard passes a structured market summary directly into the AI prompt.The data is small and structured enough to fit in one prompt, no vector store needed. Simpler and faster.

temperature = 0 on the AI model

For financial and investment data we want strictly factual responses. temperature = 0 eliminates creativity and forces the AI to stick to what the data shows.

Price trend grouping

The price trend line chart groups data by quarter using.groupby("Quarter").mean() before plotting. Without this, mutiple rows per quarter create overlapping lines instead of one clean trend line.

## Related Articles
1. PART 1: How I built a RAG App That Talks to My CSV Files
  ```markdown
https://medium.com/@paulgikonyo100/retrieval-augmented-generation-assistant-that-enables-users-to-communicate-with-data-in-plain-41bf9e9d01e7
  ```
2. PART 2: From RAG App to Real Estate Dashboard
```markdown
https://medium.com/@paulgikonyo100/from-rag-app-to-real-estate-dashboard-how-i-built-ai-powered-real-estate-market-intelligence-3abd54ec2b07
```

## Author

Paul Gikonyo

Built as part of self - directed learning journey into AI engineering - combinin background in data analytics with modern AI development tools.


## License
MIT License (Anyone can use it)
