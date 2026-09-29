# Jumia Egypt Product Scraper

A Python web scraper that uses **Playwright** to collect product information from Jumia  search pages.

## Features

The scraper collects:

* Product title
* Price
* Rating
* Discount
* Product link

It supports:

* CSV output
* JSON output
* Multiple search pages
* Custom search queries

## Requirements

Python 3.8+

Install Playwright:

```bash
pip install playwright
```

Install the Playwright browser:

```bash
playwright install chromium
```

## Usage

Run the script:

```bash
python jumia_scrape.py
```

The default settings are:

```python
asyncio.run(scrape_jumia(query='oppo', output='csv', max_pages=3))
```

This searches Jumia Egypt for **Oppo** products across 3 pages.

## Customize the Search

You can change the query and number of pages:

```python
asyncio.run(scrape_jumia(query='samsung', output='csv', max_pages=5))
```

For example:

```python
query='iphone'
```

or:

```python
query='laptop'
```

## Output

The scraper saves the results using the search query and output format.

For example:

```text
oppo.product.csv
```

The CSV contains:

```text
title
price
rating
discount
link
```

## JSON Output

The function also supports JSON:

```python
asyncio.run(scrape_jumia(query='oppo', output='json', max_pages=3))
```

## Project Structure

```text
gitscrape/
│
├── jumia_scrape.py
└── README.md
```

## Technologies

* Python
* Playwright
* Jumia Egypt
* CSV
* JSON

## Disclaimer

This project is for educational purposes. Make sure your use of the scraper complies with Jumia's terms of service, robots.txt, and applicable laws.
