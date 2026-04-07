# 121. Best Time to Buy and Sell Stock - Editorial

### Intuition

This problem introduces us to the *Sliding Window* technique.

What is the sliding window technique? As its name implies, the algorithm maintains a range, or a *window* over a list of elements, that gradually slides in a certain direction.
Note that the size of the window is not fixed and can change throughout the execution of the algorithm.

In the case of this question, the window refers to the *[holding period](https://www.investopedia.com/terms/h/holdingperiod.asp)*, or the time between buying and selling the stock.
The lower bound of the window would be the day that we buy the stock, and the upper bound the current day that we are at.

As the days go by, we gradually shift and increasing the size of the window, keeping track of the maximum profit that we have encountered thus far.

When the upper bound of the window reaches the last day in our `prices` array, the algorithm has completed and we can return the maximum profit recorded.
  
### Solution

As mentioned earlier, we implement the mechanism of the sliding window by keeping track of its lower and upper boundaries.
We can use two independent variables, `buy` and `sell` to do so.

When and how exactly do we move our sliding window?

The idea is that we are always moving the upper bound of the sizing window.
Every time we move the upper bound, we calculate the difference between the price at the upper bound (`sell`) and the price at the lower bound (`buy`).

If the difference is greater than the current maximum profit recorded, we update it.

If the price at the upper bound happens to be lower than the price at the lower bound, we reset the lower bound to be at the position of the upper bound.
We do this because we want to try to minimise the price at the lower bound of the sliding window, which makes sense as buying a stock at a lower price will always reap higher profits.

First, we initialise our result variable and the lower bound variable `buy`.
Note that since the input array minimally contains a single day, we initialise the buying price to be the price on the first day of the input array.
```py
res = 0
buy = prices[0]
```
Next, we initialise a loop to increment our upper bound variable `sell`.
```py
for sell in prices:
```
For every selling price we encounter, the first thing we do is to check if the current selling price is lower than our lowest buying price.
If so, we update the lowest buying price as the current selling price.
```py
  buy = min(buy, sell)
```
Next, we record the difference between the current selling price and the lowest buying price.
If the difference is greater than our maximum profit recorded thus far, we update it.
```py
  res = max(res, sell - buy)
```
Finally, we return the result variable `res` after the loop has completed.
```py
return res
```

### Complexity Analysis

Since the solution involves looping through the given array, our time complexity is linear.

Since we are only using two additional variables `buy` and `res`, our space complexity is linear.
