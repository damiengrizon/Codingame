```python
t = t.upper()

for i in range(h):
    row = input()
    ligneCaractere = ""
    
    for j in t:
        if ord(j) < 65:
            index = 26
        elif ord(j) > 123:
            index = 26 
        else: 
            index = ord(j) -65
        debutLettre = index*l
        finLettre = index*l + l
        ligneCaractere += row[debutLettre : finLettre]

    print(ligneCaractere)
```
