denote the restriction by $F_E:L^p(\mu|E)\to\mathbb F$. Clearly $F_E$ is bounded and $\|F_E\|\leqslant\|F\|$ for every $E$ in $\mathcal E$.

By Case 1, for every $E$ in $\mathcal E$ there is a $g_E$ in $L^q(\mu|E)$ such that for $f$ in $L^p(\mu|E)$,

$$
\text{B.3}\qquad F(f)=\int_E fg_E\,d\mu\ \text{and}\ \|g_E\|_q\leqslant\|F\|.
$$

If $D,E\in\mathcal E$, then $L^p(\mu|D\cap E)$ is contained in both $L^p(\mu|D)$ and $L^p(\mu|E)$. Moreover, $F_D|L^p(\mu|D\cap E)=F_E|L^p(\mu|D\cap E)=F_{D\cap E}$. Hence $g_D=g_E=g_{D\cap E}$ a.e. $[\mu]$ on $D\cap E$. Thus, a function $g$ can be defined on $\bigcup\{E:E\in\mathcal E\}$ by letting $g=g_E$ on $E$; put $g=0$ off $\bigcup\{E:E\in\mathcal E\}$. A difficulty arises here in trying to show that $g$ is measurable.

*Case 2a: $1<p<\infty$.* Put $\sigma=\sup\{\|g_E\|_q:E\in\mathcal E\}$; so $\sigma\leqslant\|F\|<\infty$. Since $\|g_D\|_q\leqslant\|g_E\|_q$ if $D\subseteq E$, there is a sequence $\{E_n\}$ in $\mathcal E$ such that $E_n\subseteq E_{n+1}$ for all $n$ and $\|g_{E_n}\|_q\to\sigma$. Let $G=\bigcup_{n=1}^{\infty}E_n$. If $E\in\mathcal E$ and $E\cap G=\square$, then $\|g_{E\cup E_n}\|_q^q=\|g_E\|_q^q+\|g_{E_n}\|_q^q\to\|g_E\|_q^q+\sigma^q$; thus $g_E=0$. Therefore $g=0$ off $G$ and clearly $g$ is measurable. Moreover, $g\in L^q(\mu)$ with $\|g\|_q=\sigma$.

If $f\in L^p(\mu)$, then $\{x:f(x)\ne0\}=\bigcup_{n=1}^{\infty}D_n$ where $D_n\in\mathcal E$ and $D_n\subseteq D_{n+1}$ for all $n$. Thus $\chi_{D_n}f\to f$ in $L^p(\mu)$ and so $F(f)=\lim F(\chi_{D_n}f)\overset{\text{(B.3)}}{=}\lim\int_{D_n}gf\,d\mu=\int gf\,d\mu$. Thus $F=F_g$ and $\|F\|=\|F_g\|\leqslant\|g\|_q\leqslant\sigma\leqslant\|F\|$.

*Case 2b: $p=\infty$ and $(X,\Omega,\mu)$ is $\sigma$-finite.* This is left to the reader. ■

## EXERCISE

Look at the proof of the theorem and see if you can represent $L^1(X,\Omega,\mu)^*$ for an arbitrary measure space.
