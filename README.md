# LNMTL Webnovel Crawler

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/your-username/your-repo-name/pulls)

A user-friendly Python script to download the original Chinese-language chapters of any webnovel from `lnmtl.com`. This tool is perfect for language learners, aspiring translators, or readers who want to build an offline library of their favorite novels.

The script prompts you for the novel's name and a specific chapter range, then intelligently handles the rest—from formatting the URL correctly to organizing the downloaded chapters into neat, dedicated folders.

---

## Features

-   **Crawl Any Novel**: Works with any novel available on `lnmtl.com`.
-   **Custom Chapter Ranges**: Specify exactly which chapters you want to download (e.g., chapters 50 to 150).
-   **Smart Name Handling**: Automatically creates URL-friendly "slugs" from complex names like `"Emperor's Domination"` or `"Douluo Dalu 3 - Dragon King's Legend"`.
-   **Organized Output**: Creates a main `Books` directory, with a dedicated sub-folder for each novel you download.
-   **Respectful Crawling**: Includes a configurable politeness delay between requests to avoid overwhelming the server.
-   **Robust Error Handling**: Gracefully handles common network errors and missing pages.
-   **User-Friendly**: Simple, interactive command-line interface.

## Prerequisites

Before you begin, ensure you have **Python 3.7 or newer** installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

## Installation & Setup

Follow these steps to get the crawler up and running on your local machine.

**1. Clone the Repository**

```bash
git clone https://github.com/areck97432/WebNovelCrawler.git
```

**2. Navigate to the Project Directory**

```bash
cd WebNovelCrawler
```

**3. Install Required Libraries**

The project dependencies are listed in `requirements.txt`. Install them using pip.

```bash
# It's highly recommended to do this inside a Python virtual environment.
pip install -r requirements.txt
```

## How to Use

Once the setup is complete, running the crawler is simple.

**1. Run the Script**

Execute the main Python file from your terminal:

```bash
python crawler.py
```

**2. Follow the Prompts**

The script will ask for three pieces of information:
- The name of the novel.
- The starting chapter number.
- The ending chapter number.

### Example Session

```text
--- High-Efficiency Webnovel Crawler ---
Enter the name of the novel (e.g., Emperor's Domination): Emperor's Domination
Enter the starting chapter number: 1
Enter the ending chapter number: 10

----------------------------------------
Novel Name: Emperor's Domination
Generated Slug: emperor-s-domination
Targeting chapters 1 through 10.
Output will be saved in 'Books/Emperor's Domination'
----------------------------------------

Processing Chapter 1 (1/10)...
  Fetching: https://lnmtl.com/chapter/emperor-s-domination-chapter-1
  [SUCCESS] Saved chapter 1 to Books/Emperor's Domination/emperor-s-domination-chapter-1-zn.txt

Waiting for 2 seconds before the next request...

...
```

## Example Output Structure

The script will generate a clean folder and file structure for your downloaded novels, making them easy to manage.

```text
WebNovelCrawler/
│
├── Books/
│   │
│   ├── Emperor's Domination/
│   │   ├── emperor-s-domination-chapter-1-zn.txt
│   │   ├── emperor-s-domination-chapter-2-zn.txt
│   │   └── ...
│   │
│   └── Blood Ascension/
│       ├── blood-ascension-chapter-50-zn.txt
│       ├── blood-ascension-chapter-51-zn.txt
│       └── ...
│
├── crawler.py
├── requirements.txt
└── README.md
```

## 📜 Disclaimer

This tool is intended for **personal and educational use only**. The content downloaded using this script belongs to its respective authors and publishers.

Please be respectful of the source website (`lnmtl.com`). The default request delay is set to 2 seconds. **Do not set this value too low**, as sending too many rapid requests may lead to your IP address being temporarily or permanently banned by the website.

The user of this script assumes all responsibility for its use.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.