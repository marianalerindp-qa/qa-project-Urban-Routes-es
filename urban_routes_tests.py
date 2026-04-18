import data
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main import retrieve_phone_code
from urban_routes_pages import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)

    def setup_method(self):
        self.driver.get(data.urban_routes_url)

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == address_to

    def test_reserve_taxi_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.take_taxi()
        routes_page.select_tariff()
        assert routes_page.is_taxi_selected() == True
        assert routes_page.is_tariff_selected() == True

    def test_add_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.take_taxi()
        routes_page.select_tariff()

        routes_page.click_phone_number()
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_phone_code(code)
        routes_page.click_confirm_code()
        assert routes_page.get_phone_number() == data.phone_number

    def   test_add_pay(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.take_taxi()
        routes_page.select_tariff()

        routes_page.add_pay()
        routes_page.add_card()
        routes_page.set_card_number(data.card_number)
        assert routes_page.get_new_card() == data.card_number
        routes_page.set_card_code(data.card_code)
        assert routes_page.get_new_code() == data.card_code

        routes_page.blur_active_element()
        routes_page.click_space()

        assert routes_page.is_add_card_button_enabled() == True
        routes_page.add_card_number()
        routes_page.close_pay_section()

    def test_write_message_to_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.take_taxi()
        routes_page.select_tariff()

        routes_page.set_message(data.message_for_driver)
        assert routes_page.get_message() == data.message_for_driver

    def test_reqs_manta(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.take_taxi()
        routes_page.select_tariff()

        routes_page.click_reqs_manta()
        assert routes_page.get_reqs_manta() == True

    def test_reqs_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.take_taxi()
        routes_page.select_tariff()

        routes_page.add_icecream(2)
        assert routes_page.get_icecream() == "2"

    def test_taxi_search_modal_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.take_taxi()
        routes_page.select_tariff()

        routes_page.reserve_taxi()
        routes_page.wait_modal_appears()
        assert routes_page.wait_modal_appears() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()