#Bootcamp DIO - Cibersegurança Riachuelo / Autor: Flanubio Ribeiro

from cryptography.fernet import Fernet
import os 

#1 - Carregar a chave do arquivo ".key"
def carregar_chave():
	return open("chave.key", "rb").read()

#2 - Descriptografar arquivos encontrados
def descriptografar_arquivo(arquivo, chave):
	f = Fernet(chave)
	with open(arquivo, "rb") as file:
		dados = file.read()
		dados_descriptografados = f.decrypt(dados)
	with open(arquivo, "wb") as file:
		file.write(dados_descriptografados)

#3 - Encontrar arquivos para descriptografar
def encontrar_arquivos(diretorio):
	lista = []
	for raiz, _, arquivos in os.walk(diretorio):
		for nome in arquivos:
			caminho = os.path.join(raiz, nome)
			if nome != "ransoware.py" and not nome.endswith(".key"):
				lista.append(caminho)
	return lista

#4 - Execução principal
def main():
	chave = carregar_chave()
	arquivos = encontrar_arquivos("arquivos_teste")
	for arquivo in arquivos:
		descriptografar_arquivo(arquivo, chave)
	print("Arquivos descriptografados com sucesso!")

if __name__=="__main__":
	main()
