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

## Server Services

For now, we use Ack to return '1' for success, '0' for error, then message to return response or error messages

### Open Account (request 0)

#### Request

| Params          | Type    |
| --------------- | ------- |
| requestId       | `str`   |
| Account Name    | `str`   |
| Password        | `str`   |
| Currency        | `str`   |
| Initial balance | `float` |

#### Response

| Params                   | Type  |
| ------------------------ | ----- |
| requestId                | `str` |
| Status                   | `int` |
| Message (Account Number) | `str` |

### Close Account (request 1)

#### Request

| Params         | Type  |
| -------------- | ----- |
| requestId      | `str` |
| Account Name   | `str` |
| Account Number | `int` |
| Password       | `str` |

#### Response

| Params    | Type  |
| --------- | ----- |
| requestId | `str` |
| Status    | `int` |
| Message   | `str` |

### Deposit Money (request 2)

#### Request

| Params         | Type    |
| -------------- | ------- |
| requestId      | `str`   |
| Account Name   | `str`   |
| Account Number | `int`   |
| Password       | `str`   |
| Currency       | `str`   |
| Amount         | `float` |

#### Response

| Params            | Type  |
| ----------------- | ----- |
| requestId         | `str` |
| Status            | `int` |
| Message (Balance) | `str` |

### Withdraw Money (request 3)

#### Request

| Params         | Type    |
| -------------- | ------- |
| requestId      | `str`   |
| Account Name   | `str`   |
| Account Number | `int`   |
| Password       | `str`   |
| Currency       | `str`   |
| Amount         | `float` |

#### Response

| Params            | Type  |
| ----------------- | ----- |
| requestId         | `str` |
| Status            | `int` |
| Message (Balance) | `str` |

### Broadcast Account Update (TBC) (request 4)

#### Request

| Params           | Type  |
| ---------------- | ----- |
| Monitor interval | `int` |

#### Response

| Params    | Type  |
| --------- | ----- |
| requestId | `str` |
| Status    | `int` |
| Message   | `str` |

### Transfer Money (request 5)

#### Request

| Params               | Type    |
| -------------------- | ------- |
| requestId            | `str`   |
| Account Name         | `str`   |
| Account Number       | `int`   |
| Password             | `str`   |
| Currency             | `str`   |
| Amount               | `float` |
| Payee Account Name   | `str`   |
| Payee Account Number | `int`   |

#### Response

| Params            | Type  |
| ----------------- | ----- |
| requestId         | `str` |
| Status            | `int` |
| Message (Balance) | `str` |

### Check Account Balance (request 6)

#### Request

| Params         | Type  |
| -------------- | ----- |
| requestId      | `str` |
| Account Name   | `str` |
| Account Number | `int` |
| Password       | `str` |

#### Response

| Params                    | Type  |
| ------------------------- | ----- |
| requestId                 | `str` |
| Status                    | `int` |
| Message (Account Balance) | `str` |

## Clients

Invokes server services

## Currencies available

"usd", "sgd", "rmb"

## To Do list

### Server (Java)

server start -> create a handler -> handler class creates accountManager class

#### Server Class

- [x] Service request
- [x] Service reply
- [x] Marshalling/unmarshalling
- [x] At-least-once semantics (specify semantics as argument when starting server)
- [x] At-most-once semantics (specify semantics as argument when starting server)
- [ ] Simulate loss of request and reply
- [ ] Fault tolerance
- [x] Set currency to enum type
- [x] Auto currency convert

#### Marshall Class

#### Bank Class

- [x] Open account
- [x] Close account
- [x] Deposit
- [x] Withdraw
- [ ] callback function to notify subscribers after every service
- [ ] (Idempotent) Check account balance
- [ ] (Non-idempotent) Transfer money
- [ ] Convert Currency for transfer money

### Client (Python)

- [x] Open account
- [x] Close account
- [x] Deposit
- [x] Withdraw
- [ ] Broadcast update to subscribers
- [x] (Idempotent) Check account balance
- [ ] (Non-idempotent) Transfer money
- [x] Password to be fixed length
