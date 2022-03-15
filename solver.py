word_to_find = "box"

def get_puzzle():
  o = []
  with open("puzzle.txt","r") as file:
    x = file.readlines()
    for i in x:
      o.append(i.split(",")[:-1])
    
  return o


def chunks(lst, n):
  f = []
  for i in range(0, len(lst), n):
    f.append(lst[i:i + n])
  return f

def find_letters_in_list(lst,word):
    c_in = 0
    Out_ = []
    for e,i in enumerate(lst):
        try:
          
            if i == word[c_in]:
                c_in += 1
                Out_.append(e)
                
            else:
                pass
              
        except IndexError:
            pass
    return(Out_)


def transpose(l1, l2):
  for i in range(len(l1[0])):
    row =[]
    for item in l1:
      row.append(item[i])
    l2.append(row)
  return l2
 
  
def solve():
  Rows = []
  C = []
  Column = []
  alr_found = 0
  
  puzzle = get_puzzle()
  for rows in puzzle:
    for letters in rows:
      Rows.append(letters)
  
  for X in range(len(puzzle)-1):
    C.append(str([i[X] for i in puzzle]))
  
  for i in C:
    b_c = i.replace("[","").replace("]","").replace("'","").replace(" ","")
    
    for i in b_c:
      if i == ",":
        pass
      else:
        Column.append(i)
  
  rev_rows = Rows[::-1]
  rev_columns = Column[::-1]
  
  #solving it
  col = 0
  
  Chunk_column = chunks(Column,len(word_to_find)+len(word_to_find))
  Out = Chunk_column
  
  Chunk_column_rev = chunks(Column,len(word_to_find)+len(word_to_find))[::-1]
  Out2 = Chunk_column_rev
  
  
  if word_to_find in "".join(Column).lower():
    for i in Chunk_column:
      if word_to_find in "".join(i).lower():
        l_index = find_letters_in_list(Chunk_column[col],word_to_find.upper())
        for o in l_index:
          Out[col][o] = "("+str(Out[col][o])+")"
          
      else:
        col += 1

  elif word_to_find in "".join(rev_columns).lower():
    for i in Chunk_column_rev:
      if word_to_find[::-1] in "".join(i).lower():
        l_index = find_letters_in_list(Chunk_column[col][::-1],word_to_find.upper())
        
        
        for o in l_index:
          Out[col][o+1] = "("+str(Out[col][o+1])+")"
          
      else:
        col += 1

  #give output
  x = []
  transpose(Out,x)
  return x
  

def user_friendly_data():
  print("output from algorithm:")
  for i in solve():
    print(" ".join(i))
    
user_friendly_data()