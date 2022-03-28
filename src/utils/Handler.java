package utils;

import Bank.Account;
import Bank.AccountManager;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.HashMap;

public class Handler {
    /**
     * process request from clients depending on the service type
     */
    private AccountManager accountManager = null;
    private SubscriptionService subscriptionService = null;

    public Handler() {
        accountManager = new AccountManager(); //initialize accountManager object for this runtime
        subscriptionService = new SubscriptionService();

    }

    public HashMap<String, String> handleRequest(HashMap<String, String> request) throws UnknownHostException {
        String requestType = request.get("requestType");
        String requestId = request.get("requestId");
        String status = "1";
        String message = null;
        HashMap<String, String> reply = new HashMap<String, String>();
        switch (requestType) {
            case "0": {
                System.out.println("Opening Account");
                System.out.println();
                String accountName = request.get("accountName");
                String password = request.get("password");
                Account.Currency currency = Account.Currency.valueOf(request.get("currency"));
                float initialBalance = Float.parseFloat(request.get("initialBalance"));
                int newAccountNum = accountManager.openAccount(accountName, password, currency, initialBalance);
                message = String.valueOf(newAccountNum);
                System.out.println("Account successfully opened ");
                System.out.println();
                reply.put("updateMessage", SubscriptionService.createOpenAccountMsg(request, String.valueOf(newAccountNum)));
                break;
            }
            case "1": {
                System.out.println("Closing Account");
                System.out.println();
                String accountName = request.get("accountName");
                int accountNumber = Integer.parseInt(request.get("accountNumber"));
                String password = request.get("password");

                int statusCode = accountManager.closeAccount(accountName, accountNumber, password);
                if (statusCode == 1) { //successfully close account
                    message = String.valueOf(accountNumber);
                    reply.put("updateMessage", SubscriptionService.createCloseAccountMsg(request));
                } else if (statusCode == -2) {
                    message = "Wrong account name or password";
                    status = "0";
                } else {
                    message = "Account number not found";
                    status = "0";
                }
                break;
            }
            case "2": {
                System.out.println("Deposit Money");
                System.out.println();
                String accountName = request.get("accountName");
                int accountNumber = Integer.parseInt(request.get("accountNumber"));
                String password = request.get("password");
                Account.Currency currency = Account.Currency.valueOf(request.get("currency"));
                float amount = Float.parseFloat(request.get("amount"));

                float newBalance = accountManager.depositAccount(accountNumber, accountName, password, currency, amount);
                if (newBalance == -1) { //account number not found
                    message = "Account number not found";
                    status = "0";
                } else if (newBalance == -2) {
                    message = "Wrong account name or password";
                    status = "0";
                } else {
                    message = String.valueOf(newBalance);
                    reply.put("updateMessage", SubscriptionService.createDepositMoneyMsg(request));
                }
                break;
            }

            case "3": {
                System.out.println("Withdrawing Money");
                System.out.println();
                String accountName = request.get("accountName");
                int accountNumber = Integer.parseInt(request.get("accountNumber"));
                String password = request.get("password");
                Account.Currency currency = Account.Currency.valueOf(request.get("currency"));
                float amount = Float.parseFloat(request.get("amount"));

                float newBalance = accountManager.withdrawAccount(accountNumber, accountName, password, currency, amount);
                if (newBalance == -1) { //account number not found
                    message = "Account number not found";
                    status = "0";
                } else if (newBalance == -2) {
                    message = "Wrong account name or password";
                    status = "0";
                } else if (newBalance == -3) {
                    message = "Insufficient balance in account to withdraw";
                    status = "0";
                } else {
                    message = String.valueOf(newBalance);
                    reply.put("updateMessage", SubscriptionService.createWithdrawMoneyMsg(request));
                }
                break;
            }

            case "4": {
                System.out.println("Subscribing to monitor updates to the server");
                System.out.println();
                InetAddress requestIp = InetAddress.getByName(request.get("requestIp"));
                long monitorInterval = Long.valueOf(request.get("monitorInterval"));
                int requestPort = Integer.valueOf(request.get("requestPort"));
                subscriptionService.addSubscriber(requestIp, requestPort, monitorInterval);
                break;
            }

            case "5": {
                System.out.println("Transferring money from one account to another");
                System.out.println();
                String accountName = request.get("accountName");
                int accountNumber = Integer.parseInt(request.get("accountNumber"));
                String password = request.get("password");
                Account.Currency currency = Account.Currency.valueOf(request.get("currency"));
                float amount = Float.parseFloat(request.get("amount"));
                String payeeAccountName = request.get("payeeAccountName");
                int payeeAccountNumber = Integer.parseInt(request.get("payeeAccountNumber"));
                float newBalance = accountManager.transferMoney(accountNumber, accountName, password, currency, amount,
                        payeeAccountName, payeeAccountNumber);
                if (newBalance == -1) { //account number not found
                    message = "Account number not found for either payer and/or payee";
                    status = "0";
                } else if (newBalance == -2) {
                    message = "Wrong account name or password";
                    status = "0";
                } else if (newBalance == -3) {
                    message = "Insufficient balance in account to transfer";
                    status = "0";
                } else {
                    message = String.valueOf(newBalance);
                    reply.put("updateMessage", SubscriptionService.createTransferMoneyMsg(request));
                }
                break;
            }
            case "6": {
                System.out.println("Checking account balance");
                System.out.println();
                String accountName = request.get("accountName");
                int accountNumber = Integer.parseInt(request.get("accountNumber"));
                String password = request.get("password");
                float balance = accountManager.getAccountBalance(accountNumber, accountName, password);
                if (balance == -1) {
                    message = "Account number not found";
                    status = "0";
                } else if (balance == -2) {
                    message = "Wrong account name or password";
                    status = "0";
                } else {
                    message = String.valueOf(balance);
                }
                break;
            }
        }
        reply.put("requestId", requestId);
        reply.put("status", status);
        reply.put("message", message);
        return reply;
    }

    public ArrayList<Subscriber> retrieveSubscribers() {
        return this.subscriptionService.getSubscribers();
    }
}
