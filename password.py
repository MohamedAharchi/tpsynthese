# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)  #1 Le mot de passe en paramètre est affecté dans une liste.
    found = False
    i=len(pwd)-1 # i = dernière lettre du mot de passe.
    testZonly = True
    """
    Série de tests pour 'zzzz'
    >>> getNext('zzzzz')
    """
    for i in range(0, len(password)):
        if password[i] != 'z':
           testZonly = False
           break
        else :
            testZonly = True
            i = i + 1
    if testZonly:
        raise Exception('ERREUR !')
    else:
        while not found:
            if pwd[i] < 'z':
                pwd[i] = chr(ord(pwd[i])+1)  #2 Incrémentation de 1 sur le code ASCII de la dernière lettre.
                # ord() récupère le code ASCII du paramètre 
                # chr() traduit le code ASCII en lettre.           
                found = True             
            else:            
                pwd[i] = 'a'
                i = i-1
                pwd[i] = chr(ord(pwd[i])+1)
                found = True        
        return ''.join(pwd) #3 On retourne le nouveau mot de passe.
    # Remarque : join() accepte n’importe quel type de valeur.



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
