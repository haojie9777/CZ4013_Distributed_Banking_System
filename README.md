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

### Open Account

#### Request

| Params            | Type        |
| ----------------- | ----------- |
| Account Name      | `str`       |
| Password          | `str`       |
| Currency          | `str`       |
| Initial balance   | `int`       |

#### Response

| Params                    | Type        |
| ------------------------- | ----------- |
| Ack                       | `int`       |
| Message (Account Number)  | `str`       |

### Close Account

#### Request

| Params         | Type        |
| -------------- | ----------- |
| Account Name   | `str`       |
| Account Number | `int`       |
| Password       | `str`       |

#### Response

| Params      | Type        |
| ----------- | ----------- |
| Ack         | `int`       |
| Message     | `str`       |

### Deposit Money

#### Request

| Params         | Type        |
| -------------- | ----------- |
| Account Name   | `str`       |
| Account Number | `int`       |
| Password       | `str`       |
| Currency       | `str`       |
| Amount         | `int`       |

#### Response

| Params            | Type        |
| ----------------- | ----------- |
| Ack               | `int`       |
| Message (Balance) | `str`       |

### Withdraw Money

#### Request

| Params         | Type        |
| -------------- | ----------- |
| Account Name   | `str`       |
| Account Number | `int`       |
| Password       | `str`       |
| Currency       | `str`       |
| Amount         | `int`       |

#### Response

| Params            | Type        |
| ----------------- | ----------- |
| Ack               | `int`       |
| Message (Balance) | `str`       |

### Broadcast Account Update (TBC)

#### Request

| Params           | Type        |
| ---------------- | ----------- |
| Account Name     | `str`       |
| Account Number   | `int`       |
| Password         | `str`       |
| Monitor interval | `int`       |

#### Response

| Params      | Type        |
| ----------- | ----------- |
| Ack         | `int`       |
| Message     | `str`       |

### Transfer Money

#### Request

| Params               | Type        |
| -------------------- | ----------- |
| Account Name         | `str`       |
| Account Number       | `int`       |
| Password             | `str`       |
| Currency             | `str`       |
| Amount               | `int`       |
| Payee Account Name   | `str`       |
| Payee Account Number | `int`       |

#### Response

| Params            | Type        |
| ----------------- | ----------- |
| Ack               | 'int'       |
| Message (Balance) | 'str'       |

### Check Account Balance

#### Request

| Params         | Type        |
| -------------- | ----------- |
| Account Name   | `str`       |
| Account Number | `int`       |
| Password       | `str`       |

#### Response

| Params                    | Type        |
| ------------------------- | ----------- |
| Ack                       | `int`       |
| Message (Account Balance) | `str`       |

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
