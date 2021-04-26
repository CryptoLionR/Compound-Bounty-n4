## Alchemix DAI Loan Calculator

Thank you @flipsidecrypto for the bounty opportunity!

This github repo holds a python script and a Windows executable that calculates the time it will take to payoff a DAI loan. The script requires three inputs:
* DAI Collateral Amount (in USD)
* DAI Loan Amount (in USD)
* DAI APY (in percentage)

Output:
* Loan Mature Date

This calculator is built on the following simple equation:
![equation](https://latex.codecogs.com/gif.download?Loan%20%3D%20Collateral%20*%20APY%20*%20Years)

Simple as that! After completing a calculation, the calculator restarts and you are able to input a different combination of numbers. See below for an example output.

![example output](/outputs/eg_output.png)
