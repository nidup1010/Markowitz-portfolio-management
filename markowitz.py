# Markowitz's Portfolio Management 
# Packages
import yfinance as yf
import numpy as np
import pandas as pd

'''
Calculations:
1. Weight of each stock (start with dummy weights)
2. Expected returns using the data from yahoo finance
3. Expected return of Portfolio: sumproduct of (weight * expected return)
4. Annualised return (expected return of portfolio)
5. Reward = Annualised return - riskfree return
6. Covariance between stocks- use matrix
7. Individual risk contribuion
8. variance/sd
9. sharpe ratio
10. volatility
11. Weight optimisation
'''

class  ModernPortfolioTheory:
    def __init__(self, stocks):
        self.stocks =  stocks
        self.trading_day = 252
        self.weights = [0.33, 0.2, 0]
        self.risk_free = 0.47 

    def get_expected_returns(self):        
        #expected returns
        # return self.stocks.diff().sum(axis=0)
        return self.stocks.diff().mean(axis=0)
        # return self.stocks.diff()

    def get_portfolio_return(self):
        #portfolio_return
        return np.dot(self.get_expected_returns().to_numpy(), self.weights)

    def get_annual_return(self):
        #annual return = portfolio return * trading day, which is 252
        return self.get_portfolio_return() * self.trading_day

    def get_reward(self):
        #return reward given by annual return - riskfree
        return self.get_annual_return() - self.risk_free

    def get_covariance_matrix(self):
        #calculate covariance matrix of the stocks
        return self.stocks.diff().cov()

    def get_variance(self):
        #calculate variance
        #variance = weight * sumproduct(weight, covariance)
        return np.dot((np.dot(self.weights, self.get_covariance_matrix())), self.weights)

    def get_standard_deviation(self):
        #calculate standard deviation
        return np.sqrt(self.get_variance())

    def get_sharpe_ratio(self):
    #sharpe ratio = (portfolio_return - riskfree_return)/standard deviation 
        return (self.get_portfolio_return()-self.risk_free)/self.get_standard_deviation()
    def get_volatility(self):
    #volatility = sqrt(variance*trading dayj)
        return np.sqrt(self.get_variance()*self.trading_day)
      
#data come from yahoo finance        
# data = yf.download("SPY AAPL", start="2017-01-01", end="2018-04-30")
# data_frame = pd.DataFrame(data)
# closed_data = data_frame["Adj Close"].reset_index(drop=True)
# closed_data["riskfree"] = 0
# print(closed_data)
#
data = pd.read_csv("port.csv")
newPortfolio = ModernPortfolioTheory(data)
# print(newPortfolio.stocks)
print(newPortfolio.get_expected_returns())
print(newPortfolio.get_portfolio_return())
print(newPortfolio.get_annual_return())
print(newPortfolio.get_covariance_matrix())
print(newPortfolio.get_variance())
print(newPortfolio.get_standard_deviation())
print(newPortfolio.get_sharpe_ratio())
print(newPortfolio.get_volatility())
