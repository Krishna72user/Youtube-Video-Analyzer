# 🎥 YouTube Video Analyzer (Agno + Streamlit)

An AI-powered app that analyzes YouTube videos using **Agno agents** and presents insights through an interactive **Streamlit** UI.

---

## 🚀 Features

* 🎬 Analyze any YouTube video via URL
* 🧠 AI-powered summarization of video content
* 🔑 Extract key points and insights
* ⚡ Fast inference using modern LLM APIs

---

## 🛠️ Tech Stack

* **Agno** – agent orchestration and tool usage
* **Streamlit** – web UI
* **Python** – backend logic
* **YouTubeTools(Agno)** – fetch and process video data

---

## 📂 Project Structure

```
├── app.py              # Streamlit UI
├── youtube_agent.py    # Agno agent
├── .gitignore
├── .env                # API keys
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/Krishna72user/Youtube-Video-Analyzer.git
cd Youtube-Video-Analyzer
```

2. Create a virtual environment:

```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User provides a YouTube video URL
2. Agno agent uses YouTube tools to extract video data/transcript
3. LLM processes the content
4. App returns:

   * Summary
   * Key insights
   * Answers to user questions

---

## 💡 Example Use Cases

* Quickly understand long videos
* Extract learning points from lectures/tutorials
* Analyze tech talks or ML videos

---

## 🔮 Future Improvements

* Timestamp-based summaries
* Sentiment analysis of videos
* Topic classification
* Save and load past analyses
* Deploy online (Streamlit Cloud)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📬 Contact

Created by **Krishna**

---
