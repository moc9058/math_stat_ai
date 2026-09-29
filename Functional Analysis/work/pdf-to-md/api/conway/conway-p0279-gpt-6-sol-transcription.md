So $\Omega$ contains every open set and, hence, it must be the collection of Borel sets. The converse is left to the reader. $\blacksquare$

The unique spectral measure $E$ obtained in the Spectral Theorem is called the *spectral measure for $N$*. An abbreviation for the Spectral Theorem is to say, “Let $N=\int\lambda\,dE(\lambda)$ be the *spectral decomposition* of $N$.” If $\phi$ is a bounded Borel function on $\sigma(N)$, define $\phi(N)$ by

$$
\phi(N)\equiv\int\phi\,dE,
$$

where $E$ is the spectral measure for $N$.

**2.3. Theorem.** *If $N$ is a normal operator on $\mathcal H$ with spectral measure $E$ and $B(\sigma(N))$ is the $C^*$-algebra of bounded Borel functions on $\sigma(N)$, then the map*

$$
\phi\mapsto\phi(N)
$$

*is a representation of the $C^*$-algebra $B(\sigma(N))$. If $\{\phi_i\}$ is a net in $B(\sigma(N))$ such that $\int\phi_i\,d\mu\to0$ for every $\mu$ in $M(\sigma(N))$, then $\phi_i(N)\to0$ (WOT). This map is unique in the sense that if $\tau:B(\sigma(N))\to\mathcal B(\mathcal H)$ is a representation such that $\tau(z)=N$ and $\tau(\phi_i)\to0$ (WOT) whenever $\{\phi_i\}$ is a bounded net in $B(\sigma(N))$ such that $\int\phi_i\,d\mu\to0$ for every $\mu$ in $M(\sigma(N))$, then $\tau(\phi)=\phi(N)$ for all $\phi$ in $B(\sigma(N))$.*

**Proof.** The fact that $\phi\mapsto\phi(N)$ is a representation is a consequence of Proposition 1.12. If $\{\phi_i\}$ is as in the statement, then the fact that $E_{g,h}\in M(\sigma(N))$ implies that $\phi_i(N)\to0$ (WOT).

To prove uniqueness, let $\tau:B(\sigma(N))\to\mathcal B(\mathcal H)$ be a representation with the appropriate properties. Then $\tau(u)=u(N)$ if $u\in C(\sigma(N))$ by the uniqueness of the functional calculus for normal elements of a $C^*$-algebra (VIII.2.6). If $\phi\in B(\sigma(N))$, then Proposition V.4.1 implies that there is a net $\{u_i\}$ in $C(\sigma(N))$ such that $\|u_i\|\leq\|\phi\|$ for all $u_i$ and $\int u_i\,d\mu\to\int\phi\,d\mu$ for every $\mu$ in $M(\sigma(N))$. Thus $u_i(N)\to\phi(N)$ (WOT). But $\tau(\phi)=\mathrm{WOT}\!-\!\lim\tau(u_i)=\mathrm{WOT}\!-\!\lim u_i(N)$; therefore $\tau(\phi)=\phi(N)$. $\blacksquare$

It is worthwhile to rewrite (1.11) as

$$
\tag{2.4}
\langle\phi(N)g,h\rangle=\int\phi\,dE_{g,h}
$$

for $\phi$ in $B(\sigma(N))$ and $g,h$ in $\mathcal H$. If $\phi\in B(\mathbb C)$, then the restriction of $\phi$ to $\sigma(N)$ belongs to $B(\sigma(N))$. Since the support of each measure $E_{g,h}$ is contained in $\sigma(N)$, (2.4) holds for every bounded Borel function $\phi$ on $\mathbb C$. This has certain technical advantages that will become apparent when we begin to apply (2.4).

Proposition 2.3 thus extends the functional calculus for normal operators. This functional calculus or, equivalently, the Spectral Theorem, will be exploited in this chapter. But right now we look at some examples.
