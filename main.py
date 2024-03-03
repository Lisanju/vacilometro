import os

def arquivoExisteCheck():
    if (os.path.exists("vacilos.txt")):
        with open("vacilos.txt", "r") as arquivoTxt:
            conteudoTxt = arquivoTxt.read()

    else:
        with open("vacilos.txt", "w") as arquivoTxt:
            arquivoTxt.write("")

arquivoExisteCheck():

