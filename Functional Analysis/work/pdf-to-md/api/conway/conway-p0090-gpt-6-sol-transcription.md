it suffices, since $C_b(B)$ is complete (1.6), to show that $\rho(\mathcal X^*)$ is closed. Let $\{f_n\}\subseteq\mathcal X^*$ and suppose $g\in C_b(B)$ such that $\|\rho(f_n)-g\|\to0$ as $n\to\infty$. Let $x\in\mathcal X$. If $\alpha,\beta\in\mathbb F$, $\alpha,\beta\ne0$, such that $\alpha x,\beta x\in B$, then $\alpha^{-1}g(\alpha x)=\lim\alpha^{-1}f_n(\alpha x)=\lim\beta^{-1}f_n(\beta x)=\beta^{-1}g(\beta x)$. Define $f:\mathcal X\to\mathbb F$ by letting $f(x)=\alpha^{-1}g(\alpha x)$ for any $\alpha\ne0$ such that $\alpha x\in B$. It is left as an exercise for the reader to show that $f\in\mathcal X^*$ and $\rho(f)=g$. $\blacksquare$

Compare the preceding result with Exercise 2.1.

It should be emphasized that it is not assumed in the preceding proposition that $\mathcal X$ is complete. In fact, if $\mathcal X$ is a normed space and $\widehat{\mathcal X}$ is its completion (Exercise 1.16), then $\mathcal X^*$ and $\widehat{\mathcal X}^{\,*}$ are isometrically isomorphic (Exercise 2.2).

**5.5. Theorem.** *Let $(X,\Omega,\mu)$ be a measure space and let $1<p<\infty$. If $1/p+1/q=1$ and $g\in L^q(X,\Omega,\mu)$, define $F_g:L^p(\mu)\to\mathbb F$ by*

$$
F_g(f)=\int fg\,d\mu.
$$

*Then $F_g\in L^p(\mu)^*$ and the map $g\mapsto F_g$ defines an isometric isomorphism of $L^q(\mu)$ onto $L^p(\mu)^*$.*

Since this theorem is often proved in courses in measure and integration, the proof of this result, as well as the next two, is contained in the Appendix. See Appendix B for the proofs of (5.5) and (5.6).

**5.6. Theorem.** *If $(X,\Omega,\mu)$ is a $\sigma$-finite measure space and $g\in L^\infty(X,\Omega,\mu)$, define $F_g:L^1(\mu)\to\mathbb F$ by*

$$
F_g(f)=\int fg\,d\mu.
$$

*Then $F_g\in L^1(\mu)^*$ and the map $g\mapsto F_g$ defines an isometric isomorphism of $L^\infty(\mu)$ onto $L^1(\mu)^*$.*

Note that when $p=2$ in Theorem 5.5, there is a little difference between (5.5) and (I.3.5) owing to the absence of a complex conjugate in (5.5). Also, note that (5.6) is false if the measure space is not assumed to be $\sigma$-finite (Exercise 3).

If $X$ is a locally compact space, $M(X)$ denotes the space of all $\mathbb F$-valued regular Borel measures on $X$ with the total variation norm. See Appendix C for the definitions as well as the proof of the next theorem.

**5.7. Riesz Representation Theorem.** *If $X$ is a locally compact space and $\mu\in M(X)$, define $F_\mu:C_0(X)\to\mathbb F$ by*

$$
F_\mu(f)=\int f\,d\mu.
$$
