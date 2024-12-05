import os, sys
import pyaes

# caminho do diretorio escolhido recebido 
if len(sys.argv) > 1:
        diretorio = sys.argv[1]
else:
        print("""Modo de uso: 
        python3 dencrypter.py /nome-diretorio
""")
        exit()

## defininindo chave de criptografia
key = b"testeransomwares"

## passar por todos os arquivos
for file_name in os.listdir(diretorio):
        caminho_ar = os.path.join(diretorio, file_name)

        # verificar se o arquivo tem a extensao
        if os.path.isfile(caminho_ar) and file_name.endswith('.ransomwaretroll'):
                # abrir o arquivo criptografado
                with open(caminho_ar, "rb") as file:
                        crypto_data = file.read()
                        file.close()

                ## chave para descriptografia
                aes = pyaes.AESModeOfOperationCTR(key)
                # descriptografia dos arquivos
                decrypt_data = aes.decrypt(crypto_data)

                ## criar o arquivo descriptografado
                base_name, ext = os.path.splitext(file_name)
                new_file_name = os.path.join(diretorio, base_name)
                with open(new_file_name, "wb") as new_file:
                        new_file.write(decrypt_data)
                        new_file.close()
                #remover o arquivo criptografado
                os.remove(caminho_ar)
