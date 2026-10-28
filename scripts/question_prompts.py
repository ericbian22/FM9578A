"""Concise, source-aligned prompts paired with every worked answer."""
PROMPTS=[
['Find the European call’s upper and lower no-arbitrage bounds.','Find the European put’s upper and lower no-arbitrage bounds.','Does a call quote of $4.50 violate a bound?','Construct the arbitrage strategy and explain its cash flows.'],
['State put–call parity for these European options.','Calculate the theoretical put price.','Is the market put price of $9 an arbitrage opportunity?','Specify the arbitrage portfolio and its initial and terminal cash flows.'],
['Write the call payoff and the put payoff separately.','Write the combined payoff as a function of terminal stock price.','Find profit or loss at terminal prices 60, 75 and 95.','Find both break-even stock prices.','Sketch the combined profit diagram: give its vertex, slopes and zero crossings.'],
['Compare European and American exercise rights.','Can the American call be worth less than the European call?','Why is early exercise generally not optimal without dividends?','How can dividends change the early-exercise decision?'],
['Calculate the call payoff in each state.','Calculate the hedge ratio Δ.','Construct a riskless stock–option portfolio and check both states.','Use no arbitrage to calculate the call price today.','Calculate the risk-neutral up probability and verify the price.'],
['Calculate the risk-neutral up probability.','Verify that risk-neutral expected terminal stock price equals the risk-free-grown spot price.','Calculate the physical up probability using annual expected return 12%.','Explain why the physical and pricing probabilities differ.'],
['Construct the two-step stock-price tree.','Calculate the risk-neutral up probability.','Calculate each terminal call payoff.','Use backward induction to find the call price today.','Verify the value using the direct two-step formula.'],
['Construct the two-step stock-price tree.','Calculate the risk-neutral up probability.','Calculate each terminal put payoff.','Use backward induction to calculate the put price.','Explain the financial meaning of risk-neutral valuation.'],
['Calculate the time step.','Calculate the CRR up and down factors.','Calculate the risk-neutral up probability.','Construct the stock tree and terminal put payoffs.','Compare exercise and continuation at each intermediate node.','Find the American put price and identify optimal early-exercise nodes.'],
['Calculate the CRR up and down factors.','Calculate the currency option’s risk-neutral up probability.','Construct the exchange-rate tree.','Calculate each terminal call payoff.','Calculate the call value today, discounting domestically.','Explain the role of the foreign risk-free rate.'],
['State the distribution of W₂.','State the distribution of W₅−W₂.','Calculate the mean, variance and SD of W₄.','Calculate P(W₁ > 1.5), using the standard normal CDF.','Why are increments over non-overlapping intervals independent?'],
['Identify the drift rate and variance rate.','Find the distribution of the reserve after one year.','Find the expected reserve after six months.','Find its SD after two years.','Find the probability the one-year reserve is below $25 million.'],
['Identify the drift and diffusion coefficients.','Calculate the drift at X = 40, 50 and 65.','Explain the economic meaning of mean reversion.','At X = 40 and Δt = 0.1, approximate the conditional mean and variance of the change.'],
['Identify the functions a(X,t) and b(X,t).','Calculate the instantaneous drift at X = 80.','Calculate the instantaneous variance rate at X = 80.','For Δt = 1/12, approximate the conditional mean and variance of the change.','Write the one-step Euler update using a standard normal shock.'],
['Identify the stock-price drift and diffusion coefficients.','Write the SDE for proportional price change.','Approximate the expected one-month proportional change.','Approximate the SD of one-month proportional change.','Approximate the expected dollar change and its SD over one month.'],
['Write the Euler update formula.','Calculate the price after month one using shock 0.50.','Calculate the price after month two using shock −1.20.','Calculate the price after month three using shock 0.80.','Why are the prices dependent even though the shocks are independent?'],
['Write the quarterly Euler update.','Write the monthly Euler update.','Calculate local conditional dollar means and variances for both step sizes.','How does the SD of a Wiener increment change when the step is divided by four?','Why use smaller steps in Euler simulation, and what is the cost?'],
['Calculate the two conditional expected changes over a quarter-year.','Calculate the two conditional variances.','Calculate the covariance of the two changes.','Calculate the correlation of the two changes.','What changes if correlation becomes −0.65?'],
['Show that both generated shocks have mean zero.','Show that both shocks have variance one.','Derive their covariance.','Calculate both shocks for ρ = −0.4, U = 0.6, V = −1.1.','Explain how to use these shocks in correlated-stock simulation.'],
['Write the monthly Euler update for each stock.','Calculate the local/Euler expected one-month dollar changes.','Calculate the local/Euler SDs of those changes.','Calculate the local/Euler covariance of the dollar changes.','For U = 0.8 and V = −0.5, construct the shocks and calculate both updated prices.']
]

def attach_prompts(exercises,extra):
    assert len(exercises)==len(PROMPTS)==20
    for exercise,prompts in zip(exercises,PROMPTS):
        assert len(exercise['answers'])==len(prompts),exercise['number']
        for answer,prompt in zip(exercise['answers'],prompts):
            answer['prompt']=prompt
    for item in extra:
        label=item['label']
        item['question']={
            '1 / 4':'Find the CRR factors, stock tree, call payoffs, price and initial delta. How many shares hedge 1,000 short option units?',
            '2':'Construct the two-step stock tree and price the six-month European call.',
            '3 European':'Price the six-month European put; compare with the American version below.',
            '3 American':'Price the six-month American put and identify any optimal early-exercise nodes.',
            '6 call':'Price the nine-month American call on the futures contract using three steps.',
            '6 put':'Price the nine-month American put on the futures contract using three steps.'
        }[label]
