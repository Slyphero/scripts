# scripts
## Tableau de votes
Pour générer automatiquement le code LaTeX du tableau de votes (CR AML)
1. Lancer le script `tableau.py`
2. Taper directement sur la même ligne les 4 votes 
(ne prend pas part, s'abstient, contre, pour) 
le texte puis les 4 autres votes et le dernier texte.
Le script tolère les espaces en trop.

Exemple : 1 0 1 1 Le collège des MA s'abstient 1 0 1 7 L'ordre du jour est approuvé  
donnerait le code du LaTeX suivant :  
```Tex
\begin{center}
\begin{tabular}{|c||c||c||c|c|}
\hline
1 & 0 & 1 & 1 & Le collège des MA s'abstient \\
\hline
1 & 0 & 1 & 7 & L'ordre du jour est approuvé \\
\hline
\end{tabular}
\end{center}
```

