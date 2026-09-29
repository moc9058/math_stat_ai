11. Verify the statements made in Example 8.12.

12. Say that $a_1,\ldots,a_n$ are generators of $\mathcal A$ if $\mathcal A$ is the smallest Banach algebra with identity that contains $\{a_1,\ldots,a_n\}$. Show that $a_1,\ldots,a_n$ are generators of $\mathcal A$ if and only if $\mathcal A=\operatorname{cl}\{p(a_1,\ldots,a_n):p\text{ is a polynomial in }n\text{ complex variables }z_1,\ldots,z_n\}$, and if $\Sigma$ is the maximal ideal space, then there is a homeomorphism $\tau$ of $\Sigma$ onto a compact subset $K$ of $\mathbb C^n$ such that if $p$ is a polynomial in $n$ variables, then $\gamma(p(a_1,\ldots,a_n))=\tau^\#(p)$.

13. Verify the statements made in Example 8.13.

14. (Zelazko [1968].) Let $\mathcal A$ be an algebra and suppose $\phi:\mathcal A\to\mathbb C$ is a linear functional such that $\phi(a^2)=\phi(a)^2$ for all $a$ in $\mathcal A$. Show that $\phi$ is a homomorphism.

15. Let $\mathcal A$ be an abelian Banach algebra with identity that is semisimple [that is, $\operatorname{rad}\mathcal A=(0)$]. If $\|\cdot\|$ is the norm on $\mathcal A$ and $\|\cdot\|_1$ is another norm on $\mathcal A$ that also makes $\mathcal A$ into a Banach algebra, then these two norms are equivalent. (Hint: use the Closed Graph Theorem to show that the identity map $i:(\mathcal A,\|\cdot\|)\to(\mathcal A,\|\cdot\|_1)$ is continuous.)

16. Let $\mathcal A$ be as in Example 8.13 and let $K=\{\phi\in\mathcal A^*:\phi(1)=\|\phi\|=1\}$. Show that $\operatorname{ext}K=\{\delta_z:|z|=1\}$. (See (V.7).)

17. Show that $f(x)=\exp(\pi ix)$ is a generator of $C([0,1])$ but $g(x)=\exp(2\pi ix)$ is not.

18. Show that $C(\partial\mathbb D)$ does not have a single generator though it does have a single rational generator (that is, an element $a$ such that $\{r(a):r\text{ is a rational function with poles off }\sigma(a)\}$ is dense.)

## §9*. The Group Algebra of a Locally Compact Abelian Group

If $G$ is a locally compact abelian group and $m$ is Haar measure on $G$, then $L^1(G)\equiv L^1(m)$ is a Banach algebra (Example 1.11), where for $f,g$ in $L^1(G)$ the product $f*g$ is the convolution of $f$ and $g$:

$$
f*g(x)=\int_G f(xy^{-1})g(y)\,dy.
$$

Note that $dy$ is used to designate integration with respect to $m$ rather than $dm(y)$. Because $G$ is abelian, $L^1(G)$ is abelian. In fact, $g*f(x)=\int g(xy^{-1})f(y)\,dy$. If $y^{-1}x$ is substituted for $y$ in this integral, the value of the integral does not change because Haar measure is translation invariant. Hence $g*f(x)=\int g(y)f(y^{-1}x)\,dy=\int g(y)f(xy^{-1})\,dy=f*g(x)$.

Let $e$ denote the identity of $G$. If $G$ is discrete, then $\delta_e\in L^1(G)$ and $\delta_e$ is an identity for $L^1(G)$. If $G$ is not discrete, then $L^1(G)$ does not have an identity (Exercise 1).

Some examples of nondiscrete locally compact abelian groups are $\mathbb R^n$ and $\mathbb T^n$, where $\mathbb T=$ the unit circle $\partial\mathbb D$ in $\mathbb C$ with the usual multiplication. Note
