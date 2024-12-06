from selene import browser, have

browser.open('https://google.com')
browser.element('[id=APjFqb]').type('Say Hello World with python').press_enter()
browser.element('[id=search]').should(have.text('Say "Hello, World!" With Python'))
browser.element('[name=q]').clear().type('wqaerofwenfoin').press_enter()
browser.element('[id=center_col]').should(have.text('wqaerofwenfoin'))