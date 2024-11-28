#### Imports et définition des variables globales


#### Fonctions secondaires
'''
Exercice ASCII Art
'''

def artcode_i(s):
    '''
    Encode une chaîne en une liste de tuples de manière itérative.
    '''
    c = [s[0]]
    o = [1]
    for i in s[1:]:
        if i == c[-1]:
            o[-1] += 1
        else:
            c.append(i)
            o.append(1)
    return [(c[i],o[i]) for i in range (len(c))]


def artcode_r(s):
    '''
    Encode une chaîne en une liste de tuples de manière récursive.
    '''
    if not s:
        return []
    char = s[0]
    count = 1
    while count < len(s) and s[count] == char:
        count += 1
    return [(char, count)] + artcode_r(s[count:])
#### Fonction principale
def main():
    '''
    appelle les fonctions
    '''
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
