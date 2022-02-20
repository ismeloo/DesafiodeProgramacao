def anagramas(asa):  
    if len(asa) <=2:
        return asa 
    else:
        lista = []
        for aux in anagramas(asa[1:]):
            for i in range(len(asa)):
                lista.append(aux[:i] + asa[0:1] + aux[i:])
                
        return lista


anagramas = 'as', 'sa', 'sa', 'aa', 'aa', 'aa'
print(len(anagramas))
print(anagramas)

'''O anagrma "asa", passa para a função "if", junto com  "len()", para retornar quantidade de elementos dsepoi usando o"for" para a função "aux" e trocando os valores  do anagrama para numeros e separando por pares para contar no final'''





