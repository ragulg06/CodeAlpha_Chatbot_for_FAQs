# Flight Booking FAQ Chatbot

A modern web-based chatbot interface for answering flight booking related questions. The chatbot provides a user-friendly interface with a floating chat icon that expands into a full chat window.

## Features

- Modern and responsive UI
- Floating chatbot icon
- Real-time chat interface
- Error handling and loading states
- Sample flight information display

## Prerequisites

- Python 3.12.3 or higher
- pip (Python package installer)
- Web browser (Chrome, Firefox, Safari, or Edge)

## Installation

1. Clone or download this repository to your local machine.
```bash
git clone https://github.com/ragulg06/CodeAlpha_Chatbot_for_FAQs.git
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - On Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application
1. Training the chatbot for answering FAQs:
````bash
python training.py
```` 

3. Start the chatbot server:
```bash
python chatbot_ui.py
```
This will start the Gradio server on http://127.0.0.1:7862

3. In a new terminal window, start the web server:
```bash
python -m http.server 8000
```
This will serve the web interface on http://localhost:8000

4. Open your web browser and navigate to:
```
http://localhost:8000
```

## Usage

1. The chatbot icon will appear in the bottom right corner of the webpage
2. Click the icon to open the chat interface
3. Type your questions about flight bookings
4. Click the icon again or the X button to close the chat window

## Troubleshooting

If you encounter any issues:

1. Make sure both servers are running (chatbot_ui.py and http.server)
2. Check that you're using the correct URLs:
   - Web interface: http://localhost:8000
   - Chatbot server: http://127.0.0.1:7862
3. Ensure all required packages are installed correctly
4. Check the terminal for any error messages

## Project Structure

```
FAQs ChatBot/
├── index.html          # Main webpage
├── style.css          # Styling for the webpage
├── chatbot_ui.py      # Chatbot server implementation
├── chatbot_png.png    # Chatbot icon image
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Dependencies

- gradio==4.19.2
- numpy==1.26.4
- pandas==2.2.1
- scikit-learn==1.4.1
- transformers==4.38.2
- torch==2.2.1
- python-dotenv==1.0.1
- requests==2.31.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.
