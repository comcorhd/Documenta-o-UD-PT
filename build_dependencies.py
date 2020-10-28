label = "dep:"

phrase = '''
1	A	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	_	_
2	casa	casa	NOUN	_	Gender=Fem|Number=Sing	8	nsubj	_	_
3	de	de	ADP	_	_	4	case	_	_
4	que	que	PRON	_	_	6	obj	_	_
5	eu	eu	PRON	_	Case=Nom|Gender=Unsp|Number=Sing|Person=1|PronType=Prs	6	nsubj	_	_
6	gosto	gostar	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	2	acl:relcl	_	_
7	é	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	cop	_	_
8	amarela	amarelo	PRON	_	Gender=Fem|Number=Sing|PronType=Dem	0	root	_	SpaceAfter=No
9	.	.	PUNCT	_	_	2	punct	_	SpacesAfter=\r\n
'''.strip().replace("%", "\\%")

def main(phrase, label=""):
    tex = "\\begin{figure}[H]"
    tex += "\n\t\\centering"
    tex += "\n\t\\vspace{.8cm}"
    tex += "\n\t\\begin{dependency}"
    tex += "\n\t\t\\begin{deptext}"
    tex += "\n\t\t\t"
    dic_tokens = {}
    tokens = []
    for t, linha in enumerate(phrase.splitlines()):
        if not '-' in linha.split("\t")[0]:
            tokens.append(linha.split("\t")[3])
    tex += " \\& ".join(tokens)
    tokens = []
    tex += " \\\\\n\t\t\t"
    i = 0
    for t, linha in enumerate(phrase.splitlines()):
        if not '-' in linha.split("\t")[0]:    
            tokens.append(linha.split("\t")[1])
            dic_tokens[linha.split("\t")[0]] = (t, i)
            i += 1
    tex += " \\& ".join(tokens)
    tokens = []
    tex += " \\\\\n\t\t\t"
    for t, linha in enumerate(phrase.splitlines()):
        if not '-' in linha.split("\t")[0]:
            tokens.append(linha.split("\t")[2])
    tex += " \\& ".join(tokens)
    tex += " \\\\\n\t\t\t"
    tex += " \\& ".join(("|"*(len([x for x in dic_tokens])-1)).split("|"))
    tex += " \\\\\n\t\t\t"
    tex += " \\& ".join(("|"*(len([x for x in dic_tokens])-1)).split("|"))
    tex += " \\\\"
    tex += "\n\t\t\\end{deptext}"
    for id, a in dic_tokens.items():
        if not '-' in id:
            if phrase.splitlines()[a[0]].split("\t")[7] != "root" and phrase.splitlines()[a[0]].split("\t")[6] in dic_tokens:
                tex += "\n\t\t\\depedge{" + str(dic_tokens[phrase.splitlines()[a[0]].split("\t")[6]][1]+1) + "}{" + str(a[1]+1) + "}{" + phrase.splitlines()[a[0]].split("\t")[7] + "}"
            else:
                tex += "\n\t\t\\deproot{" + str(a[1]+1) + "}{root}"
    tex += "\n\t\\end{dependency}"
    tex += "\n\t\\caption{" + " ".join([x.split("\t")[1] for x in phrase.splitlines() if not '-' in x.split("\t")[0]]) + "}"
    tex += "\n\t\\label{" + label + "}"
    tex += "\n\\end{figure}"
    return tex

if __name__ == "__main__":
    print(main(phrase, label))
