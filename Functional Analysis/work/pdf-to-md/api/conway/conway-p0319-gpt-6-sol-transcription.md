from $\operatorname{cl}[\operatorname{dom}A]$ into $\mathcal K$. So we will often only consider those $A$ such that $\operatorname{dom}A$ is dense in $\mathcal H$; such an operator $A$ is said to be *densely defined*. $\mathcal B(\mathcal H)$ still denotes the bounded operators defined on $\mathcal H$.

If $A,B$ are linear operators from $\mathcal H$ into $\mathcal K$, then $A+B$ is defined with $\operatorname{dom}(A+B)=\operatorname{dom}A\cap\operatorname{dom}B$. If $B:\mathcal H\to\mathcal H$ and $A:\mathcal H\to\mathcal L$, then $AB$ is a linear operator from $\mathcal H$ into $\mathcal L$ with $\operatorname{dom}(AB)=B^{-1}(\operatorname{dom}A)$.

**1.2. Definition.** If $A,B$ are operators from $\mathcal H$ into $\mathcal K$, then $A$ is an *extension* of $B$ if $\operatorname{dom}B\subseteq\operatorname{dom}A$ and $Ah=Bh$ whenever $h\in\operatorname{dom}B$. In symbols this is denoted by $B\subseteq A$.

Note that if $A\in\mathcal B(\mathcal H)$, then the only extension of $A$ is itself. So this concept is only of value for unbounded operators.

If $A:\mathcal H\to\mathcal K$, the *graph* of $A$ is the set

$$
\operatorname{gra}A\equiv\{h\oplus Ah\in\mathcal H\oplus\mathcal K:h\in\operatorname{dom}A\}.
$$

It is easy to see that $B\subseteq A$ if and only if $\operatorname{gra}B\subseteq\operatorname{gra}A$.

**1.3. Definition.** An operator $A:\mathcal H\to\mathcal K$ is *closed* if its graph is closed in $\mathcal H\oplus\mathcal K$. An operator is *closable* if it has a closed extension. Let $\mathcal C(\mathcal H,\mathcal K)=$ the collection of all closed densely defined operators from $\mathcal H$ into $\mathcal K$. Let $\mathcal C(\mathcal H)=\mathcal C(\mathcal H,\mathcal H)$. (It should be emphasized that the operators in $\mathcal C(\mathcal H,\mathcal K)$ are densely defined.)

When is a subset of $\mathcal H\oplus\mathcal K$ a graph of an operator from $\mathcal H$ into $\mathcal K$? If $\mathcal G=\operatorname{gra}A$ for some $A:\mathcal H\to\mathcal K$, then $\mathcal G$ is a submanifold of $\mathcal H\oplus\mathcal K$ such that if $k\in\mathcal K$ and $0\oplus k\in\mathcal G$, then $k=0$. The converse is also true. That is, suppose that $\mathcal G$ is a submanifold of $\mathcal H\oplus\mathcal K$ such that if $k\in\mathcal K$ and $0\oplus k\in\mathcal G$, then $k=0$. Let $\mathcal D=\{h\in\mathcal H:\text{ there exists a }k\text{ in }\mathcal K\text{ with }h\oplus k\text{ in }\mathcal G\}$. If $h\in\mathcal D$ and $k_1,k_2\in\mathcal K$ such that $h\oplus k_1,h\oplus k_2\in\mathcal G$, then $0\oplus(k_1-k_2)=h\oplus k_1-h\oplus k_2\in\mathcal G$. Hence $k_1=k_2$. That is, for every $h$ in $\mathcal D$ there is a unique $k$ in $\mathcal K$ such that $h\oplus k\in\mathcal G$; denote $k$ by $k=Ah$. It is easy to check that $A$ is a linear map and $\mathcal G=\operatorname{gra}A$. This gives an internal characterization of graphs that will be useful in the next proposition.

**1.4. Proposition.** *An operator $A:\mathcal H\to\mathcal K$ is closable if and only if $\operatorname{cl}[\operatorname{gra}A]$ is a graph.*

**Proof.** Let $\operatorname{cl}[\operatorname{gra}A]$ be a graph. That is, there is an operator $B:\mathcal H\to\mathcal K$ such that $\operatorname{gra}B=\operatorname{cl}[\operatorname{gra}A]$. Clearly $\operatorname{gra}A\subseteq\operatorname{gra}B$, so $A$ is closable.

Now assume that $A$ is closable; that is, there is a closed operator $B:\mathcal H\to\mathcal K$ with $A\subseteq B$. If $0\oplus k\in\operatorname{cl}[\operatorname{gra}A]$, $0\oplus k\in\operatorname{gra}B$ and hence $k=0$. By the remarks preceding this proposition, $\operatorname{cl}[\operatorname{gra}A]$ is a graph. $\blacksquare$

If $A$ is closable, call the operator whose graph is $\operatorname{cl}[\operatorname{gra}A]$ the *closure* of $A$.

**1.5. Definition.** If $A:\mathcal H\to\mathcal K$ is densely defined, let
