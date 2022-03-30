package utils;

import Bank.Account;

public class CurrencyConverter {

    private static float usdToSgd = 1.36f;
    private static float usdToRmb = 6.37f;
    private static float sgdToUsd = 0.74f;
    private static float sgdToRmb = 4.69f;
    private static float rmbToUsd = 0.16f;
    private static float rmbToSgd = 0.21f;

    // convert requestCurrency to accountCurrency
    public static float convertCurrency(float amount, Account.Currency requestCurrency, Account.Currency accountCurrency) {
        if (requestCurrency == accountCurrency) {
            return amount;
        }

        else if (requestCurrency == Account.Currency.USD) {
            if (accountCurrency == Account.Currency.SGD) {
                return amount * usdToSgd;
            } else {
                return amount * usdToRmb;
            }
        }

        else if (requestCurrency == Account.Currency.SGD) {
            if (accountCurrency == Account.Currency.USD) {
                    return amount * sgdToUsd;
                }
                else {
                    return amount * sgdToRmb;
                }
        }

        else { // request currency is in rmb
            if (accountCurrency == Account.Currency.USD) {
                return amount * rmbToUsd;
            }
            else {
                return amount * rmbToSgd;
            }
        }
    }
}
