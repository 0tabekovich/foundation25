def bigger_price(son,ls):
    ls1=[]
    while son:
        Max=0
        for x in ls:
            if x['price']>Max and x not in ls1:
                Max=x['price']
                k=x
        ls1.append(k)
        son-=1
    return ls1

ls1=[{"name":"bread","price":100},{"name":"wine","price":138},{"name":"meat","price":15},{"name":"water","price":1}]
ls1=bigger_price(2,ls1)
print(ls1)