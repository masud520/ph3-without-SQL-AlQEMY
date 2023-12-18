
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


