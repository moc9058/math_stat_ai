$$
\begin{aligned}
&\leq \inf\{\|a^*a(1-x)\|:x\in(\operatorname{ball}I)_+\}\\
&=\inf\{\|a^*a-a^*ax\|:x\in(\operatorname{ball}I)_+\}\\
&=\|a^*a+I\|.
\end{aligned}
\qquad\blacksquare
$$

If $\mathcal A,\mathcal B$ are C*-algebras with ideals $I,J$, respectively, and $\rho:\mathcal A\to\mathcal B$ is a *-homomorphism such that $\rho(I)\subseteq J$, then $\rho$ induces a *-homomorphism $\tilde\rho:\mathcal A/I\to\mathcal B/J$ defined by $\tilde\rho(a+I)=\rho(a)+J$. In particular, if $I=\ker\rho$ and $J=(0)$, then $\tilde\rho:\mathcal A/\ker\rho\to\mathcal B$ is a *-homomorphism and $\tilde\rho\circ\pi=\rho$, where $\pi:\mathcal A\to\mathcal A/\ker\rho$ is the natural map. Keep these facts in mind when reading the proof of the next result.

**4.8. Theorem.** *If $\mathcal A,\mathcal B$ are C*-algebras and $\rho:\mathcal A\to\mathcal B$ is a *-homomorphism, then $\|\rho(a)\|\leq\|a\|$ for all $a$ and $\operatorname{ran}\rho$ is closed in $\mathcal B$. If $\rho$ is a *-monomorphism, then $\rho$ is an isometry.*

**Proof.** The fact that $\|\rho(a)\|\leq\|a\|$ is a restatement of (1.11d). Now assume that $\rho$ is a *-monomorphism. As in the proof of (1.11d), it suffices to assume that $\mathcal A$ and $\mathcal B$ have identities and $\rho(1)=1$. (Why?)

If $a\in\mathcal A$ and $a=a^*$, then it is easy to see that $\rho(a)=\rho(a)^*$ and $\sigma(\rho(a))\subseteq\sigma(a)$. If $\sigma(\rho(a))\ne\sigma(a)$, there is a continuous function $f$ on $\sigma(a)$ such that $f(t)=0$ for all $t$ in $\sigma(\rho(a))$ but $f$ is not identically zero on $\sigma(a)$. Thus $f(\rho(a))=0$, but $f(a)\ne0$. Let $\{p_n\}$ be polynomials such that $p_n(t)\to f(t)$ uniformly on $\sigma(a)$. Thus $p_n(a)\to f(a)$ and $p_n(\rho(a))\to f(\rho(a))=0$. But $p_n(\rho(a))=\rho(p_n(a))\to\rho(f(a))$. Thus $\rho(f(a))=f(\rho(a))=0$. Since $\rho$ was assumed injective, $f(a)=0$, a contradiction. Hence $\sigma(a)=\sigma(\rho(a))$ if $a=a^*$. Thus by (1.11e), $\|a\|=r(a)=r(\rho(a))=\|\rho(a)\|$ if $a=a^*$. But then for arbitrary $a$, $\|a\|^2=\|a^*a\|=\|\rho(a^*a)\|=\|\rho(a)^*\rho(a)\|=\|\rho(a)\|^2$ and $\rho$ is an isometry.

To complete the proof let $\rho:\mathcal A\to\mathcal B$ be a *-homomorphism and let $\tilde\rho:\mathcal A/\ker\rho\to\mathcal B$ be the induced *-monomorphism. So $\tilde\rho$ is an isometry and hence $\operatorname{ran}\tilde\rho$ is closed. But $\operatorname{ran}\tilde\rho=\operatorname{ran}\rho$. $\blacksquare$

We turn now to some specific examples of C*-algebras and their ideals.

**4.9. Proposition.** *If $X$ is compact and $I$ is a closed ideal of $C(X)$, then there is a closed subset $F$ of $X$ such that $I=\{f\in C(X):f(x)=0\text{ for all }x\text{ in }F\}$. Moreover, $C(X)/I$ is isometrically isomorphic to $C(F)$.*

**Proof.** Let $F=\{x\in X:f(x)=0\text{ for all }f\text{ in }I\}$, so $F$ is a closed subset of $X$. If $\mu\in M(X)$ and $\mu\perp I$, then $\int|f|^2\,d\mu=0$ for every $f$ in $I$ since $|f|^2=f\bar f\in I$ whenever $f\in I$. Thus each $f$ must vanish on the support of $\mu$; hence $|\mu|(X\setminus F)=0$. Conversely, if $\mu\in M(X)$ and the support of $\mu$ is contained in $F$, $\int f\,d\mu=0$ for every $f$ in $I$. Thus $I^\perp=\{\mu\in M(X):|\mu|(X\setminus F)=0\}$. Since $I$ is closed, $I={}^{\perp}(I^\perp)=\{f\in C(X):f(x)=0\text{ for all }x\text{ in }F\}$. The remainder of the proof is left to the reader. $\blacksquare$

**4.10. Proposition.** *If $I$ is a closed ideal of $\mathcal B(\mathcal H)$, then $I\supseteq\mathcal B_0(\mathcal H)$ or $I=(0)$.*
