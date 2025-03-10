# LinkedIn Automatic Simulation Attack - POC (prova de conceito)

[![GitHub stars](https://img.shields.io/github/stars/azurejoga/Linkedin-Automatic-Attack-Simulation?style=social)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/azurejoga/Linkedin-Automatic-Attack-Simulation?style=social)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/network)  
[![GitHub pull requests](https://img.shields.io/github/issues-pr/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/pulls)  
[![GitHub issues](https://img.shields.io/github/issues/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/issues)  
[![License](https://img.shields.io/github/license/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://opensource.org/licenses/GPL-3.0)  
[meu linkedin](https://www.linkedin.com/in/juan-mathews-rebello-santos-/)
[estudo de caso em inglês](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation)

## Introdução

O **LinkedIn Automatic Simulation Attack** é uma técnica que explora a automação de interações na plataforma **LinkedIn** usando scripts como **Playwright**. Essa abordagem permite simular atividades humanas no site sem exigir que a interface esteja visível, possibilitando a execução de diversas ações de forma programada e contínua. Isso levanta sérias preocupações de segurança, incluindo **spam, ataques de força bruta e outras formas de abuso**.

## Como Funciona a Automação

A automação no LinkedIn por meio de ferramentas como **Playwright** permite que um bot:

* Realize tentativas automáticas de login.
* Envie solicitações de conexão em massa.
* Execute interações programáticas como curtidas, comentários e mensagens.
* Role a página, carregando e interagindo com novos perfis.

O script fornecido exemplifica um processo automatizado de solicitação de conexão, podendo ser adaptado para outras finalidades.

## Explicação do Código

### Instalação e Configuração

Para executar o script, instale o **Playwright** com os seguintes comandos:

```sh
pip install playwright
playwright install
```

O código Python utiliza a biblioteca `playwright.sync_api`, que permite a automação do navegador de forma síncrona.

### Estrutura do Código

#### Inicializando o Playwright e Abrindo o Navegador

```python
from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
```

Aqui, o script inicia o **Playwright**, abre o navegador **Chromium** e cria um novo contexto de navegação.

#### Acessando o LinkedIn

```python
page.goto("https://www.linkedin.com/mynetwork/")
```

O navegador navega até a página **"Minha Rede"** do LinkedIn.

#### Autenticação Manual

```python
print("Faça login manualmente no LinkedIn.")
input("Pressione Enter após fazer login e garantir que a página 'Minha Rede' esteja carregada.")
```

O script aguarda que o usuário faça login manualmente antes de prosseguir.

#### Interação com os Botões de Conexão

```python
while True:
    try:
        invite_buttons = page.locator("button:has-text('Convidar'), button:has-text('Conectar')")
        count = invite_buttons.count()
```

Localiza os botões **"Conectar"** e **"Convidar"** para enviar solicitações de conexão.

#### Loop para Clicar nos Botões

```python
for i in range(count):
    try:
        button = invite_buttons.nth(i)
        button.click(timeout=3000)
        print(f"Convite enviado para o contato {i + 1}!")
        time.sleep(5)
    except Exception as e:
        print(f"Erro ao clicar no botão {i + 1}: {e}. Tentando o próximo...")
```

O código percorre todos os botões encontrados e os clica com um intervalo de **5 segundos** entre as interações.

#### Fechando o Navegador

```python
if browser:
    browser.close()
    print("Navegador fechado.")
```

Garante que o navegador seja fechado no final da execução.

## Riscos de Segurança

1. **Ataques de Força Bruta**  
2. **Mensagens em Massa (Spam)**  
3. **Falsificação de Identidade**  
4. **Manipulação do Algoritmo**  

## Medidas de Mitigação

- **Autenticação Multifator (MFA)**
- **Monitoramento de Atividades Suspeitas**
- **Limitação de Ações Automatizadas**
- **Detecção de Navegadores Automatizados**

## Considerações Finais
Os resultados dos testes indicam que mais de 60 convites de conexão foram enviados por meio do bot, sem que houvesse qualquer bloqueio de segurança para impedir a exploração da vulnerabilidade. Além disso, os modais foram fechados sem nenhuma verificação de segurança adicional.  

De acordo com os testes de estresse realizados, nenhum bloqueador de segurança foi encontrado, e o bot enviou mais de 100 convites de conexão por meio do navegador simulado. As conclusões desse estudo de caso indicam que, mesmo com o navegador minimizado, o bot continuou executando ações de forma automatizada, sem qualquer bloqueio de segurança e conseguindo até mesmo burlar os modais do LinkedIn.  

A única limitação encontrada foi o número máximo de conexões permitidas, mas isso não é suficiente para impedir as ações do bot, pois ele pode ser expandido para realizar outras atividades maliciosas ou simplesmente esperar até a próxima segunda-feira para ser executado novamente.  

A conclusão é clara: não há qualquer tipo de verificação por parte dos servidores do LinkedIn para prevenir o uso de bots automatizados, o que representa um sério risco de segurança e levanta preocupações quanto à proteção dos usuários da plataforma. Afinal, quem pode garantir que muitos deles não são, na verdade, bots?