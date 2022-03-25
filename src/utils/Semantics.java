package utils;

import java.util.HashMap;

public class Semantics {
    /**
     * Handles logic for at-least-once and at-most-once semantics
     */

    private HashMap<String, byte[]> requestHistory = new HashMap<String, byte[]>(); //stores request IDs and their response by the server

    public Semantics(){
    }

    public boolean requestIsDuplicate(String requestId){ //return true if request is a duplicate
        if (requestHistory.containsKey(requestId)){
            return true;
        }
        else{
            return false;
        }
    }

    public void addReply(String requestId, byte[] reply){ //store the reply for a request
        return;

    }


}
