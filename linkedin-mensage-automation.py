from playwright.sync_api import sync_playwright
import pyperclip

def enviar_mensagens():
    mensagem = input("Enter the message you want to send: ")
    pyperclip.copy(mensagem)

    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        contexto = navegador.new_context()
        pagina = contexto.new_page()

        pagina.goto("https://www.linkedin.com/mynetwork/invite-connect/connections/", wait_until="load")
        print("⚠️ LinkedIn's manually login if requested.")
        input("✅ Press Enter here when the page is completely charged ...")

        pagina.wait_for_timeout(3000)

        try:
            pagina.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            pagina.wait_for_timeout(3000)
        except:
            print("[!] Failure to roll the page, trying to continue anyway ...")

        total = pagina.locator("li.mn-connection-card").count()
        print(f"[i] Total contacts found: {total}")

        for i in range(total):
            try:
                # Recolet the contact with each iteration
                contato = pagina.locator("li.mn-connection-card").nth(i)
                nome = contato.locator("span.mn-connection-card__name").inner_text()
                print(f"[{i+1}] Submitting message to: {nome.strip()}")

                botao_enviar = contato.locator("button:has-text('Mensagem'), button:has-text('Message')").first
                botao_enviar.click(force=True, timeout=10000)

                pagina.wait_for_timeout(3000)

                pagina.keyboard.press("Control+V")
                pagina.wait_for_timeout(2000)

                pagina.keyboard.press("Control+Enter")
                pagina.wait_for_timeout(5000)

                pagina.goto("https://www.linkedin.com/mynetwork/invite-connect/connections/", wait_until="load")
                pagina.wait_for_timeout(5000)

            except Exception as e:
                print(f"[x] Error sending for contact {i+1}: {e}")
                continue

        print("✅ Messages sent successfully!")
        navegador.close()

if __name__ == "__main__":
    enviar_mensagens()
