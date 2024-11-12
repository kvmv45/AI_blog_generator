**AI Blog Content Generator**

**Overview**

The AI Blog Content Generator is a Streamlit application designed to assist users in generating creative blog titles and high-quality blog content. By leveraging the Hugging Face API and Langchain, this app allows users to input a topic and receive title suggestions, as well as generate comprehensive blog posts tailored to specific keywords and desired lengths.

**Features**

**Title Generation:** Suggests ten creative titles based on the user's input topic.
**Blog Content Creation:** Generates informative and engaging blog posts based on the selected title, keywords, and length.
**User-Friendly Interface:** Built with Streamlit, providing an intuitive web interface for easy interaction.

**Requirements**

To run this application, ensure you have the following installed:
Python 3.7 or higher
Streamlit
Langchain
Hugging Face Transformers

You can install the required packages using pip:

pip install streamlit langchain transformers

**Setup Instructions**

**Clone the Repository:**

git clone https://github.com/kvmv45/ai-blog-content-generator.git
cd ai-blog-content-generator

**Set Up Environment Variables:**
Create a file named api_key.py in the root directory of your project and add your Hugging Face API key:
python
hugging_face_api_key = "YOUR_HUGGING_FACE_API_KEY"

**Run the Application:**
Start the Streamlit application with the following command:
bash
streamlit run app.py

**Access the App:**
Open your web browser and navigate to **http://localhost:8501** to access the AI Blog Content Generator.
**How It Works**
The application utilizes the Hugging Face API to access language models for generating text.
Two main prompt templates are defined:
One for generating title suggestions based on a given topic.
Another for creating blog content based on a selected title, keywords, and desired length.
User inputs are collected through Streamlit's interactive components, allowing for dynamic content generation.
