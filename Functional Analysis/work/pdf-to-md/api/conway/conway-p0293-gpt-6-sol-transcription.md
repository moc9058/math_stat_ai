then $\psi\in L^{2}(\mu)$ and $A(\psi)=AM_{\psi}1=M_{\psi}A1=M_{\psi}\phi=\phi\psi$. Also, $\|\phi\psi\|_{2}=\|A\psi\|_{2}\leq\|A\|\|\psi\|_{2}$.

Let $\Delta_{n}=\{x\in X:|\phi(x)|\geq n\}$. Putting $\psi=\chi_{\Delta_{n}}$ in the preceding argument gives

$$
\|A\|^{2}\mu(\Delta_{n})
=\|A\|^{2}\|\psi\|^{2}
\geq\|\phi\psi\|^{2}
=\int_{\Delta_{n}}|\phi|^{2}\,d\mu
\geq n^{2}\mu(\Delta_{n}).
$$

So if $\mu(\Delta_{n})\neq0$, $\|A\|\geq n$. Since $A$ is bounded, $\mu(\Delta_{n})=0$ for some $n$; equivalently, $\phi\in L^{\infty}(\mu)$. But $A=M_{\phi}$ on $L^{\infty}(\mu)$ and $L^{\infty}(\mu)$ is dense in $L^{2}(\mu)$, so $A=M_{\phi}$ on $L^{2}(\mu)$.

*Case 2:* $\mu(X)=\infty$. If $\mu(\Delta)<\infty$, let $L^{2}(\mu|\Delta)=\{f\in L^{2}(\mu):f=0\text{ off }\Delta\}$. For $f$ in $L^{2}(\mu|\Delta)$, $Af=A\chi_{\Delta}f=\chi_{\Delta}Af\in L^{2}(\mu|\Delta)$. Let $A_{\Delta}$ be the restriction of $A$ to $L^{2}(\mu|\Delta)$. By Case 1, there is a $\phi_{\Delta}$ in $L^{\infty}(\mu|\Delta)$ such that $A_{\Delta}=M_{\phi_{\Delta}}$. Now if $\mu(\Delta_{1})<\infty$ and $\mu(\Delta_{2})<\infty$, $\phi_{\Delta_{1}}|\Delta_{1}\cap\Delta_{2}=\phi_{\Delta_{2}}|\Delta_{1}\cap\Delta_{2}$ (Exercise).

Write $X=\bigcup_{n=1}^{\infty}\Delta_{n}$, where $\Delta_{n}\in\Omega$ and $\mu(\Delta_{n})<\infty$. From the argument above, if $\phi(x)=\phi_{\Delta_{n}}(x)$ when $x\in\Delta_{n}$, $\phi$ is a well-defined measurable function on $X$. Now $\|\phi_{\Delta}\|_{\infty}=\|M_{\phi_{\Delta}}\|$ (II.1.5) $=\|A_{\Delta}\|\leq\|A\|$; hence $\|\phi\|\leq\|A\|$. It is easy to check that $A=M_{\phi}$. ■

The next result will enable us to solve a number of problems concerning normal operators. It can be considered as a result that removes a technicality, but it is much more than that.

**6.7. The Fuglede–Putnam Theorem.** *If $N$ and $M$ are normal operators on $\mathcal H$ and $\mathcal K$, and $B:\mathcal K\to\mathcal H$ is an operator such that $NB=BM$, then $N^{*}B=BM^{*}$.*

**Proof.** Note that it follows from the hypothesis that $N^{k}B=BM^{k}$ for all $k\geq0$. So if $p(z)$ is a polynomial, $p(N)B=Bp(M)$. Since for a fixed $z$ in $\mathbb C$, $\exp(izN)$ and $\exp(izM)$ are limits of polynomials in $N$ and $M$, respectively, it follows that $\exp(i\bar zN)B=B\exp(i\bar zM)$ for all $z$ in $\mathbb C$. Equivalently, $B=e^{-i\bar zN}Be^{i\bar zM}$. Because $\exp(X+Y)=(\exp X)(\exp Y)$ when $X$ and $Y$ commute, the fact that $N$ and $M$ are normal implies that

$$
\begin{aligned}
f(z)&\equiv e^{-izN^{*}}Be^{izM^{*}}\\
&=e^{-izN^{*}}e^{-i\bar zN}Be^{i\bar zM}e^{izM^{*}}\\
&=e^{-i(zN^{*}+\bar zN)}Be^{i(\bar zM+zM^{*})}.
\end{aligned}
$$

But for every $z$ in $\mathbb C$, $zN^{*}+\bar zN$ and $zM^{*}+\bar zM$ are hermitian operators. Hence $\exp[-i(zN^{*}+\bar zN)]$ and $\exp[i(zM^{*}+\bar zM)]$ are unitary (Exercise 2.14). Therefore $\|f(z)\|\leq\|B\|$. But $f:\mathbb C\to\mathcal B(\mathcal K,\mathcal H)$ is an entire function. By Liouville’s Theorem, $f$ is constant.

Thus, $0=f'(z)=-iN^{*}e^{-izN^{*}}Be^{izM^{*}}+ie^{-izN^{*}}BM^{*}e^{izM^{*}}$. Putting $z=0$ gives $0=-iN^{*}B+iBM^{*}$, whence the theorem. ■

This theorem was originally proved in Fuglede [1950] under the
