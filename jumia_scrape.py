import asyncio
import csv
import json
from playwright.async_api import async_playwright

async def scrape_jumia (query= 'oppo', output='csv', max_pages=3):
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()

            products = []

            for page_num in range(1,max_pages+1):
                print(f'scrape page {page_num}')

                # Navigate to search bar

                URL = f'https://www.jumia.com.eg/catalog/?q={query}&page={page_num}#catalog-listing'
                await page.goto(URL, wait_until=('domcontentloaded'))
                # Wait product to load

                try:
                    await page.wait_for_selector ('article.prd', timeout =10000)
                except Exception:
                    print(f'not product found on page {page_num}')
                    break

                product_elements = await page.query_selector_all('article.prd')

                for product in product_elements:
                    try:
                        title_element = await product.query_selector('.name')
                        price_element = await product.query_selector('.prc')
                        rating_element = await product.query_selector('.stars')
                        discount_element = await product.query_selector('.bdg._dsct')
                        link_element = await product.query_selector('a.core')

                        title = (
                            await title_element.inner_text()
                            if title_element
                            else 'N/A'
                        )
                        price = (
                            await price_element.inner_text()
                            if price_element
                            else 'N/A'
                        )
                        rating = (
                            await rating_element.inner_text()
                            if rating_element
                            else 'N/A'
                        )
                        discount = (
                            await discount_element.inner_text()
                            if discount_element
                            else 'no discount'
                        )
                        link = (
                            await link_element.get_attribute('href')
                            if link_element
                            else 'N/A'
                        )

                        #Ensure link is absolut

                        if link != 'N/A' and not link.startswith('http'):
                            link = f'https//www.jumia.com.eg{link}'

                        products.append({
                            'title': title.strip(),
                            'price': price.strip(),
                            'rating': rating.strip(),
                            'discount': discount.strip(),
                            'link': link
                        })

                    except Exception as e:
                        print(f'Error extracting product data: {e}')  
                        continue 

            await browser.close()

            #Save data
            file_name = f'{query}.product.{output}' 
            if output == 'csv':
                with open(file_name, 'w', newline = '', encoding = 'utf-8') as file:
                    fieldnames = ['title', 'price', 'rating', 'discount', 'link' ]  

                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(products) 

            elif output == 'json':
                with open (file_name, 'w', indent=4, ensure_ascii=False):

                    print (f'Successfully scraped {len(products)} products across pages. Data saved to {file_name}')

        except Exception as e:
            print(f'An error occured: {e}')

asyncio.run(scrape_jumia(query='oppo', output='csv', max_pages=3))    




                   


