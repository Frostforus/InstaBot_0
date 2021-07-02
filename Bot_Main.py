from FunNiER import FuNnY
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random import *
from Secret_shit import password as pw, acc


class NetBotface:
    # Attributes that will be used for sure:
    __slots__ = ["driver", "username"]

    def __init__(self, username, password):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })

        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://facebook.com")
        self.username = username

        # Load Facebook and login
        self.driver.find_element_by_xpath("//a[contains(text(), 'Bejelentkezés')]").click()
        self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"pass\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        print("Login complete: ", username)
        sleep(2)

    def move_to_link(self, link="https://facebook.com"):
        self.driver.get(link)

    def scroll(self, y_amount, time=5, resolution=0.03):
        i = 0
        while i < time:
            sleep(resolution)
            self.driver.execute_script("window.scrollTo(0, window.scrollY + {})".format((resolution / time) * y_amount))
            i += resolution

    # Search for name
    def search(self, query="Gergely Farkas"):

        self.driver.find_element_by_xpath(
            "//input[@placeholder=\"Search\" and @data-testid=\"search_input\"]").send_keys(query)
        self.driver.find_element_by_xpath("//button[@data-testid=\"facebar_search_button\"]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//img[@alt=\"{0}\"]".format(query)).click()
        print("Search for: ", query, " complete")
        sleep(2)

    #  Get Post with said timestamp WIP
    def get_post(self, delta_days=7):
        print("Fetching Post...")

        delta_days = str(int((time() - delta_days * 86400) / 100000))
        print(delta_days)

        self.scroll(2000)
        xpath = "//*[starts-with(@data-store,'{\"timestamp\":{0}')]/child::div/child::div/child::div/child::div" \
                "/child::div[2]/child::div[2]/child::p "

        # Kicseréli a timestampet, hogy melyik nap legyen
        string = self.driver.find_element_by_xpath(xpath.replace("{0}", delta_days)).text
        print(string)
        return string

    def add_image_to_post(self, file_location="C:\\Users\\konrad.drexler\\Desktop\\Yes_boomer.jpg"):
        self.driver.find_element_by_xpath("// *[contains(text(), 'Photo/Video')]").click()
        sleep(1)
        self.driver.find_element_by_xpath("// *[contains(text(),'Upload photos/video')] // parent:: * // parent:: "
                                          "* // parent:: * // parent:: * // parent:: * // child::input").send_keys(
            file_location)
        sleep(10)

    #  Post string in argument for all to see
    def post(self, post_text="496d6d61206675636b20757020736f6d652066696465737a657320706f6c69746978207864", post_from=1):
        #  Go to own profile(0) or BOTPAGE(1)
        if post_from == 0:
            self.driver.find_element_by_xpath("//*[@id=\"u_0_a\"]/div[1]/div[1]/div/a").click()
            postboxstr = "What's on your mind?"
        elif post_from == 1:
            self.move_to_link("https://www.facebook.com/DeepFriedBoomers/?modal=admin_todo_tour")
            postboxstr = "Write a post..."
        else:
            print("Wrong Value..")
            postboxstr = "..."
            exit(11)
        sleep(5)

        #  Type in message
        self.driver.find_element_by_xpath("//*[@aria-label=\"{}\"]/child::*/child::*/child::*/child::*/child::*"
                                          "".format(postboxstr)).send_keys(post_text)
        #  WIP sharer with public
        if post_from == 0:
            self.driver.find_element_by_xpath("//a[starts-with(@aria-label,\"Shared with \")]").click()
            self.driver.find_element_by_xpath("//ul[@role=\"menu\"]/child::*/child::a").click()

        self.add_image_to_post("C:\\Users\\konrad.drexler\\PycharmProjects\\InstaBot_0\\pictures\\Yes_boomer.jpg")

        print("Ready to post")

        #  Confirmation downtime
        sleep(10)
        # Post post
        self.driver.find_element_by_xpath("//button[@data-testid=\"react-composer-post-button\"]").click()
        sleep(10)
        # Post post post


