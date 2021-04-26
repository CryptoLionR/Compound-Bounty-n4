#calculator for loan maturity

#imports
from datetime import datetime,timedelta

def loop():
    #get inputs
    currentdate = datetime.now()
    print('\n*********DAI Loan Calculator*********'.format(currentdate.strftime('%b %d, %Y')))
    collateral = float(input('Enter your initial collateral amount (in USD):'))
    loan = float(input('Enter the amount you would like to loan (in USD & max loan is 50% of collateral):'))
    apy = float(input('Enter the APY in percentage (e.g. 30):'))

    # Based on this equation
    # loan = collateral * apy * time

    time = loan / (collateral * apy/100) # time in years
    time = int(time*365) # days

    currentdate = datetime.now()
    print("Today's date: {}".format(currentdate.strftime('%b %d, %Y')))
    mature_date = currentdate+timedelta(time)
    print("Mature Date: {}".format(mature_date.strftime('%b %d, %Y')))

while(1):
    loop()