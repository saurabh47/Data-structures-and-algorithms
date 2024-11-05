package pizza;
import pizza.*;

public class Main {
    public static void main(String[] args) {
        // Define extra toppings
        Topping extraCheese = new Topping("Extra Cheese", 1.0);
        Topping jalapenos = new Topping("Jalapenos", 0.75);

        // Create pizzas using the factory
        Pizza pizza1 = PizzaFactory.createPizza("Margherita", "Large");
        Pizza pizza2 = PizzaFactory.createPizza("Veggie", "Medium");
        Pizza pizza3 = PizzaFactory.createPizza("Hawaiian", "Small");

        // Add extra toppings
        pizza1.addTopping(extraCheese);
        pizza2.addTopping(jalapenos);
        pizza3.addTopping(extraCheese);
        pizza3.addTopping(jalapenos);

        // Create an order and add pizzas
        Order order = new Order();
        order.addPizza(pizza1);
        order.addPizza(pizza2);
        order.addPizza(pizza3);

        // Calculate and display the total price
        double totalPrice = order.calculateTotal();
        System.out.printf("Total Order Price: $%.2f\n", totalPrice);
    }
}
