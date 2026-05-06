# restored from my disk in 25% corrupted state. kids, never ignore git warnings about losing data.

import requests
import json
import sys

BASE_URL = "https://api.cengage.co.in"
TOKEN = "oombda oombda, moochi mutt oombda"

global_headers = {
    "authority": "api.cengage.co.in",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB",
    "authorization": f"Bearer {TOKEN}",
    "user-agent": "Mozilla/5.0",
}

def get_isbn(data):
    isbns = []

    for book in data.get("data", []):
        isbn = book.get("isbn")

        if not isbn:
            print("No ISBN for", book.get("title"))
            continue

        if isbn.isalnum():
            isbns.append(isbn)
        else:
            print("Corrupted ISBN entry for", book.get("title"))

    return isbns


def get_toc(isbn):
    url = f"{BASE_URL}/api/toc/gettocbyisbn"

    # IMPORTANT: DO NOT manually set boundary/content-type
    # requests handles multipart correctly
    headers = global_headers.copy()

    files = {
        "isbn": (None, isbn)
    }

    r = requests.post(url, headers=headers, files=files)

    print("\n----- TOC for", isbn, "-----")
    print("Status:", r.status_code)

    try:
        print(json.dumps(r.json(), indent=2))
    except Exception:
        print(r.text)


def main():
    payload = {
        "pageNo": 0,
        "pageSize": 20,
        "diciplineID": [13],
        "bookCategory": 2
    }

    response = requests.post(
        f"{BASE_URL}/api/book/getcatalog",
        headers=global_headers,
        json=payload
    )

    print("Status Code:", response.status_code)

    data = response.json()
    print("Total books:", len(data.get("data", [])))

    isbns = get_isbn(data)
    print("\nISBNs:", isbns)

    while True:
        print("\n1. Get TOC")
        print("2. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            isbn = input("Enter ISBN: ").strip()
            get_toc(isbn)

        elif choice == "2":
            sys.exit(0)

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
