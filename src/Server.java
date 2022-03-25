import java.net.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import utils.*;
public class Server {

    public static void main(String[] args) throws IOException {
        System.out.println("Running Server...");
        //ask user for semantics to use: at-least-once or at-most-once
        boolean atLeastOnce = true;

        DatagramSocket aSocket = new DatagramSocket(6789);
        byte[] receivedBuffer = new byte[65535];


        DatagramPacket request = null;
        Handler handler = new Handler(); //initialize handler for the rest of this server session

        while (true){
            //receive new request from a client
            request = new DatagramPacket(receivedBuffer,receivedBuffer.length );
            aSocket.receive(request); //blocked here if no request
            //unmarshall request
            HashMap<String, String> unmarshalledRequest = Marshaller.unmarshall(receivedBuffer);

            //check for duplicated request if using at-most-once semantics
            if (atLeastOnce){
                String requestID = unmarshalledRequest.get("requestId");

            }

            //service request
            HashMap<String, String> response = handler.handleRequest(unmarshalledRequest);
            //marshall response
            byte[] marshalledResponse = Marshaller.marshall(response);

            //send response to client
            DatagramPacket reply = new DatagramPacket(marshalledResponse, marshalledResponse.length, request.getAddress(), request.getPort());
            aSocket.send(reply);
        }



    }
}
