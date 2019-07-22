/* Consider the sequence of stock prices: [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    Write a program that takes an array denoting the daily stock prices and returns the maximum profit
    that could be made by buying and then selling one share of that stock.
    There's no need to buy it if no profit is possible.


    In the Example [310, 315, 275, 295, 260, 270, 290, 230, 255, 250] the maximum profit is 30, buy at 260 and sell at 290
*/


// There's a awesome insight here
// Note that the maximum profit that can be made in any particular day is the difference between the price in the day
// and the minimum price before this day.
// Thinking this way we just have to keep track of the minimum element that has passed and check if the difference of todays
// price is bigger than the other prices.
// This leads to a O(n) solution time complexity


const buyAndSellOnce = (A)=> {
    let minimum = A[0];
    let maxProfit = 0;
    for(let i = 1; i<A.length; i++){
        maxProfit = Math.max(maxProfit, A[i]-minimum);
        minimum = Math.min(minimum, A[i]);
    }
    return maxProfit;
}

console.log(buyAndSellOnce([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]));