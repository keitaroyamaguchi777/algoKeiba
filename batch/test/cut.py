
f = open("data.txt", "w", encoding="UTF-8")

f.write(
"""sample
  sample2
    sample3""")

print(f)
f.close()

# add
f = open("data.txt", "a", encoding="UTF-8")
f.write("add")
print(f)


