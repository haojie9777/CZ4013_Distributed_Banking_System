package utils;

import java.net.InetAddress;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.HashMap;

public class SubscriptionService {

    private ArrayList<Subscriber> subscribers = new ArrayList<Subscriber>();

    public SubscriptionService() {
    }

    // add new subscriber to list of subscribers
    public void addSubscriber(InetAddress ipAddress, int port, long monitorInterval) {
        Subscriber newSubscriber = new Subscriber(ipAddress, port, monitorInterval);
        this.subscribers.add(newSubscriber);
    }

    // returns all subscribed clients and removes expired clients
    public ArrayList<Subscriber> getSubscribers() {

        ArrayList<Subscriber> subscribersList = new ArrayList<Subscriber>();

        // iterate through list of subscribers and remove expired subscribers
        Iterator<Subscriber> itr = this.subscribers.iterator();
        while (itr.hasNext()) {
            Subscriber currentSubscriber = itr.next();
            LocalDateTime expirationTime = currentSubscriber.getExpireTime();

            // remove subscriber if monitor interval has expired
            if (expirationTime.isBefore(LocalDateTime.now())) {
                itr.remove();
            }

            else {
                subscribersList.add(currentSubscriber);
            }
        }
        return subscribersList;
    }

    public static String createOpenAccountMsg(HashMap<String, String> request, int newAccountNum) {
        String monitorMsg = "A new account has been created with the following details:\n"
                + "Account Name: " + request.get("accountName") + "\n"
                + "Account Number: " + Integer.toString(newAccountNum) + "\n"
                + "Currency: " + request.get("currency") + "\n"
                + "Initial Balance: " + request.get("initialBalance") + "\n";

        return monitorMsg;
    }

    public static String createCloseAccountMsg(HashMap<String, String> request) {
        String monitorMsg = "An account with the following details has been deleted:\n"
                + "Account Name: " + request.get("accountName") + "\n"
                + "Account Number: " + request.get("accountNumber") + "\n";

        return monitorMsg;
    }

    public static String createDepositMoneyMsg(HashMap<String, String> request) {
        String monitorMsg = "A deposit has been performed with the following details:\n"
                + "Account Name: " + request.get("accountName") + "\n"
                + "Account Number: " + request.get("accountNumber") + "\n"
                + "Currency: " + request.get("currency") + "\n"
                + "Amount Deposited: " + request.get("amount") + "\n";

        return monitorMsg;
    }

    public static String createWithdrawMoneyMsg(HashMap<String, String> request) {
        String monitorMsg = "A withdrawal has been performed with the following details:\n"
                + "Account Name: " + request.get("accountName") + "\n"
                + "Account Number: " + request.get("accountNumber") + "\n"
                + "Currency: " + request.get("currency") + "\n"
                + "Amount Withdrawn: " + request.get("amount") + "\n";

        return monitorMsg;
    }

    public static String createTransferMoneyMsg(HashMap<String, String> request) {
        String monitorMsg = "A deposit has been performed with the following details:\n"
                + "Account Name: " + request.get("accountName") + "\n"
                + "Account Number: " + request.get("accountNumber") + "\n"
                + "Currency: " + request.get("currency") + "\n"
                + "Amount Transferred: " + request.get("amount") + "\n"
                + "Payee Account Name: " + request.get("payeeAccountName") + "\n"
                + "Payee Account Number: " + request.get("payeeAccountNumber") + "\n";

        return monitorMsg;
    }
}
