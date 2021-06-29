# MPC

Crypto currency security == Private key security

## Private key Security 

Single Signature 

- One approver, one key
- Used for most transactions today
- Easy, but lowest level of security

MultiSig

- Multiple approvers, multiple keys
- Dramatically increased security
- Multiple undesired attributes

ThresholdSig

- Multiple approvers, one distributed key
- Highest level of security
- All upsides of MultiSig, w/o the downsides

## Threshold signatures using MPC

Locally generate one keyh share on each approver's device
- shares naver recombined and never in the clear

At least m of n shares must be available to sign
- m parties must approve a transaction

Generate a single signature (ECDSA)
- Fast, asynchronous approvals 


# [Introduction to MPC](https://static1.squarespace.com/static/586cf12903596e5605548ae1/t/5d2fae4c0321c10001173af7/1563405901591/An+Introduction+to+MPC+and+Threshold+Cryptography.pdf)

> MPC eliminates the potential that one party becomes corrupted and misuses the key. It also eliminates the dependency on specialized secure hardware appliances, and assures accurate and secure cryptographic operations even with widely distributed, potentially untrusted devices or clouds, without any special forms of physical security.


> But what if the use case is for an enterprise wallet, where customers issue payments to a published account address? For cryptocurrencies like Bitcoin, generating a new private key will result in a new address which will have to be communicated to all customers seeking to make payments to the current account. For many businesses, changing a published address is undesirable. Fortunately, MPC introduces an attractive alternative.


> Sharding still has the problem of centrally creating and typically storing an entire key on one or more appliances, such as HSMs. Additionally, sharding requires all of the key shards to be recombined into a whole key before cryptographic operations can be executed.  (....)   One of multiple fundamental differences between MPC and sharding is the fact that with MPC an entire key does not have to be created on any device at any time, and the shares are not required to be recombined to create a whole key at any time.
