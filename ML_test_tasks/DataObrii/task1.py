a=[{6,'A'},(5,'R'),{2:'O'},{1:'C'},[3,'N'],{'hah,trick':{4:'G'}},7,'T',8,'U',9,'L',10,'A',{15:'S'},{14:'N'},{11:'T'},{12:'I'}]

def shifer(a):
  new_a = []
  for i, el in enumerate(a):
    if type(el)==type(set()):
      el = tuple(el)
      new_a.append({el[0]:el[1]})
    if type(el)==type(list()):
      new_a.append({el[0]:el[1]})
    if type(el) == type(int()):
      new_a.append({el:a[i+1]})
    if type(el) == type(dict()) and type(list(el.keys())[0]) == type(int()):
      new_a.append(el)
    if type(el) == type(dict()) and type(list(el.keys())[0]) != type(int()):
      new_a.append(list(el.values())[0])
  
  keys, vals = [], []
  for i in new_a:
      keys.extend(i.keys())
      vals.extend(i.values())

  n_a = []
  for i, j in zip(keys, vals):
      n_a.append([i, j])

  n_a = sorted(n_a)
  s = ''
  for i, j in n_a:
    s = s+ j
  return s

print(shifer(a))
