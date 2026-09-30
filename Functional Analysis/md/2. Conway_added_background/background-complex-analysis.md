# Complex analysis: prerequisites, theory, and applications to Conway

This unified English-language supplement is added study material, not part of
Conway's original text. It assumes no previous complex analysis. It first
rebuilds the real-analysis and topology tools needed to read the proofs, then
develops complex analysis and its functional-analysis applications.

The starting knowledge is elementary arithmetic with real and complex numbers,
trigonometry, and standard linear algebra. Real-analysis and topology terms
are reintroduced when needed. In particular, “modulus” means the size of a
complex number (CA.1), and “completeness” is the property guaranteeing that
Cauchy sequences have limits in the space under discussion (CA.2).
The least-upper-bound property of the real numbers is the foundational input;
CA.2 explains its meaning and how it supplies completeness. Elementary linear
algebra is not retaught. Lebesgue measure is not constructed from set theory;
CA.19 explains the terminology and links to the needed measure-theoretic proofs.

Read each result as answering two questions: what is being asserted, and why
do its assumptions make it true? The proofs display the estimates behind
phrases such as “by compactness” and “pass to the limit.” A reference to an
earlier CA item points to a tool developed here. Later applications provide
motivation; they are not prerequisites.

All results in this file use one consecutive numbering system, **CA.1–CA.52**.
The prerequisite material and the complex-analysis material are no longer
separate files. Original Conway theorem numbers and chapter organization are
unchanged. In complex analysis, a **domain** means a nonempty open connected
subset of the complex plane; “open” and “connected” are explained in CA.3
and CA.7. The domain of a function in the ordinary set-theoretic sense need
not be a domain in this more specific sense.

## Reading route

