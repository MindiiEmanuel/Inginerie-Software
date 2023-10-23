package singletonexample;

public class Main {
    public static void main(String[] args) {
        // Obține instanța singleton
        Example1 singleton = Example1.getInstance();

        // Utilizează instanța singleton
        singleton.showMessage();
    }
}
