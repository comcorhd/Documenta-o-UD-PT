label = "dep:quantomaiormenor"

phrase = '''
1	Quanto	quanto	ADV	_	_	2	advmod	_	_
2	maior	maior	ADJ	_	Gender=Fem|Number=Sing	4	amod	_	_
3	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	4	det	_	_
4	concentração	concentração	NOUN	_	Gender=Fem|Number=Sing	10	advcl	_	_
7	,	,	PUNCT	_	_	8	punct	_	_
8	menor	pequeno	ADJ	_	Gender=Fem|Number=Sing	10	amod	_	_
9	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	10	det	_	_
10	invasão	invasão	NOUN	_	Gender=Fem|Number=Sing	0	root	_	_
11	de	de	ADP	_	_	12	case	_	_
12	filtrado	filtrado	NOUN	_	Gender=Masc|Number=Sing	10	nmod	_	SpaceAfter=No
'''.strip()

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
print(tex)