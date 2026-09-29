# APPENDIX B

## The Dual of $L^p(\mu)$

In this section we will prove the following which appears as III.5.5 and III.5.6 in the text.

**Theorem.** *Let $(X,\Omega,\mu)$ be a measure space, let $1\leq p<\infty$, and let $1/p+1/q=1$. If $g\in L^q(\mu)$, define $F_g:L^p(\mu)\to\mathbb F$ by*

$$
F_g(f)=\int fg\,d\mu.
$$

*If $1<p<\infty$, the map $g\mapsto F_g$ defines an isometric isomorphism of $L^q(\mu)$ onto $L^p(\mu)^*$. If $p=1$ and $(X,\Omega,\mu)$ is $\sigma$-finite, $g\mapsto F_g$ is an isometric isomorphism of $L^\infty(\mu)$ onto $L^1(\mu)^*$.*

**Proof.** If $g\in L^q(\mu)$, then Hölder’s Inequality implies that $|F_g(f)|\leq\|f\|_p\|g\|_q$ for all $f$ in $L^p(\mu)$. Hence $F_g\in L^p(\mu)^*$ and $\|F_g\|\leq\|g\|_q$. Therefore $g\mapsto F_g$ is a linear contraction. It must be shown that this map is surjective and an isometry. Assume $F\in L^p(\mu)^*$.

*Case 1:* $\mu(X)<\infty$. Here $\chi_\Delta\in L^p(\mu)$ for every $\Delta$ in $\Omega$. Define $\nu(\Delta)=F(\chi_\Delta)$. It is easy to see that $\nu$ is finitely additive. If $\{\Delta_n\}\subseteq\Omega$ with $\Delta_1\supseteq\Delta_2\supseteq\cdots$ and $\bigcap_{n=1}^{\infty}\Delta_n=\square$, then

$$
\begin{aligned}
\|\chi_{\Delta_n}\|_p
&=\left[\int|\chi_{\Delta_n}|^p\,d\mu\right]^{1/p}\\
&=\mu(\Delta_n)^{1/p}\to0.
\end{aligned}
$$

Hence $\nu(\Delta_n)\to0$ since $F$ is bounded. It follows by standard measure theory that $\nu$ is a countably additive measure. Moreover, if $\mu(\Delta)=0$, $\chi_\Delta=0$ in $L^p(\mu)$; hence $\nu(\Delta)=0$. that is, $\nu\ll\mu$. By the Radon–Nikodym Theorem there is an $\Omega$-measurable function $g$ such $\nu(\Delta)=\int_\Delta g\,d\mu$ for every $\Delta$ in $\Omega$; that is, $F(\chi_\Delta)=$
