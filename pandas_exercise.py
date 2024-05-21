import pandas as pd

sales_data = pd.DataFrame({
    'transcition_id': [101,102,103,104,105],
    'product_id': ['p1','p2','p1','p3','p2'],
    'quantity_sold': [2,1,3,2,2],
    'revenue': [100,5,150,120,90]
})

products_data = pd.DataFrame({
    'product_id':['p1','p2','p3','p4'],
    'product_name': ['Product A','Product B','Product C','Product D'],
    'category': ['1','2','1','3']
})

print(sales_data)
print(products_data)
left_join = pd.merge(sales_data,products_data,on='product_id',how='left')
print(left_join)