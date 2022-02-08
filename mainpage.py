import json,os,requests
import cancer,children,education,women,differently,health,livelyhood
from bs4 import BeautifulSoup
from pprintpp import pprint as pp
# url = "https://www.giveindia.org/children"
# page = requests.get(url)
f = open("./mainpage.html","r")
page = f.read()
f.close()
def first_page_option():
    soup = BeautifulSoup(page,"lxml")
    main = soup.find("div",attrs={"id":"__next"})
    menu_items =((main.find_all("div",attrs={"tabindex":"-1","role":"menu","aria-hidden":"true","class":"dropdown-menu"}))[1]).find_all("a")
    option = ["1.Cancer care","2.children","3.Education","4.women","5.Differently Abled","6.Health","7.Livelihoods"]
    print("this is option. Please choose  one of them.")
    option_links= []
    for i in menu_items:
        option_links.append("https://www.giveindia.org"+i["href"])
    for i in option:
        print(i)
    user_input = int(input("enter your option: "))
    if user_input == 1:
        return(cancer.cancer())
    elif user_input == 2:
        return(children.children())
    elif user_input == 3:
        return(education.education())
    elif user_input == 4:
        return(women.women())
    elif user_input == 5:
        return(differently.differently())
    elif user_input == 6:
        return(health.health())
    elif user_input == 7:
        return(livelyhood.livelyhood())
if __name__ == "__main__":
    pp (first_page_option())


