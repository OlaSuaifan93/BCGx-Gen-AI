from flask import Flask, render_template, request
import re

app = Flask(__name__)
financial_data={'total revenue_microsoft_2021': 'the total revenue in the company microsoft during 2021 is 168088 million dollars. the average growth rate is 12%',
 'total revenue_microsoft_2022': 'the total revenue in the company microsoft during 2022 is 198270 million dollars. the average growth rate is 12%',
 'total revenue_microsoft_2023': 'the total revenue in the company microsoft during 2023 is 211915 million dollars. the average growth rate is 12%',
 'total revenue_tesla_2021': 'the total revenue in the company tesla during 2021 is 53823 million dollars. the average growth rate is 35%',
 'total revenue_tesla_2022': 'the total revenue in the company tesla during 2022 is 81462 million dollars. the average growth rate is 35%',
 'total revenue_tesla_2023': 'the total revenue in the company tesla during 2023 is 96773 million dollars. the average growth rate is 35%',
 'total revenue_apple_2021': 'the total revenue in the company apple during 2021 is 365817 million dollars. the average growth rate is 2%',
 'total revenue_apple_2022': 'the total revenue in the company apple during 2022 is 394328 million dollars. the average growth rate is 2%',
 'total revenue_apple_2023': 'the total revenue in the company apple during 2023 is 383285 million dollars. the average growth rate is 2%',
 'net income_microsoft_2021': 'the net income in the company microsoft during 2021 is 61271 million dollars. the average growth rate is 9%',
 'net income_microsoft_2022': 'the net income in the company microsoft during 2022 is 72738 million dollars. the average growth rate is 9%',
 'net income_microsoft_2023': 'the net income in the company microsoft during 2023 is 72361 million dollars. the average growth rate is 9%',
 'net income_tesla_2021': 'the net income in the company tesla during 2021 is 5644 million dollars. the average growth rate is 71%',
 'net income_tesla_2022': 'the net income in the company tesla during 2022 is 12587 million dollars. the average growth rate is 71%',
 'net income_tesla_2023': 'the net income in the company tesla during 2023 is 14974 million dollars. the average growth rate is 71%',
 'net income_apple_2021': 'the net income in the company apple during 2021 is 94680 million dollars. the average growth rate is 1%',
 'net income_apple_2022': 'the net income in the company apple during 2022 is 99803 million dollars. the average growth rate is 1%',
 'net income_apple_2023': 'the net income in the company apple during 2023 is 96995 million dollars. the average growth rate is 1%',
 'total assets_microsoft_2021': 'the total assets in the company microsoft during 2021 is 333779 million dollars. the average growth rate is 11%',
 'total assets_microsoft_2022': 'the total assets in the company microsoft during 2022 is 364840 million dollars. the average growth rate is 11%',
 'total assets_microsoft_2023': 'the total assets in the company microsoft during 2023 is 411976 million dollars. the average growth rate is 11%',
 'total assets_tesla_2021': 'the total assets in the company tesla during 2021 is 62131 million dollars. the average growth rate is 31%',
 'total assets_tesla_2022': 'the total assets in the company tesla during 2022 is 82338 million dollars. the average growth rate is 31%',
 'total assets_tesla_2023': 'the total assets in the company tesla during 2023 is 106618 million dollars. the average growth rate is 31%',
 'total assets_apple_2021': 'the total assets in the company apple during 2021 is 351002 million dollars. the average growth rate is 0%',
 'total assets_apple_2022': 'the total assets in the company apple during 2022 is 352755 million dollars. the average growth rate is 0%',
 'total assets_apple_2023': 'the total assets in the company apple during 2023 is 352583 million dollars. the average growth rate is 0%',
 'total liabilities_microsoft_2021': 'the total liabilities in the company microsoft during 2021 is 191791 million dollars. the average growth rate is 4%',
 'total liabilities_microsoft_2022': 'the total liabilities in the company microsoft during 2022 is 198298 million dollars. the average growth rate is 4%',
 'total liabilities_microsoft_2023': 'the total liabilities in the company microsoft during 2023 is 205753 million dollars. the average growth rate is 4%',
 'total liabilities_tesla_2021': 'the total liabilities in the company tesla during 2021 is 30548 million dollars. the average growth rate is 19%',
 'total liabilities_tesla_2022': 'the total liabilities in the company tesla during 2022 is 36440 million dollars. the average growth rate is 19%',
 'total liabilities_tesla_2023': 'the total liabilities in the company tesla during 2023 is 43009 million dollars. the average growth rate is 19%',
 'total liabilities_apple_2021': 'the total liabilities in the company apple during 2021 is 287912 million dollars. the average growth rate is 1%',
 'total liabilities_apple_2022': 'the total liabilities in the company apple during 2022 is 302083 million dollars. the average growth rate is 1%',
 'total liabilities_apple_2023': 'the total liabilities in the company apple during 2023 is 290437 million dollars. the average growth rate is 1%',
 'cash flow from operating activities_microsoft_2021': 'the cash flow from operating activities in the company microsoft during 2021 is 76740 million dollars. the average growth rate is 7%',
 'cash flow from operating activities_microsoft_2022': 'the cash flow from operating activities in the company microsoft during 2022 is 89035 million dollars. the average growth rate is 7%',
 'cash flow from operating activities_microsoft_2023': 'the cash flow from operating activities in the company microsoft during 2023 is 87582 million dollars. the average growth rate is 7%',
 'cash flow from operating activities_tesla_2021': 'the cash flow from operating activities in the company tesla during 2021 is 11497 million dollars. the average growth rate is 9%',
 'cash flow from operating activities_tesla_2022': 'the cash flow from operating activities in the company tesla during 2022 is 14724 million dollars. the average growth rate is 9%',
 'cash flow from operating activities_tesla_2023': 'the cash flow from operating activities in the company tesla during 2023 is 13256 million dollars. the average growth rate is 9%',
 'cash flow from operating activities_apple_2021': 'the cash flow from operating activities in the company apple during 2021 is 104038 million dollars. the average growth rate is 4%',
 'cash flow from operating activities_apple_2022': 'the cash flow from operating activities in the company apple during 2022 is 122151 million dollars. the average growth rate is 4%',
 'cash flow from operating activities_apple_2023': 'the cash flow from operating activities in the company apple during 2023 is 110543 million dollars. the average growth rate is 4%'}
