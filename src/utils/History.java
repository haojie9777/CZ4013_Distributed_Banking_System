package utils;

import java.util.HashMap;

public class History {
    /**
     * store history of requests and their replies
     */

    private HashMap<String, byte[]> requestHistory = null;

    public History(){
        this.requestHistory = new HashMap<String, byte[]>(); //stores request IDs and their response by the server
    }

    public boolean requestExists(String requestId){ //return true if request already exists
        if (requestHistory.containsKey(requestId)){
            return true;
        }
        else{
            return false;
        }
    }

    public void addReply(String requestId, byte[] reply){ //store the reply for a request
        requestHistory.put(requestId, reply);
        return;
    }
    public byte[] getReply(String requestId){ //get reply stored for a request
        return requestHistory.get(requestId);
    }


}
