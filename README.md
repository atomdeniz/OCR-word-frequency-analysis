# OCR Word Frequency Analysis

This project utilizes Optical Character Recognition (OCR) to process images, extract text, and analyze the frequency of words in English. It's designed to traverse directories, handle image files, and compile a list of words with their corresponding frequencies.

## Features

- **OCR on Images**: Uses `pytesseract` to perform OCR on various image formats.
- **Word Frequency Analysis**: Analyzes and counts the frequency of meaningful English words.
- **Directory Handling**: Recursively processes directories to handle images in an organized manner.
- **Output Generation**: Generates a CSV file listing words and their frequencies.

## Requirements

- Python 3.x
- Libraries: `pytesseract`, `PIL`, `enchant`
- Tesseract OCR Engine

## Installation

1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install required libraries using pip:

```bash
pip install pytesseract Pillow pyenchant
```
