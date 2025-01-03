README: Automação para Abrir Vídeos do YouTube com PyAutoGUI 🎥📺
Descrição do Projeto
Este projeto utiliza a biblioteca PyAutoGUI para automatizar o processo de abrir o navegador, acessar o site do YouTube, realizar uma pesquisa por palavras-chave e selecionar o primeiro vídeo dos resultados. É uma solução simples e eficiente para economizar tempo em tarefas repetitivas relacionadas ao consumo de vídeos.

Recursos
Abertura Automática do YouTube:

O script abre o navegador e acessa o site do YouTube automaticamente.
Pesquisa Dinâmica:

Permite realizar pesquisas no YouTube com termos personalizados.
Seleção de Vídeo:

Simula um clique para reproduzir o primeiro vídeo da pesquisa.
Pré-Requisitos
Python 3.8+

Bibliotecas necessárias:

PyAutoGUI: Para automação de cliques e teclas.
bash
Copiar código
pip install pyautogui
Pyperclip: Para copiar e colar texto com suporte a acentuação.
bash
Copiar código
pip install pyperclip
Resolução padrão do monitor para garantir que as coordenadas fixas funcionem corretamente.

Como Usar
Configurar o Código:

Certifique-se de que o navegador Chrome esteja instalado e acessível pelo comando "chrome".
Substitua as palavras-chave da pesquisa no código, se necessário.
Executar o Script:

Salve o código em um arquivo, por exemplo, abrir_youtube.py.
No terminal, execute:
bash
Copiar código
python abrir_youtube.py
Resultado Esperado:

O navegador será aberto.
O site do YouTube será acessado e a pesquisa será realizada.
O primeiro vídeo dos resultados será clicado e iniciado.
Exemplo do Código
python
Copiar código
import pyautogui as pa
import time
import pyperclip

# Configura o tempo padrão entre ações
pa.PAUSE = 0.5

# Abrir o navegador
pa.press('win')
pa.write('chrome')
pa.press('ENTER')

# Acessar o YouTube
pa.write("https://www.youtube.com")
pa.press('ENTER')
time.sleep(4)

# Pesquisar por "Programação"
pa.click(x=696, y=118)
pyperclip.copy("Programação")
pa.hotkey('ctrl', 'v')
pa.press('ENTER')
time.sleep(2)

# Selecionar o primeiro vídeo
pa.click(x=1007, y=557)
Dicas de Uso e Configuração
Personalização do Termo de Pesquisa:

Alterar o valor em pyperclip.copy("Programação") para o termo desejado.
Ajustar Coordenadas:

Caso as coordenadas fixas (x=696, y=118 ou x=1007, y=557) não funcionem, utilize a função pyautogui.position() para identificar as coordenadas corretas.
Atenção ao Layout:

O script pode precisar de ajustes se houver mudanças no layout do YouTube ou no navegador.
Casos de Uso
Reproduzir vídeos automaticamente em apresentações.
Testar layouts e funcionalidades do YouTube.
Automatizar processos de busca e reprodução para fins educacionais.
