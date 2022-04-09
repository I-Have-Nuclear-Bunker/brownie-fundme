from brownie import FundMe
from scripts.helper import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    fee = fund_me.getEntranceFee()
    print(fee)
    fund_me.fund({"from": account, "value": fee})
    
def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()