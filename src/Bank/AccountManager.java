package Bank;
import java.util.HashMap;

//handles adding and deleting of accounts
public class AccountManager {
    //stores list of accounts created in this runtime
    private HashMap<Integer, Account> accountsHashMap = new HashMap<Integer, Account>();

    //increment by 10 for every account generated
    private int nextAccountNumber = 1000000100;

    //enum of currencies
    private enum Currencies {
        SGD,
        USD,
        MYR
    }

    public AccountManager() {
    }

    //open new account
    public int openAccount(String name, String password, String currencyType, float balance) {
        int newAccountNum = nextAccountNumber;
        nextAccountNumber += 100; //increment account number for the next account

        Account newAccount = new Account(newAccountNum, name, password, currencyType, balance);
        accountsHashMap.put(newAccountNum,newAccount);

        return newAccountNum;
    }
    //close existing account
    public String closeAccount(String name, int accountNumber, String password){
        Account account = accountsHashMap.get(accountNumber);
        if (account == null)
        {
            return "Error: account number does not exist";
        }
        else{
            if (name == account.getName() && password == account.getPassword()){
                accountsHashMap.remove(accountNumber);
                return "Success: account successful closed";
            }
            else{
                return "Error: Wrong name or password specified";
            }
        }

    }

    public HashMap<Integer, Account> getAccounts(){
        return accountsHashMap;
    }



}
