# AI-Code-Reviewer

## Overview
AI-Code-Reviewer is a web application designed to provide AI-based code reviews. By leveraging the capabilities of Google's Generative AI, this tool offers detailed feedback on code structure, readability, potential bugs, and suggestions for improvement. The application is built using Streamlit, making it easy to deploy and use as a web app.

## Features
*AI-Powered Code Review:* Utilizes Google's Generative AI to analyze and review code.
*User-Friendly Interface:* Built with Streamlit for a simple and intuitive user experience.
*Detailed Feedback:* Provides comprehensive reviews including suggestions for improvement.

## Installation
### 1.Clone the Repository:
```ruby
git clone https://github.com/yourusername/AI-Code-Reviewer.git
cd AI-Code-Reviewer
```
### 2. Set Up Environment:
- Ensure you have Python installed (preferably Python 3.7 or higher).
- Install the required packages
```ruby
pip install -r requirements.txt
```
### Environment Variables:
- Create a .env file in the root directory.
- Add your Google API key to the .env file:
```ruby
  GOOGLE_API_KEY=your_google_api_key_here
```

## Usage
### 1. Run the Application:
```ruby
streamlit run ai_bot_reviewer.py
```
### 2. Interact with the App:

- Open your web browser and go to the local URL provided by Streamlit.
-Paste your code into the text area and click "Review Code" to receive feedback.

## How It Works
- The application initializes a language model using the ChatGoogleGenerativeAI class with the specified model and temperature settings.
- A system message is created to instruct the model to act as an expert code reviewer.
- The user's code is sent as a human message to the model.
- The model processes the input and returns a detailed review, which is then displayed in the Streamlit app.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
Thanks to the developers of Streamlit for providing an easy-to-use framework for building web applications.
Special thanks to Google's Generative AI team for their powerful language model capabilities.

