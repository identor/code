import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        System.out.println("Hello World!");
        Scanner fileScanner = new Scanner(new File("./january-input.txt"));

        int productCount = Integer.parseInt(fileScanner.nextLine());
        Product[] products = new Product[productCount];

        for (int i = 0; i < productCount; i++) {
        	// Product info format: 0 Coke_Litro 22.00 25.00 7
        	// Product Constructor: Product(String productName, double productPrice, double sellingPrice, int quantity, int productCode)
        	String[] productInfoTokens = fileScanner.nextLine().split(" ");
        	int productCode = Integer.parseInt(productInfoTokens[0]);
        	String productName = productInfoTokens[1];
        	double productPrice = Double.parseDouble(productInfoTokens[2]);
        	double productSellingPrice = Double.parseDouble(productInfoTokens[3]);
        	int productQuantity = Integer.parseInt(productInfoTokens[4]);
        	Product product = new Product(productName, productPrice, productSellingPrice, productQuantity, productCode);
        	products[i] = product;
        	System.out.println(product);
        }
        System.out.println(products);
        fileScanner.close();
    }
}

