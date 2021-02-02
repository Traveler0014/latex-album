import csv

str1 = r"""
\begin{figure}
    \begin{center}
        \includegraphics[height=0.75\textheight]{p-1_%d.jpg}
        \caption{%s}
    \end{center}
\end{figure}

\clearpage

"""
test = open("./part/pic-import.tex",mode="w",encoding="utf-8")
with open("./photos.book/album.csv",mode="r",encoding="utf-8") as f:
    reader = list(csv.reader(f))
    for i in range(102):
        test.write(str1%(i+1,'-'.join(reader[i+1])))


test.close