3. Does the unilateral shift of multiplicity 1 have a square root?

4. Show that for every $n\in\mathbb{Z}\cup\{\pm\infty\}$ there is an operator $A$ in $\mathcal{SF}$ such that $\operatorname{ind}A=n$.

5. If $A\in\mathcal{SF}$, then for every $n\geq 1$, $A^n\in\mathcal{SF}$ and $\operatorname{ind}A^n=n(\operatorname{ind}A)$.

6. If $A:\mathcal{H}\to\mathcal{H}'$ is a left semi-Fredholm operator, then there is a finite rank operator $F:\mathcal{H}\to\mathcal{H}'$ such that $\ker(A+F)=(0)$ and $\operatorname{ind}(A+F)=\operatorname{ind}A$.

7. If $A$ is a Fredholm operator in $\mathcal{B}(\mathcal{H})$, prove that the following statements are equivalent. (a) $\operatorname{ind}A=0$. (b) There is a compact operator $K$ such that $A+K$ is invertible. (c) There is a finite rank operator $F$ such that $A+F$ is invertible.

8. If $U$ is the unilateral shift of multiplicity 1 and $\pi:\mathcal{B}(\mathcal{H})\to\mathcal{B}(\mathcal{H})/\mathcal{B}_0(\mathcal{H})$ is the natural map, show that $\pi(U)$ is normal in $\mathcal{B}(\mathcal{H})/\mathcal{B}_0(\mathcal{H})$ but there is no normal operator $N$ such that $U-N$ is compact. (See Exercise IX.8.14.)

## §4. The Essential Spectrum

Now concentrate on operators acting on a single Hilbert space $\mathcal{H}$ and let $\pi:\mathcal{B}\to\mathcal{B}/\mathcal{B}_0$ be the natural map from $\mathcal{B}(\mathcal{H})$ into the Calkin algebra. Since the Calkin algebra is a Banach algebra with identity, the next definition makes sense.

**4.1. Definition.** If $A\in\mathcal{B}(\mathcal{H})$, the *essential spectrum* of $A$, $\sigma_e(A)$, is the spectrum of $\pi(A)$ in $\mathcal{B}/\mathcal{B}_0$; that is, $\sigma_e(A)=\sigma(\pi(A))$. Similarly the *left and right essential spectrum* of $A$ are defined by $\sigma_{\ell e}(A)=\sigma_\ell(\pi(A))$ and $\sigma_{re}(A)=\sigma_r(\pi(A))$, respectively.

The proof of the next proposition is a straightforward application of the general properties of the various spectra in an arbitrary Banach algebra.

**4.2. Proposition.** Let $A\in\mathcal{B}(\mathcal{H})$.

(a) $\sigma_e(A)=\sigma_{\ell e}(A)\cup\sigma_{re}(A)$.

(b) $\sigma_{\ell e}(A)=\sigma_{re}(A^*)^*$.

(c) $\sigma_{\ell e}(A)\subseteq\sigma_\ell(A)$, $\sigma_{re}(A)\subseteq\sigma_r(A)$, and $\sigma_e(A)\subseteq\sigma(A)$.

(d) $\sigma_{\ell e}(A)$, $\sigma_{re}(A)$, and $\sigma_e(A)$ are compact sets.

(e) If $K$ is a compact operator, $\sigma_{\ell e}(A+K)=\sigma_{\ell e}(A)$, $\sigma_{re}(A+K)=\sigma_{re}(A)$, and $\sigma_e(A+K)=\sigma_e(A)$.

Our understanding of semi-Fredholm operators gained in the preceding sections can now be applied to better understand the essential spectrum. Indeed, $\sigma_{\ell e}(A)=\{\lambda\in\mathbb{C}:A-\lambda\notin\mathcal{SF}_\ell\}$. Thus an application of Theorem 2.3 gives us the following.
