from time import sleep
from selenium import webdriver
from secrets import *


class Instabot:
    def __init__(self):
        try:
            name = input("Please enter the Instagram user: ")
            posts = int(input("Please enter number of posts user has: "))
        except:
            print("Error, enter a sensible input")
            quit()

        ##calculations
        final = posts / 4
        average = posts / 12
        calculation = average / 3
        calculation2 = final * 2 + calculation
        finalcalculation = calculation2 / 2
        timeinmins = finalcalculation / 60

        print("Starting...")
        sleep(0.5)
        print("")
        print("Insta name:",name)
        print("Posts:",posts)
        print("")
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com") #going to URL
        sleep(2)

        ##logging in
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")\
        .send_keys(username) #typing username
        sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")\
        .send_keys(pw) #typing password
        sleep(0.5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")\
        .click()
        sleep(3)
        print("Successfully logged into",username)

        ##closing popups
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
        .click()
        print("Closed popup x1")
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
        .click()
        print("Closed popup x2")
        sleep(1)

        ##main
        try:
            self.driver.get("https://www.instagram.com/"+name+"/")
            sleep(1)

        except:
            print("Couldn't find username")
            quit()

        print("Successfully found",name)
        print("")
        print("------Calculations-----")
        print("Estimated time in seconds:")
        print(int(finalcalculation))
        print("Estimated time in minutes:")
        print("%.2f" % timeinmins)
        print("")

        ##scrolling
        try:
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]")
            last_ht, ht = 0, 1
            count = 1
            while final > count:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(1)
                ht = self.driver.execute_script("""
                    arguments[0].scrollTo(0, arguments[0].scrollHeight);
                    return arguments[0].scrollHeight;
                    """, scroll_box)
                count += 1
                sleep(2)
            print("Finished")
            sleep(50000)

        except:
            print("Error scrolling - account may be private")
            sleep(4)
            quit()

Instabot()