| Sequence | Content and purpose |
| --- | --- |
| [CA.1–CA.8](#ca-1) | Geometry, completeness, compactness, uniform continuity, connectedness, and holes. |
| [CA.9–CA.16](#ca-9) | Series, uniform limits, real differentiation, and justified limit/integral/derivative exchanges. |
| [CA.17–CA.20](#ca-17) | Finite subdivisions of curves, orientation, measures, and polar-coordinate area integrals. |
| [CA.21–CA.35](#ca-21) | Complex differentiation, power series, Cauchy theory, Taylor expansions, and their rigidity consequences. |
| [CA.36–CA.44](#ca-36) | Infinity, winding numbers, Laurent/residue theory, and Banach-valued analytic tools. |
| [CA.45–CA.52](#ca-45) | A detailed second pass: deformation, logarithms, Morera, Bergman estimates, zero counting, local inverses, Schwarz's lemma, and worked examples. |

For Conway I.§1, read the prerequisites and CA.21–CA.35, then CA.48.
Before III.§8, also read CA.36–CA.39 and CA.44. Before VII.§3–4,
include CA.40–CA.43 and the worked spectral calculation in CA.52.
Later second-pass results are not silently used in the first-pass proofs.
Use the [full background index](background-index.md) to jump to any numbered item.

## Geometry, limits, and topology

<a id="ca-1"></a>
### Definition and Lemma CA.1. Complex geometry and estimates

Write $z=x+iy$, where $x,y$ are real and $i^2=-1$. Identify $z$ with
the point $(x,y)$ in the plane. Its **real part** is $\operatorname{Re}z=x$,
its **imaginary part** is $\operatorname{Im}z=y$, and its **complex
conjugate** is $\overline z=x-iy$, the reflection across the real axis.

The **modulus**, also called the absolute value, is $|z|=\sqrt{x^2+y^2}$.
It is the Euclidean distance from $z$ to zero. For example, $|3+4i|=5$.
It is a nonnegative real number, even when $z$ is not real. Thus
$|f(z)|\leq M$ says that the values of $f$ stay within distance $M$
of zero. We do not order complex numbers themselves by inequalities.

The distance between points is $d(z,w)=|z-w|$. For $r>0$, the **open
disk** $D(a,r)=\{z:|z-a|<r\}$ consists of points strictly less than $r$
from the center $a$. The **closed disk**
$\overline{D(a,r)}=\{z:|z-a|\leq r\}$ also contains the boundary circle
$\{z:|z-a|=r\}$. A disk includes its interior; a circle does not.

For $z\ne0$, polar form is $z=r(\cos\theta+i\sin\theta)$, where
$r=|z|>0$. The angle $\theta$ is an **argument** of $z$. Adding an
integer multiple of $2\pi$ gives the same number: this is what
“determined modulo $2\pi$” means. For example, $0$ and $2\pi$ are both
arguments of 1. Choosing arguments continuously as $z$ moves is a
separate problem, addressed by logarithm branches in CA.26.

For real $t$, we will write $e^{it}$ for $\cos t+i\sin t$ when
parametrizing circles. CA.26 defines the exponential for all complex
arguments and proves that it agrees with this notation.

The identities and inequalities used constantly are

$$
|zw|=|z||w|,\quad |z+w|\leq|z|+|w|,\quad
\big||z|-|w|\big|\leq|z-w|,\quad
\left|\frac1z-\frac1w\right|=\frac{|z-w|}{|z||w|}
\quad(zw\ne0).
$$

**Proof.** Since $z\overline z=x^2+y^2=|z|^2$, we have
$|zw|^2=zw\overline z\overline w=|z|^2|w|^2$. Taking nonnegative
square roots proves the first identity. Next,

$$
|z+w|^2=|z|^2+2\operatorname{Re}(z\overline w)+|w|^2
\leq |z|^2+2|z||w|+|w|^2=(|z|+|w|)^2.
$$

We used that the real part of a number is at most its modulus. Taking
square roots proves the **triangle inequality**. Geometrically, a direct
journey is no longer than a journey via a third point.

Apply this to $z=(z-w)+w$ to obtain $|z|-|w|\leq|z-w|$.
Interchanging $z,w$ gives $|w|-|z|\leq|z-w|$. Together these prove
the **reverse triangle inequality** $\big||z|-|w|\big|\leq|z-w|$.

Finally, $1/z-1/w=(w-z)/(zw)$ gives the reciprocal identity. If
$|z|,|w|\geq\delta>0$, it implies
$|1/z-1/w|\leq|z-w|/\delta^2$. A denominator **bounded away from zero**
means that one positive lower bound $\delta$ works for all denominators
under consideration. $\square$

<a id="ca-2"></a>
### Definition and Lemma CA.2. Limits, Cauchy sequences, and completeness

A **sequence** $z_1,z_2,\ldots$ converges to $z$, written $z_n\to z$, if

$$
\text{for every }\varepsilon>0\text{ there is }N\text{ such that }
n\geq N\ \Longrightarrow\ |z_n-z|<\varepsilon.
$$

Think of $\varepsilon$ as a requested accuracy and $N$ as the point
after which every term meets it. A **tail** is the part after some index.
The condition concerns the whole tail, not merely infinitely many terms.

A sequence is **Cauchy** if

$$
\text{for every }\varepsilon>0\text{ there is }N\text{ such that }
m,n\geq N\ \Longrightarrow\ |z_n-z_m|<\varepsilon.
$$

Convergence compares terms with a specified limit; the Cauchy condition
compares late terms with each other. It is useful when we can estimate
errors before knowing the limit. Having $|z_{n+1}-z_n|\to0$ alone is
insufficient: the partial sums of $1+1/2+1/3+\cdots$ have small successive
increments but diverge (see CA.10).

Every convergent sequence is Cauchy: once both $z_n$ and $z_m$ are
within $\varepsilon/2$ of the limit $z$, the triangle inequality gives
$|z_n-z_m|\leq|z_n-z|+|z_m-z|<\varepsilon$.

A **metric** is a distance function that is nonnegative, symmetric,
zero exactly for identical points, and satisfies the triangle inequality.
A set with a metric is a **metric space**. It is **complete** if every
Cauchy sequence in it converges to a point *in that same space*.
Completeness is a property of the space, not of a particular sequence.
The real and complex numbers are complete. The rationals are not:
finite decimal truncations of $\sqrt2$ are rational and Cauchy, but their
only real limit is the irrational number $\sqrt2$.

**The real-number input.** For a nonempty real set $S$ bounded above,
its **supremum** $\sup S$ is its least upper bound: it bounds every
element from above, and every smaller number fails to do so. An
**infimum** is the greatest lower bound. The least-upper-bound property
of $\mathbb R$ asserts that such a supremum exists in $\mathbb R$.
It need not belong to the set: $\sup(0,1)=1$.

Here is why this property implies that real Cauchy sequences converge.
A Cauchy sequence $(x_n)$ is bounded: beyond some $N$ all terms are within
1 of $x_N$, and the earlier terms form a finite set. Define

$$
\alpha_N=\inf_{n\geq N}x_n,\qquad
\beta_N=\sup_{n\geq N}x_n,\qquad x=\sup_N\alpha_N.
$$

The intervals $[\alpha_N,\beta_N]$ are nested. Each $\beta_N$ bounds all
the $\alpha_j$ from above, so $\alpha_N\leq x\leq\beta_N$.
For every $\varepsilon>0$, the Cauchy condition gives sufficiently late
tails with $\beta_N-\alpha_N\leq\varepsilon$: all pairs of their terms
are within $\varepsilon$. Thus $x_n$ and $x$ eventually lie in the same
arbitrarily short interval, proving $x_n\to x$.

**Completeness of $\mathbb C$.** Write a complex Cauchy sequence as
$z_n=x_n+iy_n$. Since

$$
|x_n-x_m|\leq|z_n-z_m|,\qquad |y_n-y_m|\leq|z_n-z_m|,
$$

both coordinates are real Cauchy sequences. They converge to real numbers
$x,y$ by the preceding argument. Put $z=x+iy$. The estimate
$|z_n-z|\leq|x_n-x|+|y_n-y|\to0$ proves $z_n\to z$.

**Uniqueness and boundedness.** If $z_n\to z$ and $z_n\to w$, then
$|z-w|\leq|z-z_n|+|z_n-w|\to0$. The left side is fixed, so it is
zero and $z=w$. Finally, a convergent sequence has a tail satisfying
$|z_n|\leq|z|+1$. Taking the maximum of this bound and the moduli of
the finitely many earlier terms bounds the whole sequence. $\square$

For a function, $f(z)\to L$ as $z\to a$ means: for each
$\varepsilon>0$ there is $\delta>0$ such that $0<|z-a|<\delta$
implies $|f(z)-L|<\varepsilon$, for every $z$ in the function's domain.
Here $a$ is approachable by domain points different from $a$.
The condition must hold from **every direction**.

Equivalently, $f(z_n)\to L$ for every sequence of such points tending
to $a$. To prove the reverse implication, if the function-limit condition
fails, some fixed error $\varepsilon_0>0$ remains possible arbitrarily
close to $a$. Choose $z_n$ with $0<|z_n-a|<1/n$ but
$|f(z_n)-L|\geq\varepsilon_0$. This contradicts the sequential condition.
Two directional calculations can therefore disprove a limit, but
agreement on two directions cannot usually prove its existence.

<a id="ca-3"></a>
### Definition and Lemma CA.3. Open sets, closure, and boundary

A set $G\subset\mathbb C$ is **open** if every $a\in G$ has some
$r>0$ with $D(a,r)\subset G$. Each point has room around it that stays
inside $G$. A set is **closed** if its complement is open. These are
not opposite alternatives: a set can be neither, and both $\varnothing$
and $\mathbb C$ are open and closed.

The **closure** $\overline E$ consists of points $a$ whose every disk
meets $E$, however small its radius. The **boundary** $\partial E$
consists of points whose every disk meets both $E$ and its complement;
equivalently $\partial E=\overline E\cap\overline{\mathbb C\setminus E}$.
An **interior point** has a disk entirely inside $E$. For an open disk,
the closure is the closed disk and the boundary is the circle. A bar over
a set means closure; a bar over a complex number means conjugation.

A **neighborhood** of $a$ contains an open set containing $a$.
Relative to a subset $E$, an open set has the form $E\cap U$ with $U$
open in the ambient space. This is **relative openness**: $[0,1/2)$ is
open relative to $[0,1]$, although it is not open in $\mathbb R$.

A function $f:E\to\mathbb C$ is **continuous at $a\in E$** if for
every $\varepsilon>0$ there is $\delta>0$ such that $z\in E$ and
$|z-a|<\delta$ imply $|f(z)-f(a)|<\varepsilon$. Continuity compares
nearby values with the actual value $f(a)$.

A set is closed exactly when it contains limits of all its convergent
sequences. A function is continuous exactly when it preserves sequential
limits. A closed subset of a complete metric space is complete.

**Proof.** Suppose $E$ is closed and $z_n\in E$ converge to $a$.
If $a\notin E$, the open complement contains $D(a,r)$ for some $r>0$.
Convergence puts a whole tail of $(z_n)$ in that disk, contradicting
$z_n\in E$. Hence $a\in E$.

Conversely, suppose $E$ contains all limits of its convergent sequences.
For $a\in\overline E$, choose $z_n\in E\cap D(a,1/n)$, possible by
the definition of closure. Then $z_n\to a$, so $a\in E$. Thus if
$a\notin E$, some disk about $a$ misses $E$; the complement is open.

For continuity, given an output tolerance $\varepsilon$, choose its
input tolerance $\delta$. A sequence tending to $a$ eventually meets
that input tolerance, so its images tend to $f(a)$. If continuity fails,
CA.2 constructs a sequence tending to $a$ whose images stay a fixed
positive distance from $f(a)$, proving the converse.

Finally, a Cauchy sequence in a closed subset of a complete metric space
first acquires a limit in the ambient space by completeness. Closedness
keeps that limit in the subset. Both hypotheses have a distinct job.
$\square$

An open disk, its boundary circle, and its closed disk are three different
sets. A function holomorphic (complex differentiable at every point,
as defined in CA.23) on the open disk need not be bounded there
or defined on the boundary: $1/(1-z)$ on $D(0,1)$ is the basic warning.

<a id="ca-4"></a>
### Theorem CA.4. Compactness in the plane and nested compact sets

A collection of relatively open sets is an **open cover** of $K$ if
every point of $K$ belongs to at least one member. A **finite subcover**
is a choice of finitely many members that still covers $K$. The set is
**compact** if every open cover has a finite subcover. This lets us turn
information around individual points into finitely many choices that
work for the whole set.

In $\mathbb C$, three conditions are equivalent: $K$ is compact; $K$
is closed and bounded; every sequence in $K$ has a subsequence converging
to a point of $K$. Here **bounded** means contained in a disk of finite
radius, and a **subsequence** $z_{n_j}$ uses strictly increasing indices.
The third condition is called **sequential compactness**. Its equivalence
with compactness holds in metric spaces. The closed-and-bounded
characterization does not hold in arbitrary metric or infinite-dimensional
normed spaces.

Nested nonempty compact sets $K_1\supseteq K_2\supseteq\cdots$ have
nonempty intersection. Their **diameter** is
$\operatorname{diam}K_n=\sup\{|x-y|:x,y\in K_n\}$.
If the diameters tend to zero, the intersection has exactly one point.

**Proof.** Every bounded real sequence has a convergent subsequence:
bisect an interval containing it, retain a half containing infinitely
many terms, and repeat. Write the retained intervals as $[a_j,b_j]$.
Their left endpoints increase, their right endpoints decrease, and their
lengths tend to zero. The number $x=\sup_j a_j$ lies in every interval,
as in CA.2. Choose a sequence term in the $j$th interval with index
larger than the previously chosen index. Infinitely many terms are
available there, and the chosen term is within $b_j-a_j$ of $x$, so
this subsequence converges. Apply this to the real coordinates and then, within that
subsequence, the imaginary coordinates. A bounded complex sequence
therefore has a convergent subsequence; closedness retains its limit.

A sequentially compact metric space is **totally bounded**: for every
$\varepsilon>0$, finitely many radius-$\varepsilon$ balls cover it.
Otherwise choose $x_1$, then $x_2$ outside its ball, then $x_3$ outside
the first two balls, and continue. Every pair of chosen points is at
least $\varepsilon$ apart. No subsequence can be Cauchy, hence none can
converge, a contradiction.

Fix an open cover. Some $\delta>0$ must make every relative ball
$D(x,\delta)\cap K$ fit in a single cover member. If not, choose
$x_n\in K$ whose radius-$1/n$ relative ball fits in none. A subsequence
tends to $x\in K$. A cover member $U$ contains $x$, and openness gives
$D(x,r)\cap K\subset U$ for some $r>0$. Eventually
$|x_{n_j}-x|<r/2$ and $1/n_j<r/2$, so the triangle inequality puts
the whole radius-$1/n_j$ relative ball inside $U$, a contradiction.
Such a uniform radius is often called a **Lebesgue number**.

Total boundedness supplies finitely many radius-$\delta/2$ balls covering
$K$. Their centers form a finite **net**: every point is within
$\delta/2$ of a center. For each center choose a cover member containing
its radius-$\delta$ relative ball. These finitely many members cover $K$.
Thus sequential compactness implies compactness, and in particular closed
bounded subsets of the plane are compact.

Conversely compactness gives boundedness from the cover $D(0,n)$.
To prove closedness, fix $a\notin K$. For each $x\in K$, disks centered
at $a$ and $x$, both of radius $|a-x|/3$, are disjoint. Finitely many
of the disks centered in $K$ cover $K$. Intersect the corresponding
disks centered at $a$. This is an open neighborhood of $a$ missing $K$,
so the complement is open. The already proved
bounded-sequence argument gives the remaining sequential equivalence.

Finally choose $x_n\in K_n$. A subsequence converges in $K_1$; for
each $m$ its tail lies in the closed set $K_m$, so its limit belongs to
every $K_m$. Two points in the intersection have distance at most
$\operatorname{diam}K_n$ for every $n$, proving uniqueness when these
diameters tend to zero. This is the nested-triangle step in Goursat's
proof, not a visual assumption about shrinking pictures. $\square$

For example, $D(0,1)$ is bounded but not compact: $1-1/n$ tends to the
missing boundary point 1, and so does every subsequence. The closed disk
is compact. The plane is complete but not compact: the sequence $n$ has
no convergent subsequence. Completeness promises a limit for sequences
already known to be Cauchy; compactness supplies convergent subsequences
of arbitrary sequences in the set.

For completeness, compactness also implies sequential compactness in a
general metric space. If no point had every neighborhood containing
infinitely many terms of a given sequence, choose at each point a
neighborhood containing only finitely many terms. A finite subcover
would contain only finitely many terms in total, a contradiction.
Thus some $x$ has infinitely many terms in every radius-$1/j$ ball;
choosing increasing indices from these balls gives a subsequence
converging to $x$. This justifies the metric-space formulation in CA.5.

<a id="ca-5"></a>
### Theorem CA.5. Uniform continuity and extrema on compact sets

A map $f:K\to Y$ is **uniformly continuous** if for every
$\varepsilon>0$ one $\delta>0$ satisfies

$$
x,y\in K,\quad d(x,y)<\delta
\quad\Longrightarrow\quad d_Y(f(x),f(y))<\varepsilon.
$$

In continuity at a point, $\delta$ may depend on that point; here it
must work everywhere. Every continuous map from a compact metric space
is uniformly continuous. A continuous real function on a nonempty compact
set is bounded and **attains** its maximum and minimum: actual points
have those values, not just values arbitrarily close to them.

**Proof.** Failure of uniform continuity means some fixed
$\varepsilon_0>0$ defeats every $\delta$. Taking $\delta=1/n$ gives
$x_n,y_n$ with $d(x_n,y_n)<1/n$ but image distance at least
$\varepsilon_0$. Compactness gives a subsequence $x_{n_j}\to x\in K$.
Since $d(y_{n_j},x)\leq1/n_j+d(x_{n_j},x)$, also $y_{n_j}\to x$.
Continuity makes both image sequences tend to $f(x)$, so their distance
tends to zero, contradicting the fixed lower bound.

For real $f$, the relatively open sets $\{x:|f(x)|<n\}$ cover $K$.
A finite subcover supplies a bound $|f|<N$ everywhere. Let $M=\sup f(K)$.
Choose $x_n$ with $M-1/n<f(x_n)\leq M$, possible by the definition
of supremum. A subsequence converges to $x\in K$, and continuity gives
$f(x)=\lim_j f(x_{n_j})=M$. Apply this argument to $-f$ to obtain
a minimum for $f$. $\square$

Pointwise continuity chooses $\delta$ after fixing a point. Compactness
is what allows a **single** delta, a step needed for uniform approximation
of contours and for Riemann-sum estimates.

For comparison, $f(x)=x$ on $(0,1)$ is continuous and bounded but has
no maximum or minimum. Its supremum 1 and infimum 0 are not attained.

<a id="ca-6"></a>
### Lemma CA.6. Positive distance and compact neighborhoods

For a nonempty set $E$, define $d(z,E)=\inf_{w\in E}|z-w|$.
This is the **distance to a set**, the smallest distance one can approach,
whether or not a nearest point exists. It is **1-Lipschitz**, meaning
$|d(z,E)-d(v,E)|\leq|z-v|$, hence continuous.
If $K$ is nonempty and compact, $G$ is open,
and $K\subset G$, then some $\delta>0$ satisfies
$\{z:d(z,K)\leq\delta\}\subset G$; this neighborhood is compact.
In particular, if a continuous function is nonzero on compact $K$, its
modulus has a strictly positive minimum there.

**Proof.** For every $w\in E$,
$d(z,E)\leq|z-w|\leq|z-v|+|v-w|$. Taking the infimum over $w$
gives $d(z,E)\leq|z-v|+d(v,E)$. Reverse $z,v$ and combine the
two inequalities to obtain the Lipschitz bound.
When $\mathbb C\setminus G$ is nonempty and closed, each $x\in K$
has a disk $D(x,r_x)\subset G$, so its distance to the complement is
at least $r_x>0$. CA.5 says the continuous distance function attains its
minimum $m$ on $K$. Its value at that minimizing point is positive, so
$m>0$. Pointwise positivity alone would not imply a positive infimum.

Take $\delta=m/2$. If $d(z,K)\leq\delta$, continuity of
$x\mapsto|z-x|$ on compact $K$ supplies a nearest point $x\in K$.
Then $|z-x|\leq\delta$, and the distance inequality yields
$d(z,\mathbb C\setminus G)\geq m-\delta>0$, so $z\in G$.
The neighborhood is closed by continuity of distance and bounded because
$K$ is bounded, hence compact by CA.4. For $G=\mathbb C$ any finite
positive delta works. The final assertion is CA.5 applied to $|f|$;
a zero minimum would be attained at a zero. $\square$

For instance, on a circle $|w-c|=r$ and a smaller disk $|z-c|\leq s<r$,
$|w-z|\geq r-s>0$. This one inequality controls every differentiated
Cauchy kernel. Two arbitrary disjoint closed unbounded sets need not have
positive distance, so the compactness hypothesis cannot be discarded.

<a id="ca-7"></a>
### Definition and Theorem CA.7. Connectedness and polygonal paths

A space is connected if it cannot be separated into two disjoint
nonempty relatively open subsets. A component is a maximal connected
subset. A path is a continuous map from $[0,1]$; a polygonal path is a
finite succession of straight segments. Every connected open subset of
$\mathbb C$ is polygonally path connected. Its components are open.
A subset of a connected space that is both open and closed is either
empty or the whole space.

Here a **separation** expresses the whole space as $U\cup V$ with
$U,V$ disjoint, nonempty, and relatively open. Each side is also
relatively closed, since its complement is the other side.
“Maximal” means a connected subset cannot be enlarged while staying
connected. “Polygonally path connected” means any two points can be
joined by finitely many straight segments lying in the set. Components
of any open subset of the plane are open, even when that set is disconnected.

**Proof.** If an interval $I=U\cup V$ had a separation, choose
$u\in U$, $v\in V$, relabeling the sets if needed so $u<v$.
Let $c=\sup(U\cap[u,v])$. Openness near $u$ gives $c>u$.
Points of $U$ approach $c$, so $c$ cannot be in the open set $V$.
Thus $c\in U$ and $c<v$. But openness of $U$ supplies points of
$U\cap[u,v]$ to the right of $c$, contradicting the supremum.
This proves that intervals are connected.

A continuous image of a connected set is connected: inverse images
of a hypothetical separation would separate the original set. In
particular, path images are connected.

Fix $a$ in an open set $G$ and let $P$ be the points reachable from $a$
by polygonal paths in $G$. Around each $z\in G$ take a disk lying in
$G$. If the disk meets $P$, straight segments inside it make all of it
reachable. Otherwise it misses $P$. Hence $P$ and $G\setminus P$ are
relatively open. Any two points of $P$ can be joined via $a$, so $P$
is path connected and therefore connected: a separation of $P$ would
separate a joining path. No connected subset containing $a$ can meet
both $P$ and its relatively open complement. Thus $P$ is exactly the
component of $a$, and it is open in the plane since $G$ is open.
If $G$ is connected, the nonempty open-and-closed subset $P$ must be
all of $G$; otherwise it and its complement would form a separation.
This reasoning proves the last assertion as well. $\square$

This explains two recurring proof steps: a function with derivative zero
is constant on a domain by integration along segments, and a set on which
all derivatives vanish propagates from one disk to a whole component by
being open and closed. It need not propagate to a different component.

<a id="ca-8"></a>
### Definition and Lemma CA.8. Convexity, holes, and simple connectedness

A set is convex if it contains the segment between each pair of its
points. It is star-shaped about $a$ if it contains every segment from
$a$ to one of its points. A domain is simply connected if every closed
continuous path can be continuously deformed to a constant path within
the domain: a deformation is a continuous $H:[0,1]^2\to G$ with
$H(s,0)=H(s,1)$ and the prescribed initial and final loops.

The variable $t$ describes position along a loop; $s$ describes the
stage of the deformation. For each $s$, equality at $t=0,1$ keeps the
path closed. Contracting a loop means $H(0,t)=\gamma(t)$ and
$H(1,t)=a$ independent of $t$. Requiring $H(s,t)\in G$ forbids
crossing points missing from $G$. Such a deformation is called a
**homotopy**.

Every star-shaped domain is simply connected.

**Proof.** For a loop $\gamma$, take
$H(s,t)=(1-s)\gamma(t)+sa$. The segments remain in the domain by
star-shapedness. At $s=0$ this is the loop and at $s=1$ it is constant;
continuity and the closed-loop condition are immediate. $\square$

Connected does not mean simply connected. The punctured plane is
connected but a circle surrounding zero cannot be contracted there;
[CA.45](background-complex-analysis.md#ca-45) proves this using invariance
of the contour integral. A disk is convex; an **annulus**
$\{z:r<|z-a|<R\}$ with $0<r<R$ is ring-shaped and is not simply
connected. These distinctions determine whether a global logarithm or
primitive can exist.

## Series and calculus that survive taking limits

<a id="ca-9"></a>
### Definition and Theorem CA.9. Absolute convergence and geometric tails

A **series** $\sum_{n=0}^\infty a_n$ means the limit, if it exists,
of the **partial sums** $S_N=a_0+\cdots+a_N$. It is not an instruction
to perform an unexplained infinite addition. **Absolute convergence**
means that the nonnegative real series $\sum|a_n|$ has a finite sum.
If
$\sum_{n\geq0}|a_n|<\infty$, the complex series $\sum a_n$ converges,
and its tail has modulus at most the corresponding absolute tail.
For $|q|<1$,

$$
\sum_{n=0}^\infty q^n=\frac1{1-q},\qquad
\left|\sum_{n=N+1}^\infty q^n\right|
\leq\frac{|q|^{N+1}}{1-|q|}.
$$

Absolutely convergent double series may be summed in either order, or by
finite diagonals, without changing their sum.

**Proof.** For $M>N$,

$$
|S_M-S_N|=\left|\sum_{n=N+1}^M a_n\right|
\leq\sum_{n=N+1}^M|a_n|\leq\sum_{n>N}|a_n|.
$$

The last expression tends to zero with $N$ because the absolute series
converges. Thus $(S_N)$ is Cauchy, and completeness (CA.2) supplies a
limit $S$. Letting $M\to\infty$ also proves
$|S-S_N|\leq\sum_{n>N}|a_n|$, the promised tail bound. The finite identity
$(1-q)\sum_{n=0}^Nq^n=1-q^{N+1}$ gives the geometric formula and
its tail estimate. For a double series with
$\sum_{n,m}|a_{n,m}|<\infty$, choose a finite set of pairs outside
which the absolute sum is less than $\varepsilon$. Any two sufficiently
large partial sums containing that set differ by at most the small tail.
This proves both convergence and independence of the order. In particular,
the Cauchy product of two absolutely convergent series equals their
product: finite rectangular sums are products of finite sums, and grouping
by diagonals preserves the limit. $\square$

For clarity, absolute summability of a double series means that the
supremum of $\sum_{(n,m)\in F}|a_{n,m}|$ over finite sets $F$ of pairs
is finite. This definition does not favor either order of summation.
The finite-set argument above shows why rows, columns, and diagonals
give the same answer.

A **norm** $\|v\|$ is a vector's size: it is zero only at zero,
satisfies $\|\lambda v\|=|\lambda|\|v\|$, and satisfies the triangle
inequality. A **Banach space** is a normed vector space complete for the
distance $\|v-w\|$. The proof works there with norms replacing modulus.
A convergent series that is not absolutely convergent is **conditionally
convergent**; the argument does not authorize its rearrangement.

<a id="ca-10"></a>
### Definition and Theorem CA.10. Limsup and the root test

For a nonnegative sequence, $\limsup b_n=\inf_N\sup_{n\geq N}b_n$,
possibly infinite. If $L$ is finite, then for every $t>L$ eventually
$b_n<t$, while for every $t<L$ infinitely many terms satisfy $b_n>t$.
If $L=\limsup|a_n|^{1/n}<1$, the series $\sum a_n$ converges
absolutely. If $L>1$, its terms do not tend to zero and it diverges.
The case $L=1$ gives no conclusion.

To interpret **limsup** (limit superior), set
$B_N=\sup\{b_N,b_{N+1},\ldots\}$. Removing terms cannot increase the
upper bound, so $B_N$ decreases to its infimum. Limsup records this
eventual upper level even when $(b_n)$ oscillates. For example, for
$b_n=1,2,1,2,\ldots$, every $B_N=2$ and the limsup is 2, although
the sequence itself has no limit.

**Proof.** The tail suprema decrease to their infimum, proving the two
assertions about limsup. If $L<1$, choose $L<t<1$; eventually
$|a_n|\leq t^n$, and compare with CA.9. If $L>1$, choose
$1<t<L$; infinitely many terms have $|a_n|>t^n$.
For the inconclusive case, $\sum n^{-2}$ and $\sum n^{-1}$ both have
root limit 1. In the block $2^k\leq n<2^{k+1}$, the first has sum at
most $2^k/2^{2k}=2^{-k}$, so its block sums are summable. The second
has block sum at least $2^k/2^{k+1}=1/2$, so infinitely many blocks
force divergence. $\square$

Applied to $a_n(z-c)^n$, this proves the radius formula in CA.25.
The radius is a **disk** condition, not a claim about every boundary
point. For example $\sum z^n/n$ converges at $z=-1$ by cancellation,
but diverges at $z=1$. At $z=-1$, grouping consecutive pairs proves
convergence, while the unpaired last term tends to zero.

<a id="ca-11"></a>
### Theorem CA.11. Uniform Cauchy criterion and the order of quantifiers

**Pointwise convergence** means $f_n(z)\to f(z)$ after fixing each
$z$ separately; the required index may depend on $z$.
**Uniform convergence on $E$** means that for every $\varepsilon>0$,
one index $N$ gives $|f_n(z)-f(z)|<\varepsilon$ for all $n\geq N$
and all $z\in E$. “Uniform” refers to independence from the point.
CA.21 uses these same definitions in complex analysis.

A sequence $f_n:E\to\mathbb C$ has a uniform limit if and only if
for every $\varepsilon>0$ there is $N$ such that
$|f_n(z)-f_m(z)|<\varepsilon$ for all $m,n\geq N$ and all $z\in E$.
For a series, a summable bound $|g_n(z)|\leq M_n$ guarantees this
condition. The limit of continuous functions is continuous under uniform
convergence, but not under pointwise convergence alone.

**Proof.** If convergence to $f$ is uniform, choose $N$ so that both
$|f_n(z)-f(z)|$ and $|f_m(z)-f(z)|$ are below $\varepsilon/2$.
Adding these bounds gives the uniform Cauchy condition.

Conversely, at each fixed $z$, CA.2 gives $f(z)=\lim_m f_m(z)$.
Use the uniform Cauchy condition with $\varepsilon/2$ and let
$m\to\infty$. This yields $|f_n(z)-f(z)|\leq\varepsilon/2<\varepsilon$
for all $n\geq N$ and all $z$. We used $\varepsilon/2$ because a
strict inequality can become non-strict in the limit. The same $N$
still works everywhere, proving uniform convergence. For series,
$\sum_{n>N}M_n$ bounds every tail at every point and tends to zero.

For continuity at $z_0$, fix one index $n$ with uniform error below
$\varepsilon/3$. Continuity of this particular $f_n$ supplies a
neighborhood on which $|f_n(z)-f_n(z_0)|<\varepsilon/3$. Then

$$
|f(z)-f(z_0)|
\leq|f(z)-f_n(z)|+|f_n(z)-f_n(z_0)|+|f_n(z_0)-f(z_0)|
<\varepsilon.
$$

Under pointwise convergence, the first error need not be small throughout
a neighborhood. Indeed, $x^n$ on $[0,1]$ tends to 0 for $x<1$ but
stays 1 at $x=1$, giving a discontinuous limit. $\square$

An estimate that depends on $z$ may establish pointwise convergence but
does not establish uniform convergence. On $|z|\leq r<1$, geometric
tails have one bound $r^{N+1}/(1-r)$, which is exactly what is needed.

<a id="ca-12"></a>
### Definition and Proposition CA.12. Total derivatives and little-o errors

For a map $F:\mathbb R^2\to\mathbb R^2$, differentiability at $a$
means that there is a real-linear map $L$ such that
$F(a+h)-F(a)=Lh+r(h)$ with $\|r(h)\|/\|h\|\to0$.
The notation $r(h)=o(\|h\|)$ abbreviates this uniform-in-direction
error statement. Partial derivatives alone examine only coordinate
directions. Continuous first partial derivatives near $a$ imply total
differentiability there.

Here $DF(a)=L$ is the **total derivative**, a linear approximation valid
in every direction. “Little-o” means that for every $\varepsilon>0$
there is $\delta>0$ such that $0<\|h\|<\delta$ implies
$\|r(h)\|\leq\varepsilon\|h\|$. An error of size $\|h\|^2$ qualifies;
one of size $3\|h\|$ does not. A **partial derivative** such as $F_x$
varies only the $x$ coordinate. The notation $C^1$ means first partial
derivatives exist and are continuous; $C^2$ means the same through
order two.

**Proof.** We use the real mean value theorem, recalled with its proof
in CA.14; this real-calculus input does not depend on complex analysis.
For one real component, split the increment as

$$
F(a_1+s,a_2+t)-F(a_1,a_2)
=[F(a_1+s,a_2+t)-F(a_1,a_2+t)]
 +[F(a_1,a_2+t)-F(a_1,a_2)].
$$

The mean value theorem expresses this as
$sF_x(\xi,a_2+t)+tF_y(a_1,\eta)$ for intermediate coordinates
$\xi,\eta$ (zero increments need no mean value point).
Subtract $F_x(a)s+F_y(a)t$. The remainder is bounded by
$(|s|+|t|)\omega(\sqrt{s^2+t^2})$, where $\omega(\delta)$ bounds
the oscillations of the partial derivatives within distance $\delta$
of $a$ and tends to zero by continuity. Since
$|s|+|t|\leq\sqrt2\sqrt{s^2+t^2}$, the required little-o bound
follows. Apply this to each component. $\square$

For complex differentiation the real-linear map must specifically be
multiplication by one complex number $c$, represented by
$\begin{pmatrix}\operatorname{Re}c&-\operatorname{Im}c\\
\operatorname{Im}c&\operatorname{Re}c\end{pmatrix}$.
This restriction yields the Cauchy–Riemann equations; it is not the
assertion that every differentiable map of the plane is holomorphic.

<a id="ca-13"></a>
### Lemma CA.13. The chain rule and differentiation along a path

If $F$ and $G$ are differentiable maps of finite-dimensional real spaces,
then $D(G\circ F)(a)=DG(F(a))DF(a)$. Consequently, if $f$ is
holomorphic and $\gamma$ is a differentiable complex-valued real path,
$\frac{d}{dt}f(\gamma(t))=f'(\gamma(t))\gamma'(t)$.

**Proof.** Write $F(a+h)=F(a)+Ah+o(\|h\|)$ and
$G(F(a)+k)=G(F(a))+Bk+o(\|k\|)$. The first expansion implies
$\|k\|\leq C\|h\|$ for small $h$. Substitution in the second
therefore gives $G(F(a+h))=G(F(a))+BAh+o(\|h\|)$.
In detail, the second remainder $r_G(k)$ satisfies
$\|r_G(k)\|/\|h\|\leq C\|r_G(k)\|/\|k\|\to0$ when $k\ne0$,
and is zero when $k=0$. Also $B\,o(\|h\|)=o(\|h\|)$ because a
fixed finite-dimensional linear map is bounded. Thus the only first-order
term is $BAh$. The complex derivative is a real derivative given by multiplication,
so the path formula is this same chain rule. $\square$

This proves the rule used to evaluate contour integrals by primitives.
There is no real mean value theorem of the form
$f(b)-f(a)=f'(c)(b-a)$ for general complex-valued functions. The safe
replacement is the **integral** of the derivative along the segment.

<a id="ca-14"></a>
### Theorem CA.14. Continuous integrals and the fundamental theorem

For a partition $a=t_0<t_1<\cdots<t_N=b$, choose a **tag**
$\tau_j\in[t_{j-1},t_j]$ in each subinterval. A **Riemann sum** is
$\sum_j g(\tau_j)(t_j-t_{j-1})$. The **mesh** is the largest
subinterval length. A Riemann integral is the common limit of these sums
as the mesh tends to zero, independently of partitions and tags. For
complex functions it is also the integral of the real part plus $i$
times the integral of the imaginary part.

A continuous complex function $g$ on $[a,b]$ has a Riemann integral,
with $|\int_a^bg|\leq\int_a^b|g|\leq(b-a)\sup|g|$.
The function $G(t)=\int_a^t g(s)\,ds$ has derivative $g(t)$.
If $F$ is continuously differentiable, then
$\int_a^bF'(t)\,dt=F(b)-F(a)$.

**Proof.** CA.5 gives uniform continuity. For sufficiently fine tagged
partitions, compare both sums with one on a **common refinement**, formed
by combining both sets of partition points. Put
$\omega(\delta)=\sup\{|g(s)-g(t)|:|s-t|\leq\delta\}$ on $[a,b]$.
Uniform continuity gives $\omega(\delta)\to0$. Replacing tags by tags
on finer pieces changes a sum by at most $(b-a)\omega(\delta)$, since
the lengths sum to $b-a$. Thus two sums with mesh at most $\delta$
differ by at most $2(b-a)\omega(\delta)$.
A sequence of sums with mesh tending to zero is Cauchy, so completeness
supplies its limit. The same estimate forces all sufficiently fine sums
to approach that limit, proving that it defines the integral.
The triangle inequality for finite sums
passes to the limit. Moreover

$$
\left|\frac{G(t+h)-G(t)}h-g(t)\right|
\leq\sup_{s\text{ between }t\text{ and }t+h}|g(s)-g(t)|\to0.
$$

For the final assertion, $F-G$ has zero derivative when $g=F'$.
Its real and imaginary parts are constant by the real mean value theorem,
so evaluating at the endpoints proves the formula. $\square$

Here the real mean value theorem follows from Rolle's theorem: subtract
the secant line, use an attained interior extremum of the resulting
function, and apply the two one-sided difference-quotient signs at an
extremum. Rolle's theorem uses continuity on the closed interval and
differentiability inside it. This continuous-integrand version suffices
for the elementary Cauchy proofs; it is distinct from the stronger
Lebesgue theorem for absolutely continuous functions.

In particular, a complex-valued function with derivative zero on a real
interval is constant: apply the real mean value theorem separately to
its real and imaginary parts. This does not require continuity of the
derivative.

<a id="ca-15"></a>
### Theorem CA.15. When limits and derivatives pass through integrals

This lemma anticipates the term **holomorphic**: it means complex
differentiable at every point of an open set, with increments allowed
in all complex directions (the full definition is CA.23). The proof
uses only the derivative and the real-variable calculus just established.

If continuous $g_n\to g$ uniformly on $[a,b]$, then
$\int g_n\to\int g$. More generally, let $q(z,t)$ and its complex
derivative $q_z(z,t)$ be jointly continuous for $z$ in an open set and
$t\in[a,b]$, with $q(\cdot,t)$ holomorphic. Then

$$
F(z)=\int_a^bq(z,t)\,dt
\quad\text{is holomorphic, and}\quad
F'(z)=\int_a^bq_z(z,t)\,dt.
$$

**Proof.** The first error is at most $(b-a)\sup|g_n-g|$.
For the second, fix a closed disk about $z_0$ contained in the domain.
Along the short segment from $z$ to $z+h$, CA.13–CA.14 give

$$
\frac{q(z+h,t)-q(z,t)}h-q_z(z,t)
=\int_0^1[q_z(z+sh,t)-q_z(z,t)]\,ds.
$$

On the product of the disk and $[a,b]$, continuity of $q_z$ is uniform
by compactness. Thus the right side tends uniformly in $t$ to zero.
Integrating and using the first assertion proves the derivative formula.
More explicitly, if the supremum of the right side over $t$ is
$\eta(h)\to0$, then the error in the difference quotient of $F$ is
at most $(b-a)\eta(h)$. This proves existence of the derivative from
its definition, rather than presuming we may interchange the symbols
for differentiation and integration.
The same proof works with a fixed finite complex measure in place of
$dt$, with its total variation replacing $b-a$. $\square$

This explains, rather than assumes, differentiation of a Cauchy kernel.
The parameter point must stay a positive distance from the contour;
otherwise the required joint bounds can fail.

<a id="ca-16"></a>
### Theorem CA.16. Uniform convergence of derivatives is the missing hypothesis

Here $C^1[a,b]$ means continuously differentiable on the interval, with
one-sided derivatives at endpoints. The value at one point matters:
derivatives determine a function only up to an additive constant.

Let $f_n\in C^1[a,b]$, let $f_n(a)$ converge, and let $f_n'$ converge
uniformly to $g$. Then $f_n$ converge uniformly to a $C^1$ function $f$
with $f'=g$.

**Proof.** By CA.14,
$f_n(t)=f_n(a)+\int_a^t f_n'(s)\,ds$. Define
$f(t)=\lim_n f_n(a)+\int_a^t g(s)\,ds$.
The error is bounded uniformly by
$|f_n(a)-f(a)|+(b-a)\sup|f_n'-g|$. The limit $g$ is continuous by
CA.11, so CA.14 gives $f'=g$. $\square$

Uniform convergence of $f_n$ alone is insufficient. On the real interval
$[-1,1]$, take $f_n(x)=\sin(nx)/n$. The bound $|f_n(x)|\leq1/n$
gives uniform convergence to the zero function, whose derivative is zero.
But $f_n'(x)=\cos(nx)$, so $f_n'(0)=1$ for every $n$.
The derivatives therefore do not converge to the derivative of the limit.
The holomorphic locally uniform limit theorem CA.35 is stronger:
convergence on a two-dimensional complex neighborhood controls
derivatives through Cauchy's formula.

## Curves, coverings, and measure-theoretic applications

<a id="ca-17"></a>
### Lemma CA.17. Finite subdivisions subordinate to a cover

The **trace** is the set of points visited, $\gamma([0,1])$.
A **subarc** is the restriction to a smaller parameter interval.
“Subordinate to a cover” means each entire subarc, not just its
endpoints, fits in one cover member.

If $\gamma:[0,1]\to G$ is continuous and its trace is covered by
open sets $U_\alpha$, some finite partition of $[0,1]$ has each
subarc contained in a single $U_\alpha$. For a continuous map from
$[0,1]^2$, the analogous statement holds for a sufficiently fine square
grid: the image of each small closed square lies in one cover member.

**Proof.** The inverse images form an open cover of the compact parameter
interval or square. The Lebesgue-number argument in CA.4 gives $\delta>0$
such that every subset of sufficiently small diameter lies in one member:
put it in a small relative ball around one of its points. Choose partition
intervals or grid squares with diameter below that bound. $\square$

This justifies the finite logarithm patches in CA.37, the polygonal
replacement in CA.38, and the deformation grid in CA.45. Compactness
alone supplies a finite cover; the Lebesgue number makes a **subdivision**
fit that cover, which is a separate step.

<a id="ca-18"></a>
### Definition and Lemma CA.18. Path parameters, orientation, and bounded variation

This item introduces the geometric conventions; CA.27 gives the full
construction of contour integrals. For a piecewise continuously
differentiable path the definition used here is
$\int_\gamma f(z)\,dz=\int_a^b f(\gamma(t))\gamma'(t)\,dt$.

The trace of $\gamma$ is its image, whereas the path includes its
parametrization and direction. The circle $e^{it}$, $0\leq t\leq2\pi$,
and the same trace traversed twice are different paths. For a continuous
path, its variation is the supremum of the sums of absolute increments
over finite partitions. Finite variation means rectifiability.

An increasing piecewise $C^1$ change of parameter that traverses the
whole parameter interval leaves the contour integral unchanged; reversing
direction changes its sign. Traversing a closed path $m$ times multiplies
its integral by $m$.

**Proof.** In the piecewise smooth case substitute
$\gamma(\theta(s))$ in the definition:
its derivative is $\gamma'(\theta(s))\theta'(s)$ by CA.13, and
ordinary real substitution gives the same integral for an increasing
parameter change. A decreasing change reverses the integration endpoints.
Concatenation splits the integral into a sum, proving the repetition
assertion. For continuous bounded-variation paths the corresponding
rules follow directly by transforming partitions and their tagged
Riemann–Stieltjes sums. $\square$

For example, on $\gamma(t)=a+re^{it}$,
$dz=ire^{it}\,dt$, **not** $dt$. Thus
$\int_\gamma(z-a)^{-1}\,dz=\int_0^{2\pi}i\,dt=2\pi i$.
This elementary calculation is the normalization of every Cauchy and
residue formula in the supplement.

<a id="ca-19"></a>
### Lemma CA.19. Finite-measure estimates for uniform kernels

**Terminology.** A positive **measure** assigns nonnegative sizes to
measurable sets and is countably additive on disjoint sets. The collection
of measurable sets is a **sigma-algebra**, closed under complements and
countable unions. The Borel sigma-algebra is generated by open sets.
A measure is finite if the whole space has finite measure.
A **complex measure** assigns complex values instead. Its **total
variation** is the positive measure defined by

$$
|\mu|(A)=\sup\left\{\sum_{j=1}^N|\mu(A_j)|:
A=\bigcup_{j=1}^N A_j,\quad A_j\text{ measurable and disjoint}\right\}.
$$

For a finite complex measure we use $|\mu|(E)<\infty$.
The notation $L^1(\mu)$ means measurable functions with finite
$\int|g|\,d\mu$, identified when they agree outside a set of measure
zero. **Almost everywhere** means outside such a set.
A **simple function** is a finite sum $\sum_jc_j1_{A_j}$ of constants
times indicators of measurable sets; its integral is $\sum_jc_j\mu(A_j)$.
A **kernel** $k(z,t)$ is just an integrand depending on an external
parameter $z$ as well as the integration variable $t$.

Let $\mu$ be a finite complex measure and let measurable kernels
$k_n(z,t)$ converge uniformly to $k(z,t)$ on $K\times E$. Then

$$
\sup_{z\in K}\left|\int_E[k_n(z,t)-k(z,t)]\,d\mu(t)\right|
\leq |\mu|(E)\sup_{K\times E}|k_n-k|\longrightarrow0.
$$

For positive $\mu$, a domination $|h_n|\leq g\in L^1(\mu)$ and
almost-everywhere convergence imply $\int|h_n-h|\to0$. In particular,
pointwise convergence with one bound $|h_n(t)|\leq M$ for all $n,t$
suffices on a finite-measure space for
**sequences**, but not for arbitrary nets.

**Proof.** For simple functions the integral inequality
$|\int u\,d\mu|\leq\int|u|\,d|\mu|$ follows by applying the
triangle inequality to the finite sum defining the integral; approximation
in $L^1(|\mu|)$ gives the general inequality. Apply it to the kernel
difference and take the supremum over $z$.
For the domination assertion, $|h|\leq g$ almost everywhere, hence
$|h_n-h|\leq2g$. The nonnegative functions
$v_n=2g-|h_n-h|$ tend almost everywhere to $2g$.
Fatou's inequality $\int\liminf v_n\leq\liminf\int v_n$ gives
$2\int g\leq2\int g-\limsup\int|h_n-h|$. Since $\int g$ is
finite, subtraction is valid. The nonnegative integrals
$\int|h_n-h|$ therefore tend to zero.
The proofs of Fatou and monotone convergence, starting from the
nonnegative simple-function definition of integration, are supplied in
[BG-I.6](chapter-01.md#bg-i-6), so that this step has an explicit
dependency rather than an unexplained theorem name. $\square$

For double integrals, read [BG-II.4–5](chapter-02.md#bg-ii-4): Tonelli
requires nonnegativity (with the stated sigma-finiteness hypotheses), and
Fubini for a complex integrand requires absolute integrability. A bounded
kernel on a finite-length contour times a finite measure satisfies that
test. This is precisely the contour–measure interchange in Runge's proof.
For total variation and measure densities, see
[BG-III.10–11](chapter-03.md#bg-iii-10) and
[BG-C.1–2](appendix-c.md#bg-c-1).

Here **sigma-finite** means the space is a countable union of measurable
sets of finite measure. Finite measures and ordinary area measure have
this property.

A **net** is a family indexed by a directed set, where any two indices
have a common later index. This distinction matters in later chapters,
not in the elementary contour proofs. For an example, index by finite
subsets $F$ of $[0,1]$, ordered by inclusion. The functions $1_F$
tend pointwise to 1, since eventually every fixed point belongs to $F$,
but their Lebesgue integrals are all zero. Thus a common bound and
pointwise convergence do not imply dominated convergence for arbitrary nets.

<a id="ca-20"></a>
### Lemma CA.20. Area integration in polar coordinates

Let $dA$ denote ordinary planar area measure. For a continuous function
$v$ on a closed disk,

$$
\int_{D(a,r)}v(z)\,dA(z)
=\int_0^r\int_0^{2\pi}v(a+\rho e^{it})\,\rho\,dt\,d\rho.
$$

The factor $\rho$ is essential. The same identity holds for nonnegative
measurable functions and, by taking real and imaginary parts, for absolutely
integrable functions.

The variables $\rho,t$ are radius and angle. At radius $\rho$, an
angular change $dt$ gives arc length approximately $\rho\,dt$.
Multiplying by radial thickness $d\rho$ explains the area weight
$\rho$. For $v=1$, the formula gives
$\int_0^r2\pi\rho\,d\rho=\pi r^2$, the area of the disk.

**Proof for the continuous case used in CA.48.** Divide the disk into
annular sectors. A sector with radii $\rho_0,\rho_1$ and angular width
$\Delta t$ has area
$\frac12(\rho_1^2-\rho_0^2)\Delta t
=\bar\rho(\rho_1-\rho_0)\Delta t$, where
$\bar\rho=(\rho_1+\rho_0)/2$. Uniform continuity bounds the error
between the sector integral and any tagged value times its area by its
oscillation times its area. Summing and refining makes the total error
tend to zero. These weighted sums are precisely the iterated-integral
Riemann sums on the right. The point at the center and the cut ray have
area zero. For the measurable extension, equality of the two measures
first holds on annular sectors, then on their generated Borel sigma-algebra
by the monotone-class argument, and finally for nonnegative functions by
simple approximation and monotone convergence. $\square$

One common improper-integral application is
$\int_{D(a,r)}|z-a|^{-1}\,dA=2\pi r$: the area factor cancels the
inverse radius. A singular kernel can therefore be integrable in area
even though it is unbounded. This explains the estimate just before
Conway's III.8.2.

## Dependency map and study checkpoints

| Before reading | Prerequisites here | What to be able to explain |
| --- | --- | --- |
| CA.21–CA.25 | CA.1–CA.3, CA.9–CA.12, CA.14–CA.16 | Why one bound works for every point, why geometric tails control a power series, and why derivatives need an additional limit argument. |
| CA.26–CA.30 | CA.4–CA.7, CA.12–CA.18 | Why the nested triangles meet, why finitely many local patches suffice, and why contour integrals have orientation. |
| CA.31–CA.36 | CA.4–CA.7, CA.10 | Why a local identity propagates only within a component, and why compactness gives boundedness and positive distances. |
| CA.37–CA.41 and CA.45–CA.46 | CA.7–CA.8, CA.17–CA.18 | The difference between a path and its trace, between a connected region and one without holes, and between local and global logarithms. |
| CA.42–CA.44 and the Conway applications | CA.9, CA.14–CA.15, CA.19 | Which limits are norm limits, which functional or integral is continuous, and which bound licenses an interchange. |

Try these checks before moving on; each answer records the key reason.

1. Why does $K\subset G$ with $K$ compact and $G$ open give room to
   enlarge $K$? The distance to the closed complement attains a positive
   minimum (CA.6); pointwise choices of radii alone would not give one radius.
2. Why is convergence on every smaller closed disk not convergence on the
   entire open disk? The required index may depend on the smaller radius.
   For $z^n$ on $D(0,1)$ the supremum remains 1 for every $n$.
3. Does the Cauchy–Riemann system at one point, without any regularity
   hypothesis, prove differentiability? No. It controls coordinate partials,
   not the total little-o remainder; see the counterexample after CA.24.
4. Why can $\int dz/z$ around a circle be nonzero if $1/z$ is
   holomorphic near the circle? Holomorphicity near the trace is not
   holomorphicity across its hole. The circle has nonzero index about zero,
   which lies outside the domain of $1/z$.
5. Why cannot one write an operator-valued Cauchy formula merely by replacing
   absolute values by norms? One must also construct the Banach-valued
   integral, prove commutation with functionals, and show those functionals
   separate points; CA.42 supplies all three steps.

## How the complex-analysis proofs fit together

| Stage | Results | Main new idea |
| --- | --- | --- |
| Differentiation and series | CA.21–CA.26 | A complex derivative has one linear approximation valid in every direction; series require uniform estimates on smaller disks. |
| From local derivatives to contour identities | CA.27–CA.29 | Goursat's subdivision cancels internal edges and converts a local derivative estimate into a zero integral. |
| From contour identities to rigidity | CA.30–CA.35 | The geometric expansion of the Cauchy kernel produces Taylor coefficients and bounds for every derivative. |
| Holes and singularities | CA.36–CA.41 | Winding numbers record where Cauchy's theorem is applicable; Laurent coefficients isolate the singular part. |
| Functional analysis | CA.42–CA.44, CA.48, CA.52 | Norm estimates, scalarization, and kernel bounds justify the book's analytic-function and spectral arguments. |
| Further explanations and consequences | CA.45–CA.51 | Deformation, branches, Morera, harmonic averages, zero counting, and disk estimates clarify what the core theory means. |

Do not begin by memorizing contour formulas. At each limit passage identify
the fixed compact set, the uniform or integrable bound, and the result that
permits the passage. Each first-pass proof below can be read without using
the later second-pass results, so the reading route is not circular.

## Convergence and complex differentiation

<a id="ca-21"></a>
### Definition CA.21. Pointwise, uniform, and locally uniform convergence

For functions $f_n:E\to\mathbb C$, pointwise convergence to $f$ means
$\forall z\in E\ \forall\varepsilon>0\ \exists N(z,\varepsilon)$ such that
$n\geq N$ implies $|f_n(z)-f(z)|<\varepsilon$. Uniform convergence means that
one $N(\varepsilon)$ works for **every** $z\in E$. Equivalently,
$\sup_E|f_n-f|\to0$. On an open set $G$, locally uniform convergence means
uniform convergence on every compact subset of $G$.

For example, $x^n\to0$ for $0\leq x<1$, but the convergence is not uniform
on $[0,1)$, since the supremum is always 1. It is uniform on $[0,r]$ for
each $r<1$. A complex power series behaves in exactly this smaller-radius way.

For example, on $|z|\leq1/2$ we have $|z^n|\leq2^{-n}$:
one geometric bound controls every point. On $|z|\leq r<1$ the bound
is instead $r^n$, and reaching the same accuracy takes longer as $r$
approaches 1.
“Locally uniform” allows dependence on the fixed compact set; it does
not allow dependence on the individual point within that set.
Every nonempty compact subset of $D(0,1)$ is contained in some $|z|\leq r<1$:
the continuous function $|z|$ attains its maximum there (CA.5), and
that maximum is strictly below 1.

<a id="ca-22"></a>
### Lemma CA.22. Uniform-limit rules and the Weierstrass M-test

The **M-test** is a reusable way to prove uniform convergence without
knowing the sum first: bound the $n$th function everywhere by a number
$M_n$, then check that the numerical series of bounds converges.

Uniform limits of continuous functions are continuous. If
$|g_n(z)|\leq M_n$ on $E$ and $\sum_n M_n<\infty$, then $\sum_n g_n$
converges uniformly and absolutely on $E$. If $\mu$ is a finite positive
measure and $f_n\to f$ uniformly with all functions measurable, then
$\int |f_n-f|\,d\mu\to0$. For a finite complex measure replace $\mu$ by
its total variation $|\mu|$ in the estimate.

**Proof.** Fix $z_0$ and $\varepsilon>0$. Choose $n$ with
$\sup_E|f_n-f|<\varepsilon/3$, then use continuity of this one $f_n$ at
$z_0$ and the triangle inequality to obtain continuity of $f$. For the
series, the supremum of any tail is at most the corresponding tail of
$\sum M_n$. Thus the partial sums are uniformly Cauchy, and completeness
of $\mathbb C$ supplies their pointwise limits with the same uniform tail
bound. Finally,
$\int |f_n-f|\,d\mu\leq\mu(E)\sup_E|f_n-f|$.
The complex-measure estimate is
$|\int h\,d\mu|\leq\int|h|\,d|\mu|$. This last inequality follows first
for simple functions by the definition of total variation and then by
the defining integral approximation. $\square$

**Why completeness enters.** The tail bound first proves only that the
partial sums are Cauchy. [CA.2](background-complex-analysis.md#ca-2)
supplies their scalar limit, and [CA.11](background-complex-analysis.md#ca-11)
shows that a bound independent of the point survives passage to that limit.
On an infinite-measure space the constant domination used in the integral
estimate may not be integrable; finite measure is a real hypothesis.

<a id="ca-23"></a>
### Definition CA.23. Holomorphic functions and complex derivatives

A function $f:G\to\mathbb C$, $G$ open, is **holomorphic** if at every
$z\in G$ the limit

$$
f'(z)=\lim_{h\to0,\ h\in\mathbb C\setminus\{0\}}
\frac{f(z+h)-f(z)}h
$$

exists. An **entire** function is holomorphic on all of $\mathbb C$.
The limit must be the same in all complex directions. A function is
**analytic** if it locally has a convergent power-series representation.
CA.25 and CA.30 prove these two conditions equivalent. In VII.§3 Conway
uses existence of a continuous complex derivative; this is also equivalent,
because CA.30 proves continuity of the derivatives of a holomorphic function.

The open-set hypothesis ensures $z+h$ is in the domain for all sufficiently
small complex $h$. Existence of the derivative is equivalently

$$
f(z+h)=f(z)+f'(z)h+r(h),\qquad |r(h)|/|h|\longrightarrow0.
$$

Thus the first-order approximation must be multiplication by *one complex
number* in every direction. In particular, differentiability implies
continuity: $f(z+h)-f(z)\to0$ in this expansion.
For $f(z)=z^2$, the quotient is $2z+h$, which tends to $2z$ along
every route to zero. This proves the derivative, not just its value
along a few lines.

<a id="ca-24"></a>
### Proposition CA.24. Real derivatives and the Cauchy–Riemann equations

Write $f(x+iy)=u(x,y)+iv(x,y)$. Complex differentiability implies
$u_x=v_y$ and $u_y=-v_x$. Conversely, real differentiability at $(x,y)$
together with those equations implies complex differentiability there.
In particular, continuous first partial derivatives satisfying these
equations throughout $G$ suffice for holomorphicity.

**Proof.** Along real increments $h=t$, the quotient tends to
$u_x+iv_x$. Along imaginary increments $h=it$, division by $i$ gives
the limit $(u_y+iv_y)/i=v_y-iu_y$. A complex derivative must give the
same number in both cases. Equating real and imaginary parts yields
$u_x=v_y$ and $v_x=-u_y$.

For the converse, total real differentiability (CA.12) gives

$$
f(z+h)-f(z)=A\,\operatorname{Re}h+B\,\operatorname{Im}h+r(h),
\quad A=u_x+iv_x,\quad B=u_y+iv_y,\quad |r(h)|/|h|\to0.
$$

The equations imply $B=-v_x+iu_x=iA$. Therefore the linear part is
$A(\operatorname{Re}h+i\operatorname{Im}h)=Ah$. After division by
$h\ne0$, the remaining error has modulus $|r(h)|/|h|\to0$, so
$f'(z)=A$. Continuous first partials ensure the required total
differentiability by CA.12.

The product rule can be checked by writing
$f(z+h)g(z+h)-f(z)g(z)$ as
$f(z+h)[g(z+h)-g(z)]+g(z)[f(z+h)-f(z)]$ and dividing by $h$.
Continuity then gives $(fg)'=fg'+gf'$. Similarly, subtraction of
reciprocals gives $(1/g)'=-g'/g^2$ where $g\ne0$, hence the quotient
rule. Polynomials and quotients of polynomials with nonzero denominator
are therefore holomorphic. For contrast, $f(z)=\overline z$ gives
$\overline h/h=1$ for real $h$ and $-1$ for imaginary $h$, so its
complex derivative does not exist. $\square$

**A counterexample to using partial derivatives alone.** Set
$u(x,y)=xy/\sqrt{x^2+y^2}$ away from $(0,0)$, set $u(0,0)=0$,
and let $f=u+i0$. Both coordinate partials of $u$ at the origin are zero,
as are those of its imaginary part, so the Cauchy–Riemann equations hold
there. The function is even continuous there, since
$|u(x,y)|\leq\sqrt{x^2+y^2}/2$.
Along $z=t(1+i)$ with $t>0$, however,
$f(z)/z=1/(\sqrt2(1+i))$, whereas along the real axis it is zero.
The complex derivative does not exist. The missing hypothesis is **total
real differentiability**, explained in
[CA.12](background-complex-analysis.md#ca-12), not just the existence
of coordinate partials.

Conversely, $f(z)=|z|^2$ is complex differentiable at zero, with derivative
zero, because $|f(h)/h|=|h|\to0$. It is not holomorphic on any disk:
at other points its Cauchy–Riemann equations fail. Differentiability at
one point and holomorphicity on an open set are different assertions.

<a id="ca-25"></a>
### Theorem CA.25. Power series, radius of convergence, and differentiation

For $\sum_{n=0}^\infty a_n(z-c)^n$, put
$L=\limsup_n|a_n|^{1/n}$ and $R=1/L$, with $1/0=\infty$ and
$1/\infty=0$. The series converges absolutely and uniformly on every
$|z-c|\leq r<R$, diverges for $|z-c|>R$, and defines a holomorphic
function for $|z-c|<R$. Its derivatives are obtained term by term there.
No conclusion about convergence on $|z-c|=R$ follows in general.

A **power series** is a series in nonnegative integer powers of the
complex displacement $z-c$ from a fixed center $c$, with fixed
coefficients $a_n$. The displacement is a complex number; its modulus
$|z-c|$ is the distance that controls convergence.
Its **radius of convergence** $R$ is the threshold between convergence
inside the disk and divergence outside. When $R=0$ only the center is
guaranteed; when $R=\infty$ every finite disk is allowed.

**Proof, first convergence.** Choose $0<r<s<R$. The spare radius $s$
is useful because it gives a geometric ratio $r/s<1$. Since
$L<1/s$, the definition of limsup gives eventually
$|a_n|\leq s^{-n}$, hence $|a_n(z-c)^n|\leq(r/s)^n$ on the smaller
disk. CA.22 proves uniform absolute convergence; finitely many initial
terms do not affect convergence. If $d=|z-c|>R$, choose
$1/d<t<L$ (also possible when $L=\infty$). Infinitely often
$|a_n|^{1/n}>t$, so $|a_n(z-c)^n|>(td)^n$ on those indices.
Since $td>1$, terms do not tend to zero and the series diverges.

**Next, justify differentiation.** On $|z-c|\leq r$, the derivative
terms are eventually bounded by $n r^{n-1}s^{-n}$. Their series is
summable: the ratio of successive bounds tends to $r/s<1$, so from
some index onward the bounds decrease at least geometrically.
Thus the derivative series also converges uniformly on smaller disks.

Let $P_N$ be the partial sums and $g$ the
uniform limit of $P_N'$ on a closed disk strictly inside the convergence
disk. On a short segment from $z$ to $z+h$ in that disk,
$P_N(z+h)-P_N(z)=h\int_0^1P_N'(z+th)\,dt$. First hold $h$ fixed
and let $N\to\infty$: the integral error is at most
$|h|\sup|P_N'-g|$, which tends to zero. We get
$f(z+h)-f(z)=h\int_0^1g(z+th)\,dt$.
Now divide by $h$ and subtract $g(z)$. The error is at most
$\sup_{0\leq t\leq1}|g(z+th)-g(z)|$, which tends to zero by
continuity of $g$ (CA.11). Hence $f'=g$. Repeating the argument
with the higher derivative series proves termwise differentiation of
every fixed order. $\square$

**Why the differentiated series has the same interior convergence.** Its
$n$th majorant is $n r^{n-1}s^{-n}$. A polynomial factor in $n$ cannot
defeat geometric decay: for $r/s<q<1$, eventually
$n(r/s)^{n-1}\leq Cq^n$, as is seen by the ratio of consecutive terms.
The same argument handles the factors $n(n-1)\cdots(n-k+1)$ for any
fixed derivative order. This proves uniform convergence of the derivative
series; it is not inferred merely from convergence of the original series.

**Example.** The geometric series has radius 1. At any point with
$|z|<1$ it may be differentiated to give
$\sum_{n\geq1}nz^{n-1}=(1-z)^{-2}$, but substituting $z=1$ is
invalid. The **factorial** notation is $n!=1\cdot2\cdots n$ for
$n\geq1$, with $0!=1$. The series $\sum z^n/n!$ has infinite radius, since the ratio
of consecutive absolute terms is $|z|/(n+1)$ and is eventually at most
$1/2$ on each fixed bounded disk.

<a id="ca-26"></a>
### Definition and Lemma CA.26. Exponentials and local logarithms

Define $e^z=\sum_{n\geq0}z^n/n!$. Then $(e^z)'=e^z$,
$e^{z+w}=e^ze^w$, and $e^z\ne0$. For real $t$, the real and imaginary
parts give $e^{it}=\cos t+i\sin t$. A **branch of the logarithm** on
an open set $U\subset\mathbb C\setminus\{0\}$ is a holomorphic $L$
with $e^{L(z)}=z$ there; then $L'(z)=1/z$.

For $a=r(\cos\theta+i\sin\theta)\ne0$, all scalar logarithms are
$\log r+i(\theta+2\pi k)$, $k\in\mathbb Z$, where $\log r$ is the
ordinary real logarithm. A **branch** makes one choice at every point
of an open set in a way that is holomorphic. Arbitrary independent
choices of angles need not even give a continuous function.

The real logarithm $\log r$ is the inverse of the real exponential:
$e^{\log r}=r$ for $r>0$. Its existence also follows from the properties
proved below. For real $x$, the series is real and
$e^x=(e^{x/2})^2>0$. Its derivative is positive, so it is strictly
increasing. For $x\geq0$, $e^x\geq1+x$, and $e^{-x}=1/e^x$.
Thus its limits at the two ends of the real axis are $\infty$ and 0.
Continuity gives every positive value exactly once.

**Proof.** CA.25 gives differentiation. Absolute convergence permits
grouping the double series for $e^ze^w$ by total degree; the binomial
formula gives $e^{z+w}$. Taking $w=-z$ gives nonvanishing. Separating the
even and odd terms gives the real cosine and sine series and hence
Euler's formula. To recall why those real series equal the trigonometric
functions: their derivatives cycle through $\sin,\cos,-\sin,-\cos$,
bounded by 1 on the real axis. The real Taylor remainder is at most
$|t|^{N+1}/(N+1)!$ and tends to zero for fixed $t$.

This real remainder estimate follows by repeatedly using the fundamental
theorem of calculus. For a real $C^{N+1}$ function $u$,

$$
u(t)-\sum_{j=0}^{N}\frac{u^{(j)}(0)}{j!}t^j
=\frac1{N!}\int_0^t(t-s)^N u^{(N+1)}(s)\,ds.
$$

For $N=0$ this is CA.14. Integration by parts, obtained by integrating
the product rule, gives the next case successively. If
$|u^{(N+1)}|\leq1$ between 0 and $t$, the integral has modulus at
most $|t|^{N+1}/(N+1)!$. This proves the sine and cosine series
without assuming the complex Taylor theorem that comes later.

For any $a\ne0$, choose one
number $\ell$ with $e^\ell=a$. On $|z-a|<|a|$ define

$$
L(z)=\ell+\sum_{n=1}^\infty\frac{(-1)^{n+1}}n
\left(\frac{z-a}{a}\right)^n.
$$

Termwise differentiation gives
$L'(z)=a^{-1}\sum_{k\geq0}(-1)^k((z-a)/a)^k=1/z$.
The product and chain rules give
$(e^{L(z)}/z)'=e^{L(z)}(zL'(z)-1)/z^2=0$.
A function with zero complex derivative is constant on this disk:
restrict to any straight segment and apply CA.13 and the real
zero-derivative result in CA.14 to both coordinates.
Its value at $a$ is 1. Thus
logarithms exist locally. A single branch does not exist on the entire
punctured plane: along $z=e^{it}$ the chain rule would give
$\frac{d}{dt}L(e^{it})=i$, contradicting equality of the values at
$t=0$ and $t=2\pi$. This is why contours and holes matter. $\square$

## Contours and Cauchy theory

<a id="ca-27"></a>
### Definition and Lemma CA.27. Contour integrals and their norm estimate

A piecewise $C^1$ path is a continuous $\gamma:[a,b]\to\mathbb C$
which is continuously differentiable on each of finitely many subintervals.
Its length is $\ell(\gamma)=\int_a^b|\gamma'(t)|\,dt$, and

$$
\int_\gamma f(z)\,dz=\int_a^b f(\gamma(t))\gamma'(t)\,dt.
$$

Reversing orientation negates the integral; concatenating paths adds their
integrals. A path is closed if its endpoints agree. For continuous $f$,

$$
\left|\int_\gamma f\right|\leq
\ell(\gamma)\sup_{\gamma([a,b])}|f|.
$$

In this notation $dz=\gamma'(t)\,dt$ records the direction and speed
of travel. It is not the same as the positive arc-length element
$|dz|=|\gamma'(t)|\,dt$. For the line segment from $u$ to $v$,
$\gamma(t)=u+t(v-u)$, $0\leq t\leq1$, so

$$
\int_{[u,v]}f(z)\,dz=(v-u)\int_0^1f(u+t(v-u))\,dt.
$$

A **primitive** (or antiderivative) of $f$ on an open set is a
holomorphic function $F$ with $F'=f$. This term concerns a function
defined on an open set, not just a formal integration symbol.

In particular, uniform convergence on a fixed contour permits passing a
limit or a uniformly convergent series through its integral.

**Proof.** The triangle inequality for the real-variable integral gives

$$
\left|\int_a^b f(\gamma(t))\gamma'(t)\,dt\right|
\leq\int_a^b |f(\gamma(t))|\,|\gamma'(t)|\,dt
\leq\sup_\gamma|f|\int_a^b|\gamma'(t)|\,dt.
$$

The orientation and concatenation rules follow
by change of parameter and additivity. Apply the inequality to $f_n-f$
to obtain
$|\int_\gamma f_n-\int_\gamma f|\leq\ell(\gamma)\sup_\gamma|f_n-f|\to0$.
If $F'=f$ along a neighborhood of the path,
the chain rule and the fundamental theorem of calculus give
$\int_\gamma f=F(\gamma(b))-F(\gamma(a))$. $\square$

Conway also uses **rectifiable** paths: continuous paths with finite total
variation, meaning the supremum of $\sum_j|\gamma(t_j)-\gamma(t_{j-1})|$
over partitions is finite. For these paths the integral is the
Riemann–Stieltjes integral $\int f(\gamma(t))\,d\gamma(t)$. It exists for
continuous $f$ on the trace: the difference between two sufficiently fine
tagged sums is at most the total variation times the oscillation of
$f\circ\gamma$ on small subintervals. Uniform continuity makes this
oscillation tend to zero. Completeness then gives the limit, and the same
length estimate holds. This construction works in a Banach space too.

The primitive rule also holds for these paths. To check it without assuming
that a rectifiable parametrization is differentiable, take a fine partition
whose subarcs lie in small convex disks inside the domain of the primitive
$F$. The real fundamental theorem along the straight segment between each
pair of endpoints gives
$F(v)-F(u)=\int_0^1F'(u+t(v-u))(v-u)\,dt$.
Subtract $F'(\gamma(\tau_j))(v-u)$ on each subinterval. Uniform
continuity of $F'$ near the compact trace bounds the sum of these errors
by $\omega(\delta)\ell(\gamma)$, where the subarc diameters are at most
$\delta$ and $\omega(\delta)\to0$. The primitive increments telescope,
so taking the limit proves the same endpoint formula for rectifiable paths.

<a id="ca-28"></a>
### Theorem CA.28. Goursat's triangle theorem and local primitives

If $f$ is holomorphic on an open neighborhood of a closed triangle $T$,
then $\int_{\partial T}f=0$, where the boundary is traversed
counterclockwise. Consequently, on a convex open set every holomorphic
function has a primitive.

**Idea of the proof.** An unknown boundary integral can be concentrated
on smaller and smaller triangles. Near their common point, differentiability
approximates $f$ by an affine function, whose closed integral is zero.
The approximation error is small enough to force the original integral
to be zero as well.

**Step 1: choose nested triangles.** Let $T_0=T$ have diameter $d$,
perimeter $p$, and boundary integral $I_0$. Join its edge midpoints,
making four triangles, each with half the diameter and perimeter.
Orient every small boundary counterclockwise. Each internal edge is
traversed twice in opposite directions, so the four integrals sum to
$I_0$. By the triangle inequality at least one has modulus at least
$|I_0|/4$; otherwise their sum could not have modulus $|I_0|$.
Choose that triangle as $T_1$ and repeat. After $n$ steps,

$$
T_0\supseteq T_1\supseteq\cdots\supseteq T_n,\quad
\operatorname{diam}T_n=d\,2^{-n},\quad
\ell(\partial T_n)=p\,2^{-n},\quad |I_0|\leq4^n|I_n|.
$$

CA.4 supplies a unique point $c$ belonging to all the closed triangles.

**Step 2: use differentiability at that one point.** Write
$f(z)=f(c)+f'(c)(z-c)+(z-c)\varepsilon(z)$, where
$\varepsilon(z)\to0$ as $z\to c$ and we set $\varepsilon(c)=0$.
The first two terms have explicit primitives
$f(c)z$ and $f'(c)(z-c)^2/2$, so their integrals around any triangle
vanish by CA.27. Only the remainder contributes to $I_n$. Thus

$$
\begin{aligned}
|I_n|
&\leq \ell(\partial T_n)
       \sup_{z\in T_n}|z-c|\,|\varepsilon(z)|\\
&\leq (p\,2^{-n})(d\,2^{-n})\sup_{T_n}|\varepsilon|,\\
|I_0|&\leq4^n|I_n|\leq dp\sup_{T_n}|\varepsilon|\longrightarrow0.
\end{aligned}
$$

The supremum tends to zero because every point of $T_n$ is within
$d\,2^{-n}$ of $c$. The fixed number $|I_0|$ must therefore be zero.
Notice the exact cancellation of $4^n$ with the two factors $2^{-n}$.
Continuity of $f'$ was never assumed.

**Step 3: construct a primitive.** In a convex open set choose a base
point $a$ and put $F(z)=\int_{[a,z]}f$. Convexity keeps the triangle
with vertices $a,z,z+h$ in the set. Its zero boundary integral gives

$$
F(z+h)-F(z)=\int_{[z,z+h]}f
=h\int_0^1f(z+th)\,dt.
$$

After dividing by $h$ and subtracting $f(z)$, the error is at most
$\sup_{0\leq t\leq1}|f(z+th)-f(z)|\to0$ by continuity. Thus
$F'=f$. This last step only required continuity and zero triangle
integrals. It will apply to continuous functions whose holomorphicity
has not yet been established. $\square$

<a id="ca-29"></a>
### Theorem CA.29. Cauchy's formula on a disk

Suppose $f$ is holomorphic on a neighborhood of the closed disk
$\overline{D(c,r)}$. If $z\in D(c,r)$, then

$$
f(z)=\frac1{2\pi i}\int_{|w-c|=r}\frac{f(w)}{w-z}\,dw.
$$

The circle is oriented counterclockwise.

**Idea.** Subtract the value $f(z)$ from the numerator. The resulting
quotient no longer blows up at $w=z$, and its closed integral is zero.
What remains is $f(z)$ times the explicitly computable integral of
$1/(w-z)$.

**Step 1: remove the blow-up without assuming Taylor's theorem.**
Fix the evaluation point $z$ inside the circle and set
$g(w)=(f(w)-f(z))/(w-z)$ for $w\ne z$, with $g(z)=f'(z)$.
The definition of the derivative says exactly that $g$ is continuous
at $z$. It is holomorphic elsewhere by the quotient rule. Choose a
slightly larger open disk around $c$ on which $f$ is holomorphic;
this is possible by CA.6 applied to the original closed disk.

**Step 2: prove that every triangle integral of $g$ is zero.**
For a triangle missing $z$, use CA.28. If a triangle contains $z$,
join $z$ to its vertices, splitting it into triangles with $z$ as a
vertex; if $z$ lies on an edge, two triangles suffice. Internal edges
cancel. It therefore suffices to handle one triangle with vertex $z$.

On its two sides from $z$, mark points a fraction $\tau$ of the way
to the other vertices. Cut off the small triangle they form at $z$.
The remaining quadrilateral stays away from $z$ and splits into two
triangles, whose integrals vanish by CA.28. Hence the original boundary
integral equals the small triangle's boundary integral. Its perimeter
is $\tau$ times the original perimeter, while $g$ is bounded on the
original compact triangle by continuity. CA.27 therefore bounds this
integral by a constant times $\tau$, tending to zero. Summing the
pieces proves the assertion for every triangle, including the edge case.

The continuous-function conclusion of CA.28 now gives a primitive for
$g$ on the larger disk. Thus its integral around $|w-c|=r$ is zero.

**Step 3: compute the remaining integral.** Since $|z-c|/r<1$,

$$
\frac1{w-z}
=\frac1{w-c}\frac1{1-(z-c)/(w-c)}
=\sum_{n=0}^\infty\frac{(z-c)^n}{(w-c)^{n+1}}
$$

uniformly on the circle. Parametrize $w=c+re^{it}$, $0\leq t\leq2\pi$.
Then

$$
\int_{|w-c|=r}\frac{dw}{(w-c)^{n+1}}
=i r^{-n}\int_0^{2\pi}e^{-int}\,dt
=\begin{cases}2\pi i,&n=0,\\0,&n\geq1.\end{cases}
$$

Uniform convergence permits termwise integration (CA.27), so
$\int dw/(w-z)=2\pi i$. Finally
$f(w)/(w-z)=g(w)+f(z)/(w-z)$, and integration gives the formula.
$\square$

**Why this proof is not circular.** We have not yet shown that $g$ is
holomorphic at $z$; using Taylor series to assert this here would presuppose
the theorem being proved. Instead we use only continuity of $g$ and its
zero triangle integrals to construct a primitive by CA.28. Taylor series
and the general removable-singularity theorem come later.

<a id="ca-30"></a>
### Theorem CA.30. Taylor expansion, Cauchy estimates, and derivatives

If $f$ is holomorphic on $D(c,R)$, then throughout that disk

$$
f(z)=\sum_{n=0}^\infty a_n(z-c)^n,
\qquad a_n=\frac{f^{(n)}(c)}{n!}
=\frac1{2\pi i}\int_{|w-c|=r}\frac{f(w)}{(w-c)^{n+1}}\,dw
$$

for any $0<r<R$. The series converges uniformly on smaller closed disks.
If $M_r=\max_{|w-c|=r}|f(w)|$, then
$|f^{(n)}(c)|\leq n!M_r/r^n$.

Here $f^{(n)}$ means the $n$th derivative, and $f^{(0)}=f$.
The assertion includes the existence of derivatives of every order:
the definition of holomorphicity originally assumed only one derivative.

**Proof.** Fix $0<r<R$ and then $s<r$. For all $|z-c|\leq s$ and
$|w-c|=r$, the geometric expansion in CA.29 has ratio of modulus at
most $s/r<1$. Multiply it by $f(w)$ and integrate term by term.
The uniform tail bound makes the exchange valid by CA.27, giving
$f(z)=\sum_{n\geq0}a_n(z-c)^n$ for $|z-c|<r$.

The coefficient estimate follows by retaining each factor in the
contour bound:

$$
|a_n|\leq\frac1{2\pi}(2\pi r)\frac{M_r}{r^{n+1}}
=\frac{M_r}{r^n}.
$$

It also bounds the Taylor terms on $|z-c|\leq s$ by
$M_r(s/r)^n$, proving uniform absolute convergence there.
CA.25 now permits differentiating this actual power series.
At $z=c$, its $n$th derivative is $n!a_n$: lower powers have vanished
under differentiation, and higher powers still contain $z-c$.
This proves that all these derivatives exist; they were not assumptions.
It also shows that the coefficients are independent of the radius $r$.
For any point in $D(c,R)$ choose $r$ between its distance from $c$
and $R$, obtaining the expansion throughout the disk.

Finally, for $|z-c|\leq s<r$, $|w-z|\geq r-s$ on the contour.
The derivatives of the kernel are
$\partial_z^n(w-z)^{-1}=n!(w-z)^{-n-1}$; this positive distance
bounds them uniformly. CA.15 therefore permits differentiation under
the fixed contour integral and yields

$$
f^{(n)}(z)=\frac{n!}{2\pi i}
\int_{|w-c|=r}\frac{f(w)}{(w-z)^{n+1}}\,dw.
$$

Termwise differentiation also proves that all derivatives are continuous
and holomorphic. $\square$

<a id="ca-31"></a>
### Theorem CA.31. The identity theorem and multiplicity of zeros

If a holomorphic function $f$ on a domain $G$ is not identically zero,
each zero $a$ is isolated and has a finite multiplicity: locally
$f(z)=(z-a)^m g(z)$ for an integer $m\geq1$ and a holomorphic $g$
with $g(a)\ne0$. If all derivatives of $f$ vanish at a point, or if its
zeros accumulate at a point **inside** $G$, then $f\equiv0$ on $G$.

A **zero** is a point where $f(a)=0$. It is **isolated** if some disk
about it contains no other zero. Its **multiplicity** (or order) is
the exponent $m$ in the factorization: for example, $(z-2)^3(z+1)$
has a zero of order 3 at 2. Zeros **accumulate at $a$** if there are
distinct zeros tending to $a$. The notation $f\equiv0$ means zero at
every point of the domain.

**Proof.** At a zero $a$, the Taylor series either has a first nonzero
coefficient $a_m$ or has all coefficients zero. In the first case,

$$
f(z)=(z-a)^m\bigl(a_m+a_{m+1}(z-a)+\cdots\bigr)=(z-a)^m g(z).
$$

The series for $g$ is holomorphic and $g(a)=a_m\ne0$. Continuity
gives a disk where $|g(z)-g(a)|<|g(a)|/2$, so
$|g(z)|>|g(a)|/2>0$. There the only zero of $f$ is $a$.

In the second case the Taylor expansion gives $f=0$ on a disk.
To propagate this local conclusion, let
$S=\{z\in G:f^{(n)}(z)=0\text{ for every }n\geq0\}$, where
$f^{(0)}=f$. Each derivative is continuous by CA.30, so limits in
$G$ of points of $S$ remain in $S$; thus $S$ is relatively closed.
At a point of $S$, Taylor's theorem gives an entire small disk on
which $f=0$. All derivatives also vanish there, so the disk lies in
$S$ and $S$ is open. If $S$ is nonempty, connectedness (CA.7)
forces $S=G$.

If distinct zeros approach an interior point $a$, continuity first
gives $f(a)=0$. A first nonzero Taylor coefficient would isolate this
zero, contradicting the approaching zeros. Thus all coefficients vanish,
$a\in S$, and the preceding argument gives $f\equiv0$. $\square$

Applying this to $f-g$ gives the usual identity theorem: two holomorphic
functions agreeing on a set with an accumulation point in the domain
agree everywhere on that domain.

This is the missing logical step in III.§8: annihilating all inverse
powers at one point forces all derivatives of the Cauchy transform to
vanish there, and therefore forces it to vanish on that connected component.

<a id="ca-32"></a>
### Theorem CA.32. Removable singularities

If $f$ is holomorphic on $0<|z-a|<r$ and bounded near $a$, it extends
uniquely to a holomorphic function on $|z-a|<r$.

**Proof.** The difficulty is to find the correct missing value and prove
differentiability there. Suppose $|f(z)|\leq M$ near $a$. Define
$h(z)=(z-a)^2f(z)$ off $a$, and $h(a)=0$. Then
$|h(z)|\leq M|z-a|^2\to0$, so $h$ is continuous at $a$, and

$$
\left|\frac{h(z)-h(a)}{z-a}\right|
=|(z-a)f(z)|\leq M|z-a|\longrightarrow0.
$$

Thus $h'(a)=0$. Away from $a$, the product rule gives holomorphicity,
so $h$ is holomorphic on the whole disk. CA.30 gives
$h(z)=\sum_{n\geq2}b_n(z-a)^n$, because its constant and linear
coefficients are zero. The series
$\widetilde f(z)=\sum_{n\geq2}b_n(z-a)^{n-2}$ is holomorphic and
equals $f(z)$ for $z\ne a$. It supplies the missing value
$\widetilde f(a)=b_2$. Any other continuous extension must take the
same limiting value, proving uniqueness. $\square$

Such a missing point is a **removable singularity**. For example,
$\sin z/z$ extends at zero with value 1, as its power series shows.

<a id="ca-33"></a>
### Theorem CA.33. Liouville's theorem and the fundamental theorem of algebra

A bounded entire function is constant. Here **bounded** means one
finite $M$ satisfies $|f(z)|\leq M$ on the whole plane, not just on
each individual disk. Every nonconstant complex
polynomial has a complex zero and consequently splits into linear factors.

**Proof.** If $|f|\leq M$ on $\mathbb C$, the Cauchy estimate on a
circle of arbitrary radius $r$ centered at any $c$ gives
$|f'(c)|\leq M/r$. Letting $r\to\infty$ gives $f'=0$. Integration
along line segments makes $f$ constant. If a nonconstant polynomial $p$
had no zero, $1/p$ would be entire and would tend to zero at infinity,
because its leading term dominates all lower terms there. To see this
explicitly, for $p(z)=a_dz^d+\cdots+a_0$ with $a_d\ne0$ and $d\geq1$,
factor

$$
p(z)=a_dz^d\left(1+\sum_{j=0}^{d-1}\frac{a_j}{a_d}z^{j-d}\right).
$$

The sum in parentheses after 1 tends to zero as $|z|\to\infty$.
For sufficiently large $|z|$ it has modulus at most $1/2$, giving
$|p(z)|\geq |a_d||z|^d/2$ and hence $1/p(z)\to0$. On a remaining
closed disk it is continuous and bounded. Liouville makes $1/p$ constant,
a contradiction. Divide by a linear factor at a root and repeat to obtain
the factorization. $\square$

<a id="ca-34"></a>
### Theorem CA.34. Maximum modulus principle

A nonconstant holomorphic function on a domain cannot have a local
maximum of its modulus. If it is continuous on the closure of a bounded
domain and holomorphic inside, its maximum modulus is attained on the
boundary.

A **local maximum of modulus at $a$** means that some neighborhood
of $a$ satisfies $|f(z)|\leq|f(a)|$. The theorem asserts that even
such a local maximum forces the function to be constant on its connected
domain. It is a statement about the real quantity $|f|$, not an ordering
of complex values.

**Proof.** Suppose $|f(z)|\leq|f(a)|$ near $a$. If $f(a)=0$, the
function vanishes near $a$ and CA.31 applies. Otherwise multiply by a
constant of modulus 1 to make $f(a)=M>0$. Cauchy's formula at the center
gives $M=(2\pi)^{-1}\int_0^{2\pi}f(a+re^{it})\,dt$ for small $r$.
The continuous function $q(t)=M-\operatorname{Re}f(a+re^{it})$ is
nonnegative, since $\operatorname{Re}f\leq|f|\leq M$, and has integral
zero by the mean identity. If $q(t_0)>0$, continuity would make it at
least $q(t_0)/2$ on a small interval, producing a positive integral.
Thus $q=0$ everywhere. Write the value of $f$ on the circle as $M+iy$.
The bound $|M+iy|^2=M^2+y^2\leq M^2$ forces $y=0$, so $f=M$
on the circle. These zeros of $f-M$ have accumulation points inside
the original domain; CA.31 makes $f$ constant there. Multiplying back
by the inverse of the earlier unit-modulus constant gives the conclusion for the
original function.
For a bounded domain, compactness of its closure gives a maximum; if it
is attained inside, the preceding conclusion makes the function constant,
in which case boundary points also attain it. $\square$

<a id="ca-35"></a>
### Theorem CA.35. Locally uniform limits of holomorphic functions

If $f_n$ are holomorphic on $G$ and converge uniformly on every compact
subset to $f$, then $f$ is holomorphic and $f_n^{(k)}\to f^{(k)}$
locally uniformly for each fixed $k\geq1$.

**Proof.** Around any $a\in G$ choose a closed disk contained in $G$.
Pass to the limit in Cauchy's formula on its boundary using CA.27. The
result represents $f$ by a contour integral whose kernel has a uniformly
convergent geometric expansion on every smaller disk; hence CA.25 makes
$f$ holomorphic. On a smaller disk $|z-a|\leq s<r$, subtract the
derivative formulas to get

$$
|f_n^{(k)}(z)-f^{(k)}(z)|
\leq\frac{k!r}{(r-s)^{k+1}}\sup_{|w-a|=r}|f_n(w)-f(w)|.
$$

A compact subset is covered by finitely many such smaller disks, proving
the assertion. Pointwise convergence alone does not justify this argument.
$\square$

In the displayed derivative estimate, $2\pi r$ is the length of the
fixed outer circle, $k!/(2\pi)$ comes from Cauchy's derivative formula,
and $(r-s)^{-k-1}$ bounds the kernel for every point in the smaller
disk. All dependence on $n$ is in the final supremum, which tends to
zero. For a general compact set, take finitely many of these bounds
and choose an index large enough for every one of them.

<a id="ca-36"></a>
### Definition and Lemma CA.36. Infinity, poles, and rational functions

Adding the point $\infty$ lets us describe the behavior for large $|z|$
as behavior near one additional point. A sequence tends to $\infty$
precisely when its modulus tends to infinity. The substitution
$\zeta=1/z$ turns that question into the familiar limit $\zeta\to0$.

The extended plane is $\mathbb C_\infty=\mathbb C\cup\{\infty\}$;
neighborhoods of $\infty$ contain $\{|z|>R\}\cup\{\infty\}$.
A function is holomorphic at infinity if $\zeta\mapsto f(1/\zeta)$
extends holomorphically to $\zeta=0$. A pole of integer order $m\geq1$ at $a$ means
$f(z)=(z-a)^{-m}g(z)$ locally, with $g$ holomorphic and $g(a)\ne0$.
A rational function is a quotient of polynomials; its finite poles are
the uncancelled zeros of its denominator. A nonconstant polynomial has a
pole at infinity. A rational function whose only possible pole is at
infinity is a polynomial.

For example, $f(z)=z^d$ becomes $\zeta^{-d}$, so it has a pole of
order $d$ at infinity. Conversely, $f(z)=1/z$ becomes $\zeta$ and
has a holomorphic extension with value zero at infinity. “Holomorphic
at infinity” does not mean taking a derivative with respect to the
symbol $\infty$; it means ordinary holomorphicity in this coordinate.

**Proof of the last assertion.** Cancel common polynomial factors and
write $p/q$. If $q$ were nonconstant, CA.33 would give a zero of $q$,
which would be a finite pole. Thus $q$ is constant. To handle infinity
in III.§8, let $K$ be compact, $|z|\leq M$ on $K$, and $\mu$ a finite
complex measure. For $|w|>M$ the geometric series is uniform in $z\in K$,
and CA.22 gives

$$
\int_K\frac{d\mu(z)}{z-w}
=-\sum_{n=0}^\infty w^{-n-1}\int_K z^n\,d\mu(z).
$$

After putting $w=1/\zeta$ this is a power series with zero constant
coefficient, convergent for $|\zeta|<1/M$ (with the evident interpretation
when $M=0$). It proves holomorphicity at infinity and value zero there
directly; it is stronger than just a formal expansion. $\square$

## Winding numbers, general contours, and singularities

<a id="ca-37"></a>
### Definition and Theorem CA.37. Winding numbers

For a closed rectifiable path $\gamma$ and a point $a$ off its trace, set
$n(\gamma;a)=(2\pi i)^{-1}\int_\gamma(z-a)^{-1}\,dz$.
This is an integer, constant on each component of the complement of the
trace, and zero on the unbounded component. For a finite collection of
oriented closed paths, called a **cycle**, add their integrals and indices.

The **winding number**, also called the **index**, counts net turns
around $a$: counterclockwise turns are positive, clockwise turns are
negative. This interpretation is justified by the logarithm calculation
below. It depends on the path with its direction and repetitions, not
just on the curve drawn on the page. At a point on the trace the
integrand has a zero denominator, so this definition does not apply.

**Proof.** On each of finitely many successive small subarcs of the path,
$\gamma(t)-a$ lies in a disk with a local logarithm from CA.26. Choose
these logarithms consecutively, adding multiples of $2\pi i$ so their
values agree at successive endpoints. The integral of $1/(z-a)$ is the
sum of the changes of these logarithms. As the path closes, the total
change has exponential 1; writing $w=x+iy$ shows $e^w=1$ precisely when
$w=2\pi i k$, $k\in\mathbb Z$. Hence the index is an integer.

Here is the patching step in more detail. CA.17 subdivides the parameter
interval so that each subarc admits a local logarithm of $z-a$.
At an endpoint shared by two subarcs, the two logarithm values have the
same exponential, so their difference is $2\pi i k$. Adding that
constant to one branch makes the values agree. The primitive rule
then expresses each subarc integral as its final logarithm value minus
its initial value. Intermediate endpoint values cancel. Only the
difference between the final and initial logarithm values remains, and
their exponentials agree because the path is closed.

The integral depends continuously on $a$ away from the trace, by the
length estimate and positive distance on a sufficiently small neighborhood.
A continuous integer-valued function is locally constant and thus constant
on each connected component. Finally
$|n(\gamma;a)|\leq\ell(\gamma)/(2\pi\operatorname{dist}(a,\{\gamma\}))$
tends to zero as $|a|\to\infty$, so the integer is zero there. $\square$

For the local-constancy step, continuity gives a neighborhood where the
index differs from its value at the center by less than $1/2$. Two
distinct integers cannot be that close, so the value is unchanged.
Connectedness prevents different such constant values on one component.
Far enough from the bounded trace the displayed bound is below 1, so
the integer is zero; constancy then gives zero on the whole unbounded
component.

For the positively oriented circle around $c$, its index is 1 inside and
0 outside: the inside calculation is the geometric-series computation in
CA.29, and the outside calculation expands in powers of $(z-c)/(a-c)$.
For an annular region the outer boundary is counterclockwise and the
inner boundary clockwise; their combined index is 1 in the annulus and
0 in the hole. Orientations cannot be dropped from Cauchy's theorem.

<a id="ca-38"></a>
### Theorem CA.38. Cauchy's theorem and formula for cycles

For a cycle $\Gamma$, the notation $\{\Gamma\}$ below means the union
of its path traces. A minus sign on a path means reversed orientation;
an integer coefficient means repeated traversal, with reversal for
negative coefficients. Integrals and winding numbers add with those
coefficients.

Let $G$ be open and $\Gamma$ a finite cycle of closed rectifiable paths
in $G$. Assume $n(\Gamma;a)=0$ for every $a\notin G$. If $f$ is
holomorphic on $G$, then

$$
\int_\Gamma f(z)\,dz=0,
\qquad
\frac1{2\pi i}\int_\Gamma\frac{f(z)}{(z-a)^{k+1}}\,dz
=\frac{n(\Gamma;a)}{k!}f^{(k)}(a)
$$

for $a\in G\setminus\{\Gamma\}$ and integers $k\geq0$.

The hypothesis about points outside $G$ is the critical one: the cycle
must have net winding zero around every point where holomorphicity is
not assumed. Merely requiring its trace to lie in $G$ would fail for
$f(z)=1/z$ and the unit circle in the punctured plane.
For $k=0$, the formula says that the integral reproduces $f(a)$ times
the number of net turns around $a$. For a positive circle containing
$a$, that number is 1 and we recover CA.29.

**Proof of the integral theorem.** Cover the compact traces by disks with
closures in $G$. Split each path into finitely many subarcs lying in such
disks and replace each by its chord. On each disk $f$ has a primitive
by CA.28, so this changes no integral. It also changes no index about any
point outside $G$, because $1/(z-a)$ has a primitive on that disk.
We have reduced the question to a finite polygonal cycle.

There are two separate tasks left: express this polygonal cycle as
boundaries of regions, then show only regions contained in $G$ contribute.
The winding-number hypothesis controls the second task. The next
paragraph supplies the bookkeeping needed for the first.

Split all its edges at intersections and cancel oppositely oriented
overlapping edges with their multiplicities. This makes a finite planar
graph. Its complementary faces have constant integer indices by CA.37.
The index on the left of an oriented edge minus the index on the right
equals its oriented multiplicity. Here is the local calculation: translate
and rotate a nonvertex point of an edge so the edge runs from $-\varepsilon$
to $\varepsilon$ along the real axis. Its integrals of $1/(z-a)$ for
$a=i\eta$ and $a=-i\eta$ have respective limits $i\pi$ and $-i\pi$
as $\eta\downarrow0$, by integrating
$(x\pm i\eta)/(x^2+\eta^2)$ over this symmetric interval. Contributions
from the rest of the cycle have the same limit on both sides, since that
rest stays away from the chosen point. Dividing the difference by $2\pi i$
gives the jump 1 for one positively directed edge, and multiplicities add.
Thus the polygonal cycle is the sum of the positively oriented boundaries
of its bounded faces, each multiplied by that face's index. Internal
edge coefficients telescope to precisely the original multiplicities.

A **face** here is a connected region left after deleting the graph's
edges and vertices from the plane. “Left” and “right” refer to standing
on an edge facing its direction of traversal. A positively oriented
face boundary keeps that face on its left. If the two adjacent faces
have indices $m_L,m_R$, their weighted boundaries put coefficient
$m_L-m_R$ on the directed edge. The jump calculation proves that this
is exactly the edge's coefficient in the original cycle. This explains
the sum of boundaries without requiring every cycle to be a simple curve.

Every face with nonzero coefficient, including its boundary, lies in
$G$: its interior cannot meet the complement, where the index is zero,
and its boundary consists of edges already in $G$. Its closure is compact.
Such a polygonal face can be subdivided into finitely many triangles:
after rotating the axes to avoid vertical edges, draw vertical segments
through its vertices, stopping at the next boundary edge. This cuts even
a face with holes into trapezoids and triangles; cut each trapezoid by a
diagonal. All pieces remain in the face closure. Apply CA.28 to the
triangles and cancel their internal boundaries. Each face integral is
zero, proving the theorem.

**Proof of the formula.** The function
$h(z)=[f(z)-f(a)]/(z-a)$, with its derivative value at $a$, is
holomorphic on $G$, as its Taylor series at $a$ shows. The integral
theorem gives $\int_\Gamma h=0$. Expanding $h$ inside that integral
gives
$\int_\Gamma f(z)/(z-a)\,dz=f(a)\int_\Gamma dz/(z-a)
=2\pi i\,n(\Gamma;a)f(a)$, the formula for $k=0$.
In a small disk about $a$ avoiding the trace, the index is constant.
Differentiate the formula there: the kernels and their derivatives
converge uniformly on the trace, which justifies passing derivatives
through the integral by the difference-quotient estimate. Repeating
gives the factor $k!$ and the asserted formula. $\square$

This is a homological condition, expressed by winding numbers; it does
not require $G$ to be simply connected. The original VII.4.1 uses exactly
this condition, not the incorrect assertion that every closed contour
in an arbitrary open set has integral zero.

The word **homological** in this paragraph is a name for this
winding-number cancellation condition. No abstract homology theory is
needed to use the theorem.

<a id="ca-39"></a>
### Lemma CA.39. Contours surrounding a compact set

This result constructs the integration paths used later: they stay inside
the holomorphicity region $G$, avoid the compact set $K$, and make one
net turn around each point of $K$. A **simple closed curve** closes up
without intersecting itself except at its common starting/ending point.

If $K\subset G\subset\mathbb C$, with $K$ compact and $G$ open, there
is a finite polygonal cycle in $G\setminus K$ with index 1 on $K$ and
0 outside $G$. One may choose a finite collection of disjoint smooth
simple closed curves with the same properties and indices only 0 or 1
off the curves.

**Proof.** If $K$ is empty, the empty cycle suffices. Otherwise choose
$\delta>0$ so that the closed $\delta$-neighborhood
of $K$ is bounded and contained in $G$. Choose a square grid of side length
$h$ with $3\sqrt2h<\delta$,
take the finitely many closed squares meeting $K$, and
add all squares sharing an edge or vertex with one of them. Their union
$P$ contains $K$ in its interior and lies within the $\delta$-neighborhood.

The extra layer of squares is important. If a point of $K$ lies on a
grid line or vertex, every square touching it is included along with a
surrounding layer. It therefore lies in the interior of the union, not
on the boundary that will become the contour. For an added square,
choose a neighboring square meeting $K$ and a point of $K$ in that
square. The distance from any point of the added square to that point
is at most $2\sqrt2h<\delta$. Thus the entire union stays in the
chosen neighborhood.
Sum the counterclockwise boundaries of the squares and cancel internal
edges. The remaining boundary is in $G\setminus K$. At points not on
the grid the index is the sum of the square indices, hence 1 in the
interior of $P$ and 0 outside. Local constancy extends this to all
points off the remaining boundary, including points of $K$ on grid lines.

For disjoint simple boundaries, resolve any corner-only contacts in
small disjoint disks about the finitely many grid vertices. These disks
can be chosen in $G\setminus K$. Replace a contact by two separated
rounded arcs, keeping the chosen region on the left as it is traversed.
Round the other corners too, using smooth arcs tangent to the straight
edges and with a smooth transition. The disks may be so small that no
new intersections are introduced. The resulting finite embedded boundary
has components which are disjoint smooth simple closed curves. Its index
is the indicator of the rounded region: it is unchanged away from the
small disks, and the local replacement keeps indices 0 and 1 inside
each disk. In particular it remains 1 on $K$ and 0 outside $G$.
Inner boundary components have clockwise orientation. $\square$

For III.§8 the polygonal version alone suffices: list its oriented
segments as $\gamma_1,\ldots,\gamma_N$ and apply CA.38. For VII.4.4
the smoothed version supplies the asserted contour system. Applying the
construction successively to a compact neighborhood of the first system
gives the nested contour systems used to prove multiplicativity of the
functional calculus.

<a id="ca-40"></a>
### Theorem CA.40. Laurent expansions and residues

If $f$ is holomorphic on $r<|z-a|<R$, it has a unique expansion
$f(z)=\sum_{n\in\mathbb Z}c_n(z-a)^n$, uniformly and absolutely
on compact subannuli. For any $r<s<R$,

$$
c_n=\frac1{2\pi i}\int_{|w-a|=s}\frac{f(w)}{(w-a)^{n+1}}\,dw.
$$

For an isolated singularity at $a$, the coefficient $c_{-1}$ is the
**residue** $\operatorname{Res}(f;a)$. A removable singularity has no
negative powers; a pole of order $m$ has finitely many negative powers
and lowest power $-m$.

Here $\mathbb Z$ is the set of all integers: a **Laurent series**
allows negative powers as well as the nonnegative powers of a Taylor
series. Its **principal part** is the negative-power part. A compact
subannulus has the form $u\leq|z-a|\leq v$ with $r<u\leq v<R$.
Convergence on it means that the positive-power and negative-power
series both converge there, with uniform absolute tail bounds.

An **isolated singularity** is a missing point $a$ around which the
function is holomorphic on a punctured disk $0<|z-a|<R$. If its
Laurent series has infinitely many nonzero negative-power coefficients,
the singularity is called **essential**. Thus $e^{1/(z-a)}$ has an
essential singularity; $(z-a)^{-3}$ has a pole of order 3. A residue is
the single coefficient of $(z-a)^{-1}$, not the entire singular part.

**Proof.** Choose $r<s<|z-a|<t<R$. Use the positive radius-$t$ circle
and the negative radius-$s$ circle as a cycle in the original annulus
$G=\{r<|w-a|<R\}$. Its index is zero outside $G$ and 1 at $z$.
Thus CA.38 gives

$$
f(z)=\frac1{2\pi i}\int_{|w-a|=t}\frac{f(w)}{w-z}\,dw
-\frac1{2\pi i}\int_{|w-a|=s}\frac{f(w)}{w-z}\,dw.
$$

On the outer circle the expansion is

$$
\frac1{w-z}=\sum_{n=0}^\infty\frac{(z-a)^n}{(w-a)^{n+1}}.
$$

On the inner circle it is instead

$$
\frac1{w-z}=-\frac1{z-a}\frac1{1-(w-a)/(z-a)}
=-\sum_{k=0}^\infty\frac{(w-a)^k}{(z-a)^{k+1}}.
$$

The minus sign here cancels the minus sign preceding the inner contour
integral. Consequently the first integral produces powers $(z-a)^n$,
$n\geq0$, while the second produces powers $(z-a)^{-k-1}$.
For a fixed compact subannulus choose $s<u\leq v<t$; the geometric
ratios are bounded respectively by $v/t<1$ and $s/u<1$. This proves
the uniform convergence needed for both exchanges of series and integral.

For any integer $n$, the coefficient integrand
$f(w)/(w-a)^{n+1}$ is holomorphic on the original annulus.
CA.38 applied to the difference of any two concentric circle contours
shows that the coefficient integral is independent of the radius.
Finally, integrate a proposed Laurent series against
$(z-a)^{-m-1}\,dz/(2\pi i)$ on a circle. Each power integrates to zero
except the $m$th term, which gives its coefficient, by the parametrization
in CA.29 (valid for integer exponents as well). Uniform convergence
licenses this coefficient extraction, proving uniqueness. The removable
and pole cases follow by Taylor expansion or by multiplying out the
factor $(z-a)^{-m}$. $\square$

<a id="ca-41"></a>
### Theorem CA.41. Residue and argument principles

Suppose $f$ is holomorphic on $G$ except at finitely many isolated
singularities $a_j$, and $\Gamma$ is a cycle avoiding them and having
zero index outside $G$. Then

$$
\int_\Gamma f=2\pi i\sum_j n(\Gamma;a_j)\operatorname{Res}(f;a_j).
$$

If $f$ is meromorphic on a neighborhood of a compact region with smooth
boundary, has no zeros or poles on the boundary, and is not identically
zero on any relevant component, then
$(2\pi i)^{-1}\int_{\partial P}f'/f$ equals the number of zeros minus
the number of poles in $P$, counted with multiplicity.

Here **meromorphic** means holomorphic except at isolated poles. A zero
of order $m$ contributes $+m$ to the count, and a pole of order $m$
contributes $-m$. Essential singularities are allowed in the first residue
formula but not in this zero-minus-pole interpretation of $f'/f$.

**Proof.** Take small disjoint positive circles $C_j$ about $a_j$.
The cycle $\Gamma-\sum_j n(\Gamma;a_j)C_j$ has zero index outside
$G\setminus\{a_j\}$. CA.38 makes its integral zero. Termwise
integration of CA.40 gives $\int_{C_j}f=2\pi i c_{-1}$.

To check the cycle hypothesis explicitly, choose each circle and its disk
inside $G$, avoiding the trace of $\Gamma$ and all other singularities.
At $a_j$, its own circle has index 1, and the other small circles have
index 0. The subtraction cancels $n(\Gamma;a_j)$ exactly. At every
point outside $G$, all the small circles have index 0 and the original
cycle also has index 0. These are precisely the excluded points of
$G\setminus\{a_j\}$. Rearranging the zero-integral conclusion now gives
the residue formula. The coefficient $c_{-1}$ appears because
$\int (z-a)^n\,dz=0$ for every integer $n\ne-1$, whereas the
$n=-1$ integral is $2\pi i$.

For the second assertion, near a zero or pole write
$f(z)=(z-a)^m g(z)$, where $m$ is positive for a zero, negative for a
pole, and $g$ is holomorphic and nonzero. Then
$f'/f=m/(z-a)+g'/g$ has residue $m$. There are only finitely many
zeros and poles in the compact region, by isolation and the absence
of boundary zeros or poles. Apply the residue formula. $\square$

The quotient $f'/f$ is called the **logarithmic derivative**, since it
would be the derivative of $\log f$ wherever a logarithm branch is chosen.
The argument principle does not require a single such branch on the
entire region. On a positively oriented region boundary the index is
1 inside the region and 0 in its holes and outside, which is why each
interior zero or pole contributes its multiplicity exactly once.

## Transfer to functional analysis

<a id="ca-42"></a>
### Theorem CA.42. Banach-valued Cauchy theory and Liouville's theorem

Recall from CA.9 that a Banach space is a normed vector space in which
Cauchy sequences converge in norm. For $F:G\to X$, a **complex
derivative in norm** means a vector $F'(z)\in X$ satisfying

$$
\left\|\frac{F(z+h)-F(z)}h-F'(z)\right\|\longrightarrow0.
$$

The **dual space** $X^*$ consists of bounded complex-linear maps
$x^*:X\to\mathbb C$. Boundedness means
$|x^*(v)|\leq\|x^*\|\,\|v\|$ for some finite constant $\|x^*\|$.
Such maps are continuous and turn vector-valued questions into scalar
ones. We use the complex Hahn–Banach extension theorem here as a
functional-analysis input: a bounded linear functional on a subspace
extends to the whole space with the same norm. The argument below shows
exactly how that input is used.

Let $X$ be a complex Banach space and $F:G\to X$ have a continuous
complex derivative in norm. Contour integrals of $F$ exist, commute
with every bounded linear functional $x^*\in X^*$, and satisfy

$$
\left\|\int_\gamma F\right\|
\leq\ell(\gamma)\sup_\gamma\|F\|.
$$

Cauchy's theorem, Cauchy's formula, Taylor expansions on disks, and
Cauchy estimates hold with $X$-valued coefficients. A bounded entire
$X$-valued function is constant.

**Proof.** Continuous Banach-valued functions on a compact interval have
Riemann integrals: uniform continuity makes fine Riemann sums Cauchy,
and completeness gives their limit. The same argument with total
variation proves the rectifiable-path construction in CA.27. Apply a
bounded linear functional to the sums and pass to the limit to obtain
commutation: if the vector sums $S_N$ tend to $I$, then
$|x^*(S_N)-x^*(I)|\leq\|x^*\|\|S_N-I\|\to0$.
Similarly,

$$
\left|\frac{x^*(F(z+h))-x^*(F(z))}{h}-x^*(F'(z))\right|
\leq\|x^*\|\left\|\frac{F(z+h)-F(z)}h-F'(z)\right\|\to0.
$$

Thus $x^*\circ F$ is scalar holomorphic.

Apply scalar CA.38 to $x^*F$. The difference between the two sides of
the proposed vector formula has value zero under every $x^*$. The
Hahn–Banach theorem implies that this vector is zero. Indeed, if $v\ne0$,
the functional on its one-dimensional span defined by
$\lambda v\mapsto\lambda\|v\|$ has norm 1 and is nonzero on $v$.
Hahn–Banach extends it to an element of $X^*$, contradicting vanishing
under every functional. This property is called **separating points**.
Thus the vector Cauchy formula holds. Expanding
its kernel uniformly on smaller disks produces a norm-convergent power
series with coefficients
$v_n=(2\pi i)^{-1}\int F(w)/(w-c)^{n+1}\,dw$. The integral norm
estimate gives $\|v_n\|\leq M_r/r^n$. The proof of CA.25 works with
norms, identifying $n!v_n=F^{(n)}(c)$. Finally apply scalar Liouville to
each $x^*F$ and separate $F(z)-F(c)$ by Hahn–Banach. $\square$

<a id="ca-43"></a>
### Lemma CA.43. The resolvent is analytic, with a genuine local series

A **unital complex Banach algebra** is a complex Banach space with
associative multiplication, an identity element $1$, and
$\|bc\|\leq\|b\|\|c\|$. Multiplication need not commute. An element
$b$ is **invertible** if an element $b^{-1}$ satisfies
$bb^{-1}=b^{-1}b=1$. For a fixed $a$ define

$$
\rho(a)=\{z\in\mathbb C:z1-a\text{ is invertible}\},\qquad
\sigma(a)=\mathbb C\setminus\rho(a).
$$

These are its **resolvent set** and **spectrum**. The **resolvent
function** is $R(z)=(z1-a)^{-1}$ on $\rho(a)$. In a matrix algebra,
the spectrum is the set of eigenvalues; in general an element can fail
to be invertible without having an eigenvector, so invertibility is the
definition used here.

Let $A$ be a nonzero unital complex Banach algebra with $\|1\|=1$.
For $a\in A$ and $z_0$ in its resolvent set put
$R_0=(z_0 1-a)^{-1}$. If $|h|\|R_0\|<1$, then

$$
((z_0+h)1-a)^{-1}
=\sum_{n=0}^\infty(-h)^nR_0^{n+1},
\qquad R'(z_0)=-R_0^2.
$$

In particular the resolvent set is open, and its resolvent function is
holomorphic in norm. The spectrum is nonempty and compact.

**Proof, existence of local inverses.** For $\|b\|<1$, the series
$S=\sum_{n\geq0}b^n$ converges in norm since $\|b^n\|\leq\|b\|^n$
and the algebra is complete. Its finite sums satisfy
$(1-b)S_N=S_N(1-b)=1-b^{N+1}$. Multiplication is continuous by the
norm inequality, so passage to the limit gives $(1-b)S=S(1-b)=1$.
This is the **Neumann series**; it proves both inverse identities.

Since $(z_0 1-a)R_0=1$, factor
$((z_0+h)1-a)=(z_0 1-a)(1+hR_0)$.
When $|h|\|R_0\|<1$, the Neumann series with $b=-hR_0$ gives

$$
((z_0+h)1-a)^{-1}
=(1+hR_0)^{-1}R_0
=R_0-hR_0^2+h^2R_0^3-\cdots.
$$

The order of the inverse factors is reversed as usual; all displayed
powers of $R_0$ commute with each other. The series converges uniformly
in norm on every smaller $h$-disk. CA.25's norm argument justifies
differentiation, whose linear coefficient is $-R_0^2$. The permitted
$h$ form a neighborhood of zero, proving that $\rho(a)$ is open.

**Proof of compactness and nonemptiness of the spectrum.**
For $|z|>\|a\|$ the same argument gives
$R(z)=z^{-1}\sum_{n\geq0}a^n/z^n$ and
$\|R(z)\|\leq1/(|z|-\|a\|)$. Thus the spectrum is closed and
bounded: it is the complement of the open set $\rho(a)$ and is contained
in $|z|\leq\|a\|$. CA.4 makes it compact as a subset of the complex
plane; this does not assert that bounded closed sets in the algebra are
compact. If the spectrum were empty, $R$ would be entire, bounded outside a disk
by this estimate and inside by continuity and compactness. CA.42 would
make it constant, and its limit zero at infinity would make it zero,
contradicting $(z1-a)R(z)=1\ne0$. $\square$

This proves the complex-analytic step behind VII.3.6 without assuming
that a Banach-valued theorem automatically follows from its scalar name.
It also explains why the assertion requires complex scalars: the real
rotation matrix in VII.3.5 has empty real spectrum.

<a id="ca-44"></a>
### Lemma CA.44. Differentiating Cauchy transforms under an integral

“Supported on $K$” means the measure has no contribution outside $K$
(equivalently its total variation is zero there). The **Cauchy transform**
here averages the kernel $1/(z-w)$ over $z$ while varying the evaluation
point $w$. Keeping these two roles separate prevents sign errors.

Let $\mu$ be a finite complex measure supported on compact $K$, and
$F(w)=\int_K(z-w)^{-1}\,d\mu(z)$ for $w\notin K$. Then

$$
F^{(n)}(w)=n!\int_K(z-w)^{-n-1}\,d\mu(z),\qquad n\geq0.
$$

**Proof.** If $K$ is empty, the transform and all the integrals are zero.
Otherwise, at $w_0\notin K$ let $d=\operatorname{dist}(w_0,K)>0$.
For $|h|<d$, uniformly in $z\in K$ on every smaller $h$-disk,

$$
\frac1{z-w_0-h}=\sum_{n=0}^\infty
\frac{h^n}{(z-w_0)^{n+1}}.
$$

The bound $|h|^n/d^{n+1}$ proves uniform absolute convergence. CA.22
permits termwise integration, and CA.25 then gives the derivative formula.

Indeed, on $|h|\leq s<d$, a common numerical majorant is $s^n/d^{n+1}$.
Its sum is finite, and CA.19 bounds the integral of every remainder by
$|\mu|(K)$ times its uniform size. Thus the actual expansion is

$$
F(w_0+h)=\sum_{n=0}^\infty h^n
\left(\int_K(z-w_0)^{-n-1}\,d\mu(z)\right).
$$

The $n$th derivative at $h=0$ is $n!$ times that coefficient. Since
$w_0$ was arbitrary outside $K$, this proves the stated formula everywhere
on the complement, not just at one chosen center.
The sign is positive, since differentiation of $(z-w)^{-1}$ with respect
to $w$ cancels two minus signs. By contrast the resolvent in CA.43 is
$(w1-a)^{-1}$ and has a negative first derivative. $\square$

## A slower second pass: topology, branches, and further consequences

<a id="ca-45"></a>
### Theorem CA.45. Deformation of contours and global primitives

CA.8 defined a deformation $H(s,t)$, where $s$ is its stage and $t$
is position along the loop. The theorem below says an integral is
unchanged when the loop moves continuously through a region where the
integrand stays holomorphic. Crossing a singularity would violate this
hypothesis.

Let $f$ be holomorphic on a domain $G$. If two closed rectifiable paths
are joined by a continuous deformation through closed paths in $G$, their
integrals of $f$ agree. In particular every holomorphic function on a
simply connected domain has a primitive, and every closed rectifiable
contour integral of that function is zero.

**Proof, including the role of a merely continuous deformation.** Cover
the compact image of $H:[0,1]^2\to G$ by open disks with closures in
$G$. By [CA.17](background-complex-analysis.md#ca-17), subdivide
the parameter square so that each small square maps into one disk.
At the image of each small square's four vertices, join successive
vertices by straight segments. The resulting polygon is inside that disk,
where $f$ has a primitive by CA.28; its integral is zero. Adjacent small
squares have identical image endpoints on a shared edge and therefore
use the same straight segment with opposite orientations. Even if they
use different disks, this segment lies in their intersection, because
both disks are convex and contain its endpoints.

Sum these zero integrals. Internal segments cancel. The two sides
corresponding to the moving starting/ending point of the closed loop
cancel, since $H(s,0)=H(s,1)$. The remaining polygonal paths approximate
the initial and final loops in the stronger sense that each subarc and
its replacement chord lie in one primitive disk. They have exactly the
same integrals by the primitive rule in CA.27. This proves invariance
without assuming that intermediate paths in the deformation are smooth
or rectifiable. A constant loop has zero integral, so simple connectedness
gives the second assertion about closed paths.

Fix $a\in G$. For $z\in G$, define $F(z)$ by integrating $f$ along
a polygonal path from $a$ to $z$, which exists by CA.7. Two such paths,
one followed by the reverse of the other, form a closed contour, so the
value is independent of the path. For small $h$ add the segment from
$z$ to $z+h$ to get
$F(z+h)-F(z)=h\int_0^1f(z+th)\,dt$. Divide and let $h\to0$:
$F'(z)=f(z)$. $\square$

**Path independence explained.** If paths $\alpha,\beta$ both go
from $a$ to $z$, their concatenation $\alpha$ followed by reversed
$\beta$ is closed. Its integral is
$\int_\alpha f-\int_\beta f=0$. This is why defining $F(z)$ by
“an integral from $a$ to $z$” gives a single value: the route has
ceased to matter. Having primitives on small disks alone would not
establish this global conclusion.

Apply the theorem to $1/z$ on $\mathbb C\setminus\{0\}$.
A positively oriented unit circle has integral $2\pi i$, whereas a
constant path has integral zero. Thus the circle cannot contract inside
the punctured plane. This proves, rather than merely draws, the obstruction
caused by the hole. Simply connectedness is a sufficient condition for
all closed integrals to vanish; CA.38's winding-number condition also
handles domains with holes and particular cycles whose indices cancel.

<a id="ca-46"></a>
### Theorem CA.46. Holomorphic logarithms and roots

If $f$ is holomorphic and nonvanishing on a simply connected domain $G$,
there exists a holomorphic $L$ with $e^L=f$. For every positive integer
$m$, the function $e^{L/m}$ is a holomorphic $m$th root of $f$.
Any two logarithms of $f$ on a connected domain differ by a constant
$2\pi i k$, $k\in\mathbb Z$.

“Nonvanishing” means $f(z)\ne0$ at every point. The proof is guided
by the equation we want: if $e^L=f$, differentiation would give
$L'=f'/f$. Thus we first integrate $f'/f$, and then choose its
additive constant to make the exponential equal to $f$ at one base
point. Simple connectedness supplies the global primitive needed here.

**Proof.** The quotient $f'/f$ is holomorphic. By CA.45 it has a
primitive $P$, chosen with $P(a)=0$. Pick one scalar $\ell$ with
$e^\ell=f(a)$, possible from polar coordinates, and put $L=P+\ell$.
Then

$$
(fe^{-L})'=e^{-L}(f'-fL')=0.
$$

By connectedness this function is constant, and its value at $a$ is 1.
Thus $f=e^L$. The exponential multiplication identity proves the root
assertion, since $(e^{L/m})^m=e^L=f$. If $e^{L_1}=e^{L_2}$, CA.26 gives
$L_1(z)-L_2(z)\in2\pi i\mathbb Z$ for each $z$. This difference
is continuous and integer-valued after scaling, hence constant on the
connected domain. $\square$

**The principal branch.** The slit plane
$G=\mathbb C\setminus(-\infty,0]$ is star-shaped about 1: a segment
from 1 to a nonreal point has nonzero imaginary part except at its
positive-real starting point, and positive real points cause no problem.
CA.8 and the theorem give a logarithm of $z$, normalized by $L(1)=0$.
It is
$\operatorname{Log}z=\log|z|+i\operatorname{Arg}z$ with
$-\pi<\operatorname{Arg}z<\pi$. To identify the branch, the real
part follows from $|e^L|=e^{\operatorname{Re}L}=|z|$; the continuous
argument in that range agrees at 1 and differs from $\operatorname{Im}L$
by a continuous integer multiple of $2\pi$, hence by zero.

Consequently $\sqrt z=e^{\operatorname{Log}z/2}$ defines a holomorphic
root on the slit plane. There is no holomorphic root of $z$ on the
whole punctured plane when $m\geq2$: if $g^m=z$, differentiation gives
$g'/g=1/(mz)$. Integration around the unit circle would give
$\int g'/g=2\pi i/m$. But this integral divided by $2\pi i$ is
the integer winding number of the closed path $g(e^{it})$ about zero,
by the chain rule and CA.37, a contradiction. A choice of a scalar root
at each point does not automatically make a continuous or holomorphic
function. This matters when selecting functions for holomorphic calculus.

<a id="ca-47"></a>
### Theorem CA.47. Morera's theorem and holomorphic parameter integrals

If $f$ is continuous on an open set $G$ and its integral over the
boundary of every triangle contained with its interior in $G$ is zero,
then $f$ is holomorphic. In particular, if $q(z,t)$ is jointly continuous
on $G\times[a,b]$ and holomorphic in $z$ for each fixed $t$, then
$F(z)=\int_a^b q(z,t)\,dt$ is holomorphic, without an initial
assumption about joint continuity of $q_z$.

Morera reverses the direction of Goursat's theorem: instead of assuming
complex differentiability and deducing zero integrals, it uses zero
triangle integrals, together with continuity, to deduce differentiability.
The proof first constructs an antiderivative; it does not estimate
difference quotients of $f$ directly.

**Proof.** On a disk in $G$, the last part of CA.28 constructs a primitive
$P$ of the continuous function $f$ using only the zero triangle integrals.
Thus $P$ is holomorphic and $P'=f$. By CA.30 derivatives of a holomorphic
function are holomorphic, proving Morera's theorem locally at every point.

For the application, continuity on compact disk–interval products gives
continuity of $F$ by the uniform integral estimate. On a fixed triangle
$T\subset G$, the integrand is bounded on $\partial T\times[a,b]$.
Parametrize the finitely many segments; the absolute double integral is
finite, so Fubini yields

$$
\int_{\partial T}F(z)\,dz
=\int_a^b\left(\int_{\partial T}q(z,t)\,dz\right)dt=0.
$$

The inner integral is zero by CA.28 for each $t$. Morera now applies.
$\square$

Continuity in Morera is essential: changing a function at a single point
does not change its integrals along segments but can destroy continuity
and holomorphicity. For example, set $f(0)=1$ and $f(z)=0$ elsewhere.
Every triangle boundary integral is zero, since changing finitely many
parameter values on a nonconstant segment does not change its Riemann
integral, but $f$ is discontinuous at zero.
Also note the logical order: Morera here uses the
already proved Taylor theorem. It is not used in the first proof of
Cauchy's formula, where doing so would risk circular reasoning.

<a id="ca-48"></a>
### Theorem CA.48. Harmonic components, mean values, and the Bergman estimate

A real $C^2$ function $u$ is **harmonic** if
$\Delta u=u_{xx}+u_{yy}=0$. If $f=u+iv$ is holomorphic, then $u,v$
are harmonic. If $\overline{D(a,r)}\subset G$, then

$$
f(a)=\frac1{2\pi}\int_0^{2\pi}f(a+re^{it})\,dt,
\qquad
|f(a)|^2\leq\frac1{\pi r^2}\int_{D(a,r)}|f(z)|^2\,dA(z).
$$

The operator $\Delta=\partial_x^2+\partial_y^2$ is the **Laplacian**,
the sum of the two second coordinate derivatives. The first identity
says the center value equals the average of the values on each circle.
The second says the squared size at the center is at most the average
of the squared sizes over the disk; the normalization $\pi r^2$ is
its area. These statements assume $f$ is holomorphic on the open set $G$.

**Proof.** CA.30 implies that the real and imaginary parts have continuous
partial derivatives of every order. Differentiating the Cauchy–Riemann
equations gives $u_{xx}+u_{yy}=v_{yx}-v_{xy}=0$ and likewise for $v$.
Equality of the mixed derivatives for a $C^2$ function follows, for
example, by writing a rectangle's double increment as an iterated integral
of either mixed derivative, interchanging the continuous integrals, then
dividing by the rectangle area and shrinking to the point.

Parametrize the circle in CA.29 with the evaluation point at its center.
Then $(w-a)^{-1}dw=i\,dt$, giving the mean-value identity. For each
$0<\rho\leq r$, the integral Cauchy–Schwarz inequality gives

$$
|f(a)|^2\leq\frac1{2\pi}\int_0^{2\pi}|f(a+\rho e^{it})|^2\,dt.
$$

One can see this particular inequality directly, without invoking a
general integral inequality. Let $q(t)=f(a+\rho e^{it})$ and let
$m=(2\pi)^{-1}\int q(t)\,dt=f(a)$. Expanding the square and using
the definition of $m$ gives

$$
0\leq\frac1{2\pi}\int_0^{2\pi}|q(t)-m|^2\,dt
=\frac1{2\pi}\int_0^{2\pi}|q(t)|^2\,dt-|m|^2.
$$

Multiply the circle inequality for $|f(a)|^2$ by $2\pi\rho$ and
integrate from 0 to $r$.
[CA.20](background-complex-analysis.md#ca-20) identifies the right
side as the area integral, while the left side is $\pi r^2|f(a)|^2$.
$\square$

**Why Conway needs this.** If $K\subset G$ is compact, CA.6 supplies
one $r>0$ with every closed disk $\overline{D(a,r)}$, $a\in K$,
contained in $G$. Apply the estimate to a holomorphic difference to get

$$
\sup_{a\in K}|f_n(a)-f_m(a)|
\leq\frac1{\sqrt\pi r}\|f_n-f_m\|_{L^2(G)}.
$$

Here $\|h\|_{L^2(G)}=(\int_G|h|^2\,dA)^{1/2}$ measures the total
squared size in the whole region. The disk integral is at most the
integral over $G$ because its integrand is nonnegative. Taking square
roots of the disk estimate gives exactly the constant $1/(\sqrt\pi r)$.
A common radius for every $a\in K$ is what permits taking the supremum.
The **Bergman space** consists of holomorphic functions on $G$ with
finite $L^2$ norm.

Thus an $L^2$-Cauchy sequence of holomorphic functions is uniformly
Cauchy on each compact subset, and its local uniform limit is holomorphic
by CA.35. To identify it with the $L^2$ limit, choose a subsequence
converging almost everywhere, as proved in BG-I.7; it also converges
pointwise to the local uniform limit, so the limits agree almost everywhere.
This establishes the analytic step behind the Hilbert/Bergman-space
example. Arbitrary $L^2$ functions do not satisfy this point-evaluation
bound: holomorphicity, through the circle mean identity, is indispensable.

<a id="ca-49"></a>
### Theorem CA.49. Rouché's theorem and stability of zero counts

Let $f,g$ be holomorphic on a neighborhood of a closed disk. If
$|g-f|<|f|$ everywhere on its boundary circle, then $f$ and $g$ have
the same number of zeros in the disk, counted with multiplicity.

The boundary inequality says the change from $f$ to $g$ is strictly
smaller than the size of $f$ there. Consequently, changing $f$ gradually
into $g$ never creates a boundary zero. The argument principle converts
this continuous change into an integer count, which cannot change
continuously from one integer to another.

**Proof.** Let $h_t=f+t(g-f)$ for $0\leq t\leq1$. On the boundary,
$|h_t|\geq |f|-|g-f|>0$. Compactness gives a single positive lower
bound valid for all boundary points and all $t$.
By the argument principle, the number of zeros of $h_t$ is

$$
N(t)=\frac1{2\pi i}\int_{\partial D}\frac{h_t'(z)}{h_t(z)}\,dz.
$$

The prime means differentiation in $z$, with $t$ held fixed:
$h_t'=f'+t(g'-f')$. The lower bound can be chosen as
$\min_{\partial D}(|f|-|g-f|)>0$, independent of $t$. It ensures
that the quotient varies continuously on the compact set
$[0,1]\times\partial D$, so its integral varies continuously too.

Thus $N(t)$ is continuous and integer-valued, so it is constant on
the connected interval $[0,1]$.
The values at 0 and 1 give the conclusion. There are finitely many zeros
inside: boundary nonvanishing and compactness exclude accumulation there,
and CA.31 excludes interior accumulation. $\square$

**Example with the inequality checked.** On $|z|=1$,
$|z^5+1|\leq2<3=|3z|$. Therefore $z^5+3z+1$ and $3z$ have the
same number of zeros in the unit disk: exactly one, with multiplicity.
The theorem does not locate that zero. Its purpose is to show how an
estimate on a boundary can control a discrete count in the interior.

<a id="ca-50"></a>
### Theorem CA.50. Open mapping and the local inverse

A nonconstant holomorphic function on a domain maps open sets to open
sets. If $f'(a)\ne0$, there are neighborhoods $U$ of $a$ and $V$
of $f(a)$ such that $f:U\to V$ is bijective with holomorphic inverse,
whose derivative at $w=f(z)$ is $1/f'(z)$.

An **open map** sends every open subset of its domain to an open set.
This is different from continuity, which concerns inverse images of
open sets. The **local inverse** assertion concerns a sufficiently
small neighborhood, not global injectivity: $e^z$ has nonzero derivative
everywhere but repeats its values after increments of $2\pi i$.

**Proof of openness.** At any $a$, CA.31 factors
$f(z)-f(a)=(z-a)^m q(z)$ near $a$, where $m\geq1$ and $q(a)\ne0$.
Choose a closed disk sufficiently small that $q$ has no zeros there.
The minimum $\eta$ of $|f(z)-f(a)|$ on its boundary is positive.
For $|w-f(a)|<\eta$, CA.49 applied to $f-f(a)$ and $f-w$ shows
that $f-w$ has $m$ zeros inside, counted with multiplicity. In particular
it has a zero, so the image contains a neighborhood of $f(a)$.
The disk can be chosen inside any given open subset of the original
domain, proving the open-mapping assertion.

**Proof of the inverse assertion.** When $f'(a)\ne0$, shrink the disk
so that $f'$ is nonzero there; the factorization has $m=1$.
The preceding zero-count argument gives exactly one preimage in that
disk for every $w$ in the small disk $V=D(f(a),\eta)$.
Let $U=f^{-1}(V)\cap D(a,r)$ and let $g:V\to U$ choose that unique
preimage. The restriction of $f$ is open and bijective, so $g$ is
continuous. For $w\to w_0$, put $z=g(w)$ and $z_0=g(w_0)$. Then

$$
\frac{g(w)-g(w_0)}{w-w_0}
=\left(\frac{f(z)-f(z_0)}{z-z_0}\right)^{-1}
\longrightarrow\frac1{f'(z_0)}.
$$

Continuity of $g$ ensures $z\to z_0$, and injectivity ensures the
quotients are defined for $w\ne w_0$. This proves holomorphicity and
the derivative formula. $\square$

To unpack the two topological steps: a zero count of 1 allows exactly
one preimage, since each distinct zero contributes a positive integer.
For an open subset $O$ of $U$, the inverse image under $g$ is
$g^{-1}(O)=f(O)$, which is open because $f$ is an open map.
This is precisely continuity of $g$, needed before taking its
difference quotient.

The complex-analytic open mapping theorem here concerns nonlinear scalar
functions. It is not the Banach-space open mapping theorem for surjective
bounded **linear** maps used in Conway III.§12. The names describe a
common conclusion, not interchangeable hypotheses or proofs.

<a id="ca-51"></a>
### Theorem CA.51. Schwarz's lemma and the meaning of a disk estimate

If $f:D(0,1)\to D(0,1)$ is holomorphic and $f(0)=0$, then
$|f(z)|\leq|z|$ and $|f'(0)|\leq1$. Equality at a nonzero point,
or $|f'(0)|=1$, forces $f(z)=cz$ with $|c|=1$.

The assumption $f(0)=0$ removes a possible translation. The conclusion
$|f(z)|\leq|z|$ says that such a disk map cannot move a point farther
from the center. The equality case is much stronger: a single equality
forces the whole map to be multiplication by a unit-modulus number,
which is a rotation.

**Proof.** Taylor expansion extends $g(z)=f(z)/z$ holomorphically to
$g(0)=f'(0)$. Fix $0<r<1$. On $|z|=r$ we have $|g(z)|\leq1/r$.
The maximum modulus principle on the closed radius-$r$ disk gives the
same bound inside. For a fixed $z$, let $r\uparrow1$ with $r>|z|$;
then $|g(z)|\leq1$. This proves both inequalities. Either equality
condition makes $|g|$ attain its global maximum 1 at an interior point.
CA.34 makes $g$ constant, proving the rigidity statement. $\square$

Notice the two radii: first work on a closed disk strictly inside the
domain, then let its radius approach 1. Boundary values of $f$ on the
unit circle were never assumed. This is the same smaller-disk technique
used in Taylor convergence and Cauchy estimates.

<a id="ca-52"></a>
### Example CA.52. Worked contour and spectral calculations

**Cauchy's derivative formula.** Let the positive circle have radius 2.
Since $e^z$ is entire and $1$ is inside,

$$
\int_{|z|=2}\frac{e^z}{(z-1)^3}\,dz
=\frac{2\pi i}{2!}(e^z)''\big|_{z=1}=\pi i e.
$$

The exponent 3 means derivative order 2, explaining the factorial.
A negatively oriented circle gives the negative value; traversing twice
gives twice the value. If the contour passed through 1, this formula
would not apply.

**A Laurent series depends on the annulus.** For $f(z)=1/[z(z-1)]$,

$$
f(z)=-\sum_{n=0}^\infty z^{n-1}\quad(0<|z|<1),\qquad
f(z)=\sum_{n=0}^\infty z^{-n-2}\quad(|z|>1).
$$

Both follow from geometric series, but they converge on different annuli.
On a circle of radius less than 1 the integral is $-2\pi i$, from
the coefficient of $z^{-1}$. On a circle of radius greater than 1 that
coefficient is zero and the integral is zero: the residues at 0 and 1
are $-1$ and $+1$ and cancel. The coefficient on the outer annulus is
not the residue at the isolated singularity 0; a residue there is computed
on a sufficiently small punctured disk.

The two expansions come from different factorizations:
$1/[z(z-1)]=-z^{-1}/(1-z)$ when $|z|<1$, and
$1/[z(z-1)]=z^{-2}/(1-1/z)$ when $|z|>1$.
The local residues can also be read from
$1/[z(z-1)]=-1/z+1/(z-1)$. For the outer circle both singularities
are enclosed, explaining why their opposite residues cancel.

**Why a contour integral gives a projection.** Consider
$T=\operatorname{diag}(\lambda_1,\lambda_2)$ with distinct eigenvalues.
For a positive circle enclosing $\lambda_1$ but not $\lambda_2$,

$$
\frac1{2\pi i}\int_\gamma(zI-T)^{-1}\,dz
=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$

The resulting matrix $P$ is a **projection** because $P^2=P$.
It sends $(v_1,v_2)$ to $(v_1,0)$, retaining the eigenspace associated
with the enclosed eigenvalue. The contour selects that part of the
spectrum through its winding numbers.

Indeed the inverse is diagonal with entries $(z-\lambda_j)^{-1}$,
whose integrals are $2\pi i$ times the corresponding winding numbers.
For a holomorphic scalar $h$, inserting $h(z)$ gives
$\operatorname{diag}(h(\lambda_1),0)$ on this one contour. A contour
system enclosing **both** eigenvalues gives
$h(T)=\operatorname{diag}(h(\lambda_1),h(\lambda_2))$.
The infinite-dimensional Riesz calculus replaces this elementary entrywise
calculation with the Banach-valued integral and resolvent identities;
it does not assume that an arbitrary operator has an eigenvector basis.

## Reading connections and references

| Where in Conway | Read first | What the supplement justifies |
| --- | --- | --- |
| I.§1, square-integrable analytic functions | CA.21–CA.35 | Cauchy estimates and why locally uniform limits remain holomorphic. |
| III.§8, Runge's theorem | CA.21–CA.39, CA.44 | Uniform kernel expansions, holomorphicity at infinity, identity theorem, the finite contour representation. |
| VII.§3, spectrum | CA.25, CA.30, CA.32–CA.33, CA.42–CA.43 | Power-series radius arguments, removable singularities, Banach-valued Liouville. |
| VII.§4, Riesz calculus | CA.27, CA.37–CA.43 | Rectifiable integrals, winding numbers, admissible and nested contours, vector Cauchy formulas. |
| Later spectral arguments using isolated zeros or poles | CA.31, CA.40–CA.41 | Multiplicity, Laurent expansions, residues and contour counts. |

The proofs above are written for this study edition. For an independent
course treatment of the underlying scalar Cauchy theory, see the
[MIT 18.112 lecture-note collection](https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/resources/lecture-notes/)
and [Dmitri Zaitsev's complex-analysis lecture notes](https://www.maths.tcd.ie/~zaitsev/intro-complex/ca-notes.pdf).
These are supplementary references, not substitutes for the proofs here.
