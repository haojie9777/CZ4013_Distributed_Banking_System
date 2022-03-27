package Bank;
import utils.CurrencyConverter;

import java.util.HashMap;

//controller class for accounts
public class AccountManager {
    //stores list of accounts created in this runtime
    private HashMap<Integer, Account> accountsHashMap = new HashMap<Integer, Account>();

    //increment by 10 for every account generated
    private int nextAccountNumber = 1000000100;

    public AccountManager() {
    }

    //open new account
    public int openAccount(String name, String password, Account.Currency currency, float balance) {
        int newAccountNum = nextAccountNumber;
        nextAccountNumber += 100; //increment account number for the next account

        Account newAccount = new Account(newAccountNum, name, password, currency, balance);
        accountsHashMap.put(newAccountNum,newAccount);

        return newAccountNum;
    }
    //close existing account
    public int closeAccount(String name, int accountNumber, String password){
        Account account = accountsHashMap.get(accountNumber);
        if (account == null)
        {
            return -1;
        }
        else{
            if (name.equals(account.getName()) && password.equals(account.getPassword())){
                accountsHashMap.remove(accountNumber);
                return 1;
            }
            else{
                return -2;
            }
        }

    }

    public HashMap<Integer, Account> getAccounts(){
        return accountsHashMap;
    }

    public float depositAccount(int accountNumber, String name, String password, Account.Currency requestCurrency, float amount){
        Account account = accountsHashMap.get(accountNumber);
        if (account == null){
            return -1;
        }
        else{
            if (name.equals(account.getName()) && password.equals(account.getPassword())){
                float convertedAmount = CurrencyConverter.convertCurrency(amount, requestCurrency, account.getCurrencyType());
                account.setBalance(account.getBalance() + convertedAmount);
                accountsHashMap.put(accountNumber, account);
                return account.getBalance();
            }
            else{
                return -2;
            }
        }
    }
    public float withdrawAccount(int accountNumber,String name ,String password, Account.Currency requestCurrency, float amount){
        Account account = accountsHashMap.get(accountNumber);
        if (account == null){
            return -1;
        }
        else{
            if (name.equals(account.getName()) && password.equals(account.getPassword())){
                float convertedAmount = CurrencyConverter.convertCurrency(amount, requestCurrency, account.getCurrencyType());
                float newBalance = account.getBalance() - convertedAmount;
                if (newBalance >= 0){
                    account.setBalance(account.getBalance() - amount);
                    accountsHashMap.put(accountNumber, account);
                    return account.getBalance();
                }
                else{
                    return -3;
                }
            }
            else{
                return -2;
            }
        }
    }


    public float getAccountBalance(int accountNumber, String name, String password){
        Account account = accountsHashMap.get(accountNumber);
        if (account == null){
            return -1;
        }
        else{
            if (name.equals(account.getName()) && password.equals(account.getPassword())){
                return account.getBalance();
            }
            else{
                return -2;
            }
        }

    }


}
