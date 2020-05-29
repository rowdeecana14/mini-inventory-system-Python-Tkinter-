from .config import Config
from .query import Query


query = Query()

class Model:
    def __init__(self):
        connect = Config()
        self.console, self.cursor = connect.console()

    def add_user(self, data):

        resp, result = query.run("INSERT INTO `tbl_user`("
                  "`user_username`, `user_password`, `user_name`, `user_gender`, `user_address`, `user_contact`, `user_position`)"
                  " VALUES(%s, %s, %s, %s, %s, %s, %s)", data)

        return result


    def add_customer(self, param):
        resp, result = query.run("INSERT INTO `tbl_customer`("
                  "`customer_fname`, `customer_mname`, `customer_lname`, `customer_address`, `customer_contact`, "
                  "`customer_birthday`, `customer_work`, `customer_gender`, `customer_email`, `user_id`) "
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", param)

        return result

    def check_product(self, prod_id):
        resp = query.fetch("SELECT `product_id` FROM `tbl_product` WHERE product_id=%s", prod_id)
        return resp

    def add_product(self, param):
        resp = query.run("INSERT INTO `tbl_product`("
                         "`product_id`, `product_name`, `product_details`, `product_brand`)"
                         " VALUES (%s, %s, %s, %s)", param)

    def add_product_storage(self, param):
        resp = query.run("INSERT INTO `tbl_stock_in`("
                         "`stock_in_quantity`, `stock_price`, `stock_in_date`, `product_id`, `user_id`) "
                         "VALUES (%s, %s, %s, %s, %s)", param)

    def check_stock(self, stock):
        resp = query.fetch("SELECT prod.*, stock.stock_price FROM `tbl_product` AS prod "
                           "INNER JOIN tbl_stock_in as stock "
                           "ON stock.product_id=prod.product_id WHERE prod.product_id=%s", stock)
        return resp

    def search_stock(self, stock):
        resp = query.fetch("SELECT prod.*, stock.stock_price, SUM(stock.stock_in_quantity) as stock_quan FROM `tbl_product` AS prod "
                           "INNER JOIN tbl_stock_in as stock "
                           "ON stock.product_id=prod.product_id WHERE prod.product_id LIKE %s OR prod.product_name LIKE %s "
                           "GROUP BY prod.product_id", ('%' + stock + '%', '%' + stock + '%'))
        return resp

    def search_customer_invoice(self, data):
        resp = query.fetch("SELECT inv.invoice_date, inv.invoice_no, cust.`customer_fname`, cust.`customer_mname`, "
                           "cust.`customer_lname`, cust.`customer_address`, cust.`customer_contact`, "
                           "cust.`customer_gender`, cust.`customer_email`, prod.product_id, SUM(sale.sales_price) as sales_price, "
                           "prod.product_name, prod.product_details, prod.product_brand, SUM(sale.sales_quantity) as sales_quantity "
                           "FROM `tbl_customer` as cust INNER JOIN tbl_invoice as inv "
                           "ON inv.customer_id=cust.customer_id INNER JOIN tbl_sales AS sale "
                           "ON sale.invoice_id=inv.invoice_id INNER JOIN tbl_product AS prod "
                           "ON prod.product_id=sale.product_id WHERE cust.customer_fname LIKE %s OR cust.customer_mname LIKE %s "
                           "OR cust.customer_lname LIKE %s GROUP BY invoice_no, prod.product_id, inv.invoice_date",
                           ('%' + data + '%', '%' + data + '%', '%' + data + '%'))

        return resp


    def search_inventory(self, data):
        resp = query.search("SELECT prod.*, stock.stock_price, SUM(stock.stock_in_quantity) as total_qty " \
                            "FROM `tbl_product` AS prod INNER JOIN tbl_stock_in as stock "
                            "ON stock.product_id=prod.product_id " \
                            "WHERE CONCAT(prod.product_id LIKE '%{0}%', prod.product_name LIKE '%{1}%', " \
                            "prod.product_brand LIKE '%{2}%')" \
                            "GROUP BY prod.product_id".format(data, data, data))

        sale = query.search("SELECT SUM(sale.`sales_quantity`) as sale_quan, sale.`product_id`, prod.* FROM `tbl_sales` as sale " \
                            "INNER JOIN tbl_product as prod ON sale.product_id = prod.product_id "\
                            "WHERE CONCAT(prod.product_id LIKE '%{0}%', prod.product_name LIKE '%{1}%', "
                            "prod.product_brand LIKE '%{2}%')"
                            "GROUP BY prod.product_id".format(data, data, data))

        return resp, sale

    def user_login(self, uname, upass):
        result = query.fetch("SELECT `user_id`, `user_username`, `user_password`, `user_name`, `user_gender`, " \
                    "`user_address`, `user_contact`, `user_position` FROM `tbl_user` WHERE user_username=%s", uname)
        return result

    def get_invoice(self, data):
        result = query.fetch("SELECT inv.*, cust.customer_fname, cust.customer_mname, cust.customer_lname, cust.customer_address, "
                              "cash.user_name FROM `tbl_invoice` AS inv INNER JOIN tbl_customer AS cust "
                              "ON cust.customer_id=inv.customer_id INNER JOIN tbl_user AS cash "
                              "ON cash.user_id=inv.user_id WHERE cust.customer_fname LIKE %s OR cust.customer_mname LIKE %s "
                              "OR cust.customer_lname LIKE %s OR cash.user_name LIKE %s OR inv.invoice_no LIKE %s",
                              ("%" + data + "%", "%" + data + "%", "%" + data + "%", "%" + data + "%", "%" + data + "%"))

        return result

    def get_invoice_sale(self, invoice):
        resp = query.fetch("SELECT sale.`sales_quantity`, sale.`sales_price`, prod.product_name FROM `tbl_sales` "
                           "AS sale INNER JOIN tbl_product AS prod ON prod.product_id=sale.product_id "
                           "INNER JOIN tbl_invoice AS inv ON inv.invoice_id=sale.invoice_id "
                           "WHERE inv.invoice_no=%s", invoice)
        return resp


    def search_user(self, user):
        resp = query.fetch("SELECT `user_id`, `user_username`, `user_password`, `user_name`, `user_gender`, "
                           "`user_address`, `user_contact`, `user_position` FROM `tbl_user` "
                           "WHERE user_username LIKE %s OR user_name LIKE %s OR user_address LIKE %s OR "
                           "user_gender LIKE %s", ('%' + user + '%', '%' + user + '%', '%' + user + '%', '%' + user + '%'))
        return resp







    def sample(self):

        data = {
            "user_username": "new_user",
            "user_password": "new_pass",
            "user_name": "User Name",
            "user_gender": "male",
            "user_address": "Negros Occidental",
            "user_contact": "New Contact",
            "user_position": "1"
        }
        query.insert(data)
