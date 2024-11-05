package pizza;

class MargheritaPizza extends Pizza {
    public MargheritaPizza(String size) {
        super(size, 8.0);
    }

    @Override
    protected double calculateBasePrice() {
        double price = basePrice;
        price += new Topping("Cheese", 1.0).getPrice();
        price += new Topping("Tomato", 0.5).getPrice();
        return price;
    }
}
