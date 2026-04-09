import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import main


class UrbanRoutesPage:
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    take_taxi_button = (By.CLASS_NAME, "button round")
    tcard_comfort = (By.XPATH, "//div[@class='tariff-picker shown']/div[text()='Comfort']")

    #Elementos para agregar un número de teléfono
    phone_number_button = (By.CLASS_NAME, "np-button")
    phone_number_field = (By.CLASS_NAME, "label")
    phone_number_next = (By.CLASS_NAME, "button full")
    phone_code_field = (By.CSS_SELECTOR, "input[id='code'][placeholder='xxxx']")
    phone_code_confirm_button = (By.XPATH, "//button[@class='button full' and text()='Confirmar']")

    #Elementos para agregar una tarjeta
    add_pay_button = (By.CLASS_NAME, "pp-button filled")
    add_card_button = (By.CLASS_NAME, "pp-row disabled")
    card_number_field = (By.ID, "number")
    cvv_number_field = (By.ID, "code")
    card_space = (By.CLASS_NAME, "plc")
    add_card_number_button = (By.CLASS_NAME, "button full")
    close_pay_section_button = (By.CLASS_NAME, "close-button section-close")

    #Elementos de requisitos extras
    message_field = (By.ID, "comment")
    reqs_manta= (By.XPATH, "//div[contains(text(), 'Manta y pañuelos')]//span[@class='slider round']")
    reqs_icecream =(By.CSS_SELECTOR, "div:has-text('Helado') .counter-plus")
    reserve_taxi_button = (By.CLASS_NAME, "smart-button")


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, address_from):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


    #Seleccionar tarifa
    def take_taxi(self):
        self.driver.find_element(*self.take_taxi_button).click()

    def select_tariff(self):
        self.driver.find_element(*self.tcard_comfort).click()


    #Agregar número de teléfono
    def click_phone_number(self):
        self.driver.find_element(*self.phone_number_button).click()

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def set_phone_code(self, phone_code):
        self.driver.find_element(*self.phone_code_field).send_keys(phone_code)

    def click_confirm_code(self):
        self.driver.find_element(*self.phone_code_confirm_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_button).text

    #Agregar tarjeta de pago
    def add_pay(self):
        self.driver.find_element(*self.add_pay_button).click()

    def add_card(self):
        self.driver.find_element(*self.add_card_button).click()

    def set_card_number(self,card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self,card_code):
        self.driver.find_element(*self.cvv_number_field).send_keys(card_code)

    def add_card_number(self):
        self.driver.find_element(*self.add_card_number_button).click()

    def close_pay_section(self):
        self.driver.find_element(*self.close_pay_section_button).click()

    def get_new_card(self):
        return self.driver.find_element(*self.card_number_field).text
    def get_new_code(self):
        return self.driver.find_element(*self.cvv_number_field).text

    #Agregar requisitos al conductor
    def set_message(self,message_for_driver):
        self.driver.find_element(*self.message_field).send_keys(message_for_driver)
    def get_message(self):
        return self.driver.find_element(*self.message_field).text

    def click_reqs_manta(self):
        self.driver.find_element(*self.reqs_manta).click()

    def add_icecream(self):
        self.driver.find_element(*self.reqs_icecream).click(2)

    def reserve_taxi(self):
        self.driver.find_element(*self.reserve_taxi_button).click()

    def wait_modal_appears(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "oder-shown")))
