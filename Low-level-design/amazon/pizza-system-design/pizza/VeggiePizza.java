package pizza;

class VeggiePizza extends Pizza {
    public VeggiePizza(String size) {
        super(size, 9.0);
    }

    @Override
    protected double calculateBasePrice() {
        double price = basePrice;
        price += new Topping("Cheese", 1.0).getPrice();
        price += new Topping("Bell Peppers", 0.8).getPrice();
        price += new Topping("Olives", 0.6).getPrice();
        return price;
    }
}