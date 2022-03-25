package utils;

import java.net.InetAddress;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Iterator;

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
}