class NetBotMath:
    # Attributes that will be used for sure:
    __slots__ = ["driver", "z"]

    def __init__(self):
        self.z = 0
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })

        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://www.mathtrainer.org/")
        sleep(2)
        self.driver.find_element_by_xpath("//*[text()='Start']").click()
        print("Ready for questions")

    def loop_questions(self):  # TODO: dont wait set time answer asap
        print("Looping questions")
        while True:

            if len(self.driver.find_elements_by_class_name("a")) == 0:
                print(f"Done with this set: {self.z}!")
                break

            while True:

                try:
                    first_number = int(self.driver.find_elements_by_class_name("a")[0].text.replace(" ", ""))
                    second_number = int(self.driver.find_elements_by_class_name("b")[0].text.replace(" ", ""))
                    operator = self.driver.find_elements_by_class_name("operator")[0].text
                    answer = self.answer_question(first_number, second_number, operator)
                    break
                except:

                    pass
            if self.driver.find_elements_by_class_name("answer")[0].text == '?':
                self.send_answer(answer)

    def send_answer(self, answer):
        print(f"Sending answer: {answer}")
        typer = ActionChains(self.driver)
        typer.send_keys(answer)
        typer.perform()

    def answer_question(self, a, b, operator):
        print(f"Answering {a} {operator} {b}")
        if operator == '+':
            return a + b
        elif operator == '−' or operator == '−' or operator == '−':
            return a - b
        elif operator == '×':
            return a * b
        elif operator == '÷':
            return int(a / b)
        else:
            print("Unknown operator")
            raise Exception("Unkown operator")

    def next_question(self):
        while True:
            try:
                while True:
                    try:
                        for number in self.driver.find_elements_by_class_name("metric-value"):
                            print(number.text)
                        break
                    except:
                        pass
                self.driver.find_element_by_xpath("//*[text()='Train']").click()
                break
            except:
                pass

    def start(self):
        x = 0

        while True:
            if x == 45:
                y = input()
                x = x - int(y) - 1
            x += 1
            self.z += 1
            self.loop_questions()
            self.next_question()


class NetBotMonkey:
    # Attributes that will be used for sure:
    __slots__ = ["driver", "username"]

    def __init__(self):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })

        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://monkeytype.com/")
        sleep(1)
        seed(1)
        print("Ready to type")

    def type(self, init_wait):
        sleep(init_wait)
        html_list = self.driver.find_elements_by_class_name("word")
        stacker = 0.00
        counter = 0
        for word in html_list:
            counter += 1
            items = word.find_elements_by_tag_name("letter")
            letters = []
            for item in items:
                letters.append(item.text)
            # print(f"Starting to print {letters}")
            braker = False
            for letter in letters:

                if round(uniform(0.05, 1), 10) > 0.98 - (stacker * stacker) and letters[-1] != letter and letters[0] != letter:
                    stacker = 0.00
                    typer = ActionChains(self.driver)
                    # print(f"Random!! at word: {letters} on letter: {letter}")
                    sleep(round(uniform(0.025, 0.05), 10))
                    typer.send_keys('d')
                    typer.send_keys(Keys.SPACE)
                    typer.perform()
                    braker = True
                    break
                self.hold_key(letter, 0.011)
                # print(f"{letter}")
                # sleep(round(uniform(0.04, 0.05), 10))
                if round(uniform(0.05, 1), 10) > 0.5 - stacker:
                    sleep(round(uniform(0.04, 0.05), 10))


                stacker += 0.05
            if braker:
                # print(f"{letters}")
                continue
            if round(uniform(0.05, 1), 10) > 0.35 - stacker and (15 < counter < 20):
                stacker += 0.1
                sleep(round(uniform(0.04, 0.06), 10))
            typer = ActionChains(self.driver)
            typer.send_keys(Keys.SPACE)
            typer.perform()
            if round(uniform(0.05, 1), 10) > 0.96 - stacker:

                sleep(round(uniform(0.04, 0.05), 10))
            if round(uniform(0.05, 1), 10) > 0.9 - stacker:
                stacker = 0.00
                sleep(round(uniform(0.04, 0.05), 10))
            # TODO: Refactor stacker outsource stuff into methods

            # print(f"Finished printing: {letters}")
            # print(f"Done: {letters}")

    def hold_key(self, letter, delay):
        typer = ActionChains(self.driver)
        typer.key_down(letter)
        sleep(delay)
        typer.key_up(letter)
        typer.perform()

    def login(self):
        self.driver.get("https://monkeytype.com/login")
        self.driver.find_element_by_xpath('//*[@id="ncmp__tool"]/div/div/div[3]/div[1]/button[2]').click()

        self.driver.find_element_by_xpath('//*[@id="middle"]/div[5]/div[3]/form/input[1]').send_keys(
            "konrad@totalcar.hu")
        self.driver.find_element_by_xpath('//*[@id="middle"]/div[5]/div[3]/form/input[2]').send_keys("botlol69")
        self.driver.find_element_by_xpath('//*[@id="middle"]/div[5]/div[3]/form/div[2]').click()
        sleep(1)
        self.driver.get("https://monkeytype.com")
        print("Login done")


if __name__ == '__main__':
    #  Initiates Bot
    blitz = NetBotMonkey()
    blitz.login()
    blitz.type(2)
    # blitz = NetBotMath()

    # new_text = "Login Complete.\nBot online.\nBuild: beta_0.1.2\nReady to Post...\n\n"
    # link = "google.com"
    # blitz.move_to_link(link)
    # blitz.search("Gergely Farkas")
    # new_text += FuNnY(blitz.get_post())
    # blitz.post(post_text=new_text, post_from=1)
