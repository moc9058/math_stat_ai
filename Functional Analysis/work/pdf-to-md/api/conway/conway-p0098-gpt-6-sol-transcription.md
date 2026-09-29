also true that $1\geq x(n)\geq 0$ for all $n$. But then $\|1-x\|_\infty\leq 1$ and $L(1-x)=1-L(x)>1$, contradicting (a). Thus (c) holds.

Now assume that $\mathbf F=\mathbf C$. Let $L_1$ be the functional obtained on $l_{\mathbf R}^{\infty}$. If $x\in l_{\mathbf C}^{\infty}$, then $x=x_1+ix_2$ where $x_1,x_2\in l_{\mathbf R}^{\infty}$. Define $L(x)=L_1(x_1)+iL_1(x_2)$. It is left as an exercise to show that $L$ is $\mathbf C$-linear. It’s clear that (b), (c), and (d) hold. It remains to show that $\|L\|=1$.

Let $E_1,\ldots,E_m$ be pairwise disjoint subsets of $\mathbf N$ and let $\alpha_1,\ldots,\alpha_m\in\mathbf C$ with $|\alpha_k|\leq 1$ for all $k$. Put $x=\sum_{k=1}^{m}\alpha_k\chi_{E_k}$; so $x\in l^\infty$ and $\|x\|_\infty\leq 1$. Then $L(x)=\sum_k\alpha_kL(\chi_{E_k})=\sum_k\alpha_kL_1(\chi_{E_k})$. But $L_1(\chi_{E_k})\geq 0$ and $\sum_kL_1(\chi_{E_k})=L_1(\chi_E)$, where $E=\bigcup_kE_k$. Hence $\sum_kL_1(\chi_{E_k})\leq 1$. Because $|\alpha_k|\leq 1$ for all $k$, $|L(x)|\leq 1$. If $x$ is an arbitrary element of $l^\infty$, $\|x\|_\infty\leq 1$, then there is a sequence $\{x_n\}$ of elements of $l^\infty$ such that $\|x_n-x\|_\infty\to 0$, $\|x_n\|_\infty\leq 1$, and each $x_n$ is the type of element of $l^\infty$ just discussed that takes on only a finite number of values (Exercise 3). Clearly, $\|L\|\leq 2$, so $L(x_n)\to L(x)$. Since $|L(x_n)|\leq 1$ for all $n$, $|L(x)|\leq 1$. Hence $\|L\|\leq 1$. Since $L(1)=1$, $\|L\|=1$. ■

A linear functional of the type described in Theorem 7.1 is called a *Banach limit*. They are useful for a variety of things, among which is the construction of representations of the algebra of bounded operators on a Hilbert space.

## Exercises

1. If $L$ is a Banach limit, show that there are $x$ and $y$ in $l^\infty$ such that $L(xy)\neq L(x)L(y)$.

2. Let $X$ be a set and $\Omega$ a $\sigma$-algebra of subsets of $X$. Suppose $\mu$ is a complex-valued countably additive measure defined on $\Omega$ such that $\|\mu\|=\mu(X)<\infty$. Show that $\mu(\Delta)\geq 0$ for every $\Delta$ in $\Omega$. (Though it is difficult to see at this moment, this fact is related to the proof of (c) in Theorem 7.1 for the complex case.)

3. Show that if $x\in l^\infty$, $\|x\|_\infty\leq 1$, then there is a sequence $\{x_n\}$, $x_n$ in $l^\infty$ such that $\|x_n\|_\infty\leq 1$, $\|x_n-x\|_\infty\to 0$, and each $x_n$ takes on only a finite number of values.

## §8*. An Application: Runge’s Theorem

The symbol $\mathbf C_\infty$ denotes the extended complex plane.

**8.1. Runge’s Theorem.** *Let $K$ be a compact subset of $\mathbf C$ and let $E$ be a subset of $\mathbf C_\infty\setminus K$ that meets each component of $\mathbf C_\infty\setminus K$. If $f$ is analytic in a neighborhood of $K$, then there are rational functions $f_n$ whose only poles lie in $E$ such that $f_n\to f$ uniformly on $K$.*

The main tool in proving Runge’s Theorem is Theorem 6.13. (A proof that does not use functional analysis can be found on p. 189 of Conway [1978].) To do this, let $R(K,E)$ be the closure in the space $C(K)$ of the rational functions with poles in $E$. By (6.13) and the Riesz Representation Theorem,
