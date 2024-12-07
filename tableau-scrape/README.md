Cal Poly's graduate outcomes Tableau stores all of the data as images... So we have to get all the images and extract info via OCR.

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