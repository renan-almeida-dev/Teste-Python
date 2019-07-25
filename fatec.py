# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import requests
import sys
from tabulate import tabulate

__author__ = "Renan Almeida"
__email__ = "renan.almeida@protonmail.com"

def main():
    url = "https://www.vestibularfatec.com.br/classificacao/lista.asp"
    lista_candidatos = []
    cabecalho = ["Classificação", "Nº Inscrição", "Nome", "Nota", "Situação"]
    
    dados_post = {
        "CodEscolaCurso" : "2301",
        "o" : "",
        "codfatec" : "60"
    }    
    
    print("[*] Bem vindo!")
    print("[*] Capturando código-fonte do site...")
    
    try:
        codigo_fonte = requests.post(url, data=dados_post).content  
    except Exception as e:
        print(e)
        sys.exit(1)
    
    else:
        print("[*] Utilizando parsing para capturar o conteúdo...")
        soup = BeautifulSoup(codigo_fonte, "html.parser")
        
        for index_linhas, linhas in enumerate(soup.findAll("tr")):
            candidato = []
            
            if index_linhas == 0:
                continue
            
            elif index_linhas <= 10:
                for linha in linhas.findAll("td"):
                    candidato.append(linha.get_text())       
                else:
                    lista_candidatos.append(candidato)
            
            else:
                print("[*] Dados obtidos, gerando tabela...")
                break
            
        print("\n")
        print(tabulate(lista_candidatos, cabecalho))
        print("\n[*] Saindo do programa...")
        sys.exit(1)

if __name__ == '__main__':
    main()
