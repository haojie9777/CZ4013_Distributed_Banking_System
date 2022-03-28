import java.net.*;
import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import utils.*;
public class Server {

    public static void main(String[] args) throws IOException {
        System.out.println("Running IDamNerd Bank's Server...");
        //ask user for semantics to use: at-least-once or at-most-once
        boolean atMostOnce = true;

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

            //get ip and port of request for subscribing needs
            unmarshalledRequest.put("requestIp", request.getAddress().toString());
            unmarshalledRequest.put("requestPort",Integer.toString(request.getPort()));

            String requestId = unmarshalledRequest.get("requestId");
            if (atMostOnce && history.requestExists(requestId)){ //send cached reply to client
                    byte[] marshalledResponse = history.getReply(requestId);
                    //send response to client
                    DatagramPacket reply = new DatagramPacket(marshalledResponse, marshalledResponse.length, request.getAddress(), request.getPort());
                    aSocket.send(reply);
                }
            else {//service brand new request
                HashMap<String, String> response = handler.handleRequest(unmarshalledRequest);  //service request
                System.out.println(response);
                byte[] marshalledResponse = Marshaller.marshall(response); //marshall response
                history.addReply(requestId, marshalledResponse); //store reply in history

                //send response to client
                DatagramPacket reply = new DatagramPacket(marshalledResponse, marshalledResponse.length, request.getAddress(), request.getPort());
                aSocket.send(reply);

                //send update to all subscribers
                if (!unmarshalledRequest.get("requestType").equals("4")
                        && !unmarshalledRequest.get("requestType").equals("6")) {
                    ArrayList<Subscriber> subscribers = handler.retrieveSubscribers();
                    for (Subscriber subscriber : subscribers) {
                        byte[] marshalledUpdateMsg = Marshaller.marshallUpdateMsg(unmarshalledRequest);
                        DatagramPacket updateMsgReply = new DatagramPacket(marshalledUpdateMsg, marshalledUpdateMsg.length, subscriber.getIpAddress(), subscriber.getPort());
                        aSocket.send(updateMsgReply);
                    }
                }
            }

        }



    }
}
