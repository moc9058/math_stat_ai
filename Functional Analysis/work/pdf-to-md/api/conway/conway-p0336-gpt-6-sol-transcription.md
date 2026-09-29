If $(X,\Omega)$ is a measurable space and $\mathcal H$ is a Hilbert space, recall the definition of a spectral measure $E$ for $(X,\Omega,\mathcal H)$ (IX.1.1). If $h,k\in\mathcal H$, let $E_{h,k}$ be the complex-valued measure given by $E_{h,k}(\Delta)=\langle E(\Delta)h,k\rangle$ for each $\Delta$ in $\Omega$.

Let $\phi:X\to\mathbb C$ be an $\Omega$-measurable function and for each $n$ let $\Delta_n=\{x\in X:n-1\leq|\phi(x)|<n\}$. So $\chi_{\Delta_n}\phi$ is a bounded $\Omega$-measurable function. Put $\mathcal H_n=E(\Delta_n)\mathcal H$. Since $\bigcup_{n=1}^{\infty}\Delta_n=X$ and the sets $\{\Delta_n\}$ are pairwise disjoint, $\bigoplus_{n=1}^{\infty}\mathcal H_n=\mathcal H$. If $E_n(\Delta)=E(\Delta\cap\Delta_n)$, $E_n$ is a spectral measure for $(X,\Omega,\mathcal H_n)$. Also, $\int\phi\,dE_n$ is a normal operator on $\mathcal H_n$. Define

$$
\mathcal D_\phi\equiv\left\{h\in\mathcal H:\sum_{n=1}^{\infty}\left\|\left(\int\phi\,dE_n\right)E(\Delta_n)h\right\|^2<\infty\right\}. \tag{4.5}
$$

By Lemma 4.4, $N_\phi:\mathcal H\to\mathcal H$ given by

$$
N_\phi h=\sum_{n=1}^{\infty}\left(\int\phi\,dE_n\right)E(\Delta_n)h \tag{4.6}
$$

for $h$ in $\mathcal D_\phi$ is a normal operator. The operator $N_\phi$ is also denoted by

$$
N_\phi=\int\phi\,dE.
$$

**4.7. Theorem.** If $E$ is a spectral measure for $(X,\Omega,\mathcal H)$, $\phi:X\to\mathbb C$ is an $\Omega$-measurable function, and $\mathcal D_\phi$ and $N_\phi$ are defined as in (4.5) and (4.6), then:

(a) $\mathcal D_\phi=\{h\in\mathcal H:\int|\phi|^2\,dE_{h,h}<\infty\}$;

(b) for $h$ in $\mathcal D_\phi$ and $f$ in $\mathcal H$, $\phi\in L^1(|E_{h,f}|)$ with

$$
\int|\phi|\,d|E_{h,f}|\leq\|f\|\left(\int|\phi|^2\,dE_{h,h}\right)^{1/2}, \tag{4.8}
$$

$$
\left\langle\left(\int\phi\,dE\right)h,f\right\rangle=\int\phi\,dE_{h,f}, \tag{4.9}
$$

and

$$
\left\|\left(\int\phi\,dE\right)h\right\|^2=\int|\phi|^2\,dE_{h,h}.
$$

**Proof.** Using the $*$-homomorphic properties associated with a spectral measure (IX.1.12), one obtains

$$
\begin{aligned}
\left\|\left(\int\phi\,dE_n\right)E(\Delta_n)h\right\|^2
&=\left\langle
\left(\int\chi_{\Delta_n}\phi\,dE\right)^*
\left(\int\chi_{\Delta_n}\phi\,dE\right)h,h
\right\rangle\\
&=\int_{\Delta_n}|\phi|^2\,dE_{h,h}.
\end{aligned}
$$

From here, (a) is immediate.

Now let $h\in\mathcal D_\phi$, $f\in\mathcal H$. By the Radon–Nikodym Theorem, there is an $\Omega$-measurable function $u$ such that $|u|\equiv1$ and $|E_{h,f}|=uE_{h,f}$, where $|E_{h,f}|$ is
