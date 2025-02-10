from playwright.sync_api import sync_playwright
import time


def main():
    with sync_playwright() as p:
        browser = None
        try:
            # Launch the browser in graphic mode
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            # AccessLinkedIn
            page.goto("https://www.linkedin.com/mynetwork/")

            # Wait for the user to log in manually
            print("Please login manually on LinkedIn.")
            input("Press Enter after logging in and ensure that the 'My Network' page is loaded.")

            while True:
                try:
                    # Checks and finds all buttons "invite" or "Connect"
                    invite_buttons = page.locator("button:has-text('Convidar'), button:has-text('Conectar')")

                    # Ensures that the buttons are available
                    count = invite_buttons.count()

                    if count == 0:
                        print("No button found, recharging the page...")
                        page.reload()
                        time.sleep(20)  # Espera para o carregamento da página
                        continue

                    print(f"{count} buttons found. Starting the process ...")

                    # Click each button found
                    for i in range(count):
                        try:
                            button = invite_buttons.nth(i)

                            # Check if there is modal blocking
                            if page.locator("div[data-test-modal-container]").is_visible():
                                print("Modal detected, closing ...")
                                page.locator("button:has-text('Entendi')").click(timeout=3000)
                                time.sleep(1)  # Wait for the closure of the modal

                            button.click(timeout=3000)  # Click with 3 second timeout
                            print(f"Invitation sent to contact {i + 1}!")
                            time.sleep(5)  # Wait 5 seconds between clicks
                        except Exception as e:
                            print(f"Error clicking the button {i + 1}: {e}. Trying the next...")

                    # Rolls the page to load more contacts
                    print("Rolling the page to load more contacts ...")
                    page.keyboard.press("End")
                    time.sleep(5)  # Awaits 5 seconds after rolling the page

                except Exception as e:
                    print(f"General error: {e}. Returning to the main loop ...")

        except Exception as e:
            print(f"Critical error: {e}")

        finally:
            # Make sure the browser will be closed
            if browser:
                browser.close()
                print("Closed browser.")


if __name__ == "__main__":
    main()
