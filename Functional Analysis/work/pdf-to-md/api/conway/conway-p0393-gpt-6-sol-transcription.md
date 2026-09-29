APPENDIX C

# The Dual of $C_0(X)$

The purpose of this section is to show that the dual of $C_0(X)$ is the space of regular Borel measures on $X$ and to put this result, and the accompanying definitions, in the context of complex-valued measures and functions.

Let $X$ be any set and let $\Omega$ be a $\sigma$-algebra of subsets of $X$; so $(X,\Omega)$ is a *measurable space*. If $\mu$ is a countably additive function defined on $\Omega$ such that $\mu(\square)=0$ and $0\leq\mu(\Delta)\leq\infty$ for all $\Delta$ in $\Omega$, call $\mu$ a *positive measure* on $(X,\Omega)$; $(X,\Omega,\mu)$ is called a *measure space*.

If $(X,\Omega)$ is a measurable space, a *signed measure* is a countably additive function $\mu$ defined on $\Omega$ such that $\mu(\square)=0$ and $\mu$ takes its values in $\mathbb{R}\cup\{\pm\infty\}$. (Note: $\mu$ can assume only one of the values $\pm\infty$.) It is assumed that the reader is familiar with the following result.

**C.1. Hahn–Jordan Decomposition.** *If $\mu$ is a signed measure on $(X,\Omega)$, then $\mu=\mu_1-\mu_2$, where $\mu_1$ and $\mu_2$ are positive measures, and $X=E_1\cup E_2$, where $E_1,E_2\in\Omega$, $E_1\cap E_2=\square$, $\mu_1(E_2)=0=\mu_2(E_1)$. The measures $\mu_1$ and $\mu_2$ are unique and the sets $E_1$ and $E_2$ are unique up to sets of $\mu_1+\mu_2$ measure zero.*

A *measure* (or *complex-valued measure*) is a complex-valued function $\mu$ defined on $\Omega$ that is countably additive and such that $\mu(\square)=0$. Note that $\mu$ does not assume any infinite values. If $\mu$ is a measure, then $(\operatorname{Re}\mu)(\Delta)\equiv\operatorname{Re}(\mu(\Delta))$ is a signed measure, as is $(\operatorname{Im}\mu)(\Delta)\equiv\operatorname{Im}(\mu(\Delta))$; hence $\mu=\operatorname{Re}\mu+i\operatorname{Im}\mu$. Applying (C.1) to $\operatorname{Re}\mu$ and $\operatorname{Im}\mu$ we get

**C.2**
$$
\mu=(\mu_1-\mu_2)+i(\mu_3-\mu_4)
$$

where $\mu_j$ $(1\leq j\leq-4)$ are positive measures, $\mu_1\perp\mu_2$ ($\mu_1$ and $\mu_2$ are *mutually singular*) and $\mu_3\perp\mu_4$. (C.2) will also be called the Hahn–Jordan decomposition of $\mu$.
