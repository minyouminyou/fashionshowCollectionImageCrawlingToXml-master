import time
import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import MakingDirectory
import os
from xml.etree.ElementTree import Element,dump,SubElement,ElementTree
import sys
from lxml import etree
from bs4 import BeautifulSoup
import xml.dom.minidom
import YoutubeVideoNameCode


# 이 클래스는 무슨 기능을 하냐면 이런 기능을 합니다.
# 1. 디자이너 넘버를 받아 해당 url로 이동 (가능)
# 2. 콜렉션들의 링크를 저장합니다.
# 3. 저장한 링크를 피라미터로 받아 이미지를 저장하는 메소드에다 던져버리기~ 그러면 이미지를 받아버리기~
# !! 콜렉션의 링크는 .item-isotope a로 찾을 수 있을 것 같다.
class Collection:
    def __init__(self):
        pass

    def prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="\t")

    def indent(self, elem, level=0):
        i = "/n" + level * "  "

        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def findCollectionLinks(self,designerNumber):
        driver = webdriver.Chrome('C:\chromedriver')
        url = "http://runway.vogue.co.kr/?post_id=&search_1=&search_2=&designer=" + str(designerNumber)
        driver.get(url)
        time.sleep(1)
        elem = driver.find_element_by_tag_name("body")
        no_of_pagedowns = 1

        makedirectory = MakingDirectory.MakeDirectory()
        makedirectory.makeDir("C:/Collection/", driver.find_element_by_css_selector(".season_tit").text)
        directoryPath = driver.find_element_by_css_selector(".season_tit").text

        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
            no_of_pagedowns -= 0.2
            if no_of_pagedowns < -2:
                break

        list = [directoryPath]
        provider_elems = driver.find_elements_by_css_selector(".item-isotope a")
        avoidFirstVogueImg = 1
        for post in provider_elems:
            if avoidFirstVogueImg == 1 :
                avoidFirstVogueImg = -1
                continue
            # urllib.request.urlretrieve(post.get_attribute("src"),"./"+directoryName+"/"+name)
            if list[-1] != post.get_attribute("href"):
                list.append(post.get_attribute("href"))
                print("href:"+post.get_attribute("href"))
            #print(post.get_attribute("href"))
        driver.quit()
        return list

    # 디자이너 url을 인자로 받아 해당하는 url을 xml리스트로 저장하는 메소드
    def saveImagesFromUrl(self,url,brandName):
        try:
            makedirectory = MakingDirectory.MakeDirectory()

            # 컬렉션 디렉토리를 만듬니다아
            driver = webdriver.Chrome('C:\chromedriver')
            driver.get(url)

            # 스크롤 내리는 부분
            time.sleep(1)
            elem = driver.find_element_by_tag_name("body")
            no_of_pagedowns = 4
            while no_of_pagedowns != 0:
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
                no_of_pagedowns -= 0.5
            #디렉토리 만드는 부분
            #makedirectory = MakingDirectory.MakeDirectory()
            #makedirectory.makeDir("C:/Collection/"+brandName, driver.find_element_by_css_selector(".season_tit").text.replace("Fall/Winter","FW").replace("Spring/Summer","SS").replace("Ready To Wear",""))
            collectionDirectoryPath = "C:/Collection/"+brandName+"/"

            #파일 찾아서 xml로 저장하는 부분
            #xmlFileName = driver.find_element_by_css_selector(".season_tit").text.replace("Fall/Winter","FW").replace("Spring/Summer","SS").replace("Ready To Wear","")
            provider_elems = driver.find_elements_by_css_selector(".wpb_wrapper img")
            index = 1
            avoidFirstVogueImg = 2
            xml = Element("xml")
            keyword = brandName+" "+driver.find_element_by_css_selector(".season_tit").text.replace("Fall/Winter","FW").replace("Spring/Summer","SS").replace("Ready To Wear","")

            videoId = YoutubeVideoNameCode.getYoutubeVideoId(keyword)
            print(type(videoId))
            print(videoId)
            youtube = Element('youtube')
            youtube.text = videoId
            xml.append(youtube)
            # YoutubeVideoNameCode.getYoutubeVideoId()
            for img in provider_elems:
                if avoidFirstVogueImg > 0 :
                    avoidFirstVogueImg -= 1
                    continue
                src = Element('src')
                src.text = img.get_attribute("src")
                src.attrib["index"] = str(index)
                xml.append(src)
                index += 1
            ElementTree(xml).write(collectionDirectoryPath+driver.find_element_by_css_selector(".season_tit").text.replace("Fall/Winter","FW").replace("Spring/Summer","SS").replace("Ready To Wear","")+".xml")
            time.sleep(0.2)
            driver.quit()

        except BaseException as e:
            tb = sys.exc_info()[-1]
            print(traceback.extract_tb(tb, limit=1)[-1][1])


    #호출하면 브랜드 이름을 구하고 디렉토리를 생성하는 메소드
    def getBrandNameAneMakeDir(self,url):
        driver = webdriver.Chrome('C:\chromedriver')
        driver.get(url)
        driver.quit()
        return directoryPath

    # 호출하면 컬렉션 이름을 구하고 디렉토리를 생성하는 메소드
    def getCollectionNameAneMakeDir(self,url,brandName):
        driver = webdriver.Chrome('C:\chromedriver')
        driver.get(url)
        makedirectory = MakingDirectory.MakeDirectory()
        directoryPath =driver.find_element_by_css_selector(".season_tit").text.replace("Spring/Summer","SS").replace("Ready To Wear","").replace("Fall/Winter","FW")
        makedirectory.makeDir("C:/"+brandName, directoryPath)
        driver.quit()
        return directoryPath












