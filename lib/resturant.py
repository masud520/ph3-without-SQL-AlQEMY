
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

