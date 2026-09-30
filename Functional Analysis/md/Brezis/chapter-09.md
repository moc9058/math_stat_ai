# 9. Sobolev Spaces and the Variational Formulation of Elliptic Boundary Value Problems in N Dimensions


<a id="pdf-page-308"></a>
## Step D: Recovery of a classical solution.

Assume that the weak solution $u\in H_0^1(\Omega)$ of (31) belongs to $C^2(\overline{\Omega})$, and assume that $\Omega$ is of class $C^1$. Then $u=0$ on $\Gamma$ (by Theorem 9.17). On the other hand, we have

$$
\int_\Omega(-\Delta u+u)v=\int_\Omega fv
\qquad \forall v\in C_c^1(\Omega)
$$

and thus $-\Delta u+u=f$ a.e. on $\Omega$ (by Corollary 4.24). In fact, $-\Delta u+u=f$ everywhere on $\Omega$, since $u\in C^2(\Omega)$; thus $u$ is a classical solution.

We describe now some other examples. *In each case it is essential to specify precisely the function space and the appropriate weak formulation.*

*Example 2 (inhomogeneous Dirichlet condition).* Let $\Omega\subset\mathbb{R}^N$ be a bounded open set. We look for a function $u:\overline{\Omega}\to\mathbb{R}$ satisfying

$$
\begin{cases}
-\Delta u+u=f & \text{in }\Omega,\\
u=g & \text{on }\Gamma,
\end{cases}
\tag{33}
$$

where $f$ is given on $\Omega$ and $g$ is given on $\Gamma$. Suppose that there exists a function $\tilde g\in H^1(\Omega)\cap C(\overline{\Omega})$ such that<sup>22</sup> $\tilde g=g$ on $\Gamma$ and consider the set

$$
K=\{v\in H^1(\Omega);\ v-\tilde g\in H_0^1(\Omega)\}.
$$

It follows from Theorem 9.17 that $K$ is independent of the choice of $\tilde g$ and depends only on $g$. $K$ is a nonempty closed convex set in $H^1(\Omega)$.

**Definition.** A *classical* solution of (33) is a function $u\in C^2(\overline{\Omega})$ satisfying (33). A *weak* solution of (33) is a function $u\in K$ satisfying

$$
\int_\Omega(\nabla u\cdot\nabla v+uv)=\int_\Omega fv
\qquad \forall v\in H_0^1(\Omega).
\tag{34}
$$

As above, any classical solution is a weak solution.

• **Proposition 9.22.** *Given any $f\in L^2(\Omega)$, there exists a unique weak solution $u\in K$ of (33). Furthermore, $u$ is obtained by*

$$
\min_{v\in K}\left\{\frac12\int_\Omega(|\nabla v|^2+v^2)-\int_\Omega fv\right\}.
$$

*Proof.* We claim that $u\in K$ is a weak solution of (33) if and only if we have

$$
\int_\Omega\nabla u\cdot(\nabla v-\nabla u)+\int_\Omega u(v-u)
\geq\int_\Omega f(v-u)
\qquad \forall v\in K.
\tag{35}
$$

<sup>22</sup> This assumption is satisfied, *for example*, if $\Omega$ is of class $C^1$ and $g\in C^1(\Gamma)$. If $\Omega$ is regular enough it is not necessary to suppose that $\tilde g\in C(\overline{\Omega})$. Applying the theory of traces (see the comments at the end of this chapter), it suffices to know that $\tilde g\in H^1(\Omega)$, i.e., $g\in H^{1/2}(\Gamma)$.



<a id="pdf-page-339"></a>

