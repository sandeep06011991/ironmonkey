__author__ = 'sandeep.polisetty'
from nutrition.models import FoodTag
from nutrition.tagConstants import getTitle
class FoodItemDTO():
    def setTag(self,a):
        self.tagValue=a

    def __init__(self,data):
        self.id=data['_id']
        info=data['_source']
        self.name=info['name']
        self.totalCal=info['total_cal']
        self.carb=info['carb_gms']
        self.fat=info['fat_gms']
        self.sugar=info['sugar_gms']
        self.protein=info['protein_gms']
        self.carbPerc=int(info['carbPerc'])
        self.fatPerc=int(info['fatPerc'])
        self.proteinPerc=int(info['proteinPerc'])
        self.sugarPerc=int(info['sugarPerc'])
        self.serving_gram=info['serving_gram']
        self.serving_desc=info['serving_desc']
        self.serving_size=info['serving_size']
        self.mfgName=info['mfg']
        self.itemDescription=info['itemDescription']

    pass





def getListOfFoodItemDTO(response):
    total=response['hits']['total']
    results=[]
    response=response['hits']['hits']
    for ech in response:
        rs=FoodItemDTO(ech)
        rs.setTag(getTitle(FoodTag.objects.get(id=rs.id).tagValue))
        results.append(rs)
    result_dict={'hits':total,'results':results}
    return result_dict
