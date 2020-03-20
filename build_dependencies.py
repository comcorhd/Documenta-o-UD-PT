label = "dep:umpronome2"

phrase = '''
5	estamos	estar	VERB	_	Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	_
6	perante	perante	ADP	PRP|@<SC	_	10	case	_	_
7	um	um	PRON	<card>|NUM|M|S|@P<	Gender=Masc|Number=Sing|PronType=Dem	5	obl	_	_
8-9	dos	_	_	_	_	_	_	_	_
8	de	de	ADP	<sam->|PRP|@N<	_	10	case	_	_
9	os	o	DET	<-sam>|<artd>|ART|M|P|@>N	Definite=Def|Gender=Masc|Number=Plur|PronType=Art	10	det	_	_
10	documentos	documento	NOUN	<np-def>|N|M|P|@P<	Gender=Masc|Number=Plur	7	nmod	_	_
11-12	do	_	_	_	_	_	_	_	_
11	de	de	ADP	<sam->|PRP|@N<	_	13	case	_	_
12	o	o	DET	<-sam>|<artd>|ART|M|S|@>N	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	13	det	_	_
13	art.	art.	NOUN	<np-def>|N|M|S|@P<	Gender=Masc|Number=Sing	10	nmod	_	ChangedBy=Issue165|SpaceAfter=No
14	46º	46º	ADJ	ADJ|M|S|@N<	Gender=Masc|Number=Sing	13	amod	_	_
'''.strip()

tex = "\\begin{figure*}[htbp]"
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
tex += "\n\\end{figure*}"
print(tex)