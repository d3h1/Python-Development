# my_string = "123456789"
# print(my_string)

# print(my_string[-2:6])
# # print(my_string[::-2])

# price = 250


# # 'price' has already been created
# if price >= 300:
#     price_new = price - (price * 0.3)
# elif price >= 200 and price < 300:
#     price_new = price - (price * 0.2)  
# elif price >= 100 and price < 200:
#     price_new = price - (price * 0.1)
# elif price < 100:
#     price_new = price - (price * 0.05)
# elif price <= 0:
#     price_new = price
# print(price_new)


def rep_cat(x, y):
    return str(x) * 10 + str(y) * 5
    

print(rep_cat(1, 2))
