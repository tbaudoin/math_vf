# syllabus_2

# Bugs

L'externalisation des tikz pose problème si on utilise des tikz dans des tableaux. Pour l'instant il faut utiliser la structure suivante

```
\tikzexternaldisable
\begin{tblr}{}
content
\end{tblr}
\tikzexternalenable
```
