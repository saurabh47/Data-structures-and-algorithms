package pizza;

import java.util.ArrayList;
import java.util.List;
class Order {
    private List<Pizza> pizzas = new ArrayList<>();

    public void addPizza(Pizza pizza) {
        pizzas.add(pizza);
    }

    public double calculateTotal() {
        return pizzas.stream().mapToDouble(Pizza::calculatePrice).sum();
    }
}