# RAG-Questions-Creator

Retrieval-Augmented Generation (RAG) based Question Creator and QA System using FAISS and LLMs.

## 📌 Overview

**RAG-Questions-Creator** is a smart system that leverages Retrieval-Augmented Generation (RAG) to automatically generate questions or answer them using external documents. It combines traditional information retrieval (IR) techniques with modern Large Language Models (LLMs), enabling dynamic interaction with unstructured data.

Key features include:

- 📂 FAISS-based document indexing and retrieval.
- 🧠 Integration with LLMs to generate or answer questions.
- 📜 PDF/text/document ingestion and chunking.
- 🔧 Minimal setup with a frontend interface.
- 💡 Support for interactive Q&A based on vector search.

---

## 📁 Project Structure

```bash
├── DataSets/                    # Datasets used for training or testing
├── Images/                      # Project screenshots or references
├── Notebook/
│   └── notebooke.ipynb          # Jupyter notebook for experimentation
├── QAsystem/
│   └── helper.py                # Helper functions for the QA system
├── faiss-index/
│   ├── index.faiss              # FAISS index file
│   ├── index.pkl                # Metadata or ID mapping for FAISS
├── frontend.py                  # Main entry point for the frontend interface
├── questionssayedali.pdf        # Source content used to generate questions
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variable template
├── LICENSE
├── README.md
└── temp.py                      # Temporary or test code
````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sayedalihassaan/RAG-Questions-Creator-main.git
cd RAG-Questions-Creator-main
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file based on `.env.example` and add your API keys and configuration:

```env
OPENAI_API_KEY=your_openai_api_key
```

### 5. Run the Frontend

```bash
python frontend.py
```

---

## 🧠 How It Works

1. **Indexing**: Documents are split into chunks and embedded using an LLM-based embedder (e.g., OpenAI embeddings), then indexed with FAISS.
2. **Retrieval**: Given a user question, relevant chunks are retrieved using similarity search.
3. **Generation**: The context is passed to an LLM to generate answers or new questions.

---

## 📸 Screenshots

![screenshot](Images/Screenshot%202025-04-14%20183555.png)

---

## 📚 Use Cases

* Automated question generation for exam preparation.
* Open-book question answering systems.
* Knowledge base assistants for custom datasets.

---

## ✅ TODO

* [ ] Add Streamlit or Gradio UI.
* [ ] Improve question generation templates.
* [ ] Extend support to other file formats (e.g., DOCX).
* [ ] Deploy as a web app using Docker or Hugging Face Spaces.

---

## 🧑‍💻 Author

**Sayed Ali Hassaan**
[GitHub Profile](https://github.com/Sayedalihassaan)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Star the Repo

If you found this project helpful, please give it a ⭐ on [GitHub](https://github.com/Sayedalihassaan/RAG-Questions-Creator-main)!

```

---

### ⚙️ Next Step

1. Copy the above content and paste it into your `README.md`.
2. Update any placeholders (like API keys or screenshot links) if needed.
3. You can add more screenshots or a demo video later under the “Screenshots” section.

Would you like help generating a simple logo or a `demo.gif` for it too?
```
