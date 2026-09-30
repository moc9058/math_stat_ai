# Background index and reading guide

This index covers the added English-language material, not the original book's
numbering. Use it alongside the [main contents](README.md) and
[learner profile](../../../LEARNER_BACKGROUND.md).

## Suggested reading route

Begin complex analysis with CA.1–CA.20 in the unified supplement; these supply
the real-analysis and topology prerequisites for the later CA results.

| Stage | Main prerequisites to refresh or learn |
| --- | --- |
| Chapter I | Metric completeness, uniform convergence, Lebesgue convergence rules, arbitrary indexed sums, and Fourier density. For the analytic-function example, read CA.21–CA.35 first. |
| Chapter II | Integral interchanges, compactness versus boundedness, strong versus norm convergence, and the initial-value and integration-by-parts facts behind Sturm–Liouville theory. |
| Chapter III | Function-space completeness, quotient infima, complex measures, Baire category, and correction-series arguments. Before Runge's theorem, read CA.21–CA.39 and CA.44. |
| Chapters IV–V | Topology and nets, seminorms, products and ultrafilters, weak topologies, compactness, cutoffs, distributions, and fixed-point prerequisites. Appendix A can be read in parallel. |
| Chapters VI–VII | Closed-range estimates, compact operators, bidual limits, and Banach-algebra series. Read the full complex-analysis supplement before the spectral and contour arguments. |
| Chapters VIII–IX | Uniform approximation, continuous functional calculus, measure changes, bounded spectral limits, and operator topologies. Use Appendix C for Radon–Nikodym and density proofs. |
| Chapter X | Domains and graph norms, absolute continuity, Cayley transforms, spectral truncation, strong differentiation, smooth approximation, and Fourier-integral limits. |
| Chapter XI | Closed-range estimates, compact perturbations, local index stability, quotient norms, and connected-component arguments. |

## Conventions and remaining foundational inputs

The added material supplies proofs of its stated lemmas and theorems. Definitions
do not require proofs. Explicitly recalled foundations include the Lebesgue
fundamental theorem for absolutely continuous functions, basic measure
construction and regularity, the elementary monotone-class argument, and the
choice principle in Zorn's lemma. Zorn's lemma is used as an axiom-equivalent
principle, not an elementary analysis theorem waiting for an omitted proof.

The source's deep results explicitly stated without proof, such as the
Eberlein–Smulian and James theorems, and its full positive Riesz-measure
construction, are not silently reclassified as proved additions. This is a
background-enriched study edition, not a claim that every external result or
every exercise in the book has now been proved. Standard linear algebra is
deliberately not retaught.

Within an inserted block, BG labels refer to added results. Links below jump to
their explicit anchors. A mathematical result may be refreshed in more than
one chapter when the later use has different hypotheses or convergence modes.

## Added results by location

### I. Hilbert Spaces

- [Definition BG-I.1. Metric language used throughout this chapter](chapter-01.md#bg-i-1)
- [Lemma BG-I.2. Closedness, completeness, and passing to limits](chapter-01.md#bg-i-2)
- [Definition BG-I.3. Pointwise, uniform, and locally uniform convergence](chapter-01.md#bg-i-3)
- [Theorem BG-I.4. Uniform-limit tools](chapter-01.md#bg-i-4)
- [Definition BG-I.5. Measure-theoretic conventions](chapter-01.md#bg-i-5)
- [Theorem BG-I.6. Three convergence rules for the Lebesgue integral](chapter-01.md#bg-i-6)
- [Lemma BG-I.7. The $L^2$ estimates and completeness omitted in Example 1.3](chapter-01.md#bg-i-7)
- [Lemma BG-I.8. Sums over an arbitrary index set](chapter-01.md#bg-i-8)
- [Definition BG-I.9. Absolute continuity and its integral representation](chapter-01.md#bg-i-9)
- [Lemma BG-I.10. The concrete Hilbert space in Example 1.8](chapter-01.md#bg-i-10)
- [Lemma BG-I.11. Completion and extension of an inner product](chapter-01.md#bg-i-11)
- [Lemma BG-I.12. The local-to-global step in Bergman completeness](chapter-01.md#bg-i-12)
- [Lemma BG-I.13. Closed spans and continuity of inner products](chapter-01.md#bg-i-13)
- [Lemma BG-I.14. Why minimizing sequences exist but minimizers need proof](chapter-01.md#bg-i-14)
- [Definition BG-I.15. Zorn's principle and the meaning of maximal](chapter-01.md#bg-i-15)
- [Lemma BG-I.16. The maximal-orthonormal-set argument](chapter-01.md#bg-i-16)
- [Lemma BG-I.17. Dense range plus an isometry gives surjectivity](chapter-01.md#bg-i-17)
- [Theorem BG-I.18. The Fourier density input, proved by averaging](chapter-01.md#bg-i-18)
- [Lemma BG-I.19. Completing the direct-sum argument](chapter-01.md#bg-i-19)

### II. Operators on Hilbert Space

- [Lemma BG-II.1. Extending an operator from a dense domain](chapter-02.md#bg-ii-1)
- [Definition BG-II.2. Essential supremum](chapter-02.md#bg-ii-2)
- [Lemma BG-II.3. Computing a multiplication-operator norm](chapter-02.md#bg-ii-3)
- [Theorem BG-II.4. The integral-interchange rule behind kernel operators](chapter-02.md#bg-ii-4)
- [Corollary BG-II.5. Square-integrable kernels and their adjoints](chapter-02.md#bg-ii-5)
- [Definition BG-II.6. Compactness versus boundedness](chapter-02.md#bg-ii-6)
- [Theorem BG-II.7. Metric compactness criteria](chapter-02.md#bg-ii-7)
- [Corollary BG-II.8. The sequential test for compact operators](chapter-02.md#bg-ii-8)
- [Lemma BG-II.9. Uniformity on a compact set](chapter-02.md#bg-ii-9)
- [Theorem BG-II.10. The initial-value theorem needed below](chapter-02.md#bg-ii-10)
- [Corollary BG-II.11. Boundary conditions and the Wronskian](chapter-02.md#bg-ii-11)
- [Lemma BG-II.12. Differentiating the Green-function formula safely](chapter-02.md#bg-ii-12)
- [Definition BG-II.13. Strong convergence versus norm convergence of operators](chapter-02.md#bg-ii-13)
- [Lemma BG-II.14. Orthogonal projection series and functional calculus](chapter-02.md#bg-ii-14)

### III. Banach Spaces

- [Definition BG-III.1. The topological vocabulary in the examples](chapter-03.md#bg-iii-1)
- [Lemma BG-III.2. Compact-set facts needed for $C_0(X)$](chapter-03.md#bg-iii-2)
- [Corollary BG-III.3. Completing the proof that $C_0(X)$ is closed](chapter-03.md#bg-iii-3)
- [Theorem BG-III.4. Hölder, Minkowski, and completeness of $L^p$](chapter-03.md#bg-iii-4)
- [Lemma BG-III.5. Completeness of the differentiable-function examples](chapter-03.md#bg-iii-5)
- [Lemma BG-III.6. Why an operator space is complete](chapter-03.md#bg-iii-6)
- [Lemma BG-III.7. Compactness identifies two topologies](chapter-03.md#bg-iii-7)
- [Lemma BG-III.8. Infima in quotient norms need not be attained](chapter-03.md#bg-iii-8)
- [Lemma BG-III.9. Summable errors and completeness](chapter-03.md#bg-iii-9)
- [Definition BG-III.10. Complex measures and total variation](chapter-03.md#bg-iii-10)
- [Lemma BG-III.11. Integration against a complex measure](chapter-03.md#bg-iii-11)
- [Lemma BG-III.12. The phase convention in duality](chapter-03.md#bg-iii-12)
- [Lemma BG-III.13. Reconstructing a complex functional from its real part](chapter-03.md#bg-iii-13)
- [Lemma BG-III.14. The chain-union step for extending functionals](chapter-03.md#bg-iii-14)
- [Lemma BG-III.15. Two approximation details for Banach limits](chapter-03.md#bg-iii-15)
- [Definition BG-III.16. Components and poles at infinity](chapter-03.md#bg-iii-16)
- [Lemma BG-III.17. Why the Cauchy transform is analytic off its support](chapter-03.md#bg-iii-17)
- [Lemma BG-III.18. The annihilator argument in Runge's theorem](chapter-03.md#bg-iii-18)
- [Lemma BG-III.19. The finite sublinear envelope in the positive-extension proof](chapter-03.md#bg-iii-19)
- [Lemma BG-III.20. Annihilators are closed; orthogonality is only an analogy](chapter-03.md#bg-iii-20)
- [Lemma BG-III.21. The natural embedding is the relevant map](chapter-03.md#bg-iii-21)
- [Definition BG-III.22. Category is a topological notion of smallness](chapter-03.md#bg-iii-22)
- [Theorem BG-III.23. Baire category theorem for complete metric spaces](chapter-03.md#bg-iii-23)
- [Lemma BG-III.24. The open-mapping proof is a controlled correction series](chapter-03.md#bg-iii-24)
- [Lemma BG-III.25. The exact sequential test for a closed graph](chapter-03.md#bg-iii-25)
- [Lemma BG-III.26. The subsequence step for multiplication operators](chapter-03.md#bg-iii-26)
- [Theorem BG-III.27. A Baire proof clarifying the quantifiers in uniform boundedness](chapter-03.md#bg-iii-27)
- [Corollary BG-III.28. Bounded pointwise convergence against finite measures](chapter-03.md#bg-iii-28)

### IV. Locally Convex Spaces

- [Definition BG-IV.1 — Topological vocabulary and finite tests](chapter-04.md#bg-iv-1)
- [Definition BG-IV.2 — Nets, convergence, and cluster points](chapter-04.md#bg-iv-2)
- [Theorem BG-IV.3 — Why nets replace sequences](chapter-04.md#bg-iv-3)
- [Lemma BG-IV.4 — Seminorm convergence and continuity estimates](chapter-04.md#bg-iv-4)
- [Definition BG-IV.5 — Pointwise, uniform, and locally uniform convergence](chapter-04.md#bg-iv-5)
- [Theorem BG-IV.6 — Uniform limits and compact-open seminorms](chapter-04.md#bg-iv-6)
- [Lemma BG-IV.7 — The countable-seminorm metric, with its missing estimates](chapter-04.md#bg-iv-7)
- [Lemma BG-IV.8 — Boundedness in a locally convex space](chapter-04.md#bg-iv-8)
- [Lemma BG-IV.9 — Compactness gives a uniform neighborhood](chapter-04.md#bg-iv-9)
- [Lemma BG-IV.10 — Compact control and contour control](chapter-04.md#bg-iv-10)
- [Definition BG-IV.11 — Test functions and local derivative control](chapter-04.md#bg-iv-11)
- [Theorem BG-IV.12 — The concrete estimate for a distribution](chapter-04.md#bg-iv-12)
- [Corollary BG-IV.13 — Functions, point masses, and derivatives](chapter-04.md#bg-iv-13)

### V. Weak Topologies

- [Lemma BG-V.1 — What changes when a topology becomes weaker](chapter-05.md#bg-v-1)
- [Lemma BG-V.2 — The finite-test principle for weak continuity](chapter-05.md#bg-v-2)
- [Lemma BG-V.3 — Annihilators remember closure](chapter-05.md#bg-v-3)
- [Theorem BG-V.4 — Weak boundedness implies norm boundedness](chapter-05.md#bg-v-4)
- [Definition BG-V.5 — Products and ultrafilters](chapter-05.md#bg-v-5)
- [Theorem BG-V.6 — Compactness and Tychonoff's theorem](chapter-05.md#bg-v-6)
- [Lemma BG-V.7 — Why the product limit in Alaoglu stays linear](chapter-05.md#bg-v-7)
- [Lemma BG-V.8 — Compactness, Hausdorffness, and minimization](chapter-05.md#bg-v-8)
- [Lemma BG-V.9 — Extending convergence from a dense set](chapter-05.md#bg-v-9)
- [Definition BG-V.10 — Separation axioms needed for continuous cutoffs](chapter-05.md#bg-v-10)
- [Theorem BG-V.11 — Urysohn cutoffs and bounded Tietze extension](chapter-05.md#bg-v-11)
- [Lemma BG-V.12 — Chains, finite intersections, and extreme points](chapter-05.md#bg-v-12)
- [Lemma BG-V.13 — Vanishing almost everywhere versus on the support](chapter-05.md#bg-v-13)
- [Lemma BG-V.14 — Sperner's finite labeling lemma](chapter-05.md#bg-v-14)
- [Theorem BG-V.15 — Brouwer's fixed-point theorem from finite approximation](chapter-05.md#bg-v-15)
- [Theorem BG-V.16 — The Baire property without a metric](chapter-05.md#bg-v-16)
- [Lemma BG-V.17 — Uniform continuity on compact groups](chapter-05.md#bg-v-17)
- [Lemma BG-V.18 — Countable stages in a transfinite construction](chapter-05.md#bg-v-18)
- [Lemma BG-V.19 — Passing from a dense set to its sequential limits](chapter-05.md#bg-v-19)

### VI. Linear Operators on a Banach Space

- [Lemma BG-VI.1 — Bounded below means closed range](chapter-06.md#bg-vi-1)
- [Lemma BG-VI.2 — Adjoint identities and their topology](chapter-06.md#bg-vi-2)
- [Lemma BG-VI.3 — Quotient estimates keep constants under control](chapter-06.md#bg-vi-3)
- [Lemma BG-VI.4 — Isometries transfer the geometry of dual balls](chapter-06.md#bg-vi-4)
- [Definition BG-VI.5 — Total boundedness and relative compactness](chapter-06.md#bg-vi-5)
- [Lemma BG-VI.6 — Uniform estimates on compact sets](chapter-06.md#bg-vi-6)
- [Lemma BG-VI.7 — Compact operators form a closed operator ideal](chapter-06.md#bg-vi-7)
- [Lemma BG-VI.8 — Pointwise bounded equicontinuous families on compact spaces](chapter-06.md#bg-vi-8)
- [Lemma BG-VI.9 — Closing an orbit preserves invariance](chapter-06.md#bg-vi-9)
- [Lemma BG-VI.10 — Canonical embeddings and bidual images](chapter-06.md#bg-vi-10)

### VII. Banach Algebras and Spectral Theory for Operators on a Banach Space

- [Lemma BG-VII.1 — Passing limits through multiplication](chapter-07.md#bg-vii-1)
- [Lemma BG-VII.2 — A quantitative Neumann-series estimate](chapter-07.md#bg-vii-2)
- [Definition BG-VII.3 — Banach-valued contour integrals](chapter-07.md#bg-vii-3)
- [Lemma BG-VII.4 — Existence, estimates, and scalarization of the integral](chapter-07.md#bg-vii-4)
- [Theorem BG-VII.5 — Weak analyticity implies norm analyticity](chapter-07.md#bg-vii-5)
- [Corollary BG-VII.6 — Nonempty spectra and the role of complex numbers](chapter-07.md#bg-vii-6)
- [Lemma BG-VII.7 — Spectral radius without an unexplained power-series boundary](chapter-07.md#bg-vii-7)
- [Lemma BG-VII.8 — Why the double contour manipulation is valid](chapter-07.md#bg-vii-8)
- [Lemma BG-VII.9 — The estimate underlying continuity of functional calculus](chapter-07.md#bg-vii-9)
- [Lemma BG-VII.10 — Analytic division at a zero](chapter-07.md#bg-vii-10)
- [Lemma BG-VII.11 — Boundary control extends polynomial limits](chapter-07.md#bg-vii-11)
- [Lemma BG-VII.12 — Laurent expansions and spectral projections](chapter-07.md#bg-vii-12)
- [Lemma BG-VII.13 — The compactness contradiction in the closed-range lemma](chapter-07.md#bg-vii-13)
- [Corollary BG-VII.14 — The solvability meaning of the Fredholm alternative](chapter-07.md#bg-vii-14)
- [Lemma BG-VII.15 — Characters are automatically bounded](chapter-07.md#bg-vii-15)
- [Lemma BG-VII.16 — Convolution estimates and approximate identities](chapter-07.md#bg-vii-16)

### VIII. C*-Algebras

- [Definition BG-VIII.1 — Uniform convergence and approximation algebras](chapter-08.md#bg-viii-1)
- [Lemma BG-VIII.2 — Uniform limits, completeness, and closed isometric images](chapter-08.md#bg-viii-2)
- [Theorem BG-VIII.3 — The complex Stone–Weierstrass theorem](chapter-08.md#bg-viii-3)
- [Lemma BG-VIII.4 — Transferring scalar inequalities through functional calculus](chapter-08.md#bg-viii-4)
- [Lemma BG-VIII.5 — Completing the quotient in a positive-form construction](chapter-08.md#bg-viii-5)

### IX. Normal Operators on Hilbert Space

- [Definition BG-IX.1 — Measurability and simple approximation](chapter-09.md#bg-ix-1)
- [Theorem BG-IX.2 — Monotone, Fatou, and dominated convergence](chapter-09.md#bg-ix-2)
- [Lemma BG-IX.3 — Bounded pointwise convergence becomes strong convergence](chapter-09.md#bg-ix-3)
- [Lemma BG-IX.4 — Changing measure in a multiplication model](chapter-09.md#bg-ix-4)
- [Lemma BG-IX.5 — Passing operator identities to limits](chapter-09.md#bg-ix-5)
- [Lemma BG-IX.6 — Why Liouville's theorem applies to operator functions](chapter-09.md#bg-ix-6)
- [Lemma BG-IX.7 — A cyclic vector on a $\sigma$-finite measure space](chapter-09.md#bg-ix-7)
- [Lemma BG-IX.8 — Replacing absolute continuity by restriction to a set](chapter-09.md#bg-ix-8)

### X. Unbounded Operators

- [Definition BG-X.1 — Equality of operators and the graph norm](chapter-10.md#bg-x-1)
- [Lemma BG-X.2 — Closedness is completeness in the graph norm](chapter-10.md#bg-x-2)
- [Definition BG-X.3 — Absolute continuity and the integral form of calculus](chapter-10.md#bg-x-3)
- [Lemma BG-X.4 — The estimates used for differential-operator domains](chapter-10.md#bg-x-4)
- [Lemma BG-X.5 — The scalar Cayley map and its exceptional point](chapter-10.md#bg-x-5)
- [Lemma BG-X.6 — Why the inverse Cayley operator is closed](chapter-10.md#bg-x-6)
- [Lemma BG-X.7 — Spectral truncation and domain-sensitive algebra](chapter-10.md#bg-x-7)
- [Lemma BG-X.8 — Differentiating a spectral exponential strongly](chapter-10.md#bg-x-8)
- [Lemma BG-X.9 — The boundary term at infinity really vanishes](chapter-10.md#bg-x-9)
- [Lemma BG-X.10 — Translation continuity and smooth approximation](chapter-10.md#bg-x-10)
- [Lemma BG-X.11 — Differentiation under the Fourier integral](chapter-10.md#bg-x-11)
- [Lemma BG-X.12 — Finishing the domain argument for Fourier diagonalization](chapter-10.md#bg-x-12)

### XI. Fredholm Theory

- [Lemma BG-XI.1 — Closed range is a quantitative lower bound](chapter-11.md#bg-xi-1)
- [Lemma BG-XI.2 — Compact operators kill weakly null bounded sequences](chapter-11.md#bg-xi-2)
- [Theorem BG-XI.3 — A local proof of stability of the finite Fredholm index](chapter-11.md#bg-xi-3)
- [Corollary BG-XI.4 — Why paths preserve index](chapter-11.md#bg-xi-4)
- [Definition BG-XI.5 — The quotient norm behind the essential spectrum](chapter-11.md#bg-xi-5)
- [Lemma BG-XI.6 — Inverting modulo compacts and its perturbation estimate](chapter-11.md#bg-xi-6)
- [Lemma BG-XI.7 — Components of open subsets of normed spaces](chapter-11.md#bg-xi-7)
- [Lemma BG-XI.8 — Paths from positive operators and Borel arguments](chapter-11.md#bg-xi-8)

### Appendix A. Preliminaries

- [Definition BG-A.1 — A compact topology refresher](appendix-a.md#bg-a-1)
- [Lemma BG-A.2 — Three compactness arguments used throughout the book](appendix-a.md#bg-a-2)
- [Lemma BG-A.3 — Product topology and the reason sequences can fail](appendix-a.md#bg-a-3)
- [Lemma BG-A.4 — Normality and Urysohn separation on compact Hausdorff spaces](appendix-a.md#bg-a-4)
- [Corollary BG-A.5 — Compactly supported cutoffs](appendix-a.md#bg-a-5)

### Appendix B. The Dual of l1

- [Lemma BG-B.1 — The duality inequality and its phase convention](appendix-b.md#bg-b-1)
- [Lemma BG-B.2 — Countable additivity from continuity at the empty set](appendix-b.md#bg-b-2)
- [Lemma BG-B.3 — Simple-function density and countable gluing](appendix-b.md#bg-b-3)

### Appendix C. The Dual of C0(X)

- [Theorem BG-C.1 — Radon–Nikodym for finite positive measures](appendix-c.md#bg-c-1)
- [Corollary BG-C.2 — The $\sigma$-finite and complex versions](appendix-c.md#bg-c-2)
- [Lemma BG-C.3 — Density of continuous functions in integral norms](appendix-c.md#bg-c-3)
- [Theorem BG-C.4 — Weak-star compactness for bounded positive measures](appendix-c.md#bg-c-4)

### Complex analysis: prerequisites and theory

- [Definition and Lemma CA.1. Complex geometry and estimates](background-complex-analysis.md#ca-1)
- [Definition and Lemma CA.2. Limits, Cauchy sequences, and completeness](background-complex-analysis.md#ca-2)
- [Definition and Lemma CA.3. Open sets, closure, and boundary](background-complex-analysis.md#ca-3)
- [Theorem CA.4. Compactness in the plane and nested compact sets](background-complex-analysis.md#ca-4)
- [Theorem CA.5. Uniform continuity and extrema on compact sets](background-complex-analysis.md#ca-5)
- [Lemma CA.6. Positive distance and compact neighborhoods](background-complex-analysis.md#ca-6)
- [Definition and Theorem CA.7. Connectedness and polygonal paths](background-complex-analysis.md#ca-7)
- [Definition and Lemma CA.8. Convexity, holes, and simple connectedness](background-complex-analysis.md#ca-8)
- [Definition and Theorem CA.9. Absolute convergence and geometric tails](background-complex-analysis.md#ca-9)
- [Definition and Theorem CA.10. Limsup and the root test](background-complex-analysis.md#ca-10)
- [Theorem CA.11. Uniform Cauchy criterion and the order of quantifiers](background-complex-analysis.md#ca-11)
- [Definition and Proposition CA.12. Total derivatives and little-o errors](background-complex-analysis.md#ca-12)
- [Lemma CA.13. The chain rule and differentiation along a path](background-complex-analysis.md#ca-13)
- [Theorem CA.14. Continuous integrals and the fundamental theorem](background-complex-analysis.md#ca-14)
- [Theorem CA.15. When limits and derivatives pass through integrals](background-complex-analysis.md#ca-15)
- [Theorem CA.16. Uniform convergence of derivatives is the missing hypothesis](background-complex-analysis.md#ca-16)
- [Lemma CA.17. Finite subdivisions subordinate to a cover](background-complex-analysis.md#ca-17)
- [Definition and Lemma CA.18. Path parameters, orientation, and bounded variation](background-complex-analysis.md#ca-18)
- [Lemma CA.19. Finite-measure estimates for uniform kernels](background-complex-analysis.md#ca-19)
- [Lemma CA.20. Area integration in polar coordinates](background-complex-analysis.md#ca-20)
- [Definition CA.21. Pointwise, uniform, and locally uniform convergence](background-complex-analysis.md#ca-21)
- [Lemma CA.22. Uniform-limit rules and the Weierstrass M-test](background-complex-analysis.md#ca-22)
- [Definition CA.23. Holomorphic functions and complex derivatives](background-complex-analysis.md#ca-23)
- [Proposition CA.24. Real derivatives and the Cauchy–Riemann equations](background-complex-analysis.md#ca-24)
- [Theorem CA.25. Power series, radius of convergence, and differentiation](background-complex-analysis.md#ca-25)
- [Definition and Lemma CA.26. Exponentials and local logarithms](background-complex-analysis.md#ca-26)
- [Definition and Lemma CA.27. Contour integrals and their norm estimate](background-complex-analysis.md#ca-27)
- [Theorem CA.28. Goursat's triangle theorem and local primitives](background-complex-analysis.md#ca-28)
- [Theorem CA.29. Cauchy's formula on a disk](background-complex-analysis.md#ca-29)
- [Theorem CA.30. Taylor expansion, Cauchy estimates, and derivatives](background-complex-analysis.md#ca-30)
- [Theorem CA.31. The identity theorem and multiplicity of zeros](background-complex-analysis.md#ca-31)
- [Theorem CA.32. Removable singularities](background-complex-analysis.md#ca-32)
- [Theorem CA.33. Liouville's theorem and the fundamental theorem of algebra](background-complex-analysis.md#ca-33)
- [Theorem CA.34. Maximum modulus principle](background-complex-analysis.md#ca-34)
- [Theorem CA.35. Locally uniform limits of holomorphic functions](background-complex-analysis.md#ca-35)
- [Definition and Lemma CA.36. Infinity, poles, and rational functions](background-complex-analysis.md#ca-36)
- [Definition and Theorem CA.37. Winding numbers](background-complex-analysis.md#ca-37)
- [Theorem CA.38. Cauchy's theorem and formula for cycles](background-complex-analysis.md#ca-38)
- [Lemma CA.39. Contours surrounding a compact set](background-complex-analysis.md#ca-39)
- [Theorem CA.40. Laurent expansions and residues](background-complex-analysis.md#ca-40)
- [Theorem CA.41. Residue and argument principles](background-complex-analysis.md#ca-41)
- [Theorem CA.42. Banach-valued Cauchy theory and Liouville's theorem](background-complex-analysis.md#ca-42)
- [Lemma CA.43. The resolvent is analytic, with a genuine local series](background-complex-analysis.md#ca-43)
- [Lemma CA.44. Differentiating Cauchy transforms under an integral](background-complex-analysis.md#ca-44)
- [Theorem CA.45. Deformation of contours and global primitives](background-complex-analysis.md#ca-45)
- [Theorem CA.46. Holomorphic logarithms and roots](background-complex-analysis.md#ca-46)
- [Theorem CA.47. Morera's theorem and holomorphic parameter integrals](background-complex-analysis.md#ca-47)
- [Theorem CA.48. Harmonic components, mean values, and the Bergman estimate](background-complex-analysis.md#ca-48)
- [Theorem CA.49. Rouché's theorem and stability of zero counts](background-complex-analysis.md#ca-49)
- [Theorem CA.50. Open mapping and the local inverse](background-complex-analysis.md#ca-50)
- [Theorem CA.51. Schwarz's lemma and the meaning of a disk estimate](background-complex-analysis.md#ca-51)
- [Example CA.52. Worked contour and spectral calculations](background-complex-analysis.md#ca-52)

Total: 216 numbered background items. See the [structural validation report](review/background-validation.json) for coverage and preservation checks.
