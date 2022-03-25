package utils;

import java.util.HashMap;

public class Semantics {
    /**
     * Handles logic for at-least-once and at-most-once semantics
     */

    private HashMap<String, Integer> requestHistory = new HashMap<String, Integer>(); //stores list of request IDs received by the server so far

    public Semantics(){
    }

    public boolean requestNotADuplicate(String UID){ //return true if request is a duplicate
        if (requestHistory.containsKey(UID)){
            return true;
        }
        else{
            requestHistory.put(UID,1);
            return false;
        }
    }


}
