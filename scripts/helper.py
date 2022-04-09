from brownie import network, MockV3Aggregator, config, accounts

forks = ["mainnet-fork", "mainnet-fork-dev"]
local_chains = ["development", "ganache-local"]


def get_account():
    if network.show_active() in local_chains or network.show_active() in forks:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"the active network is {network.show_active()}")
    print("deploying mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(8, 2000 * 10**8, {"from": get_account()})
    print("mocks deployed")