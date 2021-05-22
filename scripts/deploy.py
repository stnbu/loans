#!/usr/bin/python3

import os
import json
from brownie import t3st, accounts, config
from dotenv import load_dotenv
load_dotenv()

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    contract = t3st.deploy({"from": dev}, publish_source=False)
    print(contract)
