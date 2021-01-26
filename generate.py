str1 = r"""
\begin{figure}
    \begin{center}
        \includegraphics[height=0.75\textheight]{p-1_%d.jpg}
        \caption{}
    \end{center}
\end{figure}

\clearpage

"""
test = open("./part/pic-import.tex",mode="w")
for i in range(102):
    test.write(str1%(i+1))
test.close