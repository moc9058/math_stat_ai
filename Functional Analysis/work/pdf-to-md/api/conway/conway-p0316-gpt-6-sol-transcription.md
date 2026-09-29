**10.21. Theorem.** *Two normal operators are unitarily equivalent if and only if they have the same scalar-valued spectral measure $\mu$ and their multiplicity functions are equal a.e. $[\mu]$.*

There is some notation that is used by many and we should mention its connection with what we have just finished. Suppose $m:\mathbb C\to\{\infty,1,2,\ldots\}$ is a Borel function and $\mu$ is a compactly supported measure on $\mathbb C$ such that $\mu(\{z:m(z)=0\})=0$. If $z\in\mathbb C$ let $\mathcal H(z)$ be a Hilbert space of dimension $m(z)$. The *direct integral* of the spaces $\mathcal H(z)$, denoted by $\int\mathcal H(z)\,d\mu(z)$, is precisely the space

$$
L^2(\mu|_{\Delta_\infty};\mathcal H_\infty)
\oplus L^2(\mu|_{\Delta_1})
\oplus L^2(\mu|_{\Delta_2};\mathcal H_2)
\oplus\cdots,
$$

where $\Delta_n=\{z:m(z)=n\}$ and $\dim\mathcal H_n=n$. If $\phi:\mathbb C\to\mathcal B(\mathcal H_\infty)\cup\mathcal B(\mathbb C)\cup\mathcal B(\mathcal H_2)\cup\cdots$ such that $\phi(z)\in\mathcal B(\mathcal H_n)$ when $z\in\Delta_n$, $\phi:\Delta_n\to\mathcal B(\mathcal H_n)$ is a Borel function, and there is a constant $M$ such that $\|\phi(z)\|\leq M$ a.e. $[\mu]$, then $\int\phi(z)\,d\mu(z)$ denotes the operator $M_{\phi|_{\Delta_\infty}}\oplus\cdots$ as in (10.20). Although the direct integral notation is quite suggestive, one must revert to the notation of (10.20) to produce proofs.

**Remarks.** There are several sources for multiplicity theory. Most begin by proving Theorem 10.16. This is done for nonseparable spaces in Halmos [1951] and Brown [1974]. Another source is Arveson [1976], where the theory is set in the context of $C^*$-algebras which is its proper milieu. Also, Arveson shows that the theory can be applied to some non-normal operators. The details of this more general multiplicity theory are carried out in Ernest [1976] as part of a more general classification scheme. Another source for multiplicity theory is Dunford and Schwartz [1963].

By Theorem 4.6, every normal operator is unitarily equivalent to a multiplication operator $M_\phi$ on $L^2(X,\Omega,\mu)$ for some measure space $(X,\Omega,\mu)$. The scalar-valued spectral measure for $M_\phi$ is $\mu\circ\phi^{-1}$. What is the multiplicity function for $M_\phi$? One is tempted to say that $m_{M_\phi}(z)=$ the number of points in $\phi^{-1}(z)$. This is not quite correct. The answer can be found in Abrahamse and Kriete [1973]. Also, Abrahamse [1978] contains a survey of spectral multiplicity for normal operators treated from this point of view. An especially accessible and readable account of this can be found in Kriete [1986].

## EXERCISES

1. Let $A$ and $B$ be operators on $\mathcal H$ and $\mathcal H'$, respectively. Let $\mathcal H_0$ and $\mathcal H'_0$ be reducing subspaces for $A$ and $B$ and suppose that $A\cong B|_{\mathcal H'_0}$ and $B\cong A|_{\mathcal H_0}$. Show that $A\cong B$.

2. Let $\mu_1,\mu_2,\ldots$ be compactly supported measures on $\mathbb C$ such that $\mu_{n+1}\ll\mu_n$ for all $n$. Show that if $M$ is any normal operator whose spectral measure is absolutely continuous with respect to each $\mu_n$, then
   $$
   N_{\mu_1}\oplus N_{\mu_2}\oplus\cdots
   \cong (N_{\mu_1}\oplus N_{\mu_2}\oplus\cdots)\oplus M.
   $$
