package utils;

import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.HashMap;

public class Marshaller {
    /**
     * Handles marshalling and unmarshalling
     */

    public static HashMap<String, String> unmarshall(byte[] data) {
        String requestRaw = new String(data, StandardCharsets.UTF_8);
        String[] requestParams =  requestRaw.split("\\|");
        System.out.println(Arrays.toString(requestParams));
        String requestType = requestParams[0];

        HashMap<String, String> request = new HashMap<String, String>();
        switch (requestType) {
            case "0":
                System.out.println("Marshalling Open Account Request");
                request.put("requestType", requestParams[0]);
                request.put("requestId", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("password", requestParams[3]);
                request.put("currency", requestParams[4]);
                request.put("initialBalance", requestParams[5]);
                System.out.println(request);

                return request;

            case "1": {
                System.out.println("Marshalling Close Account Request");
                request.put("requestType", requestParams[0]);
                request.put("requestId", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", requestParams[3]);
                request.put("password", requestParams[4]);

                return request;
            }

            case "2":
                System.out.println("Marshalling Deposit Money Request");
                request.put("requestType", requestParams[0]);
                request.put("requestId", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", requestParams[3]);
                request.put("password", requestParams[4]);
                request.put("currency", requestParams[5]);
                request.put("amount", requestParams[6]);

                return request;

            case "3":
                System.out.println("Marshalling Withdraw Money Request");
                request.put("requestType", requestParams[0]);
                request.put("requestId", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", requestParams[3]);
                request.put("password", requestParams[4]);
                request.put("currency", requestParams[5]);
                request.put("amount", requestParams[6]);

                return request;

            case "4":
                System.out.println("Marshalling Broadcast Account Update Request");
                request.put("requestType", requestParams[0]);
                request.put("requestId", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", requestParams[3]);
                request.put("password", requestParams[4]);
                request.put("monitorInterval", requestParams[5]);

                return request;

            case "5":
                System.out.println("Marshalling Transfer Money Request");
                request.put("requestType", requestParams[0]);
                request.put("requestId", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", requestParams[3]);
                request.put("password", requestParams[4]);
                request.put("currency", requestParams[5]);
                request.put("amount", requestParams[6]);
                request.put("payeeAccountName", requestParams[7]);
                request.put("payeeAccountNumber", requestParams[8]);

                return request;

            case "6":
                System.out.println("Marshalling Check Account Balance Request");
                request.put("requestType", requestParams[0]);
                request.put("requestId", requestParams[1]);
                request.put("accountName", requestParams[2]);
                request.put("accountNumber", requestParams[3]);
                request.put("password", requestParams[4]);

                return request;

            default:
                System.out.println("Invalid Request");
                return request;
        }
    }

    public static byte[] marshall(HashMap<String, String> replyParams) {
        String[] reply = { replyParams.get("requestId"), replyParams.get("status"), replyParams.get("message") };
        String joinedReply = String.join("|", reply);
        return joinedReply.getBytes();
    }

    public static byte[] marshallUpdateMsg(HashMap<String, String> replyParams) {
        String[] reply = { replyParams.get("requestId"), replyParams.get("status"), replyParams.get("updateMessage") };
        String joinedReply = String.join("|", reply);
        return joinedReply.getBytes();
    }
}
