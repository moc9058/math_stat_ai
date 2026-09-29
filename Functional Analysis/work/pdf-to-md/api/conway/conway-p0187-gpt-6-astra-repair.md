172　　　　　　　　　VI. Linear Operators on a Banach Space

in $C(Y)$ such that $g(y_0)=0$ and $g(y_1)=1$. Let $f\in C(X)$ such that $Af=g$. Thus $f(\tau(y_0))=g(y_0)=0$ and $f(\tau(y_1))=1$. Hence $\tau(y_0)\ne\tau(y_1)$.

So if $\tau:Y\to X$ is a homeomorphism and $\alpha:Y\to\mathbb F$ is a continuous function, with $|\alpha(y)|\equiv1$, then $T:C(X)\to C(Y)$ defined by $(Tf)(y)=\alpha(y)f(\tau(y))$ is a surjective isometry. The next result gives a converse to this.

**2.1. The Banach–Stone Theorem.** *If $X$ and $Y$ are compact and $T:C(X)\to C(Y)$ is a surjective isometry, then there is a homeomorphism $\tau:Y\to X$ and a function $\alpha$ in $C(Y)$ such that $|\alpha(y)|=1$ for all $y$ and*

$$
(Tf)(y)=\alpha(y)f(\tau(y))
$$

*for all $f$ in $C(X)$ and $y$ in $Y$.*

**Proof.** Consider $T^*:M(Y)\to M(X)$. Because $T$ is a surjective isometry, $T^*$ is also. (Verify.) Thus $T^*$ is a weak* homeomorphism of ball $M(Y)$ onto ball $M(X)$ that distributes over convex combinations. Hence (Why?)

$$
T^*(\operatorname{ext}[\operatorname{ball}M(Y)])=\operatorname{ext}[\operatorname{ball}M(X)].
$$

By Theorem V.8.4 this implies that for every $y$ in $Y$ there is a unique $\tau(y)$ in $X$ and a unique scalar $\alpha(y)$ such that $|\alpha(y)|=1$ and

$$
T^*(\delta_y)=\alpha(y)\delta_{\tau(y)}.
$$

By the uniqueness, $\alpha:Y\to\mathbb F$ and $\tau:Y\to X$ are well-defined functions.

**2.2. Claim.** $\alpha:Y\to\mathbb F$ is continuous.

If $\{y_i\}$ is a net in $Y$ and $y_i\to y$, then $\delta_{y_i}\to\delta_y$ weak* in $M(Y)$. Hence $\alpha(y_i)\delta_{\tau(y_i)}=T^*(\delta_y)\to T^*(\delta_y)=\alpha(y)\delta_{\tau(y)}$ weak* in $M(X)$. In particular, $\alpha(y_i)=\langle 1,T^*(\delta_{y_i})\rangle\to\langle 1,T^*(\delta_y)\rangle=\alpha(y)$, proving (2.2).

**2.3. Claim.** $\tau:Y\to X$ is a homeomorphism.

As in the proof of (2.2), if $y_i\to y$ in $Y$, then $\alpha(y_i)\delta_{\tau(y_i)}\to\alpha(y)\delta_{\tau(y)}$ weak* in $M(X)$. Also, $\alpha(y_i)\to\alpha(y)$ in $\mathbb F$ by (2.2). Thus $\delta_{\tau(y_i)}=\alpha(y_i)^{-1}[\alpha(y_i)\delta_{\tau(y_i)}]\to\delta_{\tau(y)}$. By (V.6.1) this implies that $\tau(y_i)\to\tau(y)$, so that $\tau:Y\to X$ is continuous.

If $y_1,y_2\in Y$ and $y_1\ne y_2$, then $\overline{\alpha(y_1)}\delta_{y_1}\ne\overline{\alpha(y_2)}\delta_{y_2}$. Since $T^*$ is injective, it is easy to see that $\tau(y_1)\ne\tau(y_2)$ and so $\tau$ is one-to-one. If $x\in X$, then the fact that $T^*$ is surjective implies that there is a $\mu$ in $M(Y)$ such that $T^*\mu=\delta_x$. It must be that $\mu\in\operatorname{ext}[\operatorname{ball}M(Y)]$ (Why?), so that $\mu=\beta\delta_y$ for some $y$ in $Y$ and $\beta$ in $\mathbb F$ with $|\beta|=1$. Thus $\delta_x=T^*(\beta\delta_y)=\beta\alpha(y)\delta_{\tau(y)}$. Hence $\beta=\overline{\alpha(y)}$ and $\tau(y)=x$. Therefore $\tau:Y\to X$ is a continuous bijection and hence must be a homeomorphism (A.2.8). This establishes (2.3).

If $f\in C(X)$ and $y\in Y$, then $T(f)(y)=\langle Tf,\delta_y\rangle=\langle f,T^*\delta_y\rangle=\langle f,\alpha(y)\delta_{\tau(y)}\rangle=\alpha(y)f(\tau(y))$. $\blacksquare$
