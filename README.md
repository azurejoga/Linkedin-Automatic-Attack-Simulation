# LinkedIn Automatic Attack Simulation - PoC (Proof of Concept)

[![GitHub stars](https://img.shields.io/github/stars/azurejoga/Linkedin-Automatic-Attack-Simulation?style=social)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/azurejoga/Linkedin-Automatic-Attack-Simulation?style=social)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/network)  
[![GitHub pull requests](https://img.shields.io/github/issues-pr/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/pulls)  
[![GitHub issues](https://img.shields.io/github/issues/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/issues)  
[![License](https://img.shields.io/github/license/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://opensource.org/licenses/GPL-3.0)  
[My LinkedIn](https://www.linkedin.com/in/juan-mathews-rebello-santos-/)
[veja o estudo de caso, em português](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/blob/master/readme-pt_BR.md)

## Introduction

The **LinkedIn Automatic Simulation Attack** is a technique that exploits automation of interactions on the LinkedIn platform using scripts such as **Playwright**. This approach allows simulating human activities on the site without requiring the interface to be visible, enabling various actions to be performed programmatically and continuously. This raises serious security concerns, including spam, brute-force attacks, and other forms of abuse.

## How Automation Works

Automation on LinkedIn through tools like **Playwright** allows a bot to:

- Perform automatic login attempts.
- Send mass connection requests.
- Execute programmatic interactions such as likes, comments, and messages.
- Scroll through the page, loading and interacting with new profiles.

The provided script exemplifies an automated connection request process, which can be adapted for other purposes.

## Code Explanation

### Installation and Setup

To run the script, install **Playwright** with the following commands:

```sh
pip install playwright
playwright install
```

The Python code uses the `playwright.sync_api` library, which allows synchronous browser automation.

### Code Structure

#### Initializing Playwright and Opening the Browser

```python
from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
```

Here, the script starts **Playwright**, opens the **Chromium** browser, and creates a new browsing context.

#### Accessing LinkedIn

```python
page.goto("https://www.linkedin.com/mynetwork/")
```

The browser navigates to LinkedIn's **"My Network"** page.

#### Manual Authentication

```python
print("Please login manually on LinkedIn.")
input("Press Enter after logging in and ensure that the 'My Network' page is loaded.")
```

The script waits for the user to log in manually before proceeding.

#### Interacting with Connection Buttons

```python
while True:
    try:
        invite_buttons = page.locator("button:has-text('Convidar'), button:has-text('Conectar')")
        count = invite_buttons.count()
```

It locates the **"Connect"** and **"Invite"** buttons to send connection requests.

#### Loop to Click the Buttons

```python
for i in range(count):
    try:
        button = invite_buttons.nth(i)
        button.click(timeout=3000)
        print(f"Invitation sent to contact {i + 1}!")
        time.sleep(5)
    except Exception as e:
        print(f"Error clicking the button {i + 1}: {e}. Trying the next...")
```

The code iterates through all found buttons and clicks them with a **5-second** interval between interactions.

#### Closing the Browser

```python
if browser:
    browser.close()
    print("Closed browser.")
```

Ensures the browser is closed at the end of execution.

## Simulation for Educational Purposes

To safely test the script:

```sh
git clone https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation.git
cd linkedin-Automatic-Attack-Simulation
pip install playwright
playwright install
python linkedin.py
```

This test allows understanding how automation interacts with the platform without compromising security or violating terms of use.

## Security Risks

1. **Brute-Force Attacks**  
   Automated login attempts make brute-force attacks against user credentials feasible.

2. **Mass Messaging (Spam)**  
   Automation can be used to send mass messages, facilitating scams and fraud.

3. **Impersonation and Deception**  
   Bots can create fake profiles to deceive other users.

4. **Algorithm Manipulation**  
   Automated profiles can artificially engage with content, altering its relevance on the platform.

## Possible Mitigation Measures

- **Multi-Factor Authentication (MFA)**
- **Monitoring for Suspicious Activities**
- **Limiting Automated Actions**
- **Detecting Automated Browsers**

## Final Considerations

The test results indicate that more than 60 connection requests were sent by the bot without any security block to prevent the exploitation of the vulnerability. Additionally, modals were closed without any additional security verification.  

According to the stress tests conducted, no security blockers were found, and the bot sent more than 100 connection requests through the simulated browser. The conclusions drawn from this case study indicate that even with the browser minimized, the bot continued performing actions automatically, without any security restrictions, and was even able to bypass LinkedIn’s modals.  

The only limitation encountered was the maximum number of allowed connections, but this is not enough to stop the bot’s actions, as it can be expanded to carry out other malicious activities or simply wait until next Monday to be executed again.  

The conclusion is clear: there is no verification from LinkedIn's servers to prevent the use of automated bots, posing a serious security risk and raising concerns about user protection on the platform. After all, who can guarantee that many of them are not actually bots?