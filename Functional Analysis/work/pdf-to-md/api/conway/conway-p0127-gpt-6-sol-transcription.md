*dense in $\mathcal X$ if and only if the only continuous linear functional on $\mathcal X$ that vanishes on $\mathcal Y$ is the identically zero functional.*

**3.15. Corollary.** *If $\mathcal X$ is a LCS, $\mathcal Y$ is a closed linear subspace of $\mathcal X$, and $x_0\in\mathcal X\setminus\mathcal Y$, then there is a continuous linear functional $f:\mathcal X\to\mathbf F$ such that $f(y)=0$ for all $y$ in $\mathcal Y$ and $f(x_0)=1$.*

These results imply that on a LCS there are many continuous linear functionals. Compare the results of this section with those of §III.6.

The hypothesis that $\mathcal X$ is locally convex does not appear in the results prior to Theorem 3.9. The reason for this is that in the preceding results the existence of an open convex subset of $\mathcal X$ is assumed. In Theorem 3.9 such a set must be manufactured. Without the hypothesis of local convexity it may be that the only open convex sets are the whole space itself and the empty set.

**3.16. Example.** For $0<p<1$, let $L^p(0,1)$ be the collection of equivalence classes of measurable functions $f:(0,1)\to\mathbf R$ such that

$$
((f))_p=\int_0^1 |f(x)|^p\,dx<\infty.
$$

It will be shown that $d(f,g)=((f-g))_p$ is a metric on $L^p(0,1)$ and that with this metric $L^p(0,1)$ is a Fréchet space. It will also be shown, however, that $L^p(0,1)$ has only one nonempty open convex set, namely itself. So $L^p(0,1)$, $0<p<1$, is most emphatically not locally convex. The proof of these facts begins with the following inequality.

**3.17** For $s,t$ in $[0,\infty)$ and $0<p<1$, $(s+t)^p\leq s^p+t^p$.

To see this, let $f(t)=s^p+t^p-(s+t)^p$ for $t\geq0$, $s$ fixed. Then $f'(t)=pt^{p-1}-p(s+t)^{p-1}$. Since $p-1<0$ and $s+t\geq t$, $f'(t)\geq0$. Thus $0=f(0)\leq f(t)$. This proves (3.17)

If $d(f,g)=((f-g))_p$ for $f,g$ in $L^p(0,1)$, then (3.17) implies that $d(f,g)\leq d(f,h)+d(h,g)$ for all $f,g,h$ in $L^p(0,1)$. It follows that $d$ is a metric on $L^p(0,1)$. Clearly $d$ is translation invariant.

**3.18** $L^p(0,1)$, $0<p<1$, is complete.

The proof of this is left as an exercise.

**3.19** $L^p(0,1)$ is a TVS.

The continuity of addition is a direct consequence of the translation invariance of $d$. If $f_n\to f$ and $\alpha_n\to\alpha$, $\alpha_n$ in $\mathbf R$,

$$
\begin{aligned}
d(\alpha_n f_n,\alpha f)
&=((\alpha_n f_n-\alpha f))_p\\
&\leq ((\alpha_n f_n-\alpha_n f))_p+((\alpha_n f-\alpha f))_p\\
&=|\alpha_n|^p((f_n-f))_p+|\alpha_n-\alpha|^p((f))_p\\
&\leq C((f_n-f))_p+|\alpha_n-\alpha|^p((f))_p,
\end{aligned}
$$

where $C$ is a constant independent of $n$. Hence $\alpha_n f_n\to\alpha f$. Thus $L^p(0,1)$ is a Fréchet space.
