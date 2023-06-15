from brownie import TransparentUpgradeableProxyWrapper, ProxyAdminWrapper, Box, Contract
from scripts.utils import get_account


def deploy_box():
    account = get_account()
    print("Deploying Box...")
    box = Box.deploy({"from": account})
    proxy_admin = ProxyAdminWrapper.deploy({"from": account})

    proxy = TransparentUpgradeableProxyWrapper.deploy(
        box.address,
        proxy_admin.address,
        b"",
        {"from": account},
    )

    print("Proxy Admin: ", proxy_admin.address)
    print("Proxy: ", proxy.address)
    print("Box: ", box.address)

    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    print("Initial Box Value: ", proxy_box.retrieve())


def main():
    deploy_box()

'''
Just to be sure
Proxy Admin:  0x4876C81Ea50ec8A1FB300150b3cb7Fd2f81D4586
Proxy:  0x5f283445AcAaB55e61F119D07C9B6708200c3087
Box:  0x95024Ac725D712a1bcA88c4b23ad8799c9494977
'''