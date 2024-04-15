import asyncio
from pyppeteer import launch


async def generate_pdf_from_html(html_content, pdf_path):
    browser = await launch()
    page = await browser.newPage()

    await page.setContent(html_content)

    await page.pdf({'path': pdf_path, 'format': 'A4'})

    await browser.close()


# HTML content
html_content = '''<HTML HERE>'''

# PDF path to save
asyncio.get_event_loop().run_until_complete(generate_pdf_from_html(html_content, 'from_html.pdf'))
