from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=contract_address, abi=abi)

print(contract.address)
print(f"Баланс смарт-контракта: {w3.eth.get_balance(contract.address)}")
print(f"Баланс 1 accounta: {w3.eth.get_balance('0x259225E861536e2737c5e4eB50D07d9AEc724705')}")
print(f"Баланс 2 accounta: {w3.eth.get_balance('0x8878682096eB25438db616B14176a3Ea24addCB0')}")
