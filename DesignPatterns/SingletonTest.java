class Singleton {
    private static final Singleton instance = new Singleton();
    private int dummyVar = 0;

   private Singleton(){}
    public static Singleton getInstance() {
	return instance;
    }
    public void performAction() {
	System.out.printf("Performing action. dummyVar is %d.\n", dummyVar);
	dummyVar += 1;
    }
}

public class SingletonTest {
    public static void main(String[] args) {
	System.out.println("Singleton Test");
	Singleton singleton = Singleton.getInstance();
	singleton.performAction();

	Singleton singleton2 = Singleton.getInstance();
	singleton2.performAction();
    }
}