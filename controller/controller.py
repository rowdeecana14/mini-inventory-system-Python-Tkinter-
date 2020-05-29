from model import Model
from datetime import date

model = Model()

class Controller:
    def __init__(self):
        pass

    def validate(self, data):
        data = str(data).lower()  # to Validate the data entered here
        return data

    def add_invoice_sale(self, custid):
        print("customer id insertion: ", custid)
        result = model.get_last_sale_id()

        print("Result invoice: ", result)

        digit_group1 = "00"
        digit_group2 = "00000"
        if len(result) == 0:
            digit_group1 = "00"
            digit_group2 = "00001"
        else:
            invno = result[0]['invoice_no']
            invno_arr = invno.split('-')
            inv_1 = int(invno_arr[0])
            inv_2 = int(invno_arr[1])
            if inv_2 > 99999:
                digit_group1 = "0{}".format(inv_1 + 1) if inv_1 < 10 else "{}".format(inv_1 + 1)
                digit_group2 = "00001"

            else:
                if inv_2 < 10:
                    digit_group2 = "{}{}{}{}{}".format("0", "0", "0", "0", inv_2 + 1)
                elif inv_2 < 100:
                    digit_group2 = "{}{}{}{}".format("0", "0", "0", inv_2 + 1)
                elif inv_2 < 1000:
                    digit_group2 = "{}{}{}".format("0", "0", inv_2 + 1)
                elif inv_2 < 10000:
                    digit_group2 = "{}{}".format("0", inv_2 + 1)
                elif inv_2 < 100000:
                    digit_group2 = "{}".format(inv_2 + 1)

        print("digit_group1: ", digit_group1)
        print("digit_group2: ", digit_group2)
        print("digit_group: {}-{}".format(digit_group1, digit_group2))

        new_invoice = "{}-{}".format(digit_group1, digit_group2)

        # print("Result (add_invoice_sale): ", result)
        # lastid = ["0"]
        # if len(result) > 0:
        #     lastid = list(str(result[0]['invoice_id'] + 1))
        #
        # inv_date = str(date.today()).split("-")
        # zero = ["0", "0", "0", "0", "0", "0"]
        # inv_id = "".join(inv_date)
        # for i in range(len(lastid)):
        #     zero.pop(0)
        #     zero.append(lastid[i])
        # new_zero = "".join(zero)
        # new_invoice = "{}-{}".format(inv_id, new_zero)

        last_id, resp = model.add_invoice_sale(new_invoice, custid)
        return last_id, resp

    def save_sale_product(self, prodid, sale_price, sale_qnty, last_id):
        last_id, resp = model.save_sale_product(prodid, sale_price, sale_qnty, last_id)
        return last_id, resp

    def user_add(self, datas):
        return model.add_user(datas)

    def customer_add(self, data):
        resp = model.add_customer(data)
        return resp

    def get_user_info(self, data):
        return model.get_user_info(data)

    def get_user_info_using_suki(self, data):
        return model.get_user_info_using_suki(data)


    def check_cust_cardno(self, cardno):
        data = (self.validate(cardno))
        all = model.check_cust_cardno(data)

        return all

    def assinging_cust_cardno(self, cardid, custid):
        resp = model.assinging_cust_cardno(cardid, custid)
        return resp

    def checking_customer_ifexist(self, fname, lname):
        data = (self.validate(fname) + "%", self.validate(lname) + "%")
        all = model.checking_customer_ifexist(data)

        return all

    def checking_customer_ifexist_prev(self, fname, lname, prev_id):
        data = (self.validate(fname) + "%", self.validate(lname) + "%", prev_id)
        resp = model.checking_customer_ifexist_prev(data)

        return resp

    def checking_customer_ifexist_next(self, fname, lname, next_id):
        data = (self.validate(fname) + "%", self.validate(lname) + "%", next_id)
        resp = model.checking_customer_ifexist_next(data)

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
        data = (self.validate(uname), self.validate(upass), self.validate(ufullname), ugender, self.validate(uaddress)
                , ucntact, uposis)
        result = model.add_user(data)
        return result

    def add_customer(self, fname, mname, lname, gender, address, bday, contact, work, email):
        files = open("_session.txt", 'r')
        data = files.readlines()
        id = int(data[2].split(": ")[1])
        files.close()

        data = (self.validate(fname), self.validate(mname), self.validate(lname), self.validate(address)
                , contact, bday, self.validate(work), gender, email, id)
        lastid, resp = model.add_customer(data)
        return lastid, resp

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

    def search_sales_bydate(self, frm, to):
        return model.search_sales_bydate(frm, to)

    def update_user_info(self, upass, uname, ucntact, uaddress, ugender, uposis, ufullname, ustatus, hide_userid):
        data = (uname, upass, ufullname, ugender, uaddress, ucntact, uposis, ustatus, hide_userid)
        return model.update_user_info(data)

