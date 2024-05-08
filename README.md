# KukhTea
#### Video Demo:  <https://youtu.be/LmeN4IHxnho>

## Overview

The KukhTea web application is a Django-based platform that leverages OpenAI's GPT-4 model to provide users with AI-driven conversation and product recommendation functionalities. With KukhTea, users can engage in interactive conversations with an AI chatbot and explore a diverse catalog of products.

The application boasts several key features that enhance the user experience. Firstly, the AI chatbot powered by OpenAI's GPT-4 model allows users to have dynamic and engaging conversations. The chatbot is designed to provide intelligent responses and simulate human-like interactions, making it a valuable tool for users seeking information or assistance.

Additionally, KukhTea offers a comprehensive product recommendation system. Users can browse through a catalog of products and receive personalized recommendations based on their preferences and previous interactions. This feature enables users to discover new products that align with their interests and needs, enhancing their overall shopping experience.

To ensure secure access and personalized experiences, KukhTea incorporates a robust user authentication system. Users can create accounts, log in, and log out securely. This authentication system allows for personalized features such as user collections, where logged-in users can add products to their collection and manage their favorite items. This feature enables users to curate their own personalized catalog of products, making it easier to revisit and explore their preferred items.

Getting started with KukhTea is straightforward. Users can clone the repository and navigate to the project directory. By installing the required dependencies and setting up their OpenAI API key, users can quickly set up the application. Running the necessary migrations and starting the development server allows users to access the web app through their preferred web browser.

KukhTea utilizes a range of technologies to deliver its functionality. The Django web framework serves as the foundation for backend development, providing a robust and scalable platform. OpenAI's GPT-4 model powers the AI chatbot, ensuring intelligent and context-aware conversations. Frontend technologies such as HTML, CSS, and JavaScript are employed to create an intuitive and interactive user interface. The default SQLite database engine provided by Django handles data storage efficiently.

In conclusion, KukhTea is a powerful web application that combines AI-driven conversation capabilities with personalized product recommendations. With its user-friendly interface, secure authentication system, and collaborative development approach, KukhTea offers a comprehensive solution for users seeking intelligent conversations and curated product suggestions.

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
