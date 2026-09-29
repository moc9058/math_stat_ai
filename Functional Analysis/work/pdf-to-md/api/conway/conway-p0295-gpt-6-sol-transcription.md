Because $\ker X=(0)$ and $\operatorname{ran}X$ is dense, $A$ is a positive operator on $\mathcal H_1$ and $U:\mathcal H_1\to\mathcal H_2$ is an isomorphism. Now $X^*N_2^*=N_1^*X^*$, so $X^*N_2=N_1X^*$. A calculation shows that $A^2=X^*X\in\{N_1\}'$, so $A\in\{N_1\}'$. (Why?) Hence $N_2UA=N_2X=UAN_1=UN_1A$; that is, $N_2U=UN_1$ on the range of $A$. But $\ker A=(0)$, so $\operatorname{ran}A$ is dense in $\mathcal H_1$. Therefore $N_2U=UN_1$, or $N_2=UN_1U^{-1}$. $\blacksquare$

**6.11. Corollary.** *Two similar normal operators are unitarily equivalent.*

The corollary appears in Putnam [1951], while Proposition 6.10 first appeared in Douglas [1969].

## Exercises

1. If $\mathcal S\subseteq\mathcal B(\mathcal H)$, show that $\mathcal S'=\mathcal S'''$.

2. If $\mathcal S\subseteq\mathcal B(\mathcal H)$, show that $\mathcal S'$ is always a SOT closed subalgebra of $\mathcal B(\mathcal H)$.

3. Prove Proposition 6.1.

4. Let $\mathcal H$ be a Hilbert space of dimension $\alpha$ and define $S:\mathcal H^{(\infty)}\to\mathcal H^{(\infty)}$ by $S(h_1,h_2,\ldots)=(0,h_1,h_2,\ldots)$. $S$ is called the *unilateral shift of multiplicity* $\alpha$. (a) Show that $A=[A_{ij}]\in\{S\}'$ if and only if $A_{ij}=0$ for $j>i$ and $A_{ij}=A_{i+1,j+1}$ for $i\geq j$. (b) Show that $A=[A_{ij}]\in\{S\}''$ if and only if $A_{ij}=0$ for $j>i$ and $A_{ij}=A_{i+1,j+1}=$ a multiple of the identity for $i\geq j$.

5. What is $\{N_\mu\oplus N_\mu\}'$? $\{N_\mu\oplus N_\mu\}''$?

6. If $\mathcal A$ is a subalgebra of $\mathcal B(\mathcal H)$, show that $\mathcal A$ is a maximal abelian subalgebra of $\mathcal B(\mathcal H)$ if and only if $\mathcal A=\mathcal A'$.

7. Find a non-normal operator that is similar to a normal operator. (Hint: Try $\dim\mathcal H=2$.)

8. Let $\mu$ be a compactly supported measure on $\mathbb C$ and let $\mathcal H$ be a separable Hilbert space. A function $f:\mathbb C\to\mathcal H$ is a Borel function if $f^{-1}(G)$ is a Borel set when $G$ is weakly open in $\mathcal H$. Define $L^2(\mu,\mathcal H)$ to be the equivalence classes of Borel functions $f:\mathbb C\to\mathcal H$ such that $\int\|f(x)\|^2\,d\mu(x)<\infty$. Define $\langle f,g\rangle=\int\langle f(x),g(x)\rangle\,d\mu(x)$ for $f$ and $g$ in $L^2(\mu,\mathcal H)$. (a) Show that $L^2(\mu,\mathcal H)$ is a Hilbert space. Define $N$ on $L^2(\mu,\mathcal H)$ by $(Nf)(z)=zf(z)$. (b) Show that $N$ is a normal operator and $\sigma(N)=\operatorname{support}\mu$. Calculate $N^*$. (c) Show that $N\cong N_\mu^{(\alpha)}$, where $\alpha=\dim\mathcal H$. (d) Find $\{N\}'$. (Hint: Use 6.1.) (e) Find $\{N\}''$.

9. Let $\mathcal H$ be separable with basis $\{e_n\}$. Let $A$ be the diagonal operator on $\mathcal H$ given by $Ae_n=\lambda_ne_n$, where $\sup_n|\lambda_n|<\infty$. Determine $\{A\}'$ and $\{A\}''$. Give necessary and sufficient conditions on $\{\lambda_n\}$ such that $\{A\}'=\{A\}''$.

10. Let $\mathcal A$ be a $C^*$-subalgebra of $\mathcal B(\mathcal H)$ but do not assume that $\mathcal A$ contains the identity operator. Let $\mathcal M=\bigvee\{\operatorname{ran}A:A\in\mathcal A\}$ and let $P=$ the projection of $\mathcal H$ onto $\mathcal M$. Show that $\operatorname{SOT\!-\!cl}\mathcal A=\mathcal A''P=P\mathcal A''$.

11. Formulate and prove a polar decomposition for operators between different Hilbert spaces.
