# PrivateDocBot

PrivateDocBot is a Retrieval-Augmented Generation (RAG)-based AI-powered document assistant that enables intelligent search and question-answering over uploaded documents. The system utilizes **FAISS vector storage**, **sentence-transformers embeddings**, and **LLM models** like **Llama 2, Mistral**, and others for efficient retrieval and contextual responses.

This repository is fully containerized with **Docker**, allowing easy deployment with `docker-compose up --build`.

---

## 🚀 Features

- **Document Parsing & Chunking:** Automatically loads and splits PDFs into manageable chunks.
- **Vector Database with FAISS:** Efficient storage and retrieval of document embeddings.
- **Custom LLM Integration:** Supports models like **Llama 2, Mistral, and Sentence-Transformers**.
- **Streaming Token Responses:** Provides real-time token streaming for an interactive experience.
- **Fully Containerized Setup:** Quick deployment via Docker & Docker Compose.
- **Customizable QA Prompts:** Define your own templates for optimal performance.
- **Multi-threaded Performance Optimization:** Dynamically adjusts CPU usage.

---

## 📂 Project Directory Structure

```
PrivateDocBot
│── config/
│   ├── config.yml        # Configuration file (temp chunk vectorDB, max tokens, etc.)
│
│── data/                 # Directory for uploaded files
│
│── models/               # Stores models and embeddings
│   ├── sentence-transformers/
│   ├── llama-2-7b-chat.ggmlv3.q2_K.bin
│   ├── llama-2-7b-chat.ggmlv3.q8_0
│   ├── mistral-7b-openorca.Q4_K_M
│   ├── models.md         # Instructions on downloading and using models
│
│── public/               # Static assets
│   ├── logo/             # Logo files
│   ├── css/              # Stylesheets
│   ├── favicon/          # Favicon assets
│
│── src/                  # Main application logic
│   ├── loader.py         # Loads and processes documents
│   ├── model.py          # Handles embedding models and LLMs
│   ├── prompts.py        # Stores custom QA templates
│   ├── utils.py          # Utility functions (config loading, CPU core management)
│
│── vectorstore/          # FAISS database storage
│
│── main.py               # Chainlit-based entry point
│── app.py                # Main application script
│── requirements.txt      # Python dependencies
│── Dockerfile            # Docker container setup
│── docker-compose.yml    # Docker Compose setup for multi-container deployment
│── README.md             # This file
```

---

## ⚙️ Configuration (config/config.yml)

The **config.yml** file contains key settings such as:
- `DATA_PATH`: Location of uploaded documents.
- `CHUNK_SIZE`: Size of text chunks for embedding.
- `VECTOR_COUNT`: Number of retrieved documents per query.
- `MAX_NEW_TOKENS`: LLM response length control.
- `MODEL_BIN_DIR`: Path to stored LLM models.

---

## 🛠 Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/PrivateDocBot.git
cd PrivateDocBot
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Application**
#### **With Chainlit (for local development)**
```bash
chainlit run main.py -w
```
#### **With Docker (for production deployment)**
```bash
docker-compose up --build
```

---

## 🏗 How It Works

### **Document Processing Flow**
1. **Upload PDFs** → Stored in the `data/` folder.
2. **Load & Chunk** → `loader.py` reads PDFs, splits text into chunks.
3. **Embedding & Vector Storage** → Chunks are encoded using `sentence-transformers` and stored in FAISS.
4. **Query & Retrieval** → `model.py` fetches relevant chunks & passes them to the LLM.
5. **LLM Response** → The chatbot provides responses using streamed token generation.

---

## 📜 Key Components

### **🔹 `src/loader.py`**
- Loads PDF files from the `data/` directory.
- Splits text into chunks for vector embedding.
- Uses FAISS for vector storage.

### **🔹 `src/model.py`**
- Loads LLMs using `CTransformers`.
- Retrieves vectorized document chunks.
- Streams AI responses with real-time token updates.

### **🔹 `src/prompts.py`**
- Defines a **QA template** for retrieval-based AI responses.

### **🔹 `src/utils.py`**
- Determines optimal CPU threads.
- Loads configurations from `config.yml`.

---

## 🔥 Example Query
**User:** "What does the uploaded document say about AI in healthcare?"

**Bot Response:**
```
According to the document, AI in healthcare enables early diagnosis, improves patient outcomes, and enhances operational efficiency. [...] 
```

---

## 📦 Model Support

The `models/` directory includes multiple LLMs:
- **Llama 2** (`llama-2-7b-chat.ggmlv3.q8_0`)
- **Mistral 7B OpenOrca** (`mistral-7b-openorca.Q4_K_M`)
- **Sentence-Transformers** for embedding (`all-MiniLM-L6-v2`)

You can modify `config.yml` to use different models.

---

## 🐳 Running with Docker

For a fully containerized experience, simply run:
```bash
docker-compose up --build
```

This will:
1. Pull required dependencies.
2. Set up FAISS vector storage.
3. Load embeddings & models.
4. Start the PrivateDocBot service.

---

## 📜 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Pull requests are welcome! If you’d like to contribute:
1. Fork this repository.
2. Create a feature branch.
3. Submit a PR with clear descriptions.

---

## 📧 Contact
For any questions, feel free to reach out:
- **Email:** akber.anwer1234@gmail.com
- **GitHub:** [your-github-handle](https://github.com/akberanwer1234/private_doc_bot)
- **LinkedIn:** [your-github-handle](https://www.linkedin.com/in/muhammad-a-28b6511aa/)

---

🎉 **Happy Coding! 🚀**
