import java.net.*;
import java.io.*;
import java.util.HashMap;
import utils.*;
public class Server {

    public static void main(String[] args) throws IOException {
        DatagramSocket aSocket = new DatagramSocket(6789);
        byte[] receivedBuffer = new byte[65535];

        DatagramPacket request = null;
        Handler handler = new Handler(); //initialize handler for the rest of this server session

        while (true){
            //receive new request from clients
            request = new DatagramPacket(receivedBuffer,receivedBuffer.length );
            aSocket.receive(request); //blocked here if no request
            //unmarshall request
            HashMap<String, String> unmarshalledRequest = Marshaller.unmarshall(receivedBuffer);

            //service request
            HashMap<String, String> response = handler.handleRequest(unmarshalledRequest);

            //marshall response
            byte[] marshalledResponse = Marshaller.marshall(response);


            DatagramPacket reply = new DatagramPacket(marshalledResponse, marshalledResponse.getLength(), request.getAddress(), request.getPort());
            aSocket.send(reply);
        }



    }
}
