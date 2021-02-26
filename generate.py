import csv

str1 = r"""
\begin{tcolorbox}[notitle,grow to right by=1in,boxrule=0pt,colback=DarkRed,colframe=DarkRed]
    \fontsize{1cm}{0.9cm}\selectfont
    \raggedleft
    \noindent
    %s\\
    \Large
    %s\\
    %s
\end{tcolorbox}
\begin{center}
    \includegraphics[height=0.65\textheight]{p-1_%d.jpg}
\end{center}
\clearpage

"""
test = open("./part/pic-import.tex",mode="w",encoding="utf-8")
with open("./photos.book/album.csv",mode="r",encoding="utf-8") as f:
    reader = list(csv.reader(f))
    for i in range(106):
        reader[i+1].append(i+1)
        test.write(str1%tuple(reader[i+1]))
test.close

# f1 = open("./part/pic-import.tex",mode="r",encoding="utf-8")
# content = f1.read()
# f1.close()

# rep = content.replace(r'    \\','')
# with open("./part/pic-import.tex",mode="w",encoding="utf-8") as f2:
#     f2.write(rep)



# \fontsize{1.2cm}{1.08cm}\selectfont
# \noindent
# 父亲~杨光斗\\
# \Large
# 1960\\
# 照片是父亲逝世后，胞妹淑熙保存的遗照
# \begin{center}
#     \includegraphics[height=0.6\textheight]{p-1_1.jpg}
#         %\caption{父亲~杨光斗-1908\textasciitilde{}1960-照片是父亲逝世后，胞妹淑熙保存的遗照}
# \end{center}


# \clearpage