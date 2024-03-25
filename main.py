from web3 import Web3

# Connect to the Ethereum blockchain using an Infura node
infura_url = 'https://mainnet.infura.io/v3/41dbc99294a3418596dd7cf3228148c3'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is successful
if web3.is_connected():
    print("Connected to Ethereum blockchain!")
else:
    print("Failed to connect to the Ethereum blockchain.")

# Get the latest block
latest_block = web3.eth.get_block('latest')

print(f"Latest block number: {latest_block['number']}")

# Fetch transactions from the latest block
transactions = latest_block['transactions']

if transactions:
    for tx_hash in transactions:
        tx = web3.eth.get_transaction(tx_hash)
        print(f"Transaction hash: {tx_hash.hex()}")
        print(f"From: {tx['from']} -> To: {tx['to']}")
        print(f"Value: {web3.from_wei(tx['value'], 'ether')} ETH")
        print(f"Gas: {tx['gas']}")
        print("-------------------------------")
else:
    print("No transactions found in the latest block.")
