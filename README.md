# Verse of the Day

A Python application that fetches random Quranic verses and displays them in Arabic, English, and Urdu using the AlQuran Cloud API.

## Project Overview

Verse of the Day is a beginner-friendly Python project that allows users to explore random Quranic verses with translations in three languages.

The project includes two versions:
- **Command-Line Interface (CLI):** Displays verses through the terminal.
- **Graphical User Interface (GUI):** Displays verses in a simple and user-friendly desktop application.

## Project Objectives

- Learn how to work with a public API using Python.
- Understand how to send HTTP requests using the Requests library.
- Display JSON data in Python.
- Handle API and internet connection errors.
- Build a desktop application using Tkinter.

## Features

- Fetches random Quranic verses from a live API.
- Displays Arabic text.
- Provides English translation.
- Provides Urdu translation.
- Shows Surah name and Ayah number.
- Allows users to fetch a new verse.
- Includes a copy verse feature in the GUI.
- Provides error handling for connection and API problems.
- Offers both CLI and GUI versions.

## Technologies Used

- **Programming Language:** Python
- **API:** AlQuran Cloud API
- **Library:** Requests
- **GUI Framework:** Tkinter
- **Version Control:** Git and GitHub
- **Code Editor:** Visual Studio Code

## API Integration

This project uses the AlQuran Cloud API to retrieve random Quranic verses.

**API Endpoint:**

https://api.alquran.cloud/v1/ayah/random/editions/quran-uthmani,en.asad,ur.jalandhry

The API provides:
- Quranic Arabic text
- English translation
- Urdu translation
- Surah name
- Ayah number

## Project Structure

```text
VerseOfTheDay/
│
├── main.py
├── gui.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Follow these steps to run the project on your computer.

### Step 1: Clone the Repository

```bash
git clone https://github.com/Shanzay-Aslam/VerseOfTheDay.git
```

### Step 2: Open the Project Folder

```bash
cd VerseOfTheDay
```

### Step 3: Install Required Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the Command-Line Version

```bash
python main.py
```

### Step 5: Run the GUI Version

```bash
python gui.py
```

## How to Use

### Command-Line Version

1. Run `main.py`.
2. Select option 1 to get a new verse.
3. The application displays the verse in Arabic, English, and Urdu.
4. Select option 2 to exit the application.

### Graphical User Interface

1. Run `gui.py`.
2. Click the **New Verse** button.
3. The application displays a random Quranic verse with its translations.
4. Click **Copy Verse** to copy the displayed verse.
5. Click **Exit** to close the application.

## Sample Output
===== VERSE OF THE DAY =====
1. Get a New Verse
2. Exit

Enter your choice: 1

Arabic:
إِلَّا مَنِ ٱسْتَرَقَ ٱلسَّمْعَ فَأَتْبَعَهُۥ شِهَابٌۭ مُّبِينٌۭ

English:
so that anyone who seeks to learn [the unknowable] by stealth is pursued by a flame clear to see.

Urdu:
ہاں اگر کوئی چوری سے سننا چاہے تو چمکتا ہوا انگارہ اس کے پیچھے لپکتا ہے

Surah: Al-Hijr
Ayah Number: 18

===== VERSE OF THE DAY =====
1. Get a New Verse
2. Exit

Enter your choice: 2
Thank you for using Verse of the Day!

*Note: The actual verse, translations, Surah name, and Ayah number are retrieved randomly from the API.*

## Error Handling

The application includes basic error handling to manage:

- Internet connection problems.
- API request failures.
- Invalid or incomplete API responses.
- Unexpected data formats.

If a connection or API problem occurs, the application displays an appropriate error message.

## Commit History

This project was developed through five meaningful Git commits to track the development process and improvements.

1. **Initial commit:** Create Verse of the Day project.
2. **Add project dependencies:** Add the requirements file.
3. **Improve API response validation and error handling:** Make API handling more reliable.
4. **Add exit button to GUI application:** Add an exit option to the graphical interface.
5. **Add copy verse feature to GUI:** Allow users to copy the displayed verse.

## Learning Outcomes

Through this project, I learned:

- How to use a public API in Python.
- How to send GET requests using the Requests library.
- How to process JSON responses.
- How to use exception handling.
- How to create a desktop GUI using Tkinter.
- How to use Git and GitHub for project version control.

## Conclusion

Verse of the Day is a Python-based application developed to retrieve and display Quranic verses in three languages. This project helped me improve my Python programming, API integration, error handling, and GUI development skills.

## Credits

- **API Provider:** [AlQuran Cloud](https://alquran.cloud/)
- **Developer:** Shanzay Aslam
- **GitHub Repository:** [VerseOfTheDay](https://github.com/Shanzay-Aslam/VerseOfTheDay)