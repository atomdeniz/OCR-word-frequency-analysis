import os
from collections import Counter
import pytesseract
from PIL import Image
import enchant
import re

output_file_path = "./output.txt"

def is_image_file(file_path):
    """
    Check if the file is an image (JPEG, PNG, etc.).
    """
    return file_path.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif'))

def is_meaningful_word(word):
    """
    Check if the given word is a meaningful word in English.
    """
    d = enchant.Dict("en_US")
    return d.check(word)

def clean_text(text):
    """
    Clean the input text by removing non-letter characters and checking if it's ASCII.
    """
    if not text.isascii():
        return ""
    return ''.join(filter(str.isalpha, text))

def process_image(file_path, all_words):
    """
    Perform OCR on the image and process the text.
    """
    try:
        print(f"Processing {file_path}")
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img, lang='eng')
        words = text.lower().split()
        for word in words:
            word = clean_text(word)
            if word and len(word) > 2 and not word.isdigit():
                if is_meaningful_word(word):
                    all_words.append(word)

        word_counts = Counter(all_words)
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        with open(output_file_path, 'w') as file:
            for word, count in sorted_words:
                file.write(f"{word},{count}\n")
         
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def extract_number(directory_name):
    match = re.search(r'\d+', directory_name)
    return int(match.group()) if match else 0

def process_directory(directory, all_words):
    """
    Recursively process each directory and file.
    """
    directories = os.listdir(directory)
    orderred_directories = sorted(directories, key=extract_number)

    for entry in orderred_directories:
        path = os.path.join(directory, entry)
        if os.path.isdir(path):
            process_directory(path, all_words)
            print(f"Processed {path}")
        elif is_image_file(path):
            process_image(path, all_words)
        

def main(base_dir):
    all_words = []
    process_directory(base_dir, all_words)

    
if __name__ == "__main__":
    base_dir = input("Enter the base directory: ")
    main(base_dir)
