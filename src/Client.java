import java.net.*;
import java.io.*;


public class Client {
    public static void main(String[] args) throws IOException {
        DatagramSocket aSocket = null;
        try{
            aSocket = new DatagramSocket();
            byte[] m = "Hello World".getBytes();
            InetAddress aHost = InetAddress.getByName("localhost"); //ip of server
            int serverPort = 6789;
            DatagramPacket request = new DatagramPacket(m, m.length, aHost, serverPort);
            aSocket.send(request);
            byte[] buffer = new byte[1000];
            DatagramPacket reply = new DatagramPacket(buffer, buffer.length);
            aSocket.receive(reply);
            System.out.println("Reply:" + new String(reply.getData()));
        }
        finally{
            if (aSocket != null) aSocket.close();

        }



    }




}
