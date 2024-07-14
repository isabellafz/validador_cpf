import re
import numpy as np 



cpf = '877.585.750-21'


def validar_cpf(cpf: str) -> None:
    
    cpf_numerico = re.sub("[^0-9]", "", cpf)
    cpf_como_np = np.array([int(i) for i in cpf_numerico])
    numeros_dez_a_dois = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2])
    numeros_onze_a_dois = np.array([11, 10, 9, 8, 7, 6, 5, 4, 3, 2])
    primeiro_digito_valido = sum(cpf_como_np[0:9] * 10* numeros_dez_a_dois) % 11
    segundo_digito_valido = sum(cpf_como_np[0:10] * 10* numeros_onze_a_dois) % 11
    
    if cpf_como_np[9] == primeiro_digito_valido and cpf_como_np[10] == segundo_digito_valido:
        return "Cpf válido"
    else:
        return "Cpf inválido"
    
    
teste = validar_cpf('877.585.750-21')


print (teste)