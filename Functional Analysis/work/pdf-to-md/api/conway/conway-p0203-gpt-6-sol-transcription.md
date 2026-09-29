If $\mathcal A$ has an identity, $e$, then it is assumed that $\|e\|=1$.

The fact that (1.2) is satisfied is not essential. If $\mathcal A$ is an algebra and has a norm relative to which $\mathcal A$ is a Banach space and is such that the map of $\mathcal A\times\mathcal A\to\mathcal A$ defined by $(a,b)\mapsto ab$ is continuous, then there is an equivalent norm on $\mathcal A$ that satisfies (1.2) (Exercise 1).

If $\mathcal A$ has an identity $e$, then the map $\alpha\mapsto\alpha e$ is an isomorphism of $\mathbb F$ into $\mathcal A$ and $\|\alpha e\|=|\alpha|$. So it will be assumed that $\mathbb F\subseteq\mathcal A$ via this identification. Thus the identity will be denoted by 1.

The content of the next proposition is that if $\mathcal A$ does not have an identity, it is possible to find a Banach algebra $\mathcal A_1$ that contains $\mathcal A$, that has an identity, and is such that $\dim\mathcal A_1/\mathcal A=1$.

**1.3. Proposition.** *If $\mathcal A$ is a Banach algebra without an identity, let $\mathcal A_1=\mathcal A\times\mathbb F$. Define algebraic operations on $\mathcal A_1$ by*

(i) $(a,\alpha)+(b,\beta)=(a+b,\alpha+\beta)$;

(ii) $\beta(a,\alpha)=(\beta a,\beta\alpha)$;

(iii) $(a,\alpha)(b,\beta)=(ab+\alpha b+\beta a,\alpha\beta)$.

*Define $\|(a,\alpha)\|=\|a\|+|\alpha|$. Then $\mathcal A_1$ with this norm and the algebraic operations defined in (i), (ii), and (iii) is a Banach algebra with identity $(0,1)$ and $a\mapsto(a,0)$ is an isometric isomorphism of $\mathcal A$ into $\mathcal A_1$.*

**Proof.** Only (1.2) will be verified here; the remaining details are left to the reader. If $(a,\alpha),(b,\beta)\in\mathcal A_1$, then
$$
\begin{aligned}
\|(a,\alpha)(b,\beta)\|
&=\|(ab+\beta a+\alpha b,\alpha\beta)\|\\
&=\|ab+\beta a+\alpha b\|+|\alpha\beta|\\
&\leq\|a\|\|b\|+|\beta|\|a\|+|\alpha|\|b\|+|\alpha||\beta|\\
&=\|(a,\alpha)\|\|(b,\beta)\|.
\end{aligned}
$$
$\blacksquare$

**1.4. Example.** If $X$ is a compact space, then $\mathcal A=C(X)$ is a Banach algebra if $(fg)(x)=f(x)g(x)$ whenever $f,g\in\mathcal A$ and $x\in X$. Note that $\mathcal A$ is abelian and has an identity (the constantly 1 function).

If $X$ is completely regular and $\mathcal A=C_b(X)$, then $\mathcal A$ is also a Banach algebra. In fact, $C_b(X)\cong C(\beta X)$ (V.6) so that this is a special case of Example 1.4. Another special case is $l^\infty$.

**1.5. Example.** If $X$ is a locally compact space, $\mathcal A=C_0(X)$ is a Banach algebra when the multiplication is defined pointwise as in the preceding example. $\mathcal A$ is abelian, but if $X$ is not compact, $\mathcal A$ does not have an identity. If $X_\infty$ is the one-point compactification of $X$, then $C(X_\infty)\supseteq C_0(X)$ and $C(X_\infty)$ is a Banach algebra with identity.

Note that $c_0$ is a special case of Example 1.5.

**1.6. Example.** If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $\mathcal A=L^\infty(X,\Omega,\mu)$, then $\mathcal A$ is an abelian Banach algebra with identity if the operations are defined pointwise.
