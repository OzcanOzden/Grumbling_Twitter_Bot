import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


URL_SPEED_TEST = "https://www.speedtest.net/"
URL_TWITTER = "https://twitter.com/"
URL_TWEET = "https://twitter.com/compose/tweet"
MAIL = "radyoterapi1@outlook.com"
USERNAME = "LockieHafza"
PASSWORD = "onkoloji1"


class complain_bot():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up_speed = 0
        self.down_speed = 0

    def speed_test(self):
        self.driver.get(URL_SPEED_TEST)
        time.sleep(5)
        speed_test_go_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        speed_test_go_button.click()
        time.sleep(50)
        close_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
        close_button.click()
        self.up_speed = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down_speed = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def complain_about_it(self):
        self.driver.get(URL_TWITTER)
        time.sleep(random.randint(7, 10))
        mail = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        mail.send_keys(MAIL)
        mail_next_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        mail_next_button.click()
        time.sleep(random.randint(2, 5))
        username = self.driver.find_element(By.TAG_NAME, "input")
        username.send_keys(USERNAME)
        username_next_button = self.driver.find_element(By.XPATH, "//div[@data-testid='ocfEnterTextNextButton']")
        username_next_button.click()
        time.sleep(random.randint(2, 4))
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(PASSWORD)
        log_in_button = self.driver.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")
        log_in_button.click()
        time.sleep(random.randint(5, 8))
        driver.get(URL_TWEET)
        time.sleep(random.randint(5, 8))
        tweet_it = self.driver.find_element(By.XPATH, "//div[contains(@class, 'public-DraftStyleDefault-block')]")
        TWEET = f"Merhana @TurkTelekom, internet hızım 100/20 Mbps olması gerekirken neden {self.up_speed} / {self.down_speed} Mbps gözüküyor? @TTDestek"
        tweet_it.send_keys(TWEET)
        send_tweet = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']")
        send_tweet.click()
        time.sleep(random.randint(3, 5))
        log_out_menu = self.driver.find_element(By.XPATH, "//div[@aria-label='Account menu']")
        log_out_menu.click()
        time.sleep(1)
        log_out = self.driver.find_element(By.XPATH, "//div[@data-testid='AccountSwitcher_AddAccount_Button']")
        log_out.click()

bot = complain_bot()
bot.speed_test()
bot.complain_about_it()