import re

def financial_chatbot2(user_query):
    user_query = user_query.lower()
    
    if "revenue" in user_query:
        # Check for specific companies
        if re.findall("microsoft", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'total revenue' in k and 'microsoft' in k])
        elif re.findall("apple", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'total revenue' in k and 'apple' in k])
        elif re.findall("tesla", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'total revenue' in k and 'tesla' in k])
        else:
            text = "No data found for the company mentioned."
        
    if "income" in user_query:
        # Check for specific companies
        if re.findall("microsoft", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'net income' in k and 'microsoft' in k])
        elif re.findall("apple", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'net income' in k and 'apple' in k])
        elif re.findall("tesla", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'net income' in k and 'tesla' in k])
        else:
            text = "No data found for the company mentioned."
         
    if "asset" in user_query:
        # Check for specific companies
        if re.findall("microsoft", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'total asset' in k and 'microsoft' in k])
        elif re.findall("apple", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'total asset' in k and 'apple' in k])
        elif re.findall("tesla", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'total asset' in k and 'tesla' in k])
        else:
            text = "No data found for the company mentioned."
        
    if "liabilities" in user_query:
        # Check for specific companies
        if re.findall("microsoft", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'total liabilities' in k and 'microsoft' in k])
        elif re.findall("apple", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'total liabilities' in k and 'apple' in k])
        elif re.findall("tesla", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'total liabilities' in k and 'tesla' in k])
        else:
            text = "No data found for the company mentioned."
       
    if "cash" in user_query:
        # Check for specific companies
        if re.findall("microsoft", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'cash' in k and 'microsoft' in k])
        elif re.findall("apple", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'cash' in k and 'apple' in k])
        elif re.findall("tesla", user_query):
            text = " ".join([v for k, v in financial_data.items() if 'cash' in k and 'tesla' in k])
        else:
            text = "No data found for the company mentioned."
       
        
        
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        user_query = request.form['query']
        response = financial_chatbot2(user_query)
    return render_template('index2.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)      