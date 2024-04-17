# KukhTea

## Overview

KukhTea is a Django-based web application that utilizes OpenAI's GPT-4 model for AI-driven conversation and product recommendation functionalities. Users can interact with the AI chatbot and explore various products listed in the catalog.

## Features

- **AI Chatbot:** Users can engage in conversation with the AI chatbot powered by OpenAI's GPT-4 model.
- **Product Recommendations:** Users can browse through a catalog of products and receive personalized recommendations.
- **User Authentication:** Secure user authentication system with sign-up, login, and logout functionalities.
- **User Collection:** Logged-in users can add products to their collection and manage their favorite items.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone [repository_url]
   cd [your_web_app_directory]

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Set Up OpenAI API Key:**
   Replace openai_api_key in views.py with your OpenAI API key.

4. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Start the Development Server:**
   ```bash
   python manage.py runserver

5. **Access the Web App:**
   Open your web browser and navigate to http://localhost:8000.


## Technologies Used

- **Django:** Python-based web framework for backend development.
- **OpenAI GPT-4:** AI model used for the chatbot functionality.
- **HTML/CSS/JavaScript:** Frontend technologies for user interface and interaction.
- **SQLite:** Default database engine provided by Django for data storage.

## Contributing

Contributions to [Your Web App Name] are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a new Pull Request.

## Contact

If you have any questions or suggestions regarding KukhTea, feel free to contact us at kux8800@gmail.com.

Thank you for using KukhTea!