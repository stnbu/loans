#!/usr/bin/python3

import os
import json
from brownie import Test721, accounts, config
from dotenv import load_dotenv
load_dotenv()

# starting with a vyper erc721 contract to understand testing.
def main():
    token_holder_number = 5  # It's nice to use the same number for a few things
    token_holder = accounts[token_holder_number]
    dev = accounts.add(config["wallets"]["from_key"])
    contract = Test721.deploy({"from": dev}, publish_source=False)
    ret = contract.mint(token_holder, token_holder_number)
    assert contract.ownerOf(token_holder_number) == token_holder.address
