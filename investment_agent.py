import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

# Page configuration
st.set_page_config(
    page_title="AI Investment Agent Pro 📈",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2e8b57;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin-bottom: 1rem;
    }
    .stock-positive {
        color: #2e8b57;
        font-weight: bold;
    }
    .stock-negative {
        color: #d62728;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 4px 4px 0px 0px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📊 AI Investment Analyst Pro</h1>', unsafe_allow_html=True)
st.caption("Advanced stock comparison and investment insights powered by AI")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # API Key Input with session state
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ""
    
    openai_api_key = st.text_input(
        "OpenAI API Key", 
        type="password",
        value=st.session_state.api_key,
        help="Enter your OpenAI API key to enable AI analysis"
    )
    
    if openai_api_key:
        st.session_state.api_key = openai_api_key
        st.success("✅ API Key configured")
    
    st.divider()
    
    # Analysis settings
    st.header("📊 Analysis Settings")
    
    time_period = st.select_slider(
        "Analysis Period",
        options=['1mo', '3mo', '6mo', '1y', '2y', '5y'],
        value='1y'
    )
    
    comparison_type = st.radio(
        "Comparison Type",
        ["Detailed Report", "Quick Comparison", "Technical Analysis"],
        index=0
    )
    
    include_metrics = st.multiselect(
        "Include Metrics",
        ["Price History", "Financial Ratios", "Analyst Ratings", "Company News", 
         "Risk Analysis", "Growth Metrics", "Dividend Info", "Market Sentiment"],
        default=["Price History", "Financial Ratios", "Analyst Ratings"]
    )
    
    st.divider()
    st.info("💡 **Tip**: For best results, use major stock symbols (e.g., AAPL, MSFT, GOOGL)")

# Initialize session states
if 'assistant' not in st.session_state:
    st.session_state.assistant = None
if 'analysis_history' not in st.session_state:
    st.session_state.analysis_history = []

# Main content area
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    stock1 = st.text_input(
        "🔵 First Stock Symbol",
        placeholder="e.g., AAPL",
        help="Enter the stock symbol (uppercase)"
    )

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### vs")

with col3:
    stock2 = st.text_input(
        "🟢 Second Stock Symbol",
        placeholder="e.g., MSFT",
        help="Enter the stock symbol (uppercase)"
    )

# Quick metrics display when stocks are entered
if stock1 or stock2:
    st.divider()
    
    # Create tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Quick Metrics", "📊 Detailed Analysis", "📉 Charts", "📋 History"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        if stock1:
            with col1:
                try:
                    ticker1 = yf.Ticker(stock1)
                    info1 = ticker1.info
                    
                    with st.container():
                        st.markdown(f"### {info1.get('longName', stock1)}")
                        st.markdown(f"**Symbol:** {stock1}")
                        
                        current_price = info1.get('currentPrice', info1.get('regularMarketPrice', 'N/A'))
                        previous_close = info1.get('previousClose', 'N/A')
                        
                        if isinstance(current_price, (int, float)) and isinstance(previous_close, (int, float)):
                            change = current_price - previous_close
                            change_percent = (change / previous_close) * 100
                            
                            st.metric(
                                label="Current Price",
                                value=f"${current_price:.2f}",
                                delta=f"{change:.2f} ({change_percent:.2f}%)"
                            )
                        else:
                            st.metric(label="Current Price", value="N/A")
                        
                        st.markdown(f"**Market Cap:** ${info1.get('marketCap', 'N/A'):,}")
                        st.markdown(f"**PE Ratio:** {info1.get('trailingPE', 'N/A'):.2f}")
                        st.markdown(f"**52W High:** ${info1.get('fiftyTwoWeekHigh', 'N/A'):.2f}")
                        st.markdown(f"**52W Low:** ${info1.get('fiftyTwoWeekLow', 'N/A'):.2f}")
                        
                except Exception as e:
                    st.error(f"Error fetching data for {stock1}: {str(e)}")
        
        if stock2:
            with col2:
                try:
                    ticker2 = yf.Ticker(stock2)
                    info2 = ticker2.info
                    
                    with st.container():
                        st.markdown(f"### {info2.get('longName', stock2)}")
                        st.markdown(f"**Symbol:** {stock2}")
                        
                        current_price = info2.get('currentPrice', info2.get('regularMarketPrice', 'N/A'))
                        previous_close = info2.get('previousClose', 'N/A')
                        
                        if isinstance(current_price, (int, float)) and isinstance(previous_close, (int, float)):
                            change = current_price - previous_close
                            change_percent = (change / previous_close) * 100
                            
                            st.metric(
                                label="Current Price",
                                value=f"${current_price:.2f}",
                                delta=f"{change:.2f} ({change_percent:.2f}%)"
                            )
                        else:
                            st.metric(label="Current Price", value="N/A")
                        
                        st.markdown(f"**Market Cap:** ${info2.get('marketCap', 'N/A'):,}")
                        st.markdown(f"**PE Ratio:** {info2.get('trailingPE', 'N/A'):.2f}")
                        st.markdown(f"**52W High:** ${info2.get('fiftyTwoWeekHigh', 'N/A'):.2f}")
                        st.markdown(f"**52W Low:** ${info2.get('fiftyTwoWeekLow', 'N/A'):.2f}")
                        
                except Exception as e:
                    st.error(f"Error fetching data for {stock2}: {str(e)}")
    
    with tab2:
        # Detailed analysis with AI
        if st.session_state.api_key and stock1 and stock2:
            if st.button("🔍 Generate Detailed AI Analysis", type="primary", use_container_width=True):
                with st.spinner(f"🧠 AI is analyzing {stock1} vs {stock2}..."):
                    try:
                        # Initialize agent if not already done
                        if st.session_state.assistant is None:
                            st.session_state.assistant = Agent(
                                model=OpenAIChat(id="gpt-4o", api_key=st.session_state.api_key),
                                tools=[
                                    YFinanceTools(
                                        stock_price=True,
                                        analyst_recommendations=True,
                                        stock_fundamentals=True,
                                        company_news=True,
                                        company_info=True
                                    )
                                ],
                                debug_mode=False,
                                description="""You are an expert investment analyst with deep knowledge of financial markets.
                                You provide objective, data-driven insights and always disclose limitations of your analysis.""",
                                instructions=[
                                    "Format your response using markdown with clear headings and sections.",
                                    "Use tables to compare metrics side by side.",
                                    "Include both quantitative data and qualitative insights.",
                                    "Highlight key differences and investment considerations.",
                                    "Always mention data sources and timeframes.",
                                    "Include risk factors and limitations in your analysis."
                                ],
                            )
                        
                        # Create detailed query based on selected metrics
                        query = f"""
                        Compare {stock1} and {stock2} comprehensively for an investor considering these options.
                        
                        Include analysis of:
                        1. Current valuation and price performance
                        2. Financial health and fundamentals
                        3. Growth prospects and future outlook
                        4. Risk factors and volatility
                        5. Analyst consensus and recommendations
                        6. Competitive positioning
                        7. Investment suitability for different investor profiles
                        
                        Period: {time_period}
                        Additional metrics requested: {', '.join(include_metrics)}
                        
                        Provide a structured report with clear recommendations.
                        """
                        
                        response: RunOutput = st.session_state.assistant.run(query, stream=False)
                        
                        # Store in history
                        analysis_entry = {
                            'timestamp': datetime.now(),
                            'stocks': [stock1, stock2],
                            'type': comparison_type,
                            'response': response.content[:500] + "..."
                        }
                        st.session_state.analysis_history.append(analysis_entry)
                        
                        # Display response
                        st.markdown(response.content)
                        
                        # Download option
                        st.download_button(
                            label="📥 Download Analysis Report",
                            data=response.content,
                            file_name=f"stock_analysis_{stock1}_vs_{stock2}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                            mime="text/markdown"
                        )
                        
                    except Exception as e:
                        st.error(f"Error during AI analysis: {str(e)}")
                        st.info("Please check your API key and try again.")
            else:
                st.info("👈 Enter both stock symbols and click the button above to generate AI analysis")
        
        elif not st.session_state.api_key:
            st.warning("🔑 Please enter your OpenAI API key in the sidebar to enable AI analysis")
        elif not (stock1 and stock2):
            st.info("📝 Please enter both stock symbols to generate analysis")
    
    with tab3:
        # Interactive charts
        if stock1 and stock2:
            st.markdown("### 📈 Historical Price Comparison")
            
            # Date range selector
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input("Start Date", value=datetime.now() - timedelta(days=365))
            with col2:
                end_date = st.date_input("End Date", value=datetime.now())
            
            if st.button("Generate Charts", type="secondary"):
                with st.spinner("Loading historical data..."):
                    try:
                        # Fetch historical data
                        data1 = yf.download(stock1, start=start_date, end=end_date, progress=False)
                        data2 = yf.download(stock2, start=start_date, end=end_date, progress=False)
                        
                        if not data1.empty and not data2.empty:
                            # Create interactive chart
                            fig = make_subplots(
                                rows=2, cols=1,
                                subplot_titles=(f'{stock1} Price History', f'{stock2} Price History'),
                                vertical_spacing=0.1
                            )
                            
                            fig.add_trace(
                                go.Candlestick(
                                    x=data1.index,
                                    open=data1['Open'],
                                    high=data1['High'],
                                    low=data1['Low'],
                                    close=data1['Close'],
                                    name=stock1
                                ),
                                row=1, col=1
                            )
                            
                            fig.add_trace(
                                go.Candlestick(
                                    x=data2.index,
                                    open=data2['Open'],
                                    high=data2['High'],
                                    low=data2['Low'],
                                    close=data2['Close'],
                                    name=stock2
                                ),
                                row=2, col=1
                            )
                            
                            fig.update_layout(
                                height=800,
                                showlegend=True,
                                xaxis_rangeslider_visible=False
                            )
                            
                            st.plotly_chart(fig, use_container_width=True)
                            
                            # Calculate and display returns
                            st.markdown("### 📊 Performance Metrics")
                            col1, col2, col3 = st.columns(3)
                            
                            with col1:
                                ret1 = ((data1['Close'][-1] / data1['Close'][0]) - 1) * 100
                                st.metric(f"{stock1} Return", f"{ret1:.2f}%")
                            
                            with col2:
                                ret2 = ((data2['Close'][-1] / data2['Close'][0]) - 1) * 100
                                st.metric(f"{stock2} Return", f"{ret2:.2f}%")
                            
                            with col3:
                                st.metric("Difference", f"{(ret1 - ret2):.2f}%")
                            
                        else:
                            st.error("Could not fetch historical data. Please check the stock symbols.")
                            
                    except Exception as e:
                        st.error(f"Error generating charts: {str(e)}")
    
    with tab4:
        # Analysis history
        st.markdown("### 📋 Analysis History")
        
        if st.session_state.analysis_history:
            for i, entry in enumerate(reversed(st.session_state.analysis_history[-5:]), 1):
                with st.expander(f"Analysis {i}: {entry['stocks'][0]} vs {entry['stocks'][1]} - {entry['timestamp'].strftime('%Y-%m-%d %H:%M')}"):
                    st.write(entry['response'])
                    st.caption(f"Type: {entry['type']}")
        else:
            st.info("No analysis history yet. Generate some reports to see them here!")

# Footer
st.divider()
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
        <p>⚠️ <strong>Disclaimer:</strong> This tool provides analysis for informational purposes only. 
        It is not financial advice. Always conduct your own research and consult with a qualified 
        financial advisor before making investment decisions.</p>
        <p>📊 Data provided by Yahoo Finance | 🤖 AI powered by OpenAI GPT-4o</p>
    </div>
    """,
    unsafe_allow_html=True
)