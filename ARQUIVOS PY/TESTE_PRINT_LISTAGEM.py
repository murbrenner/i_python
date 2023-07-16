import PyPDF2
import pandas as pd
import os

# Abrir o arquivo PDF
pdf_file = open('C:\\Users\\ocmvc45555\\Downloads\\relatorio(602).pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Ler o arquivo CSV
csv_file = pd.read_csv('C:\\Users\\ocmvc45555\Documents\\iMacros\\Datasources\\gerar_relat.csv')

for i in csv_file.index:
    seq = (str(csv_file['SEQ'][i]))

# Loop pelas palavras-chave no arquivo CSV
    for keyword in csv_file[seq]:
        # Loop pelas páginas do arquivo PDF
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            # Verificar se a palavra-chave está na página
            if keyword in page.extractText():
                # Imprimir a página
                os.startfile('Painel de Controle\\Todos os Itens do Painel de Controle\\Dispositivos e Impressoras') # Coloque aqui o caminho da impressora
                printer_name = '\\\\SAMSUNG CADASTRO' # Coloque aqui o nome da impressora
                os.startfile(pdf_file.name, 'print', printer_name) # Imprime o arquivo PDF na impressora

# Fechar o arquivo PDF
pdf_file.close()