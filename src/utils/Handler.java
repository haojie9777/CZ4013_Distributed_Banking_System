package utils;

import Bank.AccountManager;

import java.util.HashMap;

public class Handler {
    /**
     * process request from clients depending on the service type
     */
    private AccountManager accountManager = null;

    public Handler() {
        accountManager = new AccountManager(); //initialize accountManager object for this runtime

    }
    public HashMap<String,String> handleRequest(HashMap<String, String> request){
        String requestType = request.get("requestType");
        String UID = request.get("uid");
        String status = "1";
        String message = null;
        HashMap<String, String> reply = new HashMap<String, String>();
        switch (requestType){
            case "0": {
                System.out.println("Opening Account");
                String accountName = request.get("accountName");
                String password = request.get("password");
                String currency = request.get("currency");
                float initialBalance = Float.parseFloat(request.get("initialBalance"));
                int newAccountNum = accountManager.openAccount(accountName, password, currency, initialBalance);
                message = "Account successfully opened with account number of "+String.valueOf((newAccountNum));
                System.out.println("Account successfully opened ");
                break;
            }
            case "1": {
                System.out.println("Closing Account");
                String accountName = request.get("accountName");
                int accountNumber = Integer.parseInt(request.get("accountNumber"));
                String password = request.get("password");

                int statusCode = accountManager.closeAccount(accountName, accountNumber, password);
                if (statusCode == 1){ //successfully close account
                    message = "Successfully closed account with account number "+accountNumber;
                }
                else if (statusCode == -2){
                    message = "Wrong account name or password";
                    status = "0";
                }
                else{
                    message = "Account number not found";
                    status = "0";
                }
                break;
            }
            case "2": {
                System.out.println("Deposit Money");
                String accountName = request.get("accountName");
                int accountNumber = Integer.parseInt(request.get("accountNumber"));
                String password = request.get("password");
                String currency = request.get("currency");
                float amount = Float.parseFloat(request.get("Amount"));

                float newBalance = accountManager.depositAccount(accountNumber, accountName, password, currency, amount);
                if (newBalance == -1){ //account number not found
                    message = "Account number not found";
                    status = "0";
                }
                else if (newBalance == -2){
                    message = "Wrong account name or password";
                    status = "0";
                }
                else {
                    message = "New account balance = "+String.valueOf(newBalance);
                }
            }

            case "3": {
                System.out.println("Withdraw Money");
                String accountName = request.get("accountName");
                int accountNumber = Integer.parseInt(request.get("accountNumber"));
                String password = request.get("password");
                String currency = request.get("currency");
                float amount = Float.parseFloat(request.get("Amount"));

                float newBalance = accountManager.withdrawAccount(accountNumber, accountName, password, currency, amount);
                if (newBalance == -1){ //account number not found
                    message = "Account number not found";
                    status = "0";
                }
                else if (newBalance == -2){
                    message = "Wrong account name or password";
                    status = "0";
                }
                else if (newBalance == -3){
                    message = "Insufficient balance in account to withdraw";
                    status = "0";
                }
                else {
                    message = "New account balance = "+String.valueOf(newBalance);
                }
            }
            //TODO
            case "4": {

            }
        }
        reply.put("uid",UID);
        reply.put("status",status);
        reply.put("message",message);
        return reply;
    }

}
