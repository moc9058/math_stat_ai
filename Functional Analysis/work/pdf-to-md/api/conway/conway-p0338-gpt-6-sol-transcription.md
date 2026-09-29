(c) If $\psi$ is bounded, $\rho(\phi)\rho(\psi)=\rho(\psi)\rho(\phi)=\rho(\phi\psi)$;

(d) $\rho(\phi)^*\rho(\phi)=\rho(|\phi|^2)$.

The proof of this theorem is left as an exercise.

**4.11. The Spectral Theorem.** *If $N$ is a normal operator on $\mathcal H$, then there is a unique spectral measure $E$ defined on the Borel subsets of $\mathbb C$ such that:*

(a) $N=\int z\,dE(z)$;

(b) $E(\Delta)=0$ if $\Delta\cap\sigma(N)=\square$;

(c) if $U$ is an open subset of $\mathbb C$ and $U\cap\sigma(N)\ne\square$, then $E(U)\ne0$;

(d) if $A\in\mathcal B(\mathcal H)$ such that $AN\subseteq NA$ and $AN^*\subseteq N^*A$, then $A(\int\phi\,dE)\subseteq(\int\phi\,dE)A$ for every Borel function $\phi$ on $\mathbb C$.

Before launching into the proof, a few words motivating the proof are appropriate. Suppose a spectral measure $E$ defined on the Borel subsets of $\mathbb C$ is given and let $N=\int z\,dE(z)$. It is not difficult to see that if $0\leq a\leq b<\infty$ and $\Delta$ is the annulus $\{z:a\leq|z|\leq b\}$, then $\mathcal H_\Delta=E(\Delta)\mathcal H=\{h\in\operatorname{dom}N:h\in\operatorname{dom}N^n\text{ for all }n\text{ and }a^n\|h\|\leq\|N^nh\|\leq b^n\|h\|\}$. $\mathcal H_\Delta$ is a closed subspace of $\mathcal H$ that reduces $N$ and $N|_{\mathcal H_\Delta}$ is bounded. The idea behind the proof is to write $\mathbb C$ as the disjoint union of annuli $\{\Delta_j\}$ such that for each $\Delta_j$ there is a reducing subspace $\mathcal H_{\Delta_j}$ for $N$ with $N_j\equiv N|_{\mathcal H_{\Delta_j}}$ bounded, and, moreover, such that $\mathcal H=\bigoplus_j\mathcal H_{\Delta_j}$. Once this is done the Spectral Theorem for bounded normal operators can be applied to each $N_j$ and direct sums of these can be formed to obtain the spectral measure for $N$.

So we would like to show that for the annulus $\{z:a\leq|z|\leq b\}$, $\{h\in\operatorname{dom}N:h\in\operatorname{dom}N^n\text{ for all }n\text{ and }a^n\|h\|\leq\|N^nh\|\leq b^n\|h\|\}$ is a reducing subspace for $N$. To facilitate this, we will use the operator $B=(1+N^*N)^{-1}$ which is a positive contraction (4.2). To understand what is done below note that $z\mapsto(1+|z|^2)^{-1}$ maps $\mathbb C$ onto $(0,1]$ and $a\leq|z|\leq b$ if and only if $(1+a^2)^{-1}\geq(1+|z|^2)^{-1}\geq(1+b^2)^{-1}$.

**4.12. Lemma.** *If $N$ is a normal operator, $B=(1+N^*N)^{-1}$, and $C=N(1+N^*N)^{-1}$, then $BC=CB$ and $(1+N^*N)^{-1}N\subseteq C$.*

**Proof.** From (4.2), $B$ and $C$ are contractions and $B\geq0$. It will first be shown that $(1+N^*N)^{-1}N\subseteq C$; that is, $BN\subseteq NB$. If $f\in\operatorname{dom}BN$, then $f\in\operatorname{dom}N$. Let $g\in\operatorname{dom}N^*N$ such that $f=(1+N^*N)g$. Then $N^*Ng\in\operatorname{dom}N$; hence $Ng\in\operatorname{dom}NN^*=\operatorname{dom}N^*N$. Thus $Nf=Ng+NN^*Ng=(1+N^*N)Ng$. Therefore $BNf=B(1+N^*N)Ng=Ng$. But $NBf=Ng$, so $BN=NB$ on $\operatorname{dom}N$. Thus $BN\subseteq NB$.

If $h\in\mathcal H$, let $f\in\operatorname{dom}N^*N$ such that $h=(1+N^*N)f$. So $BCh=BNBh=BNf=NBf=NBBh=CBh$. Hence $BC=CB$. $\blacksquare$

**4.13. Lemma.** *With the same notation as in Lemma 4.12, if $B=\int t\,dP(t)$ is its spectral representation, $1>\delta>0$, and $\Delta$ is a Borel subset of $[\delta,1]$, then*
