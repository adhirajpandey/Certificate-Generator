from playwright.sync_api import Playwright, sync_playwright
from undetected_playwright import stealth_sync
import time
import json

def autogen(names_file, template_link):

    #readlines from names.txt and save in names list
    with open(names_file) as f:
        names = f.read().splitlines()

    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        stealth_sync(context)
        page = context.new_page()
        
        page.goto("https://www.canva.com/")
        cookie_file = open('./cookies.json')
        cookies = json.load(cookie_file)
        context.add_cookies(cookies)
        
        page.goto("https://www.canva.com/")
        time.sleep(2)

        page.goto(template_link)

        time.sleep(3)

        place_holder = "Name Placeholder"
        
        #reverse the names list to preserve the order
        for i in reversed(names):

            #get by text Name Placeholder and double click on it to selct the entire text
            name_locator = page.query_selector(f'text={place_holder}')
            name_locator.dblclick()

            #remove the previous text
            page.keyboard.press("Control+A")
            page.keyboard.press("Delete")

            time.sleep(1)

            #type the current name
            page.keyboard.type(i)

            time.sleep(1)

            #duplicate the cert
            if names.index(i) != 0:
                butobj = page.get_by_role("button", name = "Duplicate page").first
                butobj.click()

            print("Successfully Created for Name: " + i)

            place_holder = i

            time.sleep(2)

        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)
