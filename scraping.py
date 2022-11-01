import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        page = await browser.new_page()
        page.set_default_timeout(10000000)
        await page.goto("https://emojipedia.org/people/")
        list = []
        delete = [80, 161, 242, 323, 404, 485]
        contador = 1

        while (contador < 489):
            list_temp = await page.locator(f'xpath=/html/body/div[5]/div[1]/ul/li[{contador}]').all_inner_texts()
            texto = str(list_temp).strip('[]').strip("'")[0]
            list.append(texto)
            if (contador in delete):
                contador+=2
            else:
                contador+=1
        
        print(list)
    
        await browser.close()

asyncio.run(main())