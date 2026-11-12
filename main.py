
import requests

url = "https://api.alquran.cloud/v1/ayah/random/editions/quran-uthmani,en.asad,ur.jalandhry"

while True:

    print("\n===== VERSE OF THE DAY =====")
    print("1. Get a New Verse")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()["data"]

            print("\nArabic:")
            print(data[0]["text"])

            print("\nEnglish:")
            print(data[1]["text"])

            print("\nUrdu:")
            print(data[2]["text"])

            print("\nSurah:", data[0]["surah"]["englishName"])
            print("Ayah Number:", data[0]["numberInSurah"])

        except requests.exceptions.RequestException:
            print("Internet or API connection problem!")

    elif choice == "2":
        print("Thank you for using Verse of the Day!")
        break

    else:
        print("Invalid choice! Please enter 1 or 2.")
