# FM9578A content audit — 28 October 2026

Scope: the nine supplied lecture PDFs, the suggested-exercise PDF and the Brownian-dependence supplement. This audit compares substantive concepts, formulas, numerical examples and questions, rather than treating a page count as proof of completeness. Repeated builds are consolidated. It does not claim coverage of unprovided future lectures or textbook chapters.

## Lecture checklist

| Source (physical PDF pages) | Content checked | Website destination |
|---|---|---|
| L1, 3–10 | Derivative definition and underlyings; exchange/OTC and clearing; forward/futures obligations; option rights; hedging, speculation and arbitrage | [L1](../index.html#l1) |
| L1, 11–17 | Exercise styles; four long/short payoffs and market views; four profits; break-even; financing convention; 50-strike call example and contract multiplier | L1: four positions, detailed walkthrough, position direction |
| L1, 18–24 | Stock/currency/index/futures option settlement; cycles, third-Friday/weekly conventions, LEAPS, strike spacing, class/series; position limits; corporate actions; ITM/ATM/OTM; intrinsic/time value; closing trades; bid/ask example | L1: contract checklist, lecture conventions, vocabulary |
| L2, 1–12 | Repeated L1 content retained in L1 rather than copied | [L2](../index.html#l2), cross-reference to L1 |
| L2, 13–16 | Market/model valuation; premium versus margin; initial/maintenance margin, settlement and margin calls; referenced workbook limitation | L2: valuation and margin walkthrough |
| L3, 3–10 | Notation and six price inputs; European maturity ambiguity; American exercise opportunities; frictionless/tax/borrowing assumptions | [L3](../index.html#l3): comparative statics, maturity, assumptions |
| L3, 11–17 | Call/put upper and lower bounds; dominance and arbitrage explanations; both numerical lower bounds; European parity and identical terminal portfolios | L3: bounds, upper-bound trades, parity and graph |
| L4, 3–5 | Synthetic call/put/stock; both directions of parity arbitrage | [L4](../index.html#l4): synthetic positions and walkthrough; Q2 cash flows |
| L4, 6–14 | No-dividend call non-exercise and equality; put exercise incentives; European put below intrinsic; American parity bound proofs; known-dividend bounds/parity; ex-dividend exercise timing | L4: early exercise, dividend formulas, bound proofs |
| L5, 2–18 | Strategy families, view/risk selection; principal protection; covered call and protective put | [L5](../index.html#l5) |
| L5, 19–29 | Bull-call and bear-put legs, piecewise payoffs, numerical bull spread; European box and parity derivation; butterfly; calendar/diagonal and remaining time value | L5: spreads, explicit formulas, strategy families and graph |
| L5, 30–42 | Straddle, strip, strap, strangle; asymmetric views; premium and break-even; complete 90/100/110 butterfly example | L5: movement strategies and explicit formulas; Q3; interactive payoff tool |
| L6, 2–10 | Tree interpretation; one-step replication, hedge and financing; risk-neutral expectation versus forecast; physical probability | [L6](../index.html#l6): formulas and worked replication |
| L6, 11–18 | Recombination, direct two-step probability weights, backward induction; call/put examples; 50/53/48 class question | L6: two-step tree, put/class exercise and tree graph |
| L7, 3–13 | American exercise at every node; 5.0894 put example; delta signs and dynamic rebalancing; 0.9497 root correction | [L7](../index.html#l7): exercise, delta and walkthrough |
| L7, 14–25 | Expanded variance identity; local CRR calibration; measure-change idea and SDEs; two- and five-step calibration; stock-node formula; backward-induction pseudocode | L7: volatility matching, dynamics, calibration and pseudocode |
| L7, 26–41 | Continuous yield versus cash-dividend drop; no-dividend/yield call examples; index and FX examples; foreign-interest interpretation; forward financing proof; futures growth/discounting | L7: underlying growth, cash dividends, numerical examples with intermediate node calculations |
| L7, 42–47 | Exercises 1/4 (duplicate), 2, 3 European/American, 5 FX parameters, 6 futures call/put; hedging and exercise decisions | Lecture 7 exercise answers below suggested exercises |
| L8, 2–18 | Four time/state classifications; Markov conditional law; Brownian increments, normal law, independence, variance/SD scaling | [L8](../index.html#l8): properties, notation, classification |
| L8, 19–34 | Increment simulation/sums; initial 25 example; infinitesimal notation and rough paths; drift/variance rates; exact generalized Wiener law; cash-reserve examples | L8: simulation, constant coefficients, examples, scaling and overlap graphs |
| L9, 2–24 | Repeated Wiener content; expectation and variance/covariance identities; same-path resolution figure | [L9](../index.html#l9) and L8: path resolution |
| L9, 25–32 | State/time-dependent coefficients; local conditional moments; Markov versus path dependence; mean reversion; GBM percentage/dollar units; conditioning; monthly example; deterministic limit | L9: local moments, mean reversion, GBM and monthly example |
| L9, 33–39 | Euler update and recursive algorithm; 50-path median/percentile interpretation; volatility scaling; correlated diffusions/normals; jointly updated states; return-scatter/sample-correlation interpretation | L9: Euler, correlated processes and simulation-plot explanations; Q16/Q20; interactive Brownian tool |

Title/overview/summary pages introduce or repeat the material in these rows. The physical-page inventory remains in [source-coverage.json](source-coverage.json).

## Suggested exercises: all 20 / 97 subparts

| Question | Subparts | Checked content |
|---|---|---|
| 1 | a–d | Call/put bounds, violating quote, arbitrage cash flows |
| 2 | a–d | Parity, put price, overpriced put, replication trade |
| 3 | a–e | Both payoffs, combined payoff, three profits, break-evens, profit-graph vertex and slopes |
| 4 | a–d | Exercise rights, value ordering, call early exercise and dividends |
| 5 | a–e | Payoffs, delta, riskless portfolio, price, risk-neutral verification |
| 6 | a–d | Pricing probability, expected stock, physical probability, interpretation |
| 7 | a–e | Stock tree, probability, payoffs, backward induction, direct verification |
| 8 | a–e | Put tree, probability, payoffs, valuation, interpretation |
| 9 | a–f | CRR step/factors/probability, tree, node exercise tests, root value |
| 10 | a–f | FX factors/probability/tree/payoffs/value and foreign rate |
| 11 | a–e | Wiener laws, moments, normal tail and independence |
| 12 | a–e | Drift/variance rate, reserve law, mean, SD and tail |
| 13 | a–d | Mean-reversion coefficients, drift at three states, interpretation, local moments |
| 14 | a–e | State-dependent coefficients, drift, variance rate, moments and Euler |
| 15 | a–e | GBM dollar/percentage coefficients and monthly moments |
| 16 | a–e | Recursive Euler formula, three prices, price dependence |
| 17 | a–e | Quarterly/monthly updates and moments, SD scaling, accuracy/cost |
| 18 | a–e | Means, variances, covariance, correlation and sign change |
| 19 | a–e | Normal means/variances/covariance, numerical shocks, simulation use |
| 20 | a–e | Two-stock updates, local means/SDs/covariance, numerical correlated step |

All answers have retained their subpart identifiers. Extra “Why these steps work” notes explain the method. Answers are independently worked, not official solutions.

## Brownian supplement

The covariance/correlation derivation and cases (a)–(i) are included. The notes distinguish disjoint increments, overlapping increments, dependent levels, linear Gaussian combinations, and the nonlinear square case. Zero covariance is used to infer independence only with the appropriate joint-Gaussian condition; the square case uses independence preserved under functions.

## Audit findings and limits

- Restored explicit details about short profits, market views, OTM, LEAPS terminology, initial contract pricing, maturity effects, upper-bound arbitrage trades, American-bound proofs, strategy families, box derivation, five-step calibration, forward financing, process classification, path resolution and simulation-plot interpretation.
- Expanded the existing Lecture 7 numerical examples to include terminal payoffs and intermediate continuation/exercise values. The parameters and original answers remain.
- The Markov formula, contract cycles, expanded variance identity and other items already present in later sections were checked rather than added twice.
- The text-light L9 figures on physical pages 15, 35 and 39 were rendered and visually inspected. Their interpretation is now explicit in the notes; the source's random paths are illustrative, not additional deterministic answers to reproduce.
- **Unavailable:** L2 p. 16 references `Future_Margin_Example`, which was not supplied. Its numerical rows cannot be audited. The website labels its margin illustration as independently authored.
- **Corrected source issue:** L7 p. 13 lists 0.9334, but the displayed tree gives 0.9497. CRR finite-step variance matching and frozen state-dependent moments are qualified as approximations.
- **Website versus printed sheet:** the website and Markdown hold the detailed coverage. The two-page handwritten formula sheet is a condensed reference; it cannot contain every explanation, proof, numerical tree and complete solution from 261 source pages.

Build checks verify counts, source inventory, math rendering, preserved original text/formulas during bullet formatting, responsive layout and printed-sheet bounds. They supplement the source comparison above; counts alone are not evidence of semantic completeness.
