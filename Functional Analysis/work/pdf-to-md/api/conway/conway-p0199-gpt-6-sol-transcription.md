**5.3. Lemma.** For a Banach space $\mathcal Y$ let $W$, $U_n$, and $p_n$ be as above. Let $\mathcal R$ be the set of all $y$ in $\mathcal Y$ such that $\vert\!\vert\!\vert y\vert\!\vert\!\vert\equiv\left[\sum_{n=1}^{\infty}p_n(y)^2\right]^{1/2}<\infty$. Then

(a) $W\subseteq\{y:\vert\!\vert\!\vert y\vert\!\vert\!\vert<1\}$;

(b) $(\mathcal R,\vert\!\vert\!\vert\cdot\vert\!\vert\!\vert)$ is a Banach space and the inclusion map $A:\mathcal R\to\mathcal Y$ is continuous;

(c) $A^{**}:\mathcal R^{**}\to\mathcal Y^{**}$ is injective and $(A^{**})^{-1}(\mathcal Y)=\mathcal R$;

(d) $\mathcal R$ is reflexive if and only if $\operatorname{cl}W$ is weakly compact.

**Proof.** (a) If $w\in W$, then $2^nw\in U_n$. Hence $1>p_n(2^nw)=2^np_n(w)$, so $p_n(w)<2^{-n}$. Thus $\vert\!\vert\!\vert w\vert\!\vert\!\vert^2<\sum_n(2^{-n})^2<1$.

(b) Let $\mathcal Y_n=\mathcal Y$ with the norm $p_n$ and put $\mathcal X=\bigoplus_2\mathcal Y_n$ (III.4.4). Define $\Phi:\mathcal R\to\mathcal X$ by $\Phi(y)=(y,y,\ldots)$. It is easy to see that $\Phi$ is an isometry though it is clearly not surjective. In fact, $\operatorname{ran}\Phi=\{(y_n)\in\mathcal X:y_n=y_m\text{ for all }n,m\}$. Thus $\mathcal R$ is a Banach space. Let $P_1=$ the projection of $\mathcal X$ onto the first coordinate. Then $A=P_1\circ\Phi$ and hence $A$ is continuous.

(c) With the notation from the proof of (b), it follows that $\mathcal X^{**}=\bigoplus_2\mathcal Y_n^{**}$ and $\Phi^{**}:\mathcal R^{**}\to\mathcal X^{**}$ is given by $\Phi^{**}(y^{**})=(A^{**}y^{**},A^{**}y^{**},\ldots)$. Now the fact that $\Phi$ is an isometry implies that $\Phi^*$ is surjective. (This follows in two ways. One is by a direct argument (see Exercise 2). Also, $\operatorname{ran}\Phi^*$ is closed since $\operatorname{ran}\Phi$ is closed (1.10), and $\operatorname{ran}\Phi^*$ is dense since ${}^{\perp}(\operatorname{ran}\Phi^*)=\ker\Phi=(0)$.) Hence $\ker\Phi^{**}=(\operatorname{ran}\Phi^*)^\perp=(0)$; that is, $\Phi^{**}$ is injective. Therefore $A^{**}$ is injective.

Now let $y^{**}\in(A^{**})^{-1}(\mathcal Y)$. It follows that $\Phi^{**}y^{**}=x\in\mathcal X$. Let $\{y_i\}$ be a net in $\mathcal R$ such that $\vert\!\vert\!\vert y_i\vert\!\vert\!\vert\leq\vert\!\vert\!\vert y^{**}\vert\!\vert\!\vert$ for all $i$ and $y_i\to y^{**}$ $\sigma(\mathcal R^{**},\mathcal R^*)$ (V.4.1). Thus $\Phi^{**}(y_i)\to\Phi^{**}(y^{**})$ $\sigma(\mathcal X^{**},\mathcal X^*)$. But $\Phi^{**}(y_i)=\Phi(y_i)\in\mathcal X$ and $\Phi^{**}(y^{**})=x$. Hence $\Phi(y_i)\to x$ $\sigma(\mathcal X,\mathcal X^*)$. Since $\operatorname{ran}\Phi$ is closed, $x\in\operatorname{ran}\Phi$; let $\Phi(y)=x$. Then $0=\Phi^{**}(y^{**}-y)$. Since $\Phi^{**}$ is injective, $y^{**}=y\in\mathcal R$.

(d) An argument using Alaoglu’s Theorem shows that $A^{**}(\operatorname{ball}\mathcal R^{**})=$ the $\sigma(\mathcal Y^{**},\mathcal Y^*)$ closure of $A(\operatorname{ball}\mathcal R)$. Put $C=A(\operatorname{ball}\mathcal R)$. Suppose $\operatorname{cl}W$ is weakly compact. Now $C\subseteq 2^n\operatorname{cl}W+2^{-n}\operatorname{ball}\mathcal Y^{**}$ and this set is $\sigma(\mathcal Y^{**},\mathcal Y^*)$ compact. From the preceding comments, $A^{**}(\operatorname{ball}\mathcal R^{**})\subseteq 2^n\operatorname{cl}W+2^{-n}\operatorname{ball}\mathcal Y^{**}$. Thus,

$$
\begin{aligned}
A^{**}(\operatorname{ball}\mathcal R^{**})
&\subseteq \bigcap_{n=1}^{\infty}
\left[2^n\operatorname{cl}W+2^{-n}\operatorname{ball}\mathcal Y^{**}\right]\\
&\subseteq \bigcap_{n=1}^{\infty}
\left[\mathcal Y+2^{-n}\operatorname{ball}\mathcal Y^{**}\right]\\
&=\mathcal Y.
\end{aligned}
$$

By (c), $\mathcal R^{**}=\mathcal R$ and $\mathcal R$ is reflexive.

Now assume $\mathcal R$ is reflexive; thus $\operatorname{ball}\mathcal R$ is $\sigma(\mathcal R,\mathcal R^*)$-compact. Therefore $C=A(\operatorname{ball}\mathcal R)$ is weakly compact in $\mathcal Y$. By (a), $\operatorname{cl}W$ is weakly compact. $\blacksquare$

The next theorem, as well as the preceding lemma, are from Davis, Figiel, Johnson, and Pelczynski [1974].
