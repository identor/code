import java.util.Scanner;
import java.util.ArrayList;

public class ProductTransactionProcessing {

    public static void main(String[] args) throws Exception {

        java.io.File file = new java.io.File("january-input.txt");
        Scanner input = new Scanner(file);

        int mPC = input.nextInt();
        double TSR = 0;
        double TPC = 0;
        double TPL = 0;

        ArrayList<Product> list = new ArrayList<Product>();

        for (int i = 0; i < mPC; i++) {
            int PC = input.nextInt();
            String PN = input.next();
            double PP = input.nextDouble();
            double SP = input.nextDouble();
            int SI = input.nextInt();
            list.add(new Product(PN, PP, SP, SI, PC));
        }

        input.close();
        System.out.println(list.get(9).toString());
        System.out.println(list);
    }
}
