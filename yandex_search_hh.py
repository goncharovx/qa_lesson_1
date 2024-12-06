from selene import browser, be, have
import time

browser.open('https://ya.ru/')
browser.element('[id=text]').should(be.blank).type('headhunter тестировщик').press_enter()
browser.element('[id=search-result]').should(have.text('Тестировщик'))

time.sleep(3)