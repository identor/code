public class Product implements Comparable<Product> {

    private String productName;
    private double productPrice;
    private double sellingPrice;
    private int quantity;
    private int productCode;

    public Product(String productName, double productPrice, double sellingPrice, int quantity, int productCode) {
        this.productName = productName;
        this.productPrice = productPrice;
        this.sellingPrice = sellingPrice;
        this.quantity = quantity;
        this.productCode = productCode;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public String getProductName() {
        return productName;
    }

    public double getProductPrice() {
        return productPrice;
    }

    public double getSellingPrice() {
        return sellingPrice;
    }

    public int getQuantity() {
        return quantity;
    }

    public int getProductCode() {
        return productCode;
    }

    public String toString() {
        String newString = "";
        for (int i = 0; i < productName.length(); i++) {
            if (productName.charAt(i) == '_') {
                newString = newString + " ";
            } else {
                newString = newString + productName.charAt(i);
            }
        }
        return newString;
    }

    @Override
    public int compareTo(Product oProduct) {
        return this.getProductName().compareTo(oProduct.getProductName());
    }

}
