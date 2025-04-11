# LinkedIn Automatic Simulation Attack - POC (prova de conceito)

[![GitHub stars](https://img.shields.io/github/stars/azurejoga/Linkedin-Automatic-Attack-Simulation?style=social)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/azurejoga/Linkedin-Automatic-Attack-Simulation?style=social)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/network)  
[![GitHub pull requests](https://img.shields.io/github/issues-pr/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/pulls)  
[![GitHub issues](https://img.shields.io/github/issues/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation/issues)  
[![License](https://img.shields.io/github/license/azurejoga/Linkedin-Automatic-Attack-Simulation)](https://opensource.org/licenses/GPL-3.0)  
[meu linkedin](https://www.linkedin.com/in/juan-mathews-rebello-santos-/)
[estudo de caso em inglês](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation)


# Introdução

O **LinkedIn Automatic Simulation Attack** é uma técnica que explora a automação de interações na plataforma **LinkedIn** usando scripts como **Playwright**. Essa abordagem permite simular atividades humanas no site sem exigir que a interface esteja visível, possibilitando a execução de diversas ações de forma programada e contínua. Isso levanta sérias preocupações de segurança, incluindo **spam, ataques de força bruta, coleta de dados em massa e outras formas de abuso**.

---

## Descrição do Repositório

Este repositório contém uma prova de conceito (PoC) que explora vulnerabilidades críticas na plataforma LinkedIn. Os scripts fornecidos demonstram como é possível automatizar ações como envio de convites e mensagens em massa, explorando falhas de **rate limiting**, ausência de proteções **anti-bot** e permissões irrestritas para a execução de ações automatizadas na interface do usuário.

---

## Porque?

A automação de interações em plataformas sociais, como o LinkedIn, apresenta um duplo impacto. Por um lado, pode ser utilizada para otimizar tarefas repetitivas e melhorar a eficiência. Por outro, pode ser explorada por agentes mal-intencionados para realizar ataques em larga escala, como campanhas de phishing, disseminação de malware e manipulação de informações. Este repositório tem como objetivo principal destacar as falhas estruturais de segurança no LinkedIn, incentivando a adoção de medidas que protejam os usuários e a integridade da plataforma.

---

## Scripts Disponíveis

### 1. `linkedin-connection.py`

#### Objetivo
O script `linkedin-connection.py` foi projetado para automatizar o processo de envio de convites de conexão no LinkedIn. Ele permite selecionar contatos com base em palavras-chave de busca ou interagir diretamente com a aba de conexões sugeridas, maximizando o alcance de perfis automatizados.

#### Funcionamento
- **Controle do Navegador:** O script utiliza a biblioteca Playwright para controlar o navegador Chromium.
- **Login Manual:** O operador do script realiza o login manualmente para autenticar a conta.
- **Busca Personalizada ou Ataque Direto:**
  - Busca personalizada com base em palavras-chave, como "segurança da informação".
  - Ataque direto na aba "Minha Rede", enviando convites para conexões sugeridas automaticamente.
- **Etapas Executadas:**
  1. Rola a página até o final para carregar novos contatos dinamicamente.
  2. Detecta botões com textos como "Conectar" ou "Convidar".
  3. Envia convites de conexão automaticamente, sem mensagens personalizadas.
  4. Identifica e tenta contornar bloqueios de segurança, como CAPTCHAs.

#### Vulnerabilidades Exploradas
- **Ausência de Controle de Taxa (Rate Limiting):** Não há um limite definido para o envio de convites por sessão ou por conta.
- **Falta de Proteções Anti-Bot:** Não são utilizados CAPTCHAs ou desafios que possam diferenciar humanos de bots.
- **Ações Automatizadas Repetitivas:** O LinkedIn permite a simulação de eventos DOM sem detectar padrões de automação.

#### Riscos
- Criação de perfis falsos que conseguem se conectar rapidamente a milhares de usuários reais.
- Facilitação de campanhas de coleta massiva de dados pessoais, como e-mails e cargos.
- Base para ataques de engenharia social, phishing e coleta de informações confidenciais.

#### #Resultados
Os testes realizados com o script `linkedin-connection.py` apresentaram resultados alarmantes:

1. Durante os testes iniciais, mais de 60 convites de conexão foram enviados sem que houvesse qualquer forma de bloqueio ou detecção por parte do LinkedIn.
2. Mesmo quando o navegador estava minimizado, o script continuou funcionando normalmente, enviando convites sem interrupções.
3. Os modais apresentados pelo LinkedIn, como notificações de limite de ações ou mensagens temporárias de bloqueio, foram automaticamente fechados pelo script, sem qualquer verificação adicional.
4. Em testes de estresse, o bot conseguiu enviar mais de 100 convites consecutivos sem que nenhum mecanismo de segurança fosse acionado.

Além disso, a única limitação observada foi o número máximo de conexões permitidas pela conta do LinkedIn. No entanto, essa restrição não é suficiente para impedir o uso malicioso do script, visto que ele pode ser ajustado para realizar outras ações ou ser pausado e retomado em outro momento. Esses resultados evidenciam uma grave falha nos sistemas de proteção do LinkedIn, deixando a plataforma vulnerável a abusos em larga escala.

---

### 2. `linkedin-message-automation.py`

#### Objetivo
O script `linkedin-message-automation.py` foi desenvolvido para automatizar o envio de mensagens em massa para todos os contatos de uma conta do LinkedIn. Ele utiliza uma mensagem personalizada fornecida pelo operador do script, permitindo o envio rápido e eficiente de comunicações direcionadas.

#### Funcionamento
- **Controle do Navegador:** Assim como o script anterior, ele utiliza a biblioteca Playwright para controlar o navegador Chromium.
- **Login Manual:** O operador realiza o login manualmente para garantir a autenticação.
- **Etapas Executadas:**
  1. Captura a lista de contatos carregados no navegador.
  2. Rola a página para baixo, garantindo o carregamento de todos os contatos.
  3. Itera por cada card de contato, abrindo a janela de mensagem correspondente.
  4. Utiliza a biblioteca `pyperclip` para copiar o texto da mensagem para a área de transferência.
  5. Envia a mensagem utilizando a combinação de teclas Control + Enter.
  6. Retorna à lista de contatos e continua o processo de envio.

#### Vulnerabilidades Exploradas
- **Envio Ilimitado de Mensagens:** Não há restrições para o número de mensagens enviadas por sessão ou por hora.
- **Falta de Detecção de Automação:** O LinkedIn não implementa validações comportamentais para identificar ações automatizadas.
- **Execução Repetitiva de Ações:** Não há delays ou verificações adicionais para impedir o envio contínuo de mensagens.

#### Riscos
- Disparo de mensagens de phishing contendo links maliciosos para contatos reais.
- Campanhas de desinformação ou spam em larga escala.
- Alto potencial para roubo de credenciais e ataques de engenharia social.

#### #Resultados
Os testes realizados com o script `linkedin-message-automation.py` demonstraram sua eficácia em explorar vulnerabilidades críticas da plataforma:

1. O bot conseguiu enviar mensagens para centenas de contatos em um curto período, sem que houvesse qualquer tipo de bloqueio ou limitação.
2. Mesmo em situações de alta carga, o script operou de forma estável, evidenciando a falta de desafios comportamentais no LinkedIn.
3. A ausência de mecanismos de auditoria permitiu que o script realizasse ações contínuas, mesmo após o envio de mensagens repetitivas.

Esses resultados reforçam a necessidade de medidas de mitigação eficazes para proteger os usuários contra abusos automatizados.

---

## Requisitos de Execução

- **Sistema Operacional:** Windows 11.
- **Python:** Versão 3.10 ou superior.
- **Dependências:**
  ```bash
  pip install playwright pyperclip
  playwright install
  ```

### Execução dos Scripts

1. **Automação de Conexões:**
   ```bash
   python3 linkedin-connection.py
   ```

2. **Automação de Mensagens:**
   ```bash
   python3 linkedin-message-automation.py
   ```

---

## Mitigações Recomendadas

1. **CAPTCHA para Interações Repetitivas:**
   - Implementar desafios visuais para ações consecutivas, como envio de convites e mensagens.

2. **Rate Limiting:**
   - Aplicar limites de taxa por IP e por sessão de usuário para evitar abusos.

3. **Monitoramento Comportamental:**
   - Detectar padrões de automação, como cliques repetidos em alta velocidade ou ações contínuas sem interação humana.

4. **Desafios Baseados em Movimento Humano:**
   - Utilizar delays aleatórios e movimentos irregulares de scroll para validar interações.

5. **Auditoria de Atividades Suspeitas:**
   - Monitorar cabeçalhos e atividades de ferramentas de automação, como Playwright, Selenium e Puppeteer.

---

## Conclusão

Este repositório expõe falhas críticas na infraestrutura do LinkedIn, destacando a ausência de mecanismos de proteção contra automação e abuso. A automação de convites e mensagens em massa representa um sério risco à segurança dos usuários e à integridade da plataforma. O LinkedIn deve implementar medidas robustas para mitigar esses riscos e garantir uma experiência segura para seus usuários.

---

## Autor

[Juan Mathews Rebello Santos]  
Especialista em Cibersegurança com mais de 10 anos de experiência em informática.  

**Data da Descoberta:** Abril de 2025  
**Identificador Proposto:** CVE-2025-XXXXX (em processo de submissão)

## Fontes

[github](https://github.com/azurejoga/Linkedin-Automatic-Attack-Simulation)