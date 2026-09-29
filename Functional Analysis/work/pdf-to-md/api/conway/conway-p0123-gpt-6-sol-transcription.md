## §3. Some Geometric Consequences of the Hahn–Banach Theorem

In order to exploit the Hahn–Banach Theorem in the setting of a LCS, it is necessary to establish some properties of continuous linear functionals. The proofs of the relevant propositions are similar to the proofs of the corresponding facts about linear functionals on normed spaces given in §III.5. For example, a hyperplane in a TVS is either closed or dense (see III.5.2). The proof of the next fact is similar to the proof of (III.2.1) and (III.5.3) and will not be given.

**3.1. Theorem.** *If $\mathscr{X}$ is a TVS and $f:\mathscr{X}\to\mathbb{F}$ is a linear functional, then the following statements are equivalent.*

(a) $f$ is continuous.

(b) $f$ is continuous at 0.

(c) $f$ is continuous at some point.

(d) $\ker f$ is closed.

(e) $x\mapsto |f(x)|$ is a continuous seminorm.

*If $\mathscr{X}$ is a LCS and $\mathscr{P}$ is a family of seminorms that defines the topology on $\mathscr{X}$, then the statements above are equivalent to the following:*

(f) There are $p_1,\ldots,p_n$ in $\mathscr{P}$ and positive scalars $\alpha_1,\ldots,\alpha_n$ such that $|f(x)|\leq\sum_{k=1}^{n}\alpha_kp_k(x)$ for all $x$.

The proof of the next proposition is similar to the proof of Proposition 1.14 and will not be given.

**3.2. Proposition.** *Let $\mathscr{X}$ be a TVS and suppose that $G$ is an open convex subset of $\mathscr{X}$ that contains the origin. If*

$$
q(x)=\inf\{t:t\geq 0\text{ and }x\in tG\},
$$

*then $q$ is a non-negative continuous sublinear functional and $G=\{x:q(x)<1\}$.*

Note that the difference between the preceding proposition and (1.14) is that here $G$ is not assumed to be balanced and the consequence is a sublinear functional ($q(\alpha x)=\alpha q(x)$ if $\alpha\geq 0$) that is not necessarily a seminorm.

The geometric consequences of the Hahn–Banach Theorem are achieved by interpreting that theorem in light of the correspondence between linear functionals and hyperplanes and between sublinear functionals and open convex neighborhoods of the origin. The next result is typical.

**3.3. Theorem.** *If $\mathscr{X}$ is a TVS and $G$ is an open convex nonempty subset of $\mathscr{X}$ that does not contain the origin, then there is a closed hyperplane $\mathscr{M}$ such that $\mathscr{M}\cap G=\square$.*
