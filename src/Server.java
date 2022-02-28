import Bank.*;
import java.net.*;
import java.io.*;
import java.util.HashMap;

public class Server {

    public static void main(String[] args) throws IOException {
        DatagramSocket aSocket = new DatagramSocket(1234);
        byte[] receivedBuffer = new byte[65535];

        DatagramPacket request = null;
        while (true){
            //receive new request from clients
            request = new DatagramPacket(receivedBuffer,receivedBuffer.length );
            aSocket.receive(request); //blocked here if no request

            //handle request
            DatagramPacket reply = new DatagramPacket(request.getData(), request.getLength(), request.getAddress(), request.getPort());
            aSocket.send(reply);
        }



        //        AccountManager accountManager = new AccountManager();
//        int id = accountManager.openAccount("Marcus", "iamnerd", "SGD", 7.00F);
//        System.out.println(id);
//        HashMap<Integer, Account> accountList = accountManager.getAccounts();
//
//        for (Account a : accountList.values()){
//            System.out.println(a.toString());


    }
}
