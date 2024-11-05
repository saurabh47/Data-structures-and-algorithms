package pizza;

class PizzaFactory {
    public static Pizza createPizza(String pizzaType, String size) {
        switch (pizzaType) {
            case "Margherita":
                return new MargheritaPizza(size);
            case "Veggie":
                return new VeggiePizza(size);
            case "Hawaiian":
                return new HawaiianPizza(size);
            default:
                throw new IllegalArgumentException("Unknown pizza type: " + pizzaType);
        }
    }
}
