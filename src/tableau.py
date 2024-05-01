import textwrap

def print_tableau():
    saisie = input("Saisir données : ")
    saisie_splited = saisie.split()
    n = len(saisie_splited)
    elts = []
    text = ""

    for i in range(n):
        if saisie_splited[i].isnumeric():
            if not saisie_splited[i - 1].isnumeric() and i > 0:
                elts.append(text)
                text = ""
            elts.append(saisie_splited[i])
        else:
            if text == "":
                text += saisie_splited[i]
            else:    
                text = text + " " + saisie_splited[i]
    elts.append(text)

    message_string = r'{sans_vote} & {abstentions} & {contres} & {pour} & {message} \\'

    # Fonction anonyme formattant la string de message
    message_formatter = lambda sans_vote, abstentions, contres, pour, message: message_string.format(
        sans_vote=sans_vote, abstentions=abstentions, contres=contres, pour=pour, message=message)

    # Formule LaTeX pour le tableau
    formula_string = textwrap.dedent(r'''
    \begin{center}
    \begin{tabular}{|c||c||c||c|c|}
    \hline
    $$1$$
    \hline
    $$2$$
    \hline
    \end{tabular}
    \end{center}
    ''')

    # Remplace dans la formule du tableau les caractères spéciaux assignés pour ça
    # par un message formatté
    formatted_string = formula_string.replace('$$1$$', message_formatter(*elts[0:5]))
    formatted_string = formatted_string.replace('$$2$$', message_formatter(*elts[5:]))

    # Affiche la forule LaTeX formattée
    print(formatted_string)
    
while True:
    print_tableau()