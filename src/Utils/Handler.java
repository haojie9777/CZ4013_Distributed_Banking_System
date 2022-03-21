package Utils;

import java.net.DatagramPacket;
import java.net.InetAddress;

public class Handler {
    /**
     * Handles receiving request from client and send response to client(s)
     */


    /**
     * Unmarshalls request from a client, process the request, then marshall the response
     * @param packet
     */
    private void handleRequest(DatagramPacket packet){
        byte[] data = packet.getData(); //retrieve data from packet
        InetAddress client_addr = packet.getAddress();
        int client_port = packet.getPort();
        Message request = Marshaller.unmarshall(data); //unmarshall a request

        //process request here using bank's AccountManager

        //marshall a response to send to client
    }

}
