Financial Data Chatbot
Overview
The Financial Data Chatbot is a Flask-based web application designed to provide users with quick and accurate financial information about major companies like Microsoft, Apple, and Tesla. By utilizing predefined data sets, the chatbot can respond to specific queries regarding total revenue, net income, total assets, total liabilities, and cash flow from operating activities for different fiscal years.

Features
Natural Language Processing: The chatbot can process user queries written in natural language and extract relevant financial information based on specific keywords.
Predefined Queries: The chatbot is programmed to respond to a variety of financial queries, including:
Total revenue for specific companies and years
Net income for specific companies and years
Total assets for specific companies and years
Total liabilities for specific companies and years
Cash flow from operating activities for specific companies and years
Dynamic Responses: Depending on the user's query, the chatbot generates responses by aggregating relevant financial data and providing insights.
Technologies Used
Flask: A lightweight WSGI web application framework for Python.
HTML/CSS: For front-end web design.
Regular Expressions (re): For parsing and processing user queries.
Python: The primary programming language used for building the chatbot logic.
Getting Started
To set up the project locally, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/financial-data-chatbot.git
cd financial-data-chatbot
Install Requirements: Make sure you have Python and pip installed. Install the necessary packages:

bash
Copy code
pip install Flask
Run the Application: Start the Flask application:

bash
Copy code
python app.py
Access the Application: Open your web browser and navigate to http://127.0.0.1:5000/ to interact with the chatbot.

Limitations
The chatbot currently only understands a limited set of queries. More sophisticated natural language processing features can be added for enhanced understanding.
The responses are based on predefined financial data; thus, any updates to the financial information require manual updates to the dataset.
Future Enhancements
Implement a machine learning model for better understanding and response generation based on user queries.
Expand the dataset to include more companies and additional financial metrics.
Improve the user interface for a better user experience.
License
This project is licensed under the MIT License - see the LICENSE file for details.
