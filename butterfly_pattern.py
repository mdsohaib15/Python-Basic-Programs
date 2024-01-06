# -----------BUTTERFLY PATTERN IN PYTHON----------
rows = 8
# -----------UPPER SECTION---------------
for i in range(rows):
          for j in range(i):
                    print("*",end ="")

          for k in range(2*(rows-i)):
                    print(" ",end="")

          for l in range(i):
                    print("*",end="")
          print()

# -----------LOWER SECTION---------------
for i in range(rows):
          for j in range((rows-1)-i+1):
                    print("*",end="")
          for k in range(2*i):
                    print(" ",end="")
          for l in range((rows-1) - i+1):
                    print("*",end="")
          print()
          