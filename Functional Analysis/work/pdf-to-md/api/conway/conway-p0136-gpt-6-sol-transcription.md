Distributions are, in a certain sense, generalizations of the concept of function as the following example illustrates.

**5.20. Example.** Let $f$ be a Lebesgue measurable function on $\Omega$ that is locally integrable (that is, $\int_K |f|\,d\lambda<\infty$ for every compact subset $K$ of $\Omega$—here $\lambda$ is $d$-dimensional Lebesgue measure). If $L_f:\mathcal D(\Omega)\to\mathbb F$ is defined by $L_f(\phi)=\int f\phi\,d\lambda$, $L_f$ is a distribution.

From Corollary 5.18 we arrive at the following.

**5.21. Proposition.** *A linear functional $L:\mathcal D(\Omega)\to\mathbb F$ is a distribution if and only if for every sequence $\{\phi_n\}$ in $\mathcal D(\Omega)$ such that $\operatorname{cl}\!\left[\bigcup_{n=1}^{\infty}\operatorname{spt}\phi_n\right]=K$ is compact in $\Omega$ and $\phi_n^{(k)}(x)\to0$ uniformly on $K$ as $n\to\infty$ for every $k=(k_1,\ldots,k_d)$, it follows that $L(\phi_n)\to0$.*

Proposition 5.21 is usually taken as the definition of a distribution in books on differential equations. There is the advantage that (5.21) can be understood with no knowledge of locally convex spaces and inductive limits. Moreover, most theorems on distributions can be proved by using (5.21). However, the realization that a distribution is precisely a continuous linear functional on a LCS contributes more than cultural edification. This knowledge brings power as it enables you to apply the theory of LCS’s (including the Hahn-Banach Theorem).

The exercises contain more results on distributions, but now we must return to the proof of Proposition 5.16. To do this the idea of a topological complement is needed. We have seen this idea in Section III.13.

**5.22. Proposition.** *If $\mathcal X$ is a TVS and $\mathcal Y\leq\mathcal X$, the following statements are equivalent.*

(a) *There is a closed linear subspace $\mathcal Z$ of $\mathcal X$ such that $\mathcal Y\cap\mathcal Z=(0)$, $\mathcal Y+\mathcal Z=\mathcal X$, and the map of $\mathcal Y\times\mathcal Z\to\mathcal X$ given by $(y,z)\mapsto y+z$ is a homeomorphism.*

(b) *There is a continuous linear map $P:\mathcal X\to\mathcal X$ such that $P\mathcal X=\mathcal Y$ and $P^2=P$.*

**Proof.** (a) $\Rightarrow$ (b): Define $P:\mathcal X\to\mathcal X$ by $P(y+z)=y$, for $y$ in $\mathcal Y$ and $z$ in $\mathcal Z$. It is easy to verify that $P$ is linear and $P\mathcal X=\mathcal Y$. Also, $P^2(y+z)=PP(y+z)=Py=y=P(y+z)$; so $P^2=P$. If $\{y_i+z_i\}$ is a net in $\mathcal X$ such that $y_i+z_i\to y+z$, then (a) implies that $y_i\to y$ (and $z_i\to z$). Hence $P(y_i+z_i)\to P(y+z)$ and $P$ is continuous.

(b) $\Rightarrow$ (a): If $P$ is given, let $\mathcal Z=\ker P$. So $\mathcal Z\leq\mathcal X$. Also, $x=Px+(x-Px)$ and $y=Px\in\mathcal Y$, and $z=x-Px$ has $Pz=Px-P^2x=Px-Px=0$, so $z\in\mathcal Z$. Thus, $\mathcal Y+\mathcal Z=\mathcal X$. If $x\in\mathcal Y\cap\mathcal Z$, then $Px=0$ since $x\in\mathcal Z$; but also $x=Pw$ for some $w$ in $\mathcal X$ since $x\in\mathcal Y=P\mathcal X$. Therefore $0=Px=P^2w=Pw=x$; that is, $\mathcal Y\cap\mathcal Z=(0)$. Now suppose that $\{y_i\}$ and $\{z_i\}$ are nets in $\mathcal Y$ and $\mathcal Z$. If $y_i\to y$ and $z_i\to z$, then $y_i+z_i\to y+z$ because addition is continuous. If, on the other
