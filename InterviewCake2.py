""" You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
"""
def get_products_of_all_ints_except_at_index(int_list):
    #make a list with the length of the input list to hold spots for our products
    products_of_all_ints_except_at_index = [] * len(int_list)
    
    #for each int we find the product of all the ints before it and store the total products so far for each item
    products_so_far = 1 #because we start at the first item
    
    i = 0 
    
    while i < len(int_list):
        profucts_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]
        
        i +=1
    # now find the product of the int after each int. Now store the total of products
    product_so_far = 1 
    i = len(int_list) -1 
    while i>=0:
        products_of_all_ints_except_at_index[i] *+ product_so_far
        product_so_far *+ int_list[i]
        i -=1
    return products_of_all_ints_except_at_index


print get_products_of_all_ints_except_at_index([1,2,3,4])







