**Proof.** If $h\in\ker(A-\lambda)$ and $g\in\ker(A-\mu)$, then the fact (5.6) that $A^*g=\bar\mu g$ implies that
$$
\lambda\langle h,g\rangle=\langle Ah,g\rangle=\langle h,A^*g\rangle
=\langle h,\bar\mu g\rangle=\mu\langle h,g\rangle.
$$
Thus $(\lambda-\mu)\langle h,g\rangle=0$. Since $\lambda-\mu\ne0$, $h\perp g$. ■

**5.8. Proposition.** *If $A=A^*$ and $\lambda\in\sigma_p(A)$, then $\lambda$ is a real number.*

**Proof.** If $Ah=\lambda h$, then $Ah=A^*h=\bar\lambda h$ by (5.6). So $(\lambda-\bar\lambda)h=0$. Since $h$ can be chosen different from $0$, $\lambda=\bar\lambda$. ■

The main result prior to entering the proof of Theorem 5.1 is to show that a compact self-adjoint operator has nonzero eigenvalues. If (5.3c) is examined, we see that there is a $\lambda_n$ in $\sigma_p(T)$ with $|\lambda_n|=\|T\|$. Since the preceding proposition says that $\lambda_n\in\mathbb R$, it must be that $\lambda_n=\pm\|T\|$. That is, either $\pm\|T\|\in\sigma_p(T)$. This is the key to showing that $\sigma_p(T)$ is nonvoid.

**5.9. Lemma.** *If $T$ is a compact self-adjoint operator, then either $\pm\|T\|$ is an eigenvalue of $T$.*

**Proof.** If $T=0$, the result is clear. So suppose $T\ne0$. By Proposition 2.13 there is a sequence $\{h_n\}$ of unit vectors such that $|\langle Th_n,h_n\rangle|\to\|T\|$. By passing to a subsequence if necessary, we may assume that $\langle Th_n,h_n\rangle\to\lambda$, where $|\lambda|=\|T\|$. It will be shown that $\lambda\in\sigma_p(T)$. Since $|\lambda|=\|T\|$,
$$
0\le\|(T-\lambda)h_n\|^2
=\|Th_n\|^2-2\lambda\langle Th_n,h_n\rangle+\lambda^2
\le 2\lambda^2-2\lambda\langle Th_n,h_n\rangle\to0.
$$
Hence $\|(T-\lambda)h_n\|\to0$. By (4.14), $\lambda\in\sigma_p(T)$. ■

**Proof of Theorem 5.1.** By Lemma 5.9 there is a real number $\lambda_1$ in $\sigma_p(T)$ with $|\lambda_1|=\|T\|$. Let $\mathcal E_1=\ker(T-\lambda_1)$, $P_1=$ the projection onto $\mathcal E_1$, $\mathcal H_2=\mathcal E_1^\perp$. By (5.6) $\mathcal E_1$ reduces $T$, so $\mathcal H_2$ reduces $T$. Let $T_2=T|_{\mathcal H_2}$; then $T_2$ is a self-adjoint compact operator on $\mathcal H_2$. (Why?)

By (5.9) there is an eigenvalue $\lambda_2$ for $T_2$ such that $|\lambda_2|=\|T_2\|$. Let $\mathcal E_2=\ker(T_2-\lambda_2)$. Note that $(0)\ne\mathcal E_2\subseteq\ker(T-\lambda_2)$. If it were the case that $\lambda_1=\lambda_2$, then $\mathcal E_2\subseteq\ker(T-\lambda_1)=\mathcal E_1$. Since $\mathcal E_1\perp\mathcal E_2$, it must be that $\lambda_1\ne\lambda_2$. Let $P_2=$ the projection of $\mathcal H$ onto $\mathcal E_2$ and put $\mathcal H_3=(\mathcal E_1\oplus\mathcal E_2)^\perp$. Note that $\|T_2\|\le\|T\|$ so that $|\lambda_2|\le|\lambda_1|$.

Using induction (give the details) we obtain a sequence $\{\lambda_n\}$ of real eigenvalues of $T$ such that

(i) $|\lambda_1|\ge|\lambda_2|\ge\cdots$;

(ii) If $\mathcal E_n=\ker(T-\lambda_n)$, $|\lambda_{n+1}|=\|T|_{(\mathcal E_1\oplus\cdots\oplus\mathcal E_n)^\perp}\|$.

By (i) there is a nonnegative number $\alpha$ such that $|\lambda_n|\to\alpha$.

**Claim.** $\alpha=0$; that is, $\lim\lambda_n=0$.

In fact, let $e_n\in\mathcal E_n$, $\|e_n\|=1$. Since $T$ is compact, there is an $h$ in $\mathcal H$ and a subsequence $\{e_{n_j}\}$ such that $\|Te_{n_j}-h\|\to0$. But $e_n\perp e_m$ for $n\ne m$ and $Te_{n_j}=\lambda_{n_j}e_{n_j}$. Hence $\|Te_{n_j}-Te_{n_i}\|^2=\lambda_{n_j}^2+\lambda_{n_i}^2\ge2\alpha^2$. Since $\{Te_{n_j}\}$ is a Cauchy sequence, $\alpha=0$.
