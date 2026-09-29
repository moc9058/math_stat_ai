**Proof.** If $f_1\perp f_2$, then

$$
\|f_1+f_2\|^2
=\langle f_1+f_2,f_1+f_2\rangle
=\|f_1\|^2+2\operatorname{Re}\langle f_1,f_2\rangle+\|f_2\|^2
$$

by the polar identity. Since $f_1\perp f_2$, this implies the result for $n=2$. The remainder of the proof proceeds by induction and is left to the reader. ■

Note that if $f\perp g$, then $f\perp -g$, so $\|f-g\|^2=\|f\|^2+\|g\|^2$. The next result is an easy consequence of the Pythagorean Theorem if $f$ and $g$ are orthogonal, but this assumption is not needed for its conclusion.

**2.3. Parallelogram Law.** *If $\mathcal H$ is a Hilbert space and $f$ and $g\in\mathcal H$, then*

$$
\|f+g\|^2+\|f-g\|^2=2(\|f\|^2+\|g\|^2).
$$

**Proof.** For any $f$ and $g$ in $\mathcal H$ the polar identity implies

$$
\begin{aligned}
\|f+g\|^2&=\|f\|^2+2\operatorname{Re}\langle f,g\rangle+\|g\|^2,\\
\|f-g\|^2&=\|f\|^2-2\operatorname{Re}\langle f,g\rangle+\|g\|^2.
\end{aligned}
$$

Now add. ■

The next property of a Hilbert space is truly pivotal. But first we need a geometric concept valid for any vector space over $\mathbb F$.

**2.4. Definition.** If $\mathcal X$ is any vector space over $\mathbb F$ and $A\subseteq\mathcal X$, then $A$ is a *convex set* if for any $x$ and $y$ in $A$ and $0\leq t\leq 1$, $tx+(1-t)y\in A$.

Note that $\{tx+(1-t)y:0\leq t\leq 1\}$ is the straight-line segment joining $x$ and $y$. So a convex set is a set $A$ such that if $x$ and $y\in A$, the entire line segment joining $x$ and $y$ is contained in $A$.

If $\mathcal X$ is a vector space, then any linear subspace in $\mathcal X$ is a convex set. A singleton set is convex. The intersection of any collection of convex sets is convex. If $\mathcal H$ is a Hilbert space, then every open ball $B(f;r)=\{g\in\mathcal H:\|f-g\|<r\}$ is convex, as is every closed ball.

**2.5. Theorem.** *If $\mathcal H$ is a Hilbert space, $K$ is a closed convex nonempty subset of $\mathcal H$, and $h\in\mathcal H$, then there is a unique point $k_0$ in $K$ such that*

$$
\|h-k_0\|=\operatorname{dist}(h,K)\equiv\inf\{\|h-k\|:k\in K\}.
$$

**Proof.** By considering $K-h\equiv\{k-h:k\in K\}$ instead of $K$, it suffices to assume that $h=0$. (Verify!) So we want to show that there is a unique vector $k_0$ in $K$ such that

$$
\|k_0\|=\operatorname{dist}(0,K)\equiv\inf\{\|k\|:k\in K\}.
$$

Let $d=\operatorname{dist}(0,K)$. By definition, there is a sequence $\{k_n\}$ in $K$ such that $\|k_n\|\to d$. Now the Parallelogram Law implies that

$$
\left\|\frac{k_n-k_m}{2}\right\|^2
=\frac12\bigl(\|k_n\|^2+\|k_m\|^2\bigr)
-\left\|\frac{k_n+k_m}{2}\right\|^2.
$$
