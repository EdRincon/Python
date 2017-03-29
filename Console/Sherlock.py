import re

m = """You know my powers, my dear Watson, and yet at the end of three months
I was forced to confess that I had at last met an antagonist who was my intellectual equal"""

#m = 'aabc'

if len(m) in range (1,100000):
    message = "".join(re.split("[A-Z\\n]*",m))
    count = {}

    for character in message:
        
        count.setdefault(character, 0)
        count[character] = count[character] + 1
        
    lista = list(count.values())
    lista.sort()
        
    for i in lista:

        if (lista[0]) != (lista[i]):
            print ('no funka')

            if (max(lista) - min(lista)) == 1:
                if max(lista) != (lista[(len(lista))-2]):
                    print('but it is fixeable')

            else:
                print('y no es fixeable')
                
            break
        i = i + 1 

        if i >= (len(count.values())):
            print('funka')
            
        
