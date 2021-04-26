# Alchemix DAI Loan Calculator

Thank you @flipsidecrypto for the bounty opportunity! 

Put together by @ryanl and @MonetCapital.

### Intro
In this github article, we wrote a python script that calculates the maturity date of a DAI loan. This calculator can take in **ANY** scenario as it has no limits and is based solely on one equation.

### The Calculator
*to run the calculator, you will need python installed*

This github repo holds a python script and a Windows executable that calculates the time it will take to payoff a DAI loan. The script requires three inputs:
* DAI Collateral Amount (in USD)
* DAI Loan Amount (in USD)
* DAI APY (in percentage)

Output:
* Loan Mature Date

This calculator is built on the following simple equation: 

*loan = collateral * APY * time_inYears* 

Simple as that! After completing a calculation, the calculator restarts and you are able to input a different combination of numbers. See below for an example output.

![example output](/outputs/eg_output.png)

Try it out yourself!
