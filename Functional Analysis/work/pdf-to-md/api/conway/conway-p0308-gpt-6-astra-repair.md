§10. Multiplicity Theory for Normal Operators  293

## §10. Multiplicity Theory for Normal Operators: A Complete Set of Unitary Invariants

Throughout this section only separable Hilbert spaces are considered.

When are two normal operators unitarily equivalent? The answer to this question must be given in the following way: to each normal operator we must attach a collection of objects such that two normal operators are unitarily equivalent if and only if the two collections are equal (or equivalent). Furthermore, it should be easier to verify that these collections are equivalent than to verify that the normal operators are equivalent. This is contained in the following result due to Hellinger [1907]. Note that it generalizes Theorem 3.6.

**10.1. Theorem.** (a) *If $N$ is a normal operator, then there is a sequence (possibly finite) of measures $\{\mu_n\}$ on $\mathbb C$ such that $\mu_{n+1}\ll\mu_n$ for all $n$ and*

$$
\tag*{10.2}
N\cong N_{\mu_1}\oplus N_{\mu_2}\oplus\cdots.
$$

(b) *If $N$ and $\{\mu_n\}$ are as in (a) and $M\cong N_{\nu_1}\oplus N_{\nu_2}\oplus\cdots$, where $\nu_{n+1}\ll\nu_n$ for all $n$, then $N\cong M$ if and only if $[\mu_n]=[\nu_n]$ for all $n$.*

The proof of this theorem requires several lemmas. Before beginning, we will examine a couple of false starts for a proof. This will cause us to arrive at the correct strategy for a proof and show us the necessity for some of the lemmas.

Let $N=\int z\,dE(z)$. If $e\in\mathcal H$ and $\mathcal H_e=\operatorname{cl}[W^*(N)e]$, then $N|\mathcal H_e$ is a $*$-cyclic normal operator. An application of Zorn’s Lemma and the separability of $\mathcal H$ produces a maximal sequence $\{e_n\}$ in $\mathcal H$ such that $\mathcal H_{e_n}\perp\mathcal H_{e_m}$. By the maximality of $\{e_n\}$, $\mathcal H=\bigoplus_n\mathcal H_{e_n}$. If $N_n=N|\mathcal H_{e_n}$, $N_n=N_{\mu_n}$, where $\mu_n(\Delta)=\|E(\Delta)e_n\|^2$; thus $N\cong\bigoplus_nN_{\mu_n}$. The trouble here is that $\mu_{n+1}$ is not necessarily absolutely continuous with respect to $\mu_n$. Just using Zorn’s Lemma to produce the sequence $\{\mu_n\}$ eliminates any possibility of having $\{\mu_n\}$ canonical and producing the unitary invariant desired for normal operators. Let’s try again.

Note that if $\mu_{n+1}\ll\mu_n$ for all $n$ in (10.2), then $\mu_n\ll\mu_1$ for all $n$. This in turn implies that $\mu_1$ is a scalar-valued spectral measure for $N$. Using Lemma 8.6 we are thus led to choose $\mu_1$ as follows. Let $e_1$ be a separating vector for $W^*(N)$; this exists by Corollary 7.9 and the separability of $\mathcal H$. Put $\mu_1(\Delta)=\|E(\Delta)e_1\|^2$. If $\mathcal H_1=\operatorname{cl}[W^*(N)e_1]$. then $N|\mathcal H_1\cong N_{\mu_1}$. Let $N_2\equiv N|\mathcal H_1^\perp$; so $N_2$ is normal. A pair of easy exercises shows that the spectral measure $E_2$ for $N_2$ is given by $E_2(\Delta)=E(\Delta)|\mathcal H_1^\perp$ and $W^*(N_2)=W^*(N)|\mathcal H_1^\perp$ $(\equiv\{A\in\mathcal B(\mathcal H_1^\perp):A=T|\mathcal H_1^\perp\text{ for some }T\text{ in }W^*(N)\})$. Let $e_2$ be a separating vector for $W^*(N_2)$ and put $\mu_2(\Delta)=\|E_2(\Delta)e_2\|^2$. By the easy exercises above, $\mu_2(\Delta)=\|E(\Delta)e_2\|^2$, so that $\mu_2\ll\mu_1$, and $\mathcal H_2\equiv\operatorname{cl}[W^*(N)e_2]=\operatorname{cl}[W^*(N_2)e_2]\leqslant\mathcal H_1^\perp$. Also, $N|\mathcal H_2\cong N_{\mu_2}$.
