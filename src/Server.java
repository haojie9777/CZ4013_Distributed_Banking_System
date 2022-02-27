import Bank.*;

import java.util.HashMap;

public class Server {

    public static void main(String[] args) {
        AccountManager accountManager = new AccountManager();
        int id = accountManager.openAccount("Marcus", "iamnerd", "SGD", 7.00F);
        System.out.println(id);
        HashMap<Integer, Account> accountList = accountManager.getAccounts();

        for (Account a : accountList.values()){
            System.out.println(a.toString());
        }



    }
}
