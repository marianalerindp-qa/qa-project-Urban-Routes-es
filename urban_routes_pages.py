import selenium.webdriver.common.driver_finder
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import main
import data


class UrbanRoutesPage:
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    take_taxi_button = (By.CSS_SELECTOR, "button.button.round")
    tariff_picker = (By.CSS_SELECTOR, ".tariff-picker")
    tcard_comfort = (By.XPATH, "//div[contains(@class,'tcard')][.//div[text()='Comfort']]")

    #Elementos para agregar un número de teléfono
    phone_number_button = (By.CSS_SELECTOR, "div.np-button > div.np-text")
    phone_number_field = (By.ID, "phone")
    phone_number_next = (By.CSS_SELECTOR, "button.button.full")
    phone_code_field = (By.CSS_SELECTOR, "input[id='code'][placeholder='xxxx']")
    phone_code_confirm_button = (By.XPATH, "//button[@class='button full' and text()='Confirmar']")

    #Elementos para agregar una tarjeta
    add_pay_button = (By.CSS_SELECTOR, "div.pp-button.filled > div.pp-text")
    add_card_button = (By.CSS_SELECTOR, "div.pp-row.disabled")
    card_number_field = (By.CSS_SELECTOR, "#number")
    cvv_number_field = (By.CSS_SELECTOR, "#code")
    card_space = (By.CSS_SELECTOR, ".card-wrapper")
    add_card_number_button = (By.CSS_SELECTOR, "div.pp-buttons > button[type='submit']")
    close_pay_section_button = (By.CSS_SELECTOR, "button.close-button")

    #Elementos de requisitos extras
    message_field = (By.ID, "comment")
    reqs_manta_check= (By.XPATH, f"//div[@class='r-sw-container'][.//div[text()='Manta y pañuelos']]//input[@type='checkbox']")
    reqs_manta_switch= (By.XPATH, "//div[text()='Manta y pañuelos']/following::span[@class='slider round'][1]")
    reqs_icecream_counter = (By.XPATH, "//div[contains(text(),'Helado')]/ancestor::div[contains(@class,'r-counter-container')]//div[contains(@class,'counter-value')]")
    reqs_icecream_plus = (By.XPATH, "//div[text()='Helado']/following::div[@class='counter-plus']")
    reserve_taxi_button = (By.CSS_SELECTOR, "button.smart-button")
    reserve_taxi_confirm = (By.CSS_SELECTOR, "div.app > .order")


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, address_from):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property("value")

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


    #Seleccionar tarifa
    def take_taxi(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.take_taxi_button))
        self.driver.find_element(*self.take_taxi_button).click()

    def select_tariff(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.tcard_comfort))
        self.driver.find_element(*self.tcard_comfort).click()

    def is_taxi_selected(self):
        taxi = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.tariff_picker))
        return "shown" in taxi.get_attribute("class")

    def is_tariff_selected(self):
        tariff = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.tcard_comfort))
        return "active" in tariff.get_attribute("class")
        #return self.driver.find_element(*self.tcard_comfort).is_selected()

    #Agregar número de teléfono
    def click_phone_number(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.phone_number_button))
        self.driver.find_element(*self.phone_number_button).click()

    def set_phone_number(self, phone_number):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.phone_number_field))
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.phone_number_next).click()

    def set_phone_code(self, code):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.phone_code_field))
        self.driver.find_element(*self.phone_code_field).send_keys(code)

    def click_confirm_code(self):
        WebDriverWait(self.driver,10).until((expected_conditions.visibility_of_element_located(self.phone_code_confirm_button)))
        self.driver.find_element(*self.phone_code_confirm_button).click()

    def get_phone_number(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.phone_number_button))
        return self.driver.find_element(*self.phone_number_button).text

    def get_phone_code(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.phone_code_field))
        return self.driver.find_element(*self.phone_code_field).get_property("value")

    #Agregar tarjeta de pago
    def add_pay(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.add_pay_button))
        self.driver.find_element(*self.add_pay_button).click()

    def add_card(self):
        self.driver.find_element(*self.add_card_button).click()

    def set_card_number(self, card_number):
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(self.card_number_field))
        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        self.driver.find_element(*self.card_number_field).send_keys(Keys.TAB)

    def set_card_code(self, card_code):
        element = self.driver.find_element(*self.cvv_number_field)
        self.driver.execute_script("""
                arguments[0].value = arguments[1];
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """, element, card_code)

    def click_space(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.card_space))
        self.driver.find_element(*self.card_space).click()

    def blur_active_element(self):
        self.driver.execute_script("document.activeElement.blur();")

    def is_add_card_button_enabled(self):
        element = self.driver.find_element(*self.add_card_number_button)
        return element.is_enabled()



    def add_card_number(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(self.add_card_number_button))
        self.driver.find_element(*self.add_card_number_button).click()

    def close_pay_section(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.close_pay_section_button))
        self.driver.find_element(*self.close_pay_section_button).click()

    def get_new_card(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_new_code(self):
        return self.driver.find_element(*self.cvv_number_field).get_property('value')

    #Agregar requisitos al conductor
    def set_message(self,message_for_driver):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.message_field))
        self.driver.find_element(*self.message_field).send_keys(message_for_driver)

    def get_message(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    def click_reqs_manta(self):
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(self.reqs_manta_switch))
        self.driver.find_element(*self.reqs_manta_switch).click()

    def get_reqs_manta(self):
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(self.reqs_manta_check))
        return self.driver.find_element(*self.reqs_manta_check).is_selected()

    def add_icecream(self, count):
        icecream = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(self.reqs_icecream_plus))
        for n in range(count):
            icecream.click()

    def get_icecream(self):
        return self.driver.find_element(*self.reqs_icecream_counter).text

    def reserve_taxi(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.reserve_taxi_button))
        self.driver.find_element(*self.reserve_taxi_button).click()

    def wait_modal_appears(self):
        taxi = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.reserve_taxi_confirm))
        return "shown" in taxi.get_attribute("class")