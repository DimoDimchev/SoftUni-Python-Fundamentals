class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, name):
        Catalogue.products.append(name)

    def get_by_letter(self, first_letter):
        temp_list = list(filter(lambda word: word[0] == first_letter, Catalogue.products))
        return temp_list

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += f'\n'.join(sorted(Catalogue.products))
        return result
