# LinkedIn Automatic Simulation Attack - PoC (Proof of Concept)

[![GitHub stars](https://img.shields.io/github/stars/azurejoga/Linkedin-Automatic-Attack-Simulation?style=social)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/azurejoga/Linkedin-Automatic-Attack-Simulation?style=social)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/network)  
[![GitHub pull requests](https://img.shields.io/github/issues-pr/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/pulls)  
[![GitHub issues](https://img.shields.io/github/issues/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/issues)  
[![License](https://img.shields.io/github/license/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://opensource.org/licenses/GPL-3.0)  
[My LinkedIn](https://www.linkedin.com/in/juan-mathews-rebello-santos-/)  
[Estudo de caso em Português](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/blob/master/readme-pt_BR.md)

# Introduction

The **LinkedIn Automatic Simulation Attack** is a technique that leverages automation of interactions on the **LinkedIn** platform using scripts such as **Playwright**. This approach allows simulating human activities on the site without requiring the interface to be visible, enabling various actions to be executed programmatically and continuously. This raises serious security concerns, including **spam, brute-force attacks, mass data collection, and other forms of abuse**.

---

## Repository Description

This repository contains a proof of concept (PoC) exploring critical vulnerabilities in the LinkedIn platform. The provided scripts demonstrate how actions such as sending mass invitations and messages can be automated, exploiting **rate limiting** flaws, lack of **anti-bot protections**, and unrestricted permissions for automated actions on the user interface.

---

## Why?

Automating interactions on social platforms like LinkedIn has a dual impact. On one hand, it can optimize repetitive tasks and improve efficiency. On the other, it can be exploited by malicious actors to conduct large-scale attacks, such as phishing campaigns, malware dissemination, and information manipulation. The primary goal of this repository is to highlight LinkedIn's structural security flaws and encourage the adoption of measures to protect users and the platform's integrity.

---

## Available Scripts

### 1. `linkedin-connection.py`

#### Objective
The `linkedin-connection.py` script is designed to automate the process of sending LinkedIn connection invitations. It allows selecting contacts based on search keywords or directly interacting with the suggested connections tab, maximizing the reach of automated profiles.

#### Functionality
- **Browser Control:** The script uses the Playwright library to control the Chromium browser.
- **Manual Login:** The script operator manually logs in to authenticate the account.
- **Custom Search or Direct Attack:**
  - Custom search based on keywords, such as "information security".
  - Direct attack on the "My Network" tab, sending invitations to suggested connections automatically.
- **Execution Steps:**
  1. Scrolls the page to the bottom to dynamically load new contacts.
  2. Detects buttons with texts such as "Connect" or "Invite".
  3. Sends connection invitations automatically without personalized messages.
  4. Identifies and attempts to bypass security blocks, such as CAPTCHAs.

#### Exploited Vulnerabilities
- **Lack of Rate Limiting:** No defined limit for sending invitations per session or account.
- **Absence of Anti-Bot Protections:** No CAPTCHAs or challenges to differentiate humans from bots.
- **Repetitive Automated Actions:** LinkedIn allows DOM event simulation without detecting automation patterns.

#### Risks
- Creation of fake profiles that can quickly connect with thousands of real users.
- Facilitation of mass data collection campaigns, such as emails and job titles.
- Basis for social engineering attacks, phishing, and collection of sensitive information.

#### #Results
The tests conducted with the `linkedin-connection.py` script revealed alarming results:

1. During initial tests, over 60 connection invitations were sent without any form of blocking or detection by LinkedIn.
2. Even when the browser was minimized, the script continued to function normally, sending invitations without interruptions.
3. Modals presented by LinkedIn, such as action limit notifications or temporary block messages, were automatically closed by the script without further verification.
4. In stress tests, the bot successfully sent over 100 consecutive invitations without triggering any security mechanisms.

Additionally, the only observed limitation was LinkedIn's maximum connection limit per account. However, this restriction is insufficient to prevent malicious use of the script, as it can be adjusted to perform other actions or be paused and resumed later. These results highlight a severe flaw in LinkedIn's protection systems, leaving the platform vulnerable to large-scale abuses.

---

### 2. `linkedin-message-automation.py`

#### Objective
The `linkedin-message-automation.py` script was developed to automate the process of sending mass messages to all contacts of a LinkedIn account. It uses a personalized message provided by the script operator, enabling fast and efficient communication.

#### Functionality
- **Browser Control:** Like the previous script, it uses the Playwright library to control the Chromium browser.
- **Manual Login:** The operator manually logs in to ensure authentication.
- **Execution Steps:**
  1. Captures the list of contacts loaded in the browser.
  2. Scrolls down to ensure all contacts are loaded.
  3. Iterates through each contact card, opening the corresponding message window.
  4. Uses the `pyperclip` library to copy the message text to the clipboard.
  5. Sends the message using the Control + Enter key combination.
  6. Returns to the contact list and continues the sending process.

#### Exploited Vulnerabilities
- **Unlimited Message Sending:** No restrictions on the number of messages sent per session or hour.
- **Lack of Automation Detection:** LinkedIn does not implement behavioral validations to identify automated actions.
- **Continuous Action Execution:** No delays or additional checks to prevent continuous message sending.

#### Risks
- Sending phishing messages containing malicious links to real contacts.
- Large-scale spam or disinformation campaigns.
- High potential for credential theft and social engineering attacks.

#### #Results
The tests conducted with the `linkedin-message-automation.py` script demonstrated its effectiveness in exploiting critical platform vulnerabilities:

1. The bot successfully sent messages to hundreds of contacts in a short period without any blocking or limitation.
2. Even under high load conditions, the script operated stably, highlighting the lack of behavioral challenges on LinkedIn.
3. The absence of auditing mechanisms allowed the script to perform continuous actions, even after sending repetitive messages.

These results reinforce the need for effective mitigation measures to protect users from automated abuse.

---

## Execution Requirements

- **Operating System:** Windows 11.
- **Python:** Version 3.10 or higher.
- **Dependencies:**
  ```bash
  pip install playwright pyperclip
  playwright install
  ```

### Script Execution

1. **Connection Automation:**
   ```bash
   python3 linkedin-connection.py
   ```

2. **Message Automation:**
   ```bash
   python3 linkedin-message-automation.py
   ```

---

## Recommended Mitigations

1. **CAPTCHA for Repetitive Interactions:**
   - Implement visual challenges for consecutive actions, such as sending invitations and messages.

2. **Rate Limiting:**
   - Apply rate limits by IP and user session to prevent abuse.

3. **Behavioral Monitoring:**
   - Detect automation patterns, such as rapid repetitive clicks or continuous actions without human interaction.

4. **Human-Based Movement Challenges:**
   - Use random delays and irregular scroll movements to validate interactions.

5. **Suspicious Activity Auditing:**
   - Monitor headers and activities of automation tools like Playwright, Selenium, and Puppeteer.

---

## Conclusion

This repository exposes critical flaws in LinkedIn's infrastructure, highlighting the absence of mechanisms to protect against automation and abuse. Automating mass invitations and messages poses a serious risk to user security and platform integrity. LinkedIn must implement robust measures to mitigate these risks and ensure a safe experience for its users.

---

## Author

[Juan Mathews Rebello Santos]  
Cybersecurity Specialist with over 10 years of experience in IT.  

**Discovery Date:** April 2025  
**Proposed Identifier:** CVE-2025-XXXXX (in submission process)

## Sources

[GitHub](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation)