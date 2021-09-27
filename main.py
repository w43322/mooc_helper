from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

edge_options={
    "executable_path": "/Users/w43322/Desktop/code/edgedriver_mac64/msedgedriver",
    # ofcourse change path to driver you downloaded.
    "capabilities":
    {
        "platformName": 'mac os x', # I get this from Chrome driver's capabilities
        # "os" : "OS X", # also ok.
    }
}

driver=webdriver.Edge(**edge_options)
driver.get("https://www.icourse163.org/")

print("1-互评 2-刷课")

cmd=int(input())

if cmd==1:
    print("用手机扫二维码登录\n打开课程的链接\n把新打开的标签页的地址复制到第一个标签页\n并关闭新打开的标签页\n打开到开始评分的页面\n在命令行中随便输入点什么\n回车")
    c=input()
    while(1):
        time.sleep(1)
        Course_Name=driver.find_element_by_xpath("//h4[@class='f-fc3 courseTxt']").text
        Boxes=driver.find_elements_by_xpath("//div[@class='s']")
        for Box in Boxes:
            Inputs=Box.find_elements_by_class_name("j-select")
            Input=Inputs[-1]
            Input.send_keys(Keys.SPACE)
        Comments=driver.find_elements_by_xpath("//textarea[@name='inputtxt']")
        for Comment in Comments:
            Comment.send_keys("呦呦呦，这不是"+Course_Name+"慕课作业吗？几天不见，这么拉了？")
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='u-btn u-btn-default f-fl j-submitbtn']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='j-gotonext']").click()
elif cmd==2:
    print("差不多得了")
    c=input()
    time.sleep(1)
    Select1=driver.find_element_by_xpath("//div[@class='f-fl j-chapter']")
    Select2=driver.find_element_by_xpath("//div[@class='f-fl j-lesson']")
    ChapterStr=[]
    LessonStr=[]
    
    Select1.click()
    Chapters=Select1.find_elements_by_xpath("//div[@class='f-thide list']")
    while len(Chapters)!=0:
        Chapter=Chapters[0]
        if Chapter.text=="" or Chapter.text in ChapterStr:
            Chapters.remove(Chapter)
            continue
        ChapterStr.append(Chapter.text)
        Chapter.click()
        time.sleep(1)
        Select2=driver.find_element_by_xpath("//div[@class='f-fl j-lesson']")
        Select2.click()
        time.sleep(1)
        Lessons=Select2.find_elements_by_xpath("//div[@class='f-thide list']")
        while len(Lessons)!=0:
            Lesson=Lessons[0]
            if Lesson.text=="" or Lesson.text in LessonStr:
                Lessons.remove(Lesson)
                continue
            LessonStr.append(Lesson.text)
            Lesson.click()
            time.sleep(1)

            dataidStr=[]
            dataidStr.append(driver.find_element_by_xpath("//li[@class='f-fl current']").get_attribute("data-id"))
            Buttons=driver.find_elements_by_xpath("//li[@class='f-fl']")
            while len(Buttons)!=0:
                Button=Buttons[0]
                if Button.get_attribute("data-id") in dataidStr:
                    Buttons.remove(Button)
                    continue
                dataidStr.append(Button.get_attribute("data-id"))
                Button.click()
                time.sleep(1)
                Buttons=driver.find_elements_by_xpath("//li[@class='f-fl']")




            Select2=driver.find_element_by_xpath("//div[@class='f-fl j-lesson']")
            Select2.click()
            time.sleep(1)
            Lessons=Select2.find_elements_by_xpath("//div[@class='f-thide list']")

        Select1=driver.find_element_by_xpath("//div[@class='f-fl j-chapter']")
        Select1.click()
        Chapters=Select1.find_elements_by_xpath("//div[@class='f-thide list']")

#python3 ./mooc_helper/main.py

