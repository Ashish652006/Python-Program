rows=int(input("Enter no. of rows"))
cols=int(input("Enter number of columns"))
matrix=[]
print("Enter the elements row by row");
for i in range(rows):
    row=[]
for j in range(cols):
    value=int(input(f"Element at position({i},{j})"))
    row.append(value)
    matrix.append(row)
print("\nMatrix")
for row in matrix:
    print(row)
    search_element=int(input("\nEnter the element to search"))
found=False
for i in range(rows):
 for j in range(cols):
  if matrix[i][j]==search_element:
   print(f"{search_element} found at position({i},{j})")
   found = True 
 break
if not found:
 print(f"{search_element} not found in the matrix")