import asyncio
from pyppeteer import launch
from pyppeteer.errors import PageError

async def scrape_website():
    try:
        # Launch a headless browser
        browser = await launch()

        # Create a new page
        page = await browser.newPage()

        # Navigate to the website
        await page.goto('https://www.99.co/singapore/rent/hdb')

        # Wait for some time (you can adjust this as needed)
        await asyncio.sleep(5)

        # Get the HTML content of the entire page
        page_content = await page.content()

        # Close the browser
        await browser.close()

        # Return the page content
        return page_content
    except PageError as e:
        print(f"Error: {e}")
        # Retry the operation after a delay
        await asyncio.sleep(10)
        return await scrape_website()

# Run the scraping function
website_html = asyncio.get_event_loop().run_until_complete(scrape_website())

# Now you have the entire HTML content of the website in the 'website_html' variable
print(website_html)
