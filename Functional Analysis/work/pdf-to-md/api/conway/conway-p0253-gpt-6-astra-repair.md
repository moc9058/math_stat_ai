238　　　　　　　　　　　　　　　　　VIII. $C^*$-Algebras

is, of course, a function on $\sigma(a)$. [Just evaluate the polynomial at any $z$ in $\sigma(a)$.] The last part of (2.3) says that $\gamma(p(a,a^*))=\tau^\#(p)$. We define a map $\rho\colon C(\sigma(a))\to C^*(a)$ so that the following diagram commutes:

**2.4**
$$
\begin{array}{ccc}
C^*(a)&\xrightarrow{\gamma}&C(\Sigma)\\
{}_{\rho}\nwarrow&&\nearrow_{\tau^\#}\\
&C(\sigma(a))&
\end{array}
$$

Note that if $\mathcal B$ is any $C^*$-algebra and $a$ is a normal element of $\mathcal B$, then $\mathcal A=C^*(a)$ is an abelian $C^*$-algebra contained in $\mathcal B$ and so (2.4) applies. Moreover, in light of Proposition 1.14, the spectrum of $a$ does not depend on whether $a$ is considered as an element of $\mathcal A$ or $\mathcal B$. The following definition is, therefore, unambiguous.

**2.5. Definition.** If $\mathcal B$ is a $C^*$-algebra with identity and $a$ is a normal element of $\mathcal B$, let $\rho\colon C(\sigma(a))\to C^*(a)\subseteq\mathcal B$ be as in (2.4). If $f\in C(\sigma(a))$ define

$$
f(a)\equiv\rho(f).
$$

The map $f\mapsto f(a)$ of $C(\sigma(a))\to\mathcal B$ is called the *functional calculus for $a$*.

Note that if $p(z,\bar z)$ is a polynomial in $z$ and $\bar z$, then $\rho(p(z,\bar z))=p(a,a^*)$. In particular, $\rho(z^n\bar z^m)=a^na^{*m}$ so that $\rho(z)=a$ and $\rho(\bar z)=a^*$. Also, $\rho(1)=1$.

The properties of this functional calculus can be obtained from the fact that $\rho$ is an isometric $*$-isomorphism of $C(\sigma(a))$ into $\mathcal B$—with one exception. How does this functional calculus compare with the Riesz Functional Calculus? If $f\in\operatorname{Hol}(a)$, $f|_{\sigma(a)}\in C(\sigma(a))$; so $f(a)$ has two possible interpretations. Or does it?

**2.6. Theorem.** *If $\mathcal B$ is a $C^*$-algebra and $a$ is a normal element of $\mathcal B$, then the functional calculus has the following properties.*

(a) *$f\mapsto f(a)$ is a $*$-monomorphism.*

(b) $\|f(a)\|=\|f\|_\infty$.

(c) *$f\mapsto f(a)$ is an extension of the Riesz Functional Calculus.*

*Moreover, the functional calculus is unique in the sense that if $\tau\colon C(\sigma(a))\to C^*(a)$ is a $*$-homomorphism that extends the Riesz Functional Calculus, then $\tau(f)=f(a)$ for every $f$ in $C(\sigma(a))$.*

**Proof.** Let $\rho\colon C(\sigma(a))\to C^*(a)$ be the map defined by $\rho(f)=f(a)$. From (2.4), (a) and (b) are immediate.

Let $\pi\colon\operatorname{Hol}(a)\to\mathcal A\subseteq\mathcal B$ denote the map defined by the Riesz Functional Calculus. Since $\rho(z)=\pi(z)=a$, an algebraic manipulation gives that $\rho(f)=\pi(f)$ for every rational function $f$ with poles off $\sigma(a)$. If $f\in\operatorname{Hol}(a)$, then by Runge’s Theorem there is a sequence $\{f_n\}$ of such rational functions such that $f_n(z)\to f(z)$ uniformly in a neighborhood of $\sigma(a)$. Thus $\pi(f_n)\to\pi(f)$. By (b), $\rho(f_n)\to\rho(f)$. Thus $\rho(f)=\pi(f)$.

To prove uniqueness, let $\tau\colon C(\sigma(a))\to\mathcal B$ be a $*$-homomorphism that extends
