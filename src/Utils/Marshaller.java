package utils;

import java.util.HashMap;

public class Marshaller {
    /**
     * Handles marshalling and unmarshalling
     */

    public static HashMap<String, Object> unmarshall(byte[] data) {
        String requestParams[] = new String(data).split("|");
        String requestType = requestParams[0];

        HashMap<String, Object> request = new HashMap<String, Object>();

        switch (requestType) {
            case "0":
                System.out.println("Marshalling Open Account Request");
                request.put("requestType", requestParams[0]);
                request.put("uid", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("password", requestParams[3]);
                request.put("currency", requestParams[4]);
                request.put("initialBalance", Float.parseFloat(requestParams[5]));

                return request;

            case "1": {
                System.out.println("Marshalling Close Account Request");
                request.put("requestType", requestParams[0]);
                request.put("uid", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", requestParams[3]);
                request.put("password", requestParams[4]);

                return request;
            }

            case "2":
                System.out.println("Marshalling Deposit Money Request");
                request.put("requestType", requestParams[0]);
                request.put("uid", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", Integer.parseInt(requestParams[3]));
                request.put("password", requestParams[4]);
                request.put("currency", requestParams[5]);
                request.put("amount", Float.parseFloat(requestParams[6]));

                return request;

            case "3":
                System.out.println("Marshalling Withdraw Money Request");
                request.put("requestType", requestParams[0]);
                request.put("uid", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", Integer.parseInt(requestParams[3]));
                request.put("password", requestParams[4]);
                request.put("currency", requestParams[5]);
                request.put("amount", Float.parseFloat(requestParams[6]));

                return request;

            case "4":
                System.out.println("Marshalling Broadcast Account Update Request");
                request.put("requestType", requestParams[0]);
                request.put("uid", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", Integer.parseInt(requestParams[3]));
                request.put("password", requestParams[4]);
                request.put("monitorInterval", Integer.parseInt(requestParams[5]));

                return request;

            case "5":
                System.out.println("Marshalling Transfer Money Request");
                request.put("requestType", requestParams[0]);
                request.put("uid", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", Integer.parseInt(requestParams[3]));
                request.put("password", requestParams[4]);
                request.put("currency", requestParams[5]);
                request.put("amount", Float.parseFloat(requestParams[6]));
                request.put("payeeAccountName", requestParams[7]);
                request.put("payeeAccountNumber", Integer.parseInt(requestParams[8]));

                return request;

            case "6":
                System.out.println("Marshalling Check Account Balance Request");
                request.put("requestType", requestParams[0]);
                request.put("uid", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", Integer.parseInt(requestParams[3]));
                request.put("password", requestParams[4]);

                return request;

            default:
                System.out.println("Invalid Reuqest");
                return request;
        }
    }

    public static byte[] marshall(HashMap<String, Object> replyParams) {
        byte[] payload = new byte[0];
        return payload;
    };

}
