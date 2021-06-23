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
