package pizza;

class HawaiianPizza extends Pizza {
    public HawaiianPizza(String size) {
        super(size, 10.0);
    }

    @Override
    protected double calculateBasePrice() {
        double price = basePrice;
        price += new Topping("Cheese", 1.0).getPrice();
        price += new Topping("Ham", 1.5).getPrice();
        price += new Topping("Pineapple", 1.2).getPrice();
        return price;
    }
}
