# Overview

Cal Poly's graduate outcomes Tableau stores all of the data as images... So we have to get all the images and extract info via OCR. Data cleaning on the companies is done later (with job scraping) - effectively, we ignore companies that don't have job postings with their exact company name.

# Instructions

1. Run `create_url_txt_files.py` to create url lists
2. Run `scrape.py` on the url list you wish to scrape. Usage: `python scrape.py (URLS_TXT_FILE) --output_dir (IMAGES_OUTPUT_DIR) --output_file (RESULTS_OUTPUT_FILENAME) --is_numeric?`

**Note**: `is_numeric` doesn't work well...

Get image sources code (JS):

```js
function getImgSourcesByFullXPath(fullXPath) {
    const result = document.evaluate(fullXPath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
    const element = result.singleNodeValue;

    if (!element) {
        console.error("No element found for the provided XPath:", fullXPath);
        return [];
    }

    const imgElements = element.querySelectorAll('img');
    const imgSources = Array.from(imgElements).map(img => img.getAttribute('src') || '');
    copy(imgSources) // copy to clipboard
    return imgSources;
}
```
