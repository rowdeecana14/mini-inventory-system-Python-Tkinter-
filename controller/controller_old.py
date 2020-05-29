from model import Model

model = Model()

class Controller:
    def __init__(self):
        pass

    def validate(self, data):
        data = str(data)  # to Validate the data entered here
        return data

    def user_add(self, datas):
        # temp_data = []
        #
        # for data in datas.values():
        #     temp_data.append(data)
        # model.add_user(temp_data)
        return model.add_user(datas)

    def customer_add(self, data):
        resp = model.add_customer(data)
        return resp

    def product_add(self, prod_id, product, storage):
        resp = model.check_product(prod_id)
        result = ""
        if len(resp) == 0:
            result = model.add_product(product)
            result = model.add_product_storage(storage)
        else:
            result = model.add_product_storage(storage)

        return resp, result

    def user_add(self, ufullname, uposis, ugender, uaddress, ucntact, uname, upass):
        data = (uname, upass, ufullname, ugender, uaddress, ucntact, uposis)
        result = model.add_user(data)
        return result

    def user_login(self, uname, upass):
        return model.user_login(uname, upass)

    def check_stock_no(self, stock):
        return model.check_stock(stock)

    def search_stock_no(self, stock):
        return model.search_stock(stock)

    def search_inventory(self, data):
        return model.search_inventory(data)

    def search_user(self, data):
        return model.search_user(data)

    def get_invoice(self, data):
        return model.get_invoice(data)

    def get_invoice_sale(self, data):
        return model.get_invoice_sale(data)

    def search_customer_invoice(self, data):
        return model.search_customer_invoice(data)

    # def sample(self):
    #     model.sample()
