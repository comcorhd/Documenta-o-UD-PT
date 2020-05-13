label = "dep:epp"

phrase = '''
11	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	13	det	_	_
12	seguintes	seguinte	ADJ	_	Gender=Fem|Number=Plur	13	amod	_	_
13	concentrações	concentração	NOUN	_	Gender=Fem|Number=Plur	10	nsubj:pass	_	SpaceAfter=No
14	:	:	PUNCT	_	_	10	punct	_	_
15	petróleo	petróleo	NOUN	_	Gender=Masc|Number=Sing	13	appos	_	_
17	(	(	PUNCT	_	_	19	punct	_	SpaceAfter=No
18	5	5	NUM	_	NumType=Card	19	nummod	_	SpaceAfter=No
19	%	%	SYM	_	_	15	appos:parataxis	_	SpaceAfter=No
20	,	,	PUNCT	_	_	35	punct	_	_
33	e	e	CCONJ	_	_	35	cc	_	_
34	100	100	NUM	_	NumType=Card	35	nummod	_	SpaceAfter=No
35	%	%	SYM	_	_	15	conj	_	_
36	de	de	ADP	_	_	37	case	_	_
37	FSA	FSA	NOUN	_	Gender=Fem|Number=Sing	19	nmod	_	SpaceAfter=No
38	)	)	PUNCT	_	_	43	punct	_	SpaceAfter=No
39	e	e	CCONJ	_	_	40	cc	_	_
40	diesel	diesel	NOUN	_	Gender=Masc|Number=Sing	15	conj	_	_
41	(	(	PUNCT	_	_	43	punct	_	SpaceAfter=No
42	1	1	NUM	_	NumType=Card	43	nummod	_	SpaceAfter=No
43	%	%	SYM	_	_	40	appos:parataxis	_	SpaceAfter=No
44	,	,	PUNCT	_	_	57	punct	_	_
56	32	32	NUM	_	NumType=Card	57	nummod	_	SpaceAfter=No
57	%	%	SYM	_	_	43	conj	_	SpaceAfter=No
'''.strip().replace("%", "\\%")

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