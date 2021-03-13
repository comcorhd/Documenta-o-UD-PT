# Guidelines das guidelines UD-PT

Repositório de trabalho para preparação da Documentação UD em português (e para língua portuguesa).

Para consultar a última versão da documentação:
[http://comcorhd.letras.puc-rio.br/Documenta-o-UD-PT/](http://comcorhd.letras.puc-rio.br/Documenta-o-UD-PT/)

* [Para lançar nova versão](#para-lancar-nova-versao)
* [Guidelines](#guidelines)
    * [Chapter, section, subsection, label, caption e fullref](#chapter-section-subsection-label-caption-e-fullref)
    * [Aspas e itálico](#aspas-e-itálico)
    * [Citações](#citações)
    * [Maiúsculas e minúsculas](#maiúsculas-e-minúsculas)
    * [Representação de sentenças](#representação-de-sentenças)


## Para lançar nova versão

`cp main.pdf Documenta-o-UD-PT.pdf`

## Guidelines

### Chapter, section, subsection, label, caption e fullref

1) Adicionar **label** para todas as tabelas, figuras, frases, capítulos, seções e subseções, e **caption** para todas as tabelas, figuras e frases, no formato:

```LaTeX
\label{tab/fig/dep/sec:nome}
\caption{}
```

Exemplo:

```LaTeX
\label{fig:example}
\caption{Figura ilustrativa}
```

2) **Captions** de frases e nomes de **chapters**/**sections**/**subsections** devem ter a expressão em foco em itálico:

```LaTeX
\caption{João \emph{começou a fazer} o dever de casa}
```

```LaTeX
\subsection{Verbo \emph{ser} como verbo pleno}
```

3) Adicionar referência para todas as tabelas, figuras, frases, seções e subseções:

```LaTeX
Como na \fullref{fig:example}, ...
```

Resultado: `Como na Figura 1: Figura ilustrativa, ...`

4) **Não** adicione ponto final nos captions para que ele possa ser lido como referência.

### Aspas e itálico

1) **Não** utilizar aspas na documentação, pois elas não são decodificadas pelo LaTeX. Substituir pelo comando *say*:

```LaTeX
\say{Citação importante de um filósofo}
```

Resultado: `"Citação importante de um filósofo"`

2) Utilizar \say{aspas} para palavras e lemas que quero representar, e \emph{itálico} para as outras anotações (pos, deprel, etc.):

```LaTeX
Apenas os verbos \say{ser} e \say{estar} são considerados verbos de ligação, e portanto serão sempre anotados como \emph{AUX}.
```

Resultado: Apenas os verbos "ser" e "estar" são considerados verbos de ligação, e portanto serão sempre anotados como *AUX*.

- Exceto no caso de **caption** e **chapters**/**section**/**subsection**, como visto na [Seção Chapter, section, subsection, label, caption e fullref](#chapter-section-subsection-label-caption-e-fullref), pois o LaTeX não aceita aspas dentro desses lugares, portanto deixamos em itálico as palavras que queremos destacar, e não com aspas.

### Citações

1) Citações devem seguir o nome no arquivo **localbibliography.bib**, por exemplo:

```
@inproceedings{mcdonald2013universal,
  title={Universal dependency annotation for multilingual parsing},
  author={McDonald, Ryan and Nivre, Joakim and Quirmbach-Brundage, Yvonne and Goldberg, Yoav and Das, Dipanjan and Ganchev, Kuzman and Hall, Keith and Petrov, Slav and Zhang, Hao and Oscar, T and others},
  booktitle={Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
  pages={92--97},
  year={2013}
}
```

Como citar:

1) `\citep{mcdonald2013universal}`

2) `\citet{mcdonald2013universal}`

Resultado 1: `(McDonald et al. 2013)`

Resultado 2: `McDonald et al. 2013`

### Maiúsculas e minúsculas

1) Colunas UD são representadas em minúsculas (upos, deprel, etc.)

2) upos são maiúsculas (VERB, AUX, etc.)

3) deprel são minúsculas (ccomp, xcomp, etc.)

### Representação de sentenças

1) Sentenças ideais que representam algum fenômeno podem ser desenhadas utilizando o pacote `tikz-dependency`, cortando a sentença para caber horizontalmente na página.

2) Sentenças de anotação complexa devem ter uma imagem (com rótulo `fig:`) da anotação completa, tendo em realce as linhas de destaque.

3) Para facilitar a montagem de uma sentença utilizando o `tikz-dependency`, utilize o script `build_dependencies.py` da seguinte forma:

  (a) Abra o arquivo `build_dependencies.py` com algum editor de texto;

  (b) Edite as variáveis `label` (com o nome do rótulo da dependência, que deve começar com `dep:`), e `phrase`, com o trecho do arquivo CoNLL-U que deseja representar utilizando a árvore de dependências;

  (c) Salve o script com as modificações e execute-o:

    $ python3 build_dependencies.py

  (d) Cole o resultado no arquivo do LaTeX e edite o `caption` para deixar em itálico a palavra que deve estar em foco na sentença.
