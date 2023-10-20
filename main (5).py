def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices

products = ["sarees"," tops","tshirts","sarees","jeans","sarees"]
target = "sarees"
target2 = "oil"
result = linearSearchProduct( products, target)
print(result)p