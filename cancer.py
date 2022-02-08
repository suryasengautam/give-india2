import json,os,requests,mainpage
from bs4 import BeautifulSoup
from pprintpp import  pprint as pp
pp(os.getcwd())
# url  = "https://www.giveindia.org/cancer-care"
# url=mainpage.first_page_option()
# page = requests.get(url)
f = open("./cancer_page.html","r")
# f.write(page.text)
page = f.read()
f.close()
soup = BeautifulSoup(page,"lxml")
row_element= (soup.find("div",class_="container").find("div",attrs={"class":"row","style":"padding-top:1rem"}))


all_ngo_det=((row_element.find_all("div",class_="d-flex program-card-11 col-lg-4 col-xl-4 col-md-4 col-sm-6 col-12 col-xs-12 col-12 col-sm-6 col-md-6 col-lg-4")))
lis = []
def cancer():
    for i in all_ngo_det:
        dic = {}
        # dic = {"ngo_name":"","ngo_work":"","Purpose_ngo":"","Place":""}
        x= (i.find_all("div",class_="jsx-1989162857 card-body"))[0]
        Purpose_ngo=((x.find("span",class_="jsx-1989162857 small-text float-left")).get_text())
        y = x.find("span",class_="jsx-1989162857 small-text float-left")
        Place = ((x.find("span",class_="jsx-1989162857 small-text mid-grey float-right")).get_text())
        ngo_work_nme_tag=((i.find("div",class_="jsx-1989162857 card-body")).find("h5",class_="jsx-1989162857 card-title text-clamp-3"))
        ngo_work =(ngo_work_nme_tag.get_text())
        ngo_name1= ((ngo_work_nme_tag.find("span",class_="jsx-1989162857 sh w-100")).get_text())
        ngo_name=(ngo_name1.replace('\xa0', ' '))[4:]
        dic["ngo_name"]=ngo_name
        dic["ngo_work"]=ngo_work.split("Charutar")[0].split("\xa0by")[0]
        dic["Place"]=Place
        dic["Purpose_ngo"]=Purpose_ngo
        lis.append(dic)
    f = open("./main_ngo/cancer_out.json","w")
    json.dump(lis,f,indent=4)
    return(lis)
if __name__ == "__main__":
    pp(cancer())

# f = open("./give_india/cancer_page_output.html","w")
# json.dump(lis,f,indent=4)
# pp("done")
    