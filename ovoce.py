"Martinuv komentar"
ovoce = ['banan', 'jablko', 'hruska', 'citron']
  
for plod in ovoce:
  print(plod)
  
for i in range(0, len(ovoce)):
  print(ovoce[i])
  
for i, plod in enumerate(ovoce):
  print(i, plod)
  
vsechno = ''
for plod in ovoce:
  vsechno = vsechno + plod
print(vsechno)

"pomoci mezery mi spoj prvky ovoce"
print(' '.join(ovoce))

"Definice funkce ""Palindromy"", porovnavam prvni index"
"s poslednim, druhy s predposlednim , az se setkaji v pulce"
def is_palindrome(s):

"""

Return True if the string s is a palindrom
(string) -> bool

>>> is_palindrome('hugo')
False
>>> is_palindrome('jelenovipivonelej')
True

return s == s[::1]
"""

for i in range(0, len(s)//2): """dve lomitka pro cele deleni"""
  if s[i] != s[-i-1]:
    return False
return True

"""Nechceme ho pouzit jako vstupni bod nasi aplikace, podivat se na to presne"""
if __name__=='__main__':
  import doctest
  """Pokud najde >>> udela z toho testovaci pripad"""
  doctest.tesmod()