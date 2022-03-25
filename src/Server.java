import java.net.*;
import java.io.*;
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
        Handler handler = new Handler(); //initialize handler
        History history = new History(); //initialize history of requests and replies

        while (true){
            //receive new request from a client
            request = new DatagramPacket(receivedBuffer,receivedBuffer.length );
            aSocket.receive(request); //blocked here if no request
            //unmarshall request
            HashMap<String, String> unmarshalledRequest = Marshaller.unmarshall(receivedBuffer);

            String requestId = unmarshalledRequest.get("requestId");
            if (atLeastOnce && history.requestExists(requestId)){ //check for duplicated request if using at-most-once semantics
                    byte[] marshalledResponse = history.getReply(requestId);
                    //send response to client
                    DatagramPacket reply = new DatagramPacket(marshalledResponse, marshalledResponse.length, request.getAddress(), request.getPort());
                    aSocket.send(reply);
                }
            else{
                HashMap<String, String> response = handler.handleRequest(unmarshalledRequest);  //service request
                byte[] marshalledResponse = Marshaller.marshall(response); //marshall response
                history.addReply(requestId, marshalledResponse); //store reply in history
                //send response to client
                DatagramPacket reply = new DatagramPacket(marshalledResponse, marshalledResponse.length, request.getAddress(), request.getPort());
                aSocket.send(reply);
                }

        }



    }
}
