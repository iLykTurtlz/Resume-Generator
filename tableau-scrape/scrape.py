import os
import argparse
import requests
import easyocr
import json

def download_image(url, save_path):
    """
    Download an image from the web and save it locally.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for HTTP issues
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def extract_numbers_from_image(image_path):
    """
    Run OCR on an image using EasyOCR to extract numbers only.
    """
    try:
        reader = easyocr.Reader(['en'], gpu=False)  # Initialize the OCR reader
        results = reader.readtext(image_path, detail=0)  # Extract text without coordinates
        numbers = [res.strip() for res in results if res.strip().isdigit()]  # Keep only digits
        return numbers
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return []

def extract_text_from_image(image_path):
    """
    Run OCR on an image using EasyOCR to extract all text.
    """
    try:
        reader = easyocr.Reader(['en'], gpu=False)  # Initialize the OCR reader
        results = reader.readtext(image_path, detail=0)  # Extract text without coordinates
        text = [res.strip() for res in results if res.strip()]  # Keep non-empty results
        return text
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return []

def process_images(image_urls, output_dir, is_numeric):
    """
    Process a list of image URLs: download them, run OCR, and return the extracted text or numbers.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    all_results = []

    for i, url in enumerate(image_urls):
        print(f"Processing image {i + 1}/{len(image_urls)}: {url}")

        image_path = os.path.join(output_dir, f"image_{i + 1}.png")
        if download_image(url, image_path):
            print(f"Image saved: {image_path}")

            if is_numeric:
                results = extract_numbers_from_image(image_path)
                print(f"Extracted numbers: {results}")
            else:
                results = extract_text_from_image(image_path)
                print(f"Extracted text: {results}")

            all_results.extend(results)
        else:
            print(f"Failed to download image {url}. Adding an empty entry.")
            all_results.append("")

    return all_results

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process a list of image URLs to extract text or numbers.")
    parser.add_argument("urls_file", help="Path to the file containing the list of image URLs (one URL per line).")
    parser.add_argument("--output_dir", default="images", help="Directory to save the downloaded images.")
    parser.add_argument("--output_file", default="results.json", help="Name of the JSON file to save extracted results.")
    parser.add_argument("--is_numeric", action="store_true", help="If set, extract only numeric values.")

    args = parser.parse_args()

    # Read URLs from the provided file
    try:
        with open(args.urls_file, "r") as file:
            image_urls = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading URLs file: {e}")
        exit(1)

    # Process images and extract numbers or text based on the --is_numeric flag
    results = process_images(image_urls, args.output_dir, args.is_numeric)

    # Save the extracted results to the specified output file
    try:
        with open(args.output_file, "w", encoding="utf-8") as file:
            json.dump(results, file, indent=4)
        print(f"Extracted results saved to {args.output_file}")
    except Exception as e:
        print(f"Error writing to output file: {e}")
