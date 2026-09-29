$\mathcal{F}$ by inclusion, so $\mathcal{F}$ becomes a directed set. For each $F$ in $\mathcal{F}$, define

$$
h_F=\sum\{h_i:i\in F\}.
$$

Since this is a finite sum, $h_F$ is a well-defined element of $\mathcal{H}$. Now $\{h_F:F\in\mathcal{F}\}$ is a net in $\mathcal{H}$.

**4.11. Definition.** With the notation above, the sum $\sum\{h_i:i\in I\}$ converges if the net $\{h_F:F\in\mathcal{F}\}$ converges; the value of the sum is the limit of the net.

If $\mathcal{H}=\mathbb{F}$, the definition above gives meaning to an uncountable sum of scalars. Now Corollary 4.10 can be given its precise meaning; namely, $\sum\{|\langle h,e\rangle|^2:e\in\mathcal{E}\}$ converges and the value $\leq\|h\|^2$ (Exercise 9).

If the set $I$ in Definition 4.11 is countable, then this definition of convergent sum is not the usual one. That is, if $\{h_n\}$ is a sequence in $\mathcal{H}$, then the convergence of $\sum\{h_n:n\in\mathbb{N}\}$ is not equivalent to the convergence of $\sum_{n=1}^{\infty}h_n$. The former concept of convergence is that defined in (4.11) while the latter means that the sequence $\left\{\sum_{k=1}^{n}h_k\right\}_{n=1}^{\infty}$ converges. Even if $\mathcal{H}=\mathbb{F}$, these concepts do not coincide (see Exercise 12). If, however, $\sum\{h_n:n\in\mathbb{N}\}$ converges, then $\sum_{n=1}^{\infty}h_n$ converges (Exercise 10). Also see Exercise 11.

**4.12. Lemma.** *If $\mathcal{E}$ is an orthonormal set and $h\in\mathcal{H}$, then*

$$
\sum\{\langle h,e\rangle e:e\in\mathcal{E}\}
$$

*converges in $\mathcal{H}$.*

**Proof.** By (4.9), there are vectors $e_1,e_2,\ldots$ in $\mathcal{E}$ such that $\{e\in\mathcal{E}:\langle h,e\rangle\neq 0\}=\{e_1,e_2,\ldots\}$. We also know that $\sum_{n=1}^{\infty}|\langle h,e_n\rangle|^2\leq\|h\|^2<\infty$. So if $\varepsilon>0$, there is an $N$ such that $\sum_{n=N}^{\infty}|\langle h,e_n\rangle|^2<\varepsilon^2$. Let $F_0=\{e_1,\ldots,e_{N-1}\}$ and let $\mathcal{F}=$ all the finite subsets of $\mathcal{E}$. For $F$ in $\mathcal{F}$ define $h_F\equiv\sum\{\langle h,e\rangle e:e\in F\}$. If $F$ and $G\in\mathcal{F}$ and both contain $F_0$, then

$$
\begin{aligned}
\|h_F-h_G\|^2
&=\sum\{|\langle h,e\rangle|^2:e\in(F\setminus G)\cup(G\setminus F)\}\\
&\leq\sum_{n=N}^{\infty}|\langle h,e_n\rangle|^2\\
&<\varepsilon^2.
\end{aligned}
$$

So $\{h_F:F\in\mathcal{F}\}$ is a Cauchy net in $\mathcal{H}$. Because $\mathcal{H}$ is complete, this net converges. In fact, it converges to $\sum_{n=1}^{\infty}\langle h,e_n\rangle e_n$. ■

**4.13. Theorem.** *If $\mathcal{E}$ is an orthonormal set in $\mathcal{H}$, then the following statements are equivalent.*

(a) $\mathcal{E}$ is a basis for $\mathcal{H}$.

(b) If $h\in\mathcal{H}$ and $h\perp\mathcal{E}$, then $h=0$.

(c) $\bigvee\mathcal{E}=\mathcal{H}$.

(d) If $h\in\mathcal{H}$, then $h=\sum\{\langle h,e\rangle e:e\in\mathcal{E}\}$.
