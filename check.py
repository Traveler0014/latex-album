f1 = open("./part/pic-import.tex",mode="r",encoding="utf-8")
content = f1.read()
f1.close()

rep = content.replace(r'    \\','')
with open("./part/pic-import.tex",mode="w",encoding="utf-8") as f2:
    f2.write(rep)
