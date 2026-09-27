# 🏠 Room Vision AI

Room Vision AI is an AI-powered application that uses computer vision and generative AI to analyse images of rooms and provide intelligent insights based on the visual information detected in the image.

## 📌 Project Overview

Room Vision AI combines **Python, Generative AI, and image analysis** to create an interactive tool that can understand the visual characteristics of a room.

The project is designed to explore how AI can be applied to real-world visual analysis and provide useful, natural-language insights from an uploaded room image.

## ✨ Features

* 📷 Upload and analyse room images
* 🤖 AI-powered image understanding
* 🧠 Generative AI-based analysis
* 💬 Natural-language responses
* 🔍 Identification of visible room elements and characteristics
* ⚡ Interactive user experience
* 🐍 Built using Python

## 🛠️ Technologies Used

* **Python**
* **Generative AI / Gemini API**
* **Computer Vision**
* **Streamlit**
* **Pillow (PIL)**
* **Python-dotenv**

## 🔄 How It Works

The application follows a simple workflow:

```text
User uploads a room image
        ↓
Image is processed by the application
        ↓
Image is sent to the AI model
        ↓
AI analyses the visual information
        ↓
Results are presented to the user
```

## 🚀 Getting Started

### Prerequisites

Make sure you have:

* Python 3.10 or later
* A Gemini API key
* Git installed on your system

### Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/room-vision-ai.git
```

Move into the project directory:

```bash
cd room-vision-ai
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 API Key Configuration

Create a `.env` file in the project directory:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key.

**Important:** Never upload your actual API key or `.env` file to GitHub.

## ▶️ Running the Application

If the application is built using Streamlit, run:

```bash
streamlit run app.py
```

The application will open in your browser.

## 📸 Example

Upload an image of a room and allow the application to analyse its visual features using AI.

The application can then generate an AI-based response describing the room and providing relevant insights.

## 📂 Project Structure

```text
room-vision-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
└── assets/
    └── sample_images/
```

## 🎯 Learning Objectives

This project was developed to gain practical experience with:

* Generative AI applications
* AI-powered image analysis
* Python programming
* API integration
* Prompt engineering
* Streamlit application development
* Environment-variable management
* Git and GitHub

## 🔮 Future Improvements

Possible future enhancements include:

* Room object detection
* Furniture identification
* Interior design recommendations
* Colour and lighting analysis
* Room-type classification
* AI-generated improvement suggestions
* Image comparison
* Personalised interior design recommendations
* Web deployment

## 👩‍💻 Author

**Bhumi Saini**

M.A. Economics | Data Analytics & AI Enthusiast


This project is intended for educational and portfolio purposes.
