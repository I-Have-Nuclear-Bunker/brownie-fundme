from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helper import get_account, deploy_mocks, local_chains

def deploy_fund_me():
    account = get_account()
    if network.show_active() not in local_chains:
        address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract Deployed at {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
