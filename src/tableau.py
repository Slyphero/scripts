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

    print(('\\begin{center}\n'
        '\\begin{tabular}{|c||c||c||c|c|}\n'
        '\\hline\n'
        f'{elts[0]} & {elts[1]} & {elts[2]} & {elts[3]} & {elts[4]} \\\\\n'
        '\\hline\n'
        f'{elts[5]} & {elts[6]} & {elts[7]} & {elts[8]} & {elts[9]} \\\\\n'
        '\\hline\n'
        '\\end{tabular}\n'
        '\\end{center}\n'))
    
while True:
    print_tableau()