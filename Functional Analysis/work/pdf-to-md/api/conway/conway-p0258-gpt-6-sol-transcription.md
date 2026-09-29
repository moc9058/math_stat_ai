**PROOF.** If $h\in\mathcal H$, then $\|Ah\|^2=\langle Ah,Ah\rangle=\langle A^*Ah,h\rangle=\langle |A|h,|A|h\rangle$. Thus

$$
\tag{3.12}
\|Ah\|^2=\||A|h\|^2.
$$

Since $(\operatorname{ran}A^*)^\perp=\ker A$, $\operatorname{ran}A^*$ is dense in $(\ker A)^\perp$. If $f\in\operatorname{ran}A^*$, $f=A^*g$ for $g$ in $(\ker A^*)^\perp=\operatorname{cl}\operatorname{ran}A$. Therefore, $\{A^*Ak:k\in\mathcal H\}$ is dense in $\operatorname{cl}[\operatorname{ran}A^*]=(\ker A)^\perp$. But $A^*Ak=|A|^2k=|A|h$, where $h=|A|k$. That is, $\{|A|h:h\in\mathcal H\}$ is dense in $(\ker A)^\perp$. If $W:\operatorname{ran}|A|\to\operatorname{ran}A$ is defined by

$$
\tag{3.13}
W(|A|h)=Ah,
$$

then (3.12) implies that $W$ is a well-defined isometry. Thus $W$ extends to an isometry $W:(\ker A)^\perp\to\operatorname{cl}(\operatorname{ran}A)$. If $Wh$ is defined to be $0$ for $h$ in $\ker A$, $W$ is a partial isometry. By (3.13), $W|A|=A$.

For the uniqueness, note that $A^*A=PU^*UP$. Now $U^*U=E\equiv$ the projection onto the initial space of $U$ (Exercise 16), $(\ker U)^\perp=(\ker P)^\perp=\operatorname{cl}(\operatorname{ran}P)$. Thus $A^*A=PEP=P^2$. By the uniqueness of the positive square root, $P=|A|$. Since $A=U|A|$, $U|A|h=Ah=W|A|h$. That is, $U$ and $W$ agree on a dense subset of their common initial space. Hence $U=W$. ■

## Exercises

1. Prove the uniqueness statement in Proposition 3.4 for the case that $\mathcal A$ is abelian.

2. Prove Proposition 3.5.

3. Let $A\in\mathcal B(L^2(0,1))$ be defined by $(Af)(t)=tf(t)$. Show that $A\geq 0$ and find $A^{1/n}$.

4. Let $(X,\Omega,\mu)$ be a $\sigma$-finite measure space, let $\phi\in L^\infty(X,\Omega,\mu)$, and define $M_\phi$ as in Theorem II.1.5. Show that $M_\phi\geq 0$ if and only if $\phi(x)\geq 0$ a.e. $[\mu]$. What is $M_\phi^{1/n}$? If $M_\phi\in\operatorname{Re}\mathcal B(\mathcal H)$, find the positive and negative parts of $M_\phi$.

5. Find an example of a positive operator on a Hilbert space that has a nonhermitian square root.

6. If $a\in\operatorname{Re}\mathcal A$, show that $|a|\equiv(a^2)^{1/2}=a_++a_-$.

7. If $a\in\mathcal A_+$, show that $x^*ax\in\mathcal A_+$ for every $x$ in $\mathcal A$.

8. If $a,b\in\mathcal A$, $0\leq a\leq b$, and $a$ is invertible, then $b$ is invertible and $b^{-1}\leq a^{-1}$.

9. If $a,b\in\operatorname{Re}\mathcal A$, $a\leq b$, and $ab=ba$, then $f(a)\leq f(b)$ for every increasing continuous function $f$ on $\mathbb R$.

10. If $a\in\operatorname{Re}\mathcal A$ and $\|a\|\leq 1$, show that $a$ is the sum of two unitaries. (Hint: First solve this for $\mathcal A=\mathbb C$.)

11. If $\alpha>0$, define $f_\alpha:(-\alpha^{-1},\infty)\to\mathbb R$ by $f_\alpha(t)=t/(1+\alpha t)=\alpha^{-1}[1-(1+\alpha t)^{-1}]$. Show:

    (a) If $0\leq a\leq b$ in $\mathcal A$, $f_\alpha(a)\leq f_\alpha(b)$ for all $\alpha>0$;

    (b) $f_\alpha(t)<\min\{t,\alpha^{-1}\}$ for $t>0$;

    (c) $\lim_{\alpha\to 0}f_\alpha(t)=t$ uniformly on bounded intervals in $[0,\infty)$;

    (d) if $0\leq\alpha\leq\beta$, $f_\alpha\leq f_\beta$ on $[0,\infty)$;

    (e) $f_\alpha\circ f_\beta=f_{\alpha+\beta}$;

    (f) $\lim_{\alpha\to\infty}\alpha f_\alpha(t)=1$ uniformly on bounded intervals in $[0,\infty)$.
