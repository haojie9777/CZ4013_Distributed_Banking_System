package Bank;

public class Account {
    private String accNum;
    private String name; //var length
    private String password; //fixed length of 10 chars
    private String currencyType;
    private float balance;

    public Account(String name, String password, String currencyType, float balance) {
        this.name = name;
        this.password = password;
        this.currencyType = currencyType;
        this.balance = balance;
    }

    //getters and setters
    public String getAccNum() {
        return accNum;
    }

    public void setAccNum(String accNum) {
        this.accNum = accNum;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getCurrencyType() {
        return currencyType;
    }

    public void setCurrencyType(String currencyType) {
        this.currencyType = currencyType;
    }

    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }

    @Override
    public String toString() {
        return "Account{" +
                "accNum='" + accNum + '\'' +
                ", name='" + name + '\'' +
                ", password='" + password + '\'' +
                ", currencyType='" + currencyType + '\'' +
                ", balance=" + balance +
                '}';
    }








}
