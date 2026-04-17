#one loop inside another loop

for i in range(3):
    print("outer loop")


    for j in range(3):
      print("    inner loop")

print("================================================================================")
print("2nd example")
# 2nd example : one loop inside another loop
i = 4
rows = i
cols = i

matrix = []
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(2)
    matrix.append(row)

for row in matrix:
    print(' '.join(map(str, row)))

