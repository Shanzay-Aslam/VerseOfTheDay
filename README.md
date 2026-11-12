
# ☪ Verse of the Day – Quran Verse Application

## 1. Project Overview

Verse of the Day is a Python-based application that provides users with random verses from the Holy Quran.

The application retrieves Quranic verses through the AlQuran Cloud API and displays the original Arabic text along with English and Urdu translations.

The main purpose of this project is to make Quranic verses easily accessible while practicing Python programming, API integration, and graphical user interface development.

The application is available in two versions:
- Command-Line Interface (CLI)
- Graphical User Interface (GUI)

## 2. Project Objectives

The main objectives of this project are:

- To understand how APIs work.
- To retrieve real-time data using Python.
- To practice sending HTTP requests using the Requests library.
- To display Quranic verses in multiple languages.
- To develop a simple and user-friendly GUI.
- To improve Python programming and problem-solving skills.

## 3. Key Features

### Arabic Quran Verses
Displays the original Arabic text of randomly selected Quranic verses.

### English Translation
Provides an English translation to help users understand the meaning of each verse.

### Urdu Translation
Displays Urdu translations for Urdu-speaking users.

### Surah Information
Shows the English name of the Surah and the corresponding Ayah number.

### Random Verse Generator
Fetches a new random Quranic verse whenever the user selects the New Verse option.

### Command-Line Version
Allows users to access Quranic verses directly through the terminal.

### Graphical User Interface
Provides an attractive and simple interface with a dedicated verse display area and interactive button.

### Error Handling
Handles API connection problems and displays an error message if the request fails.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | GUI development |
| Requests | Sending HTTP requests |
| AlQuran Cloud API | Retrieving Quranic verses |
| VS Code | Development environment |

## 5. API Integration

This project uses the AlQuran Cloud API to retrieve Quranic data.

API Endpoint:

https://api.alquran.cloud/v1/ayah/random/editions/quran-uthmani,en.asad,ur.jalandhry

The API provides three editions:

- quran-uthmani – Arabic Quran text
- en.asad – English translation
- ur.jalandhry – Urdu translation

The application sends a GET request to the API and receives the response in JSON format.

Python processes the returned data and displays the verse and its information.

## 6. Project Structure

VerseOfTheDay/
│
├── main.py       # Command-line application
├── gui.py        # Graphical user interface
└── README.md     # Project documentation

## 7. Installation Requirements

Before running the application, make sure you have:

- Python installed on your computer.
- An active internet connection.
- Visual Studio Code or another Python editor.

Install the required Python library:

pip install requests

Note: Tkinter is included with most standard Windows Python installations.

## 8. How to Run the Project

### Run the Command-Line Version

Open the project folder in VS Code.

Open the terminal and execute:

python main.py

Select option 1 to get a new verse.

Select option 2 to exit the application.

### Run the GUI Version

Open the terminal and execute:

python gui.py

The application window will open and automatically display a Quranic verse.

Click the New Verse button to retrieve another random verse.

## 9. Error Handling

The application includes basic error handling to manage API connection issues.

If the internet connection is unavailable or the API request fails, the application displays an appropriate error message instead of stopping unexpectedly.


## 10. Learning Outcomes

Through this project, I gained practical experience in:

- Python programming fundamentals.
- Working with external APIs.
- Sending GET requests using Requests.
- Processing JSON responses.
- Using functions and loops.
- Implementing exception handling.
- Developing GUI applications with Tkinter.

## 11. Conclusion

Verse of the Day is a simple and useful Python application that combines Quranic content with practical programming concepts.

This project helped me understand API integration, data handling, and GUI development while building an application with real-world functionality.

## 12. Credits

Quranic data provided by:

AlQuran Cloud API  
https://alquran.cloud/
