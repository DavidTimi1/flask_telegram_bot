# flask_telegram_bot
Simple telegram bot that gives ai responses built using flask

## Live Testing
Sample deployment of the bot live, visit: [Telegram Bot](https://t.me/beetcoin_bbot)


## Features
- Responds to user messages using AI-powered responses.
- Built with Flask for handling HTTP requests.
- Utilizes the Gemini API for AI responses.
- Leverages the `pyTelegramBotAPI` package for Telegram bot integration.

## Requirements
- Python 3.7 or higher
- Flask
- pyTelegramBotAPI

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/davidtimi1/flask_telegram_bot.git
    cd flask_telegram_bot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
1. Obtain a Telegram bot token by creating a bot through [BotFather](https://core.telegram.org/bots#botfather).
2. Obtain an API key for the Gemini API.
3. Create a `.env` file in the project root and add the following:
    ```
        TELEGRAM_BOT_TOKEN=your_telegram_bot_token
        GEMINI_API_KEY=your_gemini_api_key
    ```

## Usage
1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Set up a webhook for your Telegram bot:
    Use the following command to set the webhook URL:
    ```
    https://api.telegram.org/bot<your_bot_token>/setWebhook?url=<your_server_url>/webhook
    ```
    Replace `<your_bot_token>` with your Telegram bot token and `<your_server_url>` with the URL where your Flask app is hosted.

3. Interact with your bot on Telegram.

## Chat and File Storage
The bot stores chat messages and files as follows:

1. **Chat Messages**:
    - **Chat Messages**:
        - User messages and bot responses are converted to a serializable form and stored in JSON format in the `chats/` directory.
        - Persistent storage of chat history is not implemented by default but can be added using a database like SQLite or MongoDB.

2. **File Storage**:
    - Files sent by users are temporarily stored in a `files` directory on the server.
    - These files are retained only for a short duration to be used as input for the AI model.
    - After processing, the files are either deleted or can be configured for further handling based on your requirements.

To implement persistent storage, you can modify the code to integrate a database or cloud storage solution.

## Project Structure
```
flask_telegram_bot/
├── app.py               # Main Flask application
├── bot.py               # Telegram bot logic
├── gemini_api.py        # Gemini API integration
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── README.md            # Project documentation
```


## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes and push to your fork:
    ```bash
    git commit -m "Add feature-name"
    git push origin feature-name
    ```
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Flask](https://flask.palletsprojects.com/)
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [Gemini API](https://example.com/gemini-api-docs)
- BotFather for Telegram bot creation
- OpenAI for AI inspiration