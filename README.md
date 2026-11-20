# erdos412-sigma

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24389489.svg)](https://doi.org/10.5281/zenodo.24389489)

Code for the paper

> M. Mirzavaziri and D. Yaqubi, *Funnels, descent and mixing: on a problem of Erdős on the iterated sum of divisors*.

Erdős Problem #412 asks whether, for all m, n ≥ 2, the orbits of m and n under iteration of σ (sum of divisors) eventually meet.
The scripts below compute the (conjectural) classes of σ and of several related multiplicative maps, and run the statistical tests reported in the paper.

Pure Python 3, no dependencies except `numpy` (only for one fit). Factorisation is Miller–Rabin + Pollard rho (`orb.py`).

A class is determined by following each orbit up to a bound `B` (default 10^22 or 10^30) and merging with union–find.

## Scripts and where their output appears

| script | usage | paper |
|---|---|---|
| `orb.py` | factorisation helpers; `python3 orb.py N k` prints classes for n ≤ N with bound 10^k | Sec. 5 |
| `cls.py` | class computation for σ, unitary σ*, Dedekind ψ, completely multiplicative p→p+1 | Sec. 3, 5 |
| `growth.py` | `python3 growth.py sigma 22 1000000` — C(x) at powers of 10 | Table 1 |
| `run1.py` | largest classes and representatives | Sec. 5 |
| `more.py` | truncated σ, ψ invariant (eventual v₃), representative statistics | Sec. 3, 5 |
| `hazard.py` | `python3 hazard.py 1000000` — survival by step, representatives per dyadic block | Sec. 5 |
| `sizes.py` | class size distribution | Sec. 5 |
| `mheight.py` | distribution of merge heights, late merges | Sec. 6 |
| `model.py` | relabelling model R_y (`python3 model.py 1000 1000000`) and the uniform random map (`unif`) | Table 2 |
| `model2.py` | R_1000 with exemptions: `none`, `mers`, `smooth`; optional third argument = shift (1 or 2) | Table 2 |
| `swap.py` | Mersenne swap (five Mersenne primes exchanged with the next prime) | Table 2 |
| `mtrack.py`, `base.py` | Mersenne primes along merging paths vs. baseline | Sec. 6 |
| `late.py`, `base2.py` | late merges: value before merge divisible by a Mersenne prime, 2-adic valuations | Sec. 6 |
| `funnel_search.py` | `python3 funnel_search.py 4` — all geometric maps with S={2,3} and parameters in {0,…,3}: which have property E, and do they all have a funnel | Sec. 4 |
| `funnel_search3.py` | `python3 funnel_search3.py 150000 1` — random geometric maps with S={2,3,5} | Sec. 4 |
| `inv_collect.py`, `inv_test.py` | collect orbit points above 10^10, then test 59 candidate invariants | Sec. 7 |

Running times on one core: σ up to 10^6 about 2 minutes; each relabelling model up to 10^6 about 5 minutes.

`base.py` reads `cl6.pkl`, written by `sizes.py`. `inv_test.py` reads `inv.pkl`, written by `inv_collect.py`.

## License

MIT
