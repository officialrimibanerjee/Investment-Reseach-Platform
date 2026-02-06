# 📈 AI Investment Analyst Pro

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

An advanced AI-powered investment analysis tool that provides comprehensive stock comparison, technical analysis, and investment insights using real-time market data and GPT-4o intelligence.

## ✨ Features

### 📊 **Core Analysis**
- **Side-by-side Stock Comparison** – Compare any two stocks across multiple metrics
- **Real-time Market Data** – Current prices, volume, market cap, and more
- **Historical Performance** – Interactive charts with customizable time periods
- **AI-Powered Insights** – GPT-4o generated detailed investment reports

### 📈 **Advanced Features**
- **Interactive Charts** – Candlestick charts with technical indicators
- **Financial Metrics** – PE ratio, EPS, dividend yield, and fundamental analysis
- **Analyst Consensus** – Aggregated ratings and price targets
- **Risk Assessment** – Volatility analysis and risk metrics
- **Portfolio Context** – Analysis suitable for different investor profiles

### 🛠️ **User Experience**
- **Responsive Design** – Clean, professional interface with dark mode support
- **Export Capabilities** – Download reports in markdown format
- **Analysis History** – Track your previous comparisons
- **Customizable Settings** – Tailor analysis to your specific needs
- **Mobile-Friendly** – Optimized for all screen sizes

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (GPT-4o access)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
cd advanced_ai_agents/single_agent_apps/ai_investment_agent
```

2. **Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run investment_agent.py
```

The application will open in your default browser at `http://localhost:8501`

## 📁 Project Structure

```
ai_investment_agent/
├── investment_agent.py     # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # This documentation
└── .env.example           # Environment variables template
```

## 🔧 Configuration

### OpenAI API Key
1. Obtain an API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Enter the key in the sidebar of the application
3. The key is stored in session state (not persisted)

### Analysis Settings
- **Time Period**: Choose from 1 month to 5 years
- **Comparison Type**: Detailed Report, Quick Comparison, or Technical Analysis
- **Metrics**: Select which metrics to include in the analysis
- **Stock Symbols**: Enter valid stock symbols (e.g., AAPL, MSFT, GOOGL)

## 💻 Usage Guide

### Basic Comparison
1. Enter two stock symbols in the input fields
2. View quick metrics in the "Quick Metrics" tab
3. Click "Generate Detailed AI Analysis" for comprehensive insights
4. Explore interactive charts in the "Charts" tab

### Advanced Features
- **Custom Date Ranges**: Select specific start and end dates for historical analysis
- **Metric Selection**: Choose which financial metrics to include
- **Report Export**: Download analysis as markdown files
- **History Tracking**: Review previous analyses in the History tab

### Example Analysis
```python
# Sample stock comparisons:
- AAPL vs MSFT (Technology sector)
- JPM vs BAC (Banking sector)
- TSLA vs NIO (Electric vehicles)
- VOO vs QQQ (ETFs)
```

## 📊 Data Sources

- **Market Data**: Yahoo Finance API (via yfinance)
- **Company Information**: Real-time stock data and fundamentals
- **Analyst Data**: Ratings, price targets, and recommendations
- **News & Sentiment**: Latest company news and market sentiment

## 🔒 Security & Privacy

- **API Keys**: Stored locally in session state, not persisted
- **Data Handling**: All processing done client-side
- **No Data Storage**: Analysis history stored only in browser session
- **Open Source**: Transparent codebase for security review

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

**IMPORTANT: This tool is for informational purposes only.**

- Not financial advice
- Not a substitute for professional financial advice
- Past performance does not guarantee future results
- Always conduct your own research
- Consult with a qualified financial advisor before making investment decisions

The creators are not responsible for any investment decisions made based on this tool's analysis.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [OpenAI](https://openai.com/) for GPT-4o API
- [Yahoo Finance](https://finance.yahoo.com/) for market data
- [Agno](https://github.com/agno-agi/agno) for the agent framework
- All contributors and users of the project

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Shubhamsaboo/awesome-llm-apps/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Shubhamsaboo/awesome-llm-apps/discussions)
- **Documentation**: Check the Wiki for detailed guides

---

<div align="center">
  <p>Made by Rimi BANerjee </p>
  <p>
    <a href="https://github.com/Shubhamsaboo/awesome-llm-apps">GitHub</a> •
    <a href="https://streamlit.io/gallery">Streamlit Gallery</a> •
    <a href="https://openai.com">OpenAI</a>
  </p>
</div>
