package utils;

import java.net.InetAddress;
import java.time.LocalDateTime;

public class Subscriber {

    private InetAddress ipAddress;
    private int port;
    private LocalDateTime expireTime;

    public Subscriber(InetAddress ipAddress, int port, long monitorInterval) {
        this.ipAddress = ipAddress;
        this.port = port;
        this.expireTime = LocalDateTime.now().plusSeconds(monitorInterval);
    }

    public InetAddress getIpAddress() {
        return ipAddress;
    }

    public int getPort() {
        return port;
    }
}
