
# 🥗 AI Health Assistant

An AI-powered **Health and Nutrition Assistant** built with **Python, Streamlit, RAG, FAISS, LangChain, and LLMs**.

The application provides personalized health calculations, diet recommendations, and an AI-based health and nutrition chatbot. Users can enter their personal information such as age, gender, height, weight, activity level, fitness aim, diet type, and allergies.

---

## 🚀 Features

### 📊 Health Calculations

The application calculates:

* **BMI (Body Mass Index)**
* **BMR (Basal Metabolic Rate)**
* **TDEE (Total Daily Energy Expenditure)**
* **Daily Calorie Target**

The calorie target changes according to the user's goal:

* Weight Maintenance
* Weight Loss
* Weight Gain

The application uses activity-level factors to calculate TDEE.

---

### 🍽️ AI Diet Recommendation

The application generates a personalized **one-day diet plan** based on:

* Age
* Gender
* Height
* Weight
* Activity Level
* Fitness Goal
* Diet Type
* Food Allergies
* BMI
* BMR
* TDEE
* Daily calorie target

The generated plan includes:

1. Breakfast
2. Morning Snack
3. Lunch
4. Evening Snack
5. Dinner

For each meal, the AI provides:

* Food
* Portion
* Approximate calories
* Approximate protein

---

### 🤖 AI Health Assistant

Users can ask health and nutrition-related questions through the chatbot.

The assistant retrieves relevant information from the nutrition knowledge base before generating an answer. It is designed to provide beginner-friendly explanations and avoid inventing medical facts.

---

## 🧠 RAG Architecture

The project uses **Retrieval-Augmented Generation (RAG)** to provide nutrition information to the AI.

### RAG Pipeline

```text
Nutrition PDF
     ↓
PDF Loader
     ↓
Text Splitting
     ↓
Hugging Face Embeddings
     ↓
FAISS Vector Database
     ↓
Similarity Search
     ↓
Relevant Nutrition Context
     ↓
LLM
     ↓
AI Response
```

The nutrition PDF is loaded using `PyPDFLoader`, split into chunks using `RecursiveCharacterTextSplitter`, converted into embeddings using `all-MiniLM-L6-v2`, and stored in a FAISS vector database.

When the application receives a question, it performs similarity search and retrieves the three most relevant documents before sending the context to the LLM.

---

## 🛠️ Tech Stack

| Technology              | Purpose                         |
| ----------------------- | ------------------------------- |
| Python                  | Core programming language       |
| Streamlit               | Web application interface       |
| LangChain               | RAG pipeline                    |
| FAISS                   | Vector database                 |
| Hugging Face Embeddings | Text embeddings                 |
| Sentence Transformers   | Embedding model                 |
| OpenAI-compatible API   | LLM interaction                 |
| PyPDF                   | PDF processing                  |
| python-dotenv           | Environment variable management |

Project dependencies are listed in `requirements.txt`.

---

## 📁 Project Structure

```text
AI-Health-Assistant/
│
├── app.py
├── diet.py
├── rag.py
├── create_database.py
├── llm_test.py
├── prompt.md
├── requirements.txt
│
├── data/
│   └── nutrition.pdf
│
├── vector_db/
│   └── FAISS vector database files
│
└── README.md
```

### File Description

**`app.py`**
Main Streamlit application containing the user interface, health calculations, diet recommendation system, and AI health assistant.

**`diet.py`**
Contains the BMI, BMR, TDEE, and calorie-target calculation functions.

**`rag.py`**
Creates and loads the FAISS-based nutrition knowledge database.

**`create_database.py`**
Runs the RAG database creation process.

**`llm_test.py`**
Used to test the LLM API connection and generate a sample nutrition response.

---

## ⚙️ Installation


### 1. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file:

```text
hf_token=YOUR_HUGGINGFACE_TOKEN
```

The application loads the token from the environment and uses the Hugging Face router through an OpenAI-compatible client.

**Do not upload your `.env` file or API key to GitHub.**

---

## 🧠 Create the RAG Database

Make sure the nutrition PDF is available at:

```text
data/nutrition.pdf
```

Then run:

```bash
python create_database.py
```

This creates the FAISS vector database used by the application.

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 How It Works

### Step 1 — User Information

The user provides:

```text
Gender
Age
Weight
Height
Activity Level
Fitness Goal
Diet Type
Allergies
```

### Step 2 — Health Metrics

The application calculates:

```text
BMI
BMR
TDEE
Calorie Target
```

### Step 3 — Retrieve Knowledge

The user's diet requirements or health question is converted into a search query.

The RAG system retrieves relevant information from the nutrition knowledge base.

### Step 4 — AI Generation

The retrieved information is provided to the LLM along with the user's information or question.

### Step 5 — Response

The application displays:

* Personalized diet recommendation
* Nutrition information
* Health and nutrition answers

---

## 🔐 Safety & Limitations

This application is designed for **general wellness and educational purposes**.

It does **not**:

* Diagnose diseases
* Prescribe medicines
* Claim to cure diseases
* Replace professional medical advice

For serious medical concerns, users are instructed to consult a qualified healthcare professional.

---

## 🎯 Project Objective

The objective of this project is to demonstrate how **AI, LLMs, RAG, vector databases, and Python** can be combined to create an interactive health and nutrition assistant.

---

## 🔮 Future Improvements

Possible future enhancements include:

* 🏃 Exercise recommendations
* 📈 Progress tracking
* 🥘 Larger food and nutrition database
* 📅 Weekly meal planning
* 🔐 User authentication
* 💾 User profile storage
* 📱 Mobile-friendly interface
* 🩺 Integration with verified healthcare datasets
* 📊 Nutrition and fitness analytics dashboard

---

## 👩‍💻 Author

**Somya Sharma**

Aspiring Data Analyst | Python | SQL | Power BI | AI & Data Analytics

---

⭐ If you find this project useful, consider giving the repository a star!
