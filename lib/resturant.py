
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews_list = []

    def restaurant_name(self):
        return self.name
    
    def reviews(self):
        return self.reviews_list
    
    def customers(self):
        return list(set(review.customer for review in self.reviews_list))

    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews_list)
        total_reviews = len(self.reviews_list) 
        if total_reviews == 0:
            return 0
        average = total_ratings / total_reviews
        return average


class Customer:
    all_customers = []

    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name
        self.reviews_list = []
        Customer.all_customers.append(self)
    
    def given_name(self):
        return self.name
    
    def last_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.name} {self.family_name}"
    
    def restaurants(self):
        return (list(review.restaurant for review in self.reviews_list))
    
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self.reviews_list.append(new_review)
        restaurant.reviews_list.append(new_review)

    def num_reviews(self):
        return len(self.reviews_list)
    
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        else:
            return None
    
    @classmethod
    def find_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name() == given_name]

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def restaurant_rating(self, value):
         if isinstance (value, (int, float)):
            return value 
         else:
            return "Enter a valid number"
        
    def __str__(self):
        return f"{self.customer.full_name()}, Restaurant: {self.restaurant} -> {self.rating}"
# Examples
    # Creating instances of Restaurant
restaurant1 = Restaurant("Java food")
restaurant2 = Restaurant("Sarena hotel")
restaurant3 = Restaurant("Kilimanjaro palace")

# Creating instances of Customer
customer1 = Customer("Alina", "Jonte")
customer2 = Customer("Moha", "Abdi")
customer3 = Customer("Charli", "Mukoma")

# Adding reviews for restaurants by customers
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant2, 3)
customer3.add_review(restaurant1, 2)
customer3.add_review(restaurant3, 4)

# Retrieving and printing information
print(restaurant1.restaurant_name())  # Output: Java food

# Get all reviews for a restaurant
reviews_for_restaurant1 = restaurant1.reviews()
for review in reviews_for_restaurant1:
    print(review)  # Output: Alina jonte, Restaurant: Java food -> 4
    
# Get unique customers who reviewed a restaurant
customers_for_restaurant2 = restaurant2.customers()
for customer in customers_for_restaurant2:
    print(customer.full_name())  # Output: Alina jonte, MOha Abdi
    
# Get unique restaurants reviewed by a customer
restaurants_reviewed_by_customer3 = customer3.restaurants()
for restaurant in restaurants_reviewed_by_customer3:
    print(restaurant.restaurant_name())  # Output: Java food, Kilimanjaro palace

# Average star rating for a restaurant
average_rating_restaurant2 = restaurant2.average_star_rating()
print(average_rating_restaurant2)  # Output: 4.0

# Find a customer by name
found_customer = Customer.find_by_name("Moha Abdi")
print(found_customer.full_name())  # Output: Moha Abdi

# Find customers by given name
customers_named_alice = Customer.find_by_given_name("Alina")
for customer in customers_named_alice:
    print(customer.full_name())  # Output: Alina Jonte
