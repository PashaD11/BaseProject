from selene.support.conditions.be import *
from selene.browser import *
from selene.api import *

class Homepage:

    def click_sign_in_button(self):
        s('[data-mqarker="Responsive_desktop"] [data-testid="sign_in_button"]').click()
