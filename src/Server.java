import java.net.*;
import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import utils.*;
public class Server {

    public static void main(String[] args) throws IOException {
        System.out.println("Welcome to CZ4013 Bank Server!");
        System.out.println("Please select the invocation semantics to use:");
        System.out.println("1. At-most-once Semantics");
        System.out.println("2. At-least-once semantics");

        Scanner input = new Scanner(System.in);
        String semantics = input.nextLine();

        while (!semantics.equals("1") && !semantics.equals("2")) {
            System.out.println("Please input either 1 or 2 only!");
            semantics = input.nextLine();
        }

        boolean atMostOnce = semantics.equals("1");

        System.out.println("Starting CZ4013 Bank's Server...");
        //ask user for semantics to use: at-least-once or at-most-once
        if (atMostOnce) {
            System.out.println("Server running with at-most-once semantics!");
        }
        else {
            System.out.println("Server running with at-least-once semantics");
        }

        System.out.println("---------------------------------------------------");
        System.out.println();

        float lossRate = (float) 0.5; //set loss rate for reply to client


        DatagramSocket aSocket = new DatagramSocket(6789);
        byte[] receivedBuffer = new byte[65535];


        DatagramPacket request = null;
        Handler handler = new Handler(); //initialize handler
        History history = new History(); //initialize history of requests and replies

        while (true) {
            //receive new request from a client
            request = new DatagramPacket(receivedBuffer, receivedBuffer.length);
            aSocket.receive(request); //blocked here if no request

            //unmarshall request
            HashMap<String, String> unmarshalledRequest = Marshaller.unmarshall(receivedBuffer);

            //get ip and port of request for subscribing needs
            unmarshalledRequest.put("requestIp", (request.getAddress().toString()).substring(1));
            unmarshalledRequest.put("requestPort", Integer.toString(request.getPort()));

            String requestId = unmarshalledRequest.get("requestId");
            if (atMostOnce && history.requestExists(requestId)) { //send cached reply to client
                byte[] marshalledResponse = history.getReply(requestId);
                //simulate loss of reply
                if (Math.random() >= lossRate) {
                    DatagramPacket reply = new DatagramPacket(marshalledResponse, marshalledResponse.length, request.getAddress(), request.getPort());
                    aSocket.send(reply);
                } else {
                    System.out.println("Reply to client lost!");
                }

            } else {//service brand new request
                HashMap<String, String> response = handler.handleRequest(unmarshalledRequest);  //service request
                byte[] marshalledResponse = Marshaller.marshall(response); //marshall response
                history.addReply(requestId, marshalledResponse); //store reply in history

                if (Math.random() >= lossRate) {
                    //send response to client
                    DatagramPacket reply = new DatagramPacket(marshalledResponse, marshalledResponse.length, request.getAddress(), request.getPort());
                    aSocket.send(reply);
                } else {
                    System.out.println("Reply to client lost!");
                }

                //send update to all subscribers
                if (!unmarshalledRequest.get("requestType").equals("4")
                        && !unmarshalledRequest.get("requestType").equals("6") && response.get("status").equals("1")) {
                    ArrayList<Subscriber> subscribers = handler.retrieveSubscribers();
                    for (Subscriber subscriber : subscribers) {
                        byte[] marshalledUpdateMsg = Marshaller.marshallUpdateMsg(response);
                        DatagramPacket updateMsgReply = new DatagramPacket(marshalledUpdateMsg, marshalledUpdateMsg.length, subscriber.getIpAddress(), subscriber.getPort());
                        aSocket.send(updateMsgReply);
                                System.out.println("Sent update to " + subscriber.getIpAddress() + ":" + subscriber.getPort());
                    }
                }
            }
        }
    }
}
