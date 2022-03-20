# CZ4013_Distributed_Banking_System

Banking system project for CZ4013 Distributed Systems. Banking system consist of a banking server and several client instances. 

# Getting Started

### Quick Start

Instructions go here

## Project Structure

```
project file and folder structure goes here
```

## Bank Account Details

1. Account number (int)
1. Name of account holder (var str)
1. Password (fix len str)
1. Currency (enum)
1. Balance (float)

## Server functions provided for clients

1. Open account: Provide name, password, currency, initial balance. Returns account number (generated by server)
1. Close account: Provide name, account number, password. Return ack/OKAY. Incorrect input, throw err
1. Depost/withdraw money: Provide name, account number, password, currency type, amount. Return updated balance. Incorrect input (wrong name, wrong account number, wrong password, incorrect currency, insufficient amount), throw proper error message
1. Broadcast account updates to all registered clients using callback mechanism. Account updates include all functions above. Remove client from callback list after monitor interval
1. NON_IMPOTENT: Transfer money from one account to another. Provide name, account number, password, currency type, amount, and payee's name, account number. Throw error if provided inputs are wrong, or if currency type doesn't match
1. IMPOTENT: Check account balance. Provide name, account number and password. Return account balance.

## Clients

Invokes server services

## To Do list

### Server (Java)

#### Server Class

- [ ] Service request
- [ ] Service reply
- [ ] Marshalling/unmarshalling
- [ ] At-least-once semantics (specify semantics as argument when starting server)
- [ ] At-most-once semantics (specify semantics as argument when starting server)
- [ ] Simulate loss of request and reply
- [ ] Fault tolerance

#### Bank Class

- [x] Open account
- [x] Close account
- [x] Deposit
- [x] Withdraw
- [ ] Broadcast update to subscribers
- [x] (Idempotent) Check account balance
- [ ] (Non-idempotent) Transfer money

### Client (Python)

- [ ]
- [ ]