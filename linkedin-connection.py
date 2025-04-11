from playwright.sync_api import sync_playwright
import time

def search_and_connect(page, search_term):
    while True:
        try:
            connect_buttons = page.locator("button:has-text('Conectar')")
            count = connect_buttons.count()

            if count == 0:
                print("No button found, rolling the page ...")
                page.keyboard.press("End")
                time.sleep(5)
                continue

            print(f"{count} buttons found. Starting connection process ...")

            for i in range(count):
                try:
                    button = connect_buttons.nth(i)
                    button.click(timeout=3000)
                    time.sleep(2)

                    if page.locator("button:has-text('Enviar sem nota')").is_visible():
                        page.locator("button:has-text('Enviar sem nota')").click()
                        print(f"Invitation sent to contact {i + 1}!")
                        time.sleep(5)
                    
                    if page.locator("div[data-test-modal-container]").is_visible():
                        print("Block modal detected. Ending process.")
                        return
                except Exception as e:
                    print(f"Error clicking the button {i + 1}: {e}. Trying the next ...")

            page.keyboard.press("End")
            time.sleep(5)
        except Exception as e:
            print(f"General error: {e}. Returning to the main loop ...")

def connect_from_network_page(page):
    while True:
        try:
            invite_buttons = page.locator("button:has-text('Convidar'), button:has-text('Conectar')")
            count = invite_buttons.count()

            if count == 0:
                print("No button found, recharging the page ...")
                page.reload()
                time.sleep(20)
                continue

            print(f"{count} buttons found. Starting connection process ...")

            for i in range(count):
                try:
                    button = invite_buttons.nth(i)
                    if page.locator("div[data-test-modal-container]").is_visible():
                        print("Modal detected, closing ...")
                        page.locator("button:has-text('Entendi')").click(timeout=3000)
                        time.sleep(1)

                    button.click(timeout=3000)
                    print(f"Invitation sent to contact {i + 1}!")
                    time.sleep(5)
                except Exception as e:
                    print(f"Error clicking the button {i + 1}: {e}. Trying the next ...")

            print("Rolling the page to load more contacts ...")
            page.keyboard.press("End")
            time.sleep(5)
        except Exception as e:
            print(f"General error: {e}. Returning to the main loop ...")

def main():
    with sync_playwright() as p:
        browser = None
        try:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            # Question before you login
            choice = input("Choose an option:\n1 - Search for Term\n2 - Connect on the network page\nEnter 1 or 2: ").strip()

            if choice == "1":
                search_term = input("Enter the research term: ").strip()
                target_url = f"https://www.linkedin.com/search/results/people/?keywords={search_term}"
                page.goto(target_url)
            elif choice == "2":
                target_url = "https://www.linkedin.com/mynetwork/"
                page.goto(target_url)
            else:
                print("Invalid option.")
                return

            print("Make login manually on LinkedIn.")
            input("Press Enter after login and the page is completely loaded ...")

            # After manual login, resumes action
            if choice == "1":
                search_and_connect(page, search_term)
            elif choice == "2":
                connect_from_network_page(page)

        except Exception as e:
            print(f"Critical error: {e}")
        finally:
            if browser:
                browser.close()
                print("Closed browser.")

if __name__ == "__main__":
    main()
