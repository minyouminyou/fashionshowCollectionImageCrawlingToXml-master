import Collection
import os
import MakingDirectory
collection = Collection.Collection()
# list = []
# list = collection.findCollectionLinks('22')
# for a in list:
#     print(a)

#collection.saveImagesFromUrl('http://runway.vogue.co.kr/?post_id=&search_1=&search_2=&designer=22','cloe-image')
# print(os.path)

# 브랜드 디자이너 넘버들 = 21, 62, 43 | 44, 83, 156, 105, 32, 102 | 785, 4, 134 | 8, 838, 544, 65, 572

#designerNumbers = [21, 62, 43, 44, 83, 156, 105, 32, 102, 785, 4, 134, 8, 838, 544, 65, 572]
designerNumbers=[838]
list = []
directoryPath = None
for num in designerNumbers:
    brandUrl = "http://runway.vogue.co.kr/?post_id=&search_1=&search_2=&designer=" + str(num)
    list = collection.findCollectionLinks(num)
    brandName = list[0]
    for index, collectionUrl in enumerate(list):
        if index == 0:
            continue
        collection.saveImagesFromUrl(collectionUrl,brandName)
    directoryPath = None


#collection.getCollectionNameAneMakeDir("http://runway.vogue.co.kr/2016/09/30/spring-2017-chloe/#0",brandName)