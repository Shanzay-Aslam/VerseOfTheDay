
import tkinter as tk
import requests

# API URL
url = "https://api.alquran.cloud/v1/ayah/random/editions/quran-uthmani,en.asad,ur.jalandhry"

# Main Window
root = tk.Tk()
root.title("Verse of the Day")
root.geometry("900x750")
root.configure(bg="#F5F0E8")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="☪  VERSE OF THE DAY",
    font=("Georgia", 28, "bold"),
    bg="#F5F0E8",
    fg="#315C46"
)
heading.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Read, Reflect and Connect with the Quran",
    font=("Arial", 12),
    bg="#F5F0E8",
    fg="#777777"
)
subtitle.pack(pady=5)

# Verse Card
card = tk.Frame(
    root,
    bg="white",
    padx=30,
    pady=25,
    highlightbackground="#D8CDBA",
    highlightthickness=1
)
card.pack(padx=45, pady=25, fill="both", expand=True)

# Arabic
arabic = tk.Label(
    card,
    text="Arabic verse will appear here",
    font=("Traditional Arabic", 25),
    bg="white",
    fg="#315C46",
    wraplength=730,
    justify="center"
)
arabic.pack(pady=15)

# English
english = tk.Label(
    card,
    text="English translation will appear here",
    font=("Arial", 13),
    bg="white",
    fg="#444444",
    wraplength=730,
    justify="center"
)
english.pack(pady=15)

# Urdu
urdu = tk.Label(
    card,
    text="اردو ترجمہ یہاں ظاہر ہوگا",
    font=("Arial", 19),
    bg="white",
    fg="#315C46",
    wraplength=730,
    justify="center"
)
urdu.pack(pady=15)

# Surah Information
surah_info = tk.Label(
    card,
    text="Surah and Ayah information",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#777777"
)
surah_info.pack(pady=20)


# Get Random Verse Function

def get_verse():

    try:
        status.config(text="Loading verse...")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        result = response.json()

        if result.get("code") != 200:
            status.config(text="Unable to load verse. Try again!")
            return

        data = result["data"]

        if len(data) != 3:
            status.config(text="Verse data is incomplete!")
            return

        arabic.config(text=data[0]["text"])
        english.config(text=data[1]["text"])
        urdu.config(text=data[2]["text"])

        surah = data[0]["surah"]["englishName"]
        ayah = data[0]["numberInSurah"]

        surah_info.config(
            text=f"Surah: {surah}   |   Ayah: {ayah}"
        )

        status.config(text="Verse loaded successfully!")

    except requests.exceptions.RequestException:
        status.config(text="Connection problem! Please try again.")

    except (KeyError, IndexError, TypeError, ValueError):
        status.config(text="Invalid data received from API!")

# New Verse Button
new_button = tk.Button(
    root,
    text="✦  New Verse",
    font=("Arial", 13, "bold"),
    bg="#315C46",
    fg="white",
    activebackground="#244634",
    activeforeground="white",
    padx=30,
    pady=12,
    relief="flat",
    cursor="hand2",
    command=get_verse
)
new_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 11, "bold"),
    bg="#8B3A3A",
    fg="white",
    activebackground="#6B2929",
    activeforeground="white",
    padx=25,
    pady=8,
    relief="flat",
    cursor="hand2",
    command=root.destroy
)
exit_button.pack(pady=5)

# Status
status = tk.Label(
    root,
    text="Click New Verse to get a Quran verse",
    font=("Arial", 10),
    bg="#F5F0E8",
    fg="#777777"
)
status.pack(pady=10)

# Load first verse automatically
get_verse()

# Run Application
root.mainloop()
