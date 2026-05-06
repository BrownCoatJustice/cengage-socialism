# cengage socialism
trying to find a way to get all cengage digital content for free by exploiting their API. ssshhh!

what i need help with
1. like um the um uhh... oh yeah...<br>I need to find a way to figure out the ISBN of the digital content. right now, if you have them in your bookshelf (cengage digital.exe's) then you can get 'em pretty easily.<br>just can't figure out which isbns have digital content and which don't... and that is fucking me up.

fuck it im too lazy to explain my code...
chatgpt, take over:

## Overview

This script interacts with the Cengage Digital API to retrieve a list of books and attempt to fetch their Table of Contents (TOC) using ISBNs.

## What it does

- Sends a request to the Cengage catalog API to fetch a list of available books.
- Extracts ISBN values from the response.
- Filters out missing or invalid ISBN entries.
- Attempts to fetch the Table of Contents (TOC) for each ISBN using a separate endpoint.
- Provides a simple command-line interface to test TOC retrieval for a default or user-provided ISBN.

## Main functions

### `get_isbn(data)`
Parses the catalog response and returns a list of valid ISBNs.

- Iterates through book data
- Checks for ISBN presence
- Skips invalid or missing entries

### `get_toc(isbn)`
Fetches Table of Contents data for a given ISBN.

- Sends a `multipart/form-data` POST request
- Manually constructs request body with boundary
- Prints status code and response (JSON or raw text if parsing fails)

## Flow

1. Fetch catalog data from API  
2. Extract ISBNs  
3. Print catalog response and ISBN list  
4. Show menu:
   - Fetch TOC for a default ISBN
   - Enter custom ISBN
   - Exit

## Limitations

- Many ISBNs do not return TOC data because they are not linked to digital content.
- API token is hardcoded in the script.
- Multipart request is manually constructed, which is brittle.
- Some responses may be empty or inconsistent depending on ISBN.

## Notes

- This script is mainly for testing and exploring the API behavior. It is not intended for production use.
- The ISBN in the physical copy and digital version do not match.
- To open the Network tab of Cengage's Electron interface modify the `electron.js` file after extracting the `app.asar` from the `resources` folder in the app root.
