package singletonexample;

public class Example1 {
    // Variabilă statică care deține singura instanță a clasei
    private static Example1 uniqueInstance;

    // Constructor privat pentru a preveni instanțierea din alte clase
    private Example1() {}

    // Metodă statică pentru a obține instanța unică a clasei
    public static Example1 getInstance() {
        if (uniqueInstance == null) {
            uniqueInstance = new Example1();
        }
        return uniqueInstance;
    }

    // O metodă
    public void showMessage() {
        System.out.println("Hello from Singleton!");
    }
}