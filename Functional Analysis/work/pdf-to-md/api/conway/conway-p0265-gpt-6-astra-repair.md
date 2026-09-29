250　　　　　　　　　　　　　　　　　VIII. $C^*$-Algebras

application of Zorn’s Lemma implies that $\mathcal E$ has a maximal element $E_0$. Let $\mathcal H_0=\bigoplus\{\operatorname{cl}[\pi(\mathcal A)e]:e\in E_0\}$. If $h\in\mathcal H\ominus\mathcal H_0$, then $0=\langle\pi(a)e,h\rangle$ for every $a$ in $\mathcal A$ and $e$ in $E_0$. So if $a,b\in\mathcal A$ and $e\in E_0$, $0=\langle\pi(b^*a)e,h\rangle=\langle\pi(b)^*\pi(a)e,h\rangle=\langle\pi(a)e,\pi(b)h\rangle$. That is, $\pi(\mathcal A)e\perp\pi(\mathcal A)h$ for all $e$ in $E_0$. Hence $E_0\cup\{h\}\in\mathcal E$; by the maximality of $E_0$ it must be that $h=0$. Therefore $\mathcal H=\mathcal H_0$.

For $e$ in $E_0$ let $\mathcal H_e=\operatorname{cl}[\pi(\mathcal A)e]$. If $a\in\mathcal A$, clearly $\pi(a)\mathcal H_e\subseteq\mathcal H_e$. Since $a^*\in\mathcal A$ and $\pi(a)^*=\pi(a^*)$, $\mathcal H_e$ reduces $\pi(a)$. So if $\pi_e:\mathcal A\to\mathcal B(\mathcal H_e)$ is defined by $\pi_e(a)=\pi(a)|\mathcal H_e$, $\pi_e$ is a representation of $a$. Clearly $\pi=\bigoplus\{\pi_e:e\in E_0\}$. $\blacksquare$

In light of the preceding theorem, it becomes important to understand cyclic representations. To do this, let $\pi:\mathcal A\to\mathcal B(\mathcal H)$ be a cyclic representation with cyclic vector $e$. Define $f:\mathcal A\to\mathbb C$ by $f(a)=\langle\pi(a)e,e\rangle$. Note that $f$ is a bounded linear functional on $\mathcal A$ with $\|f\|\leq\|e\|^2$. Since $f(1)=\|e\|^2$, $\|f\|=\|e\|^2$. Moreover, $f(a^*a)=\langle\pi(a^*a)e,e\rangle=\langle\pi(a)^*\pi(a)e,e\rangle=\|\pi(a)e\|^2\geq 0$.

**5.10. Definition.** If $\mathcal A$ is a $C^*$-algebra, a linear functional $f:\mathcal A\to\mathbb C$ is *positive* if $f(a)\geq 0$ whenever $a\in\mathcal A_+$. A *state* on $\mathcal A$ is a positive linear functional on $\mathcal A$ of norm 1.

**5.11. Proposition.** *If $f$ is a positive linear functional on a $C^*$-algebra $\mathcal A$, then*

$$
|f(y^*x)|^2\leq f(y^*y)f(x^*x)
$$

*for every $x,y$ in $\mathcal A$.*

**Proof.** If $[x,y]=f(y^*x)$ for $x,y$ in $\mathcal A$, then $[\cdot,\cdot]$ is a semi-inner product on $\mathcal A$. The proposition now follows by the CBS inequality (I.1.4). $\blacksquare$

**5.12. Corollary.** *If $f$ is a non-zero positive linear functional on the $C^*$-algebra $\mathcal A$, then $f$ is bounded and $\|f\|=f(1)$.*

**5.13. Example.** If $X$ is a compact space, then the positive linear functionals on $C(X)$ correspond to the positive measures on $X$. The states correspond to the probability measures on $X$.

As was shown above, each cyclic representation gives rise to a positive linear functional. It turns out that each positive linear functional gives rise to a cyclic representation.

**5.14. Gelfand–Naimark–Segal Construction.** *Let $\mathcal A$ be a $C^*$-algebra with identity.*

(a) *If $f$ is a positive linear functional on $\mathcal A$, then there is a cyclic representation $(\pi_f,\mathcal H_f)$ of $\mathcal A$ with cyclic vector $e$ such that $f(a)=\langle\pi_f(a)e,e\rangle$ for all $a$ in $\mathcal A$.*

(b) *If $(\pi,\mathcal H)$ is a cyclic representation of $\mathcal A$ with cyclic vector $e$ and*
