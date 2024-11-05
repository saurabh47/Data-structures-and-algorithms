package pizza;
import java.util.ArrayList;
import java.util.List;

abstract class Pizza {
    protected String size;
    protected double basePrice;
    protected List<Topping> toppings = new ArrayList<>();

    public Pizza(String size, double basePrice) {
        this.size = size;
        this.basePrice = basePrice;
    }

    public void addTopping(Topping topping) {
        toppings.add(topping);
    }

    protected abstract double calculateBasePrice();

    public double calculatePrice() {
        double totalPrice = calculateBasePrice();
        for (Topping topping : toppings) {
            totalPrice += topping.getPrice();
        }
        return totalPrice;
    }
}