from bottle import route, view, get, post, request
from datetime import datetime

class AgeEra:   
    def	__init__(self,	n,	f, g):    
        self.Name = n
        self.Factor = f
        self.Goods = g

class Infos: 
    goodsList = { 
        'Dye': 'BE', 'Lumber' : 'BE', 'Marble' : 'BE', 'Stone' : 'BE', 'Wine' : 'BE',				
	    'Cloth' : 'I', 'Ebony' : 'I', 'Jewelry' : 'I', 'Limestone' : 'I', 'Iron' : 'I',
	    'Alabaster' : 'EMA', 'Copper' : 'EMA', 'Gold' : 'EMA', 'Granite' : 'EMA', 'Honey' : 'EMA',
	    'Brick': 'HMA', 'Dried Herbs': 'HMA', 'Glass': 'HMA', 'Rope': 'HMA', 'Salt': 'HMA',
	    'Basalt': 'LMA', 'Brass': 'LMA', 'Silk': 'LMA', 'Talc Powder': 'LMA', 'Gunpowder': 'LMA',
	    'Paper' : 'CA', 'Coffee': 'CA', 'Wire': 'CA', 'Porcelain': 'CA', 'Tar': 'CA',
	    'Coke': 'IN', 'Fertilizer' : 'IN', 'Rubber': 'IN', 'Textiles': 'IN', 'Whale Oil': 'IN',
	    'Machine Parts' : 'PE', 'Gasoline' : 'PE', 'Tinplate' : 'PE', 'Explosives' : 'PE', 'Asbestos' : 'PE',
	    'Ferroconcrete' : 'ME', 'Convenience Food' : 'ME', 'Flavorants' : 'ME', 'Packaging' : 'ME', 'Luxury Materials' : 'ME',
	    'Semiconductors' : 'PME', 'Steel': 'PME', 'Renewable Resources': 'PME', 'Industrial Filters': 'PME', 'Genome Data': 'PME',
	    'Electromagnets': 'CE', 'Gas': 'CE', 'Plastics': 'CE', 'Robots': 'CE', 'Bionics Data': 'CE',
	    'Translucent Concrete': 'TO', 'Nutrition Research': 'TO', 'Preservatives': 'TO', 'Papercrete': 'TO', 'Smart Materials': 'TO',
	    'Biogeochemical Data' : 'TF', 'Purified Water' : 'TF', 'Algae' : 'TF', 'Superconductors' : 'TF', 'Nanoparticles' : 'TF',
	    'A.I. Data' : 'AF', 'Bioplastics': 'AF', 'Nanowire': 'AF', 'Paper Batteries': 'AF', 'Transester Gas': 'AF'
    }

    eras = {
        "BE": { "Name": "Bronze Age", "MyGoods": ['Dye', 'Lumber', 'Marble', 'Stone' , 'Wine' ] },
        "I": { "Name": "Iron Age", "MyGoods": ['Cloth', 'Ebony', 'Jewelry', 'Limestone', 'Iron' ] },
        "EMA": { "Name": "Early Middle Age", "MyGoods": ['Alabaster', 'Copper', 'Gold', 'Granite', 'Honey' ] },
        "HMA": { "Name": "High Middle Age", "MyGoods" : ['Brick', 'Dried Herbs', 'Glass', 'Rope', 'Salt' ] },
        "LMA": { "Name": "Late Middle Age", "MyGoods" : ['Basalt', 'Brass', 'Silk', 'Talc Powder', 'Gunpowder'] },
        "CA": { "Name": "Colonial Age", "MyGoods": [ 'Paper', 'Coffee', 'Wire', 'Porcelain', 'Tar'] }, 
        "IN": { "Name": "Industrial Age", "MyGoods" : [ 'Coke', 'Fertilizer', 'Rubber' ,'Textiles', 'Whale Oil'] },
        "PE": { "Name": "Progressive Era", "MyGoods" : [ 'Machine Parts', 'Gasoline', 'Tinplate', 'Explosives', 'Asbestos'] },
        "ME": { "Name": "Modern Era", "MyGoods" : [ 'Ferroconcrete', 'Convenience Food', 'Flavorants' , 'Packaging' , 'Luxury Materials' ] },
        "PME": { "Name": "PostModern Era", "MyGoods" : [ 'Semiconductors', 'Steel', 'Renewable Resources', 'Industrial Filters', 'Genome Data' ] },
        "CE": { "Name": "Contemporary Era", "MyGoods" : [ 'Electromagnets', 'Gas', 'Plastics', 'Robots', 'Bionics Data' ] },
        "TO":  { "Name": "Tomorrow", "MyGoods" : [ 'Translucent Concrete', 'Nutrition Research', 'Preservatives', 'Papercrete', 'Smart Materials' ] },
        "TF":  { "Name": "The Future", "MyGoods" : [ 'Biogeochemical Data', 'Purified Water', 'Algae', 'Superconductors', 'Nanoparticles' ] },
        "AF": { "Name": "Artic Future", "MyGoods": [ 'A.I. Data', 'Bioplastics', 'Nanowire', 'Paper Batteries', 'Transester Gas' ] },
    }

    eras["BE"]["Iron Age"] = AgeEra("Bronze Age", 0.5, eras["I"]["MyGoods"])

    eras["I"]["Bronze Age"] = AgeEra("Bronze Age", 2, eras["BE"]["MyGoods"])
    eras["I"]["Early Middle Ages"] = AgeEra("Early Middle Age", 0.5, eras["EMA"]["MyGoods"])
    
    eras["EMA"]["Iron Age"] = AgeEra("Iron Age", 2, eras["I"]["MyGoods"])
    eras["EMA"]["High Middle Age"] = AgeEra("High Middle Age",  0.5, eras["HMA"]["MyGoods"])

    eras["HMA"]["Early Middle Ages"] = AgeEra("Early Middle Ages", 2, eras["EMA"]["MyGoods"])
    eras["HMA"]["Late Middle Ages"] = AgeEra("Late Middle Ages", 0.5, eras["LMA"]["MyGoods"])
    
    eras["LMA"]["High Middle Ages"] = AgeEra("High Middle Ages", 2, eras["HMA"]["MyGoods"])
    eras["LMA"]["Colonial Age"] = AgeEra("Colonial Age", 0.6, eras["CA"]["MyGoods"])
    eras["LMA"]["Industrial Age"] = AgeEra("Industrial Age", 0.5, eras["IN"]["MyGoods"])

    eras["CA"]["Late Middle Ages"] = AgeEra("Late Middle Ages", 1.5, eras["LMA"]["MyGoods"])
    eras["CA"]["Industrial Age"] = AgeEra("Industrial Age", 0.7, eras["IN"]["MyGoods"])
    eras["CA"]["Progessive Era"] = AgeEra("Progessive Era", 0.6, eras["PE"]["MyGoods"])
    eras["CA"]["Modern Era"] = AgeEra("Modern Era", 0.5, eras["ME"]["MyGoods"])

    eras["IN"]["Late Middle Ages"] = AgeEra("Late Middle Ages", 2.0, eras["LMA"]["MyGoods"])
    eras["IN"]["Colonial Age"] = AgeEra("Colonial Age", 1.3, eras["CA"]["MyGoods"])
    eras["IN"]["Progessive Era"] = AgeEra("Progessive Era", 0.8, eras["PE"]["MyGoods"])
    eras["IN"]["Modern Era"] = AgeEra("Modern Era", 0.6, eras["ME"]["MyGoods"])
    eras["IN"]["PostModern Era"] = AgeEra("PostModern Era", 0.5, eras["PME"]["MyGoods"])

    eras["PE"]["Colonial Age"] = AgeEra("Colonial Age", 1.6, eras["CA"]["MyGoods"])
    eras["PE"]["Industrial Age"] = AgeEra("Industrial Age", 1.2, eras["IN"]["MyGoods"])
    eras["PE"]["Modern Era"] = AgeEra("Modern Era", 0.8, eras["ME"]["MyGoods"])
    eras["PE"]["PostModern Era"] = AgeEra("PostModern Era", 0.6, eras["PME"]["MyGoods"])
    eras["PE"]["Contemporary Era"] = AgeEra("Contemporary Era", 0.5, eras["CE"]["MyGoods"])

    eras["ME"]["Colonial Age"] = AgeEra("Colonial Age", 2.0, eras["CA"]["MyGoods"])
    eras["ME"]["Industrial Age"] = AgeEra("Industrial Age", 1.6, eras["IN"]["MyGoods"])
    eras["ME"]["Progressive Age"] = AgeEra("Progressive Age", 1.2, eras["PE"]["MyGoods"])
    eras["ME"]["PostModern Era"] = AgeEra("Modern Era", 0.8, eras["PME"]["MyGoods"])
    eras["ME"]["Contemporary"] = AgeEra("PostModern Era", 0.6, eras["CE"]["MyGoods"])
    eras["ME"]["Tomorrow"] = AgeEra("Contemporary Era", 0.5, eras["TO"]["MyGoods"])
    
    eras["PME"]["Industrial Age"] = AgeEra("Industrial Age", 1.8, eras["IN"]["MyGoods"])
    eras["PME"]["Progressive Age"] = AgeEra("Progressive Age", 1.5, eras["PE"]["MyGoods"])
    eras["PME"]["Modern Era"] = AgeEra("Modern Era", 1.2, eras["ME"]["MyGoods"])
    eras["PME"]["Contemporary"] = AgeEra("Contemporary Era", 0.8, eras["CE"]["MyGoods"])
    eras["PME"]["Tomorrow"] = AgeEra("Tomorrow", 0.7, eras["TO"]["MyGoods"])
    eras["PME"]["Artic Future"] = AgeEra("Artic Future", 0.6, eras["AF"]["MyGoods"])

    eras["CE"]["Progressive Age"] = AgeEra("Progressive Age", 1.8, eras["PE"]["MyGoods"])
    eras["CE"]["Modern Era"] = AgeEra("Modern Era", 1.5, eras["PME"]["MyGoods"])
    eras["CE"]["PostModern Era"] = AgeEra("PostModern Era", 1.2, eras["PME"]["MyGoods"])
    eras["CE"]["Tomorrow"] = AgeEra("Tomorrow", 0.8, eras["TO"]["MyGoods"])
    eras["CE"]["Artic Future"] = AgeEra("Artic Future", 0.7, eras["AF"]["MyGoods"])

    eras["TO"]["Modern Era"] = AgeEra("Modern Era", 1.7, eras["PME"]["MyGoods"])
    eras["TO"]["PostModern Era"] = AgeEra("PostModern Era", 1.4, eras["PME"]["MyGoods"])
    eras["TO"]["Contemporary"] = AgeEra("Contemporary Era", 1.1, eras["CE"]["MyGoods"])
    eras["TO"]["Artic Future"] = AgeEra("Artic Future", 0.8, eras["AF"]["MyGoods"])

    eras["AF"]["PostModern Era"] = AgeEra("PostModern Era", 1.6, eras["PME"]["MyGoods"])
    eras["AF"]["Contemporary"] = AgeEra("Contemporary Era", 1.3, eras["CE"]["MyGoods"])
    eras["AF"]["Tomorrow"] = AgeEra("Artic Future", 1.1, eras["TO"]["MyGoods"])

    @classmethod
    def getGoodsList(cls):
        from json import dumps
        ret = []
        for k,v in cls.goodsList.items():
            ret.append(k)
        return { "goods" : ret }

@route('/foe')
@view('foe')
def foe():
    """Renders the FoE list."""
    return dict(
        year=datetime.now().year
    )

@get("/goods")
def goods(): 
    return Infos.getGoodsList()

    """ return {"goods" : ['Dye', 'Lumber', 'Marble', 'Stone', 'Wine',				
		'Cloth', 'Ebony', 'Jewelry', 'Limestone', 'Iron',
		'Alabaster', 'Copper', 'Gold', 'Granite', 'Honey',
		'Brick', 'Dried Herbs', 'Glass', 'Rope', 'Salt',
		'Basalt', 'Brass', 'Silk', 'Talc Powder', 'Gunpowder',
		'Paper', 'Coffee', 'Wire', 'Porcelain', 'Tar',
		'Coke', 'Fertilizer', 'Rubber', 'Textiles', 'Whale Oil',
		'Machine Parts', 'Gasoline', 'Tinplate', 'Explosives', 'Asbestos',
		'Ferroconcrete', 'Convenience Food', 'Flavorants', 'Packaging', 'Luxury Materials',
		'Semiconductors', 'Steel', 'Renewable Resources', 'Industrial Filters', 'Genome Data',
		'Electromagnets', 'Gas', 'Plastics', 'Robots', 'Bionics Data',
		'Translucent Concrete', 'Nutrition Research', 'Preservatives', 'Papercrete', 'Smart Materials',
		'Biogeochemical Data', 'Purified Water', 'Algae', 'Superconductors', 'Nanoparticles',
		'A.I. Data', 'Bioplastics', 'Nanowire', 'Paper Batteries', 'Transester Gas']}
    """

@post('/rates')
def rates():
    sel = request.json["selected"]    
   
    matched = Infos.eras[Infos.goodsList[sel]]
    ret = { "val" : sel, "name" : matched["Name"], "eras": [] }
    for k,v in matched.items():
        if k != "Name" and k != "MyGoods":
            new = { "Name" : v.Name, "Factor" : v.Factor, "Goods" : v.Goods } 
            ret["eras"].append(new.copy())            

    return ret   