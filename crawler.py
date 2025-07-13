import requests
from bs4 import BeautifulSoup
import time
import os
import sys
import re

# --- Configuration ---
REQUEST_DELAY_SECONDS = 2
ROOT_OUTPUT_FOLDER = "Books"

# --- Helper Functions ---

def create_slug(book_name):
    """Converts a book name into a URL-friendly 'slug'."""
    # Convert to lowercase
    s = book_name.lower()
    # Replace any character that is not a letter or number with a hyphen
    s = re.sub(r'[^a-z0-9]+', '-', s)
    # Remove any leading or trailing hyphens
    s = s.strip('-')
    return s

def fetch_html(url):
    """Fetches HTML content from a URL with appropriate headers."""
    print(f"  Fetching: {url}")
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        print(f"  [ERROR] HTTP Error for {url}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"  [ERROR] Could not fetch {url}: {e}")
    return None

def parse_and_extract_content(html_content):
    """Parses HTML and extracts the Chinese text from the specified tags."""
    if not html_content:
        return None
    
    soup = BeautifulSoup(html_content, 'html.parser')
    original_sentences = soup.find_all('sentence', class_='original')
    
    if not original_sentences:
        print('  [WARNING] No \'<sentence class="original">\' tags found on the page. The page structure might have changed.')
        return ""
        
    chapter_text = [s.get_text(strip=True) for s in original_sentences]
    return "".join(chapter_text)

def save_chapter(book_name, book_slug, chapter_number, content):
    """Saves the extracted content to a text file in a structured folder."""
    novel_folder = os.path.join(ROOT_OUTPUT_FOLDER, book_name)
    
    try:
        os.makedirs(novel_folder, exist_ok=True)
    except OSError as e:
        print(f"  [FATAL ERROR] Could not create directory {novel_folder}: {e}")
        sys.exit(1)
            
    # Use the pre-generated slug for the filename
    filename = f"{book_slug}-chapter-{chapter_number}-zn.txt"
    filepath = os.path.join(novel_folder, filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [SUCCESS] Saved chapter {chapter_number} to {filepath}")
    except IOError as e:
        print(f"  [ERROR] Could not write file {filepath}: {e}")

# --- Main Crawler Logic ---

def get_user_input():
    """Gets and validates the novel name and chapter range from the user."""
    book_name = input("Enter the name of the novel (e.g., Emperor's Domination): ")
    
    while True:
        try:
            start_chapter = int(input("Enter the starting chapter number: "))
            end_chapter = int(input("Enter the ending chapter number: "))
            if start_chapter <= 0 or end_chapter < start_chapter:
                print("[ERROR] Invalid chapter range. Please ensure start > 0 and end >= start.")
                continue
            return book_name, start_chapter, end_chapter
        except ValueError:
            print("[ERROR] Please enter valid numbers for chapters.")

def main():
    """Main function to run the webnovel crawler."""
    print("--- High-Efficiency Webnovel Crawler ---")
    
    book_name, start_chapter, end_chapter = get_user_input()
    
    # Generate the URL-friendly slug from the book name
    book_slug = create_slug(book_name)
    base_url = f"https://lnmtl.com/chapter/{book_slug}-chapter-{{}}"
    total_chapters_to_crawl = (end_chapter - start_chapter) + 1
    
    print("\n----------------------------------------")
    print(f"Novel Name: {book_name}")
    print(f"Generated Slug: {book_slug}")
    print(f"Targeting chapters {start_chapter} through {end_chapter}.")
    print(f"Output will be saved in '{os.path.join(ROOT_OUTPUT_FOLDER, book_name)}'")
    print("----------------------------------------\n")

    for i, chapter_num in enumerate(range(start_chapter, end_chapter + 1)):
        print(f"Processing Chapter {chapter_num} ({i + 1}/{total_chapters_to_crawl})...")
        
        url = base_url.format(chapter_num)
        html = fetch_html(url)
        
        if html:
            content = parse_and_extract_content(html)
            if content:
                # Pass the slug to the save function for consistent naming
                save_chapter(book_name, book_slug, chapter_num, content)
            elif content == "":
                 print(f"  [INFO] Chapter {chapter_num} had no content to save.")
            else:
                print(f"  [ERROR] Failed to parse content for chapter {chapter_num}.")
        
        if i < total_chapters_to_crawl - 1:
            print(f"\nWaiting for {REQUEST_DELAY_SECONDS} seconds before the next request...")
            time.sleep(REQUEST_DELAY_SECONDS)
            print()
            
    print("\n----------------------------------------")
    print("Crawling process finished.")

if __name__ == "__main__":
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        print("[SETUP] Required libraries not found.")
        print("Please run the following command to install them:")
        print("pip install requests beautifulsoup4")
        sys.exit(1)

    main()