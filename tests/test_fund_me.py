import pytest
from scripts.helper import get_account, local_chains
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions

def test_can_f_can_w():
    account = get_account()
    fund_me = deploy_fund_me()
    fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

def test_only_owner_can_withdraw():
    if(network.show_active() not in local_chains):
        pytest.skip("Only for local testing")
    fund_me = deploy_fund_me()
    robber_man = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": robber_man})