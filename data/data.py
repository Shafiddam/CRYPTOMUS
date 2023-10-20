# note --------------------   Адреса кошельков:
# region
# 001 = аккаунт enot_2022_001@mail.ru
trx_001 = 'EQB94TnVLzqszq0sR3Mo5weDJLSEUzTmtZ4uQIg8S_kT3ppQ'
usdt_polygon_001 = '0xfa6ff48df53bd9daf7f21024e82636e67971e5fb'
xmr_monero_001 = '8Aiy886tZbCNDDKyBddWAf2eGWrYbJakCDnjCEbMcBZdHag9i6jLGtWbwPcErVz3SC3fUxpGHC43sKeJgEyqWGWj2tZodyT'
ton_001 = 'EQBtm_lUIJkq3gSM9mrOPa701IyHV_4sT9VriF9TIyfc76gi'
btc_001 = 'bc1qhxuyu4w4rn5fnuskaldjhul3vrpqm35elr8jh5'

# с номером 15 = аккаунт 89058308055 (enot_2022_015@mail.ru)
trx_015 = 'TPHE1AXMYt8Y5png8PvZWdmpEwAayemhhL'
usdt_polygon_015 = '0x7ff3875f1c43adba160b97432359fc5da0ef0d9a'
xmr_monero_015 = '88KggJdNHNdBmZSzPRsBFQSdAjmCmJ8UGVP2eJKTJsFpAxAqxkismDf5ARhCNr282e6zbMnYnaWqDZciqFkzJPd1QhFpsgN'
ton_015 = 'EQB94TnVLzqszq0sR3Mo5weDJLSEUzTmtZ4uQIg8S_kT3ppQ'
btc_015 = 'bc1q9xysrp22zx2575af5quluxnxr67448c029s56a'

# Мой публичный адрес для получения USDT (Trust Wallet):
usdt_trust_wallet = '0x6B6dD11c39f7F247Bd1FFE9F3B2a6246C44e248C'
# endregion

secret_key_001 = 'Y3FUI6TI5TGVQ62D'; account_001 = 'enot_2022_001@mail.ru'
##################
link_prod = 'https://app.cryptomus.com/dashboard/'
link_signup = 'https://app.cryptomus.com/signup'
link_login = 'https://app.cryptomus.com/login'
link_prod_personal = 'https://app.cryptomus.com/dashboard/'
link_prod_business = 'https://app.cryptomus.com/dashboard/business/'
link_prod_p2p = 'https://app.cryptomus.com/dashboard/p2p-balance/'
phone_number = '89058308055'
bot_token = ''  # токен бота в телеграм
chat_id = ''  # мой Chat ID в телеграм

password_for_new_email = ''  # пусть будет такой новый пароль
new_password_for_change_password = 'Change!psw!2023'  # пусть будет такой новый пароль
passwords = {
    "enot_2022_001@mail.ru": "Enot!@2022"
}
# Словарь для соответствия кода валюты и символа
currency_symbols = {
    'JPY': '¥',
    'TMT': 'TMT',
    'AMD': '֏',
    'PHP': '₱',
    'UZS': 'Soʻm',
    'USD': '$',
    'PLN': 'zł',
    'ISK': 'kr',
    'GBP': '£',
    'DKK': 'kr',
    'NOK': 'kr',
    'RUB': '₽',
    'CZK': 'Kč',
    'CHF': '₣',
    'EUR': '€',
    'KZT': '₸',
    'CAD': '$',
    'UAH': '₴',
    'TRY': '₺',
    'SEK': 'kr',
    'IDR': 'Rp',
    'INR': '₹',
    'VND': '₫',
    'CNY': '元',
    'KRW': '₩',
    'MYR': 'MYR',
    'THB': '฿',
    'AZN': '₼'
}

# region selectors
selector_btn_phone_number = 'form > div.form__title-wrapper > div > div:nth-child(2)'
selector_input_phone_number = 'form > div.form__input-wrapper > div:nth-child(1) > div > input'
selector_input_password = 'form > div.form__input-wrapper > div:nth-child(2) > div > input'
selector_error = 'div.form__input-wrapper > div:nth-child(4) > div > span'

svg_logo = '#root > nav > div > div > div.navbar__avatar > a > div > svg' # кубик
svg_logo_text = '#root > nav > div > div > div.navbar__avatar > a > div > span' # текст Cryptomus
btn_sign_up = '#root > nav > div > div > div.navbar__content > div.content__button > a > button'
selector_btn_tonkeeper = 'div.LoginSocial_icon__wrapper__lmsQI'
selector_btn_telegram = '#telegram-login-cryptomus_accountbot'
btn_google_login = "div.LoginSocial_button__wrapper__1SHW2 > div:nth-child(1)"
btn_apple_login = "div.LoginSocial_button__wrapper__1SHW2 > a > div"
selector_btn_qr_code = 'div.LoginSocial_button__wrapper__1SHW2>div:nth-child(4)'
selector_qr_tonkeeper_pict  = '#react-qrcode-logo'
selector_qr_pict  = 'QRLogin_qr__wrapper__siibJ'
selector_message_text = "//*[contains(@class,'ModalHead_modal_actions__title')][text()='Log in via TonKeeper']"
selector_message_text2 = "//*[contains(@class,'ModalHead_modal_actions__title')][text()='Sign up via TonKeeper']"
selector_qr_message_text = "//*[contains(@class,'ModalHead_modal_actions__title')][text()='Log in with QR code']"
selector_qr_code_tonkeeper = '#react-qrcode-logo'
selector_modal_tonkeeper = 'div > div.Modal_modal_content__8KQIg'
selector_modal_qr = 'div > div.ModalHead_wrapper__L9c46'
selector_qr_code_pict = "div>div.Modal_modal_content__8KQIg>div>div>svg"

# selector_btn_login = "button.btn.primary.large"
selector_input_mail= "input[name='login']"
selector_checkbox_device = '.PrivateSwitchBase-input'
selector_input_code_2fa = '.ConfirmCodeForm_input__hy3\+H>div>input'
selector_btn_theme = 'div.content__actions>div.actions__theme-controller>button'
selector_zendesk_help_text = 'body > div > div > div > button > div'
selector_language_btn = 'div.actions__language>div>div>button'
selector_language_dropdown_menu = 'div.DropdownLanguage_dropdown__menu__Fcjwz'
selector_reset_password = "//a[@class='form__link'][text()='Forgot your password?']"
selector_input_login = 'input.form__input[name="login"]'
selector_input_code = 'input.form__input[name="code"]'
selector_reset_continue = "//span[@class='button-text large'][text()='Continue']"
selector_btn_login = "//span[@class='button-text large'][text()='Login']"
btn_next = "//span[text()='Next']"
btn_next_in_apple = "//button[@id='sign-in']"
selector_btn_signup = "//span[@class='button-text large'][text()='Sign up']"
selector_btn_create = "//span[@class='button-text large'][text()='Create an account']"
selector_reset_confirm = "//span[@class='button-text large'][text()='Confirm']"
selector_login_confirm = "//span[@class='button-text large'][text()='Confirm']"
selector_enter_password = 'input.form__input[name="password"]'
selector_reset_create = "//span[@class='button-text large'][text()='Create']"
selector_password_link = "//a[contains(text(), 'Forgot your password?')]"
agree_terms = 'checkbox__label'
enter_code = 'input[name="code"]'
# endregion



# region Mail.ru
btn_enter_mail_primary = "[data-testid='enter-mail-primary']"  # кнопка "Войти" на главной
iframe_iframe = "ag-popup__frame__layout__iframe"
input_user_name = 'input[name="username"]'
btn_next_button = "[data-test-id='next-button']"  # кнопка "Ввести пароль"
input_password = 'input[name="password"]'
btn_submit_button = "[data-test-id='submit-button']"  # кнопка "Войти" в модалке ввода пароля
field_registration = "//span[@class='ll-sj__normal'][text()='Registration']"
field_binding_google_2fa = "//span[@class='ll-sj__normal'][text()='Binding google 2FA']"
btn_back_in_mail = "._3s9BW3cG2EDQ_ySBGAaZVY" #!!!
field_personal_wallet_transactions = "//span[@class='ll-sj__normal'][text()='Personal wallet transactions']"
field_business_wallet_transactions = "//span[@class='ll-sj__normal'][text()='Business wallet transactions']"
field_p2p_wallet_transactions = "//span[@class='ll-sj__normal'][text()='P2P Wallet Transactions']"
attach_download = ".attach-list__controls-element-download"
element_code = "//p[contains(text(), 'Your code:')]"
element_text = "//p[contains(text(), 'Withdrawals are frozen until') and contains(text(), 'because you changed email')]"
# endregion

# модалка кукис:
selector_cookie_modal = '.CookieModal_wrapper__CRNPp'
# selector_btn_cookie_confirm = '#root > div > div.CookieModal_button_wrapper__uzNb9 > button.btn.primary.large'
selector_btn_cookie_confirm = '#root > div > div.CookieModal_button_wrapper__uzNb9 > button.btn.primary.small > span'
selector_btn_cookie_partners = '#root > div > div.CookieModal_button_wrapper__uzNb9 > button.btn.outlined.large'
svg_logo = '#root > nav > div > div > div.navbar__avatar > a > div > svg'  # кубик
svg_logo_text = '#root > nav > div > div > div.navbar__avatar > a > div > span'  # текст Cryptomus
btn_sign_up = '#root > nav > div > div > div.navbar__content > div.content__button > a > button'
selector_qr_code_modal_tonkeeper = 'div>div.Modal_modal_content__8KQIg>div>div>div>div'
selector_qr_code_modal_qr = "div>div.Modal_modal_content__8KQIg>div>div>svg"
selector_btn_theme = 'div.content__actions>div.actions__theme-controller>button'
selector_zendesk_help_text = 'body > div > div > div > button > div'
selector_language_btn = 'div.actions__language>div>div>button'
selector_language_dropdown_menu = 'div.DropdownLanguage_dropdown__menu__Fcjwz'
selector_input_1 = 'input.form__input'
selector_reset_continue = "//span[@class='button-text large'][text()='Continue']"
selector_reset_confirm = "//span[@class='button-text large'][text()='Confirm']"
selector_password_link = "//a[contains(text(), 'Forgot your password?')]"


# region Dashboard
selector_btn_personal_withdrawal = "//*[contains(@class,'control-button__text')][text()='Withdrawal']"
select_network_in_pay_button = "//*[@class='css-h0tzer']"
# select_network_in_pay = "//*[@class='css-h0tzer'][text()='tron (TRC-20)']"
select_network_need_in_pay = "//*[@class='css-h0tzer']"  #
btn_personal_withdrawal_select_wallet = "//*[contains(@class,'css-m5dwgz')][text()='Crypto wallet']"
input_subject_in_modal_ticket = "//input[@name='subject' and contains(@class, 'form__input')]"
input_message_in_modal_ticket = "//textarea[@name='message' and @class='Tickets_multInput__ilExK']"
input_search_find_currency = '.InputSearch_input__Lx2Hk'
input_find_currency = '//input[@placeholder="Find currency"]'
input_search_find_currency_in_show_more = '.WalletBalancesModal_wrapper_header__91ybm .InputSearch_input__Lx2Hk'
input_name_of_recurring_payment = "input[placeholder='Name of recurring payment']"
input_search_find_currency_in_pay = "//input[@role='combobox'][@placeholder='Search']"
select_first_currency = 'downshift-0-item-0'
subject_in_ticket = '.Tickets_ticket_item_title__n-MDo'
message_in_ticket = "//div[@class='Chat_message__TisQd Chat_my_message__dffY9']/p"
write_message_in_ticket = "//textarea[@placeholder='Write message...']"
btn_send_message_in_ticket = "//span[@class='button-text large' and text()='Send']"
btn_resume_message_in_ticket = "//span[@class='button-text large' and text()='Resume']"
# btn_add_pin_code_in_security = "//div[contains(@class, 'content__item single_row') and .//p[contains(@class, " \
#         "'text__title') and text()='PIN code'] and .//span[contains(@class, 'button-text large') and text()='Add']]"
btn_add_pin_code_in_security = "div > div:nth-child(5) > div.item__control.pin > div > button > span"
input1_add_pin_code_in_security = "form > div > div > form > input:nth-child(1)"
input2_add_pin_code_in_security = "form > div > div > form > input:nth-child(2)"
input3_add_pin_code_in_security = "form > div > div > form > input:nth-child(3)"
input4_add_pin_code_in_security = "form > div > div > form > input:nth-child(4)"
modal_new_ticket = ".Modal_modal__yEgVW"
selector_currency_text__name = "//*[contains(@class,'SelectorCurrency_text__name')][text()='USDT']"
selector_currency_text__name_usd = "//*[contains(@class,'SelectorCurrency_text__name')][text()='USD']"
usdt_in_static_wallet = "//span[@class='item__name'][text()='USDT']"
currency_text_name_usdt = "//*[contains(@class,'text__name')][text()='USDT']"
input_wallet_address = 'address'
input_address = '//input[@placeholder="Address"]'
amount_to_auto_withdrawal = '//input[@placeholder="Auto-withdrawal amount"]'
insert_blockchain_name = '//input[@placeholder="Enter blockchain name"]'
insert_hash_text = '//input[@placeholder="Enter hash"]'
insert_coin_name = '//input[@placeholder="Enter coin or token name"]'
btn_select_network = "//*[contains(@class,'css-xigvda')][text()='Select network']"
invoice_select_network = "//span[text()='Select network']"
btn_select_network_polygon = "//*[contains(text(), 'Polygon')]"
btn_create_payment = "//button[.//span[@class='button-text large'][text()='Create payment']]"
error_invalid_code_message = "//span[@class='error__description'][text()='Invalid code.']"
snackbar_message_in_pay_locator = "#notistack-snackbar"
snackbar_create_ticket = "//div[@id='notistack-snackbar' and @class='SnackbarItem-message' and text()='Ticket sent']"
snackbar_close_ticket = "//div[@id='notistack-snackbar' and @class='SnackbarItem-message' and text()='Ticket closed']"
selector_invoice_share_link = "//span[contains(@class, 'copy__text') and contains(@class, 'text__cutted') and contains(text(), 'https://pay.cryptomus.com/pay/')]"
static_wallet_invoice_share_link = "//span[contains(@class, 'copy__text') and contains(@class, 'text__cutted') and contains(text(), 'https://pay.cryptomus.com/wallet/')]"
recurring_payment_invoice_share_link = "//span[contains(@class, 'copy__text') and contains(@class, 'text__cutted') and contains(text(), 'https://pay.cryptomus.com/recurring/')]"
invoice_qrcode_logo = "react-qrcode-logo"
pay_static_wallet_qr_code = '.checkout__qr-wrapper'
invoice_static_wallet_qrcode_logo = "react-qrcode-logo"
input_amount_to_send = 'amount'
input_in_spot = '//form[contains(@class, "Buy_form_buy__lzEJl")]//input[contains(@placeholder, "Enter amount")]'
input_in_spot_to_sell = '//form[contains(@class, "Sell_form__sell")]//input[contains(@placeholder, "Enter amount")]'
input_in_spot_limit_to_buy = '//form[contains(@class, "Buy_form_buy__lzEJl")]//input[contains(@placeholder, "Enter amount")]'
input_in_spot_limit_to_sell = '//form[contains(@class, "Sell_form__sell")]//input[contains(@placeholder, "Enter amount")]'
input_in_spot_limit_market_price = '//form[contains(@class, "Buy_form_buy__lzEJl")]//input[contains(@placeholder, "Market price")]'
input_in_spot_limit_market_price_in_sell = '//form[contains(@class, "Sell_form__sell")]//input[contains(@placeholder, "Market price")]'
input_amount_set_limit_price = 'div:nth-child(2) > div.Form_input__6\+OIz > div.Form_amount_input__qhiaF > div > ' \
                               'div > div > span > div > input'
btn_withdraw = "//span[@class='button-text large'][text()='Withdraw']"
btn_show_more = "//span[@class='button-text large'][text()='Show more']"
input_code_2fa = 'code'
btn_confirm = "//span[@class='button-text large'][text()='Confirm']"
btn_logout = "//span[@class='button-text large'][text()='Logout']"
close_modal_bind_google_success = "//span[@class='button-text large'][text()='Got it!']"
close_modal_got_it = "//span[@class='button-text large'][text()='Got it!']"
merchant_name_01 = "//span[@class='merchant__name'][text()='01']"
btn_mass_payout = "//span[normalize-space(@class)='control-button__text' and normalize-space(text())='Mass payout']"
btn_personal_transfer = "//span[normalize-space(@class)='control-button__text' and normalize-space(text())='Transfer']"
btn_personal_convert = "//span[normalize-space(@class)='control-button__text' and normalize-space(text())='Convert']"
btn_convert_spot = "//p[text()='Spot']"
btn_download_transaction = ".Filter_download_excel_wrapper__lXRNd"
btn_spot_limit = "//span[@class='button-text medium'][text()='Limit']"
btn_buy_in_convert_spot_limit = ".Buy_button__jlTFU"
btn_convert_spot_market_buy = ".Buy_button__jlTFU"
btn_convert_spot_market_sell = ".Sell_button__fFmyU"
btn_convert_limit = "//span[normalize-space(@class)='button-text medium' and normalize-space(text())='Limit']"
close_modal_balances_of_personal_wallets = "button.ModalHead_button__wrapper__4evjY"
close_modal = "div.ModalHead_close__wrapper__1LY\+b > button"
btn_convert_in_convert_market = "//span[@class='button-text large' and text()='Convert']"
btn_convert_in_convert_limit = "//span[@class='button-text large' and text()='Place the order']"
btn_business_transfer = "//span[normalize-space(@class)='control-button__text' and normalize-space(text())='Transfer']"
btn_p2p_transfer = "//span[normalize-space(@class)='control-button__text' and normalize-space(text())='Transfer']"
btn_personal_transfer_select_wallet = "//span[normalize-space(@class)='control-button__text' and normalize-space(text())='Transfer']"
btn_transfer_confirm = "//span[normalize-space(@class)='button-text large' and normalize-space(text())='Transfer']"
btn_personal_wallet = "//a[text()='Personal wallet']"
btn_business_wallet = "//a[text()='Business wallet']"
btn_p2p_wallet = "//a[contains(@class, 'Sidebar_links__item__h7dw-') and contains(@href, '/dashboard/p2p-balance/')]"
usdt_sent = "//p[normalize-space(@class)='TransactionHeaderItem_titleText__PI2MO' and normalize-space(text())='USDT Sent']"
bind_google_success = ".bind-google__success"
usdt_received = "//p[normalize-space(@class)='TransactionHeaderItem_titleText__PI2MO' and normalize-space(text())='USDT Received']"
# btn_disable_pin_code = "//div[contains(@class, 'content__item single_row') and .//p[contains(@class, 'text__title') " \
#             "and text()='PIN code'] and .//span[contains(@class, 'button-text large') and text()='Disable']]"
btn_disable_pin_code = "//span[contains(@class, 'button-text large') and text()='Disable']"
amount_usdt = "//p[contains(@class, 'TransactionHeaderItem_amountTitle') and contains(normalize-space(), '1 USDT')]"
btn_create_merchant = "//div[contains(@class, 'add-button__text') and contains(normalize-space(), 'Create merchant')]"
btn_confirm_create_merchant = "//span[contains(@class, 'button-text large') and contains(normalize-space(), 'Create merchant')]"
btn_send = "//span[@class='button-text large']/span[text()='Send']"
btn_send_add_coin = "//span[@class='button-text large' and text()='Send']"
btn_close_modal_create_merchant = "button.ModalHead_button__wrapper__4evjY"
out_new_feature = ".ShadowAlert_shadow__wrapper__GOca6"
small_man = "div.dropdown-profile"  # button.IconButton_icon_button__+CB4E.IconButton_large__wcTzA"
select_settings = "//button[text()='Settings']"
select_currency = "//button[text()='Сurrency']"
add_coin = "div.Sidebar_wallets__title_wrapper__pk3d1 > div > button:nth-child(2)"
auto_withdrawal = "//a[text()='Auto-withdrawal']"
promo_code = "//a[text()='Promo code']"
btn_kyc = "//a[text()='KYC personal wallet']"
btn_verification = "//span[@class='button-text large'][text()='Verification']"
promo_code_activate = "//span[@class='button-text large'][text()='Activate']"
account_deleting = "//a[text()='Account deleting']"
btn_add_address = "//span[@class='button-text large'][text()='Add address']"
btn_delete = "//span[@class='button-text large'][text()='Delete']"
btn_change_email_in_security = "//span[@class='button-text large'][text()='Change']"
btn_change_password_in_security = "//div[@class='item__control password']//span[@class='button-text large' and text()='Change']"
btn_add_phone_number_in_security = "//div[contains(@class, 'content__item') and .//p[contains(@class, 'text__title') " \
                        "and text()='Phone number'] and .//span[contains(@class, 'button-text') and text()='Add']]"
btn_continue_in_add_phone = "//span[@class='button-text large'][text()='Continue']"
btn_enable_in_security = "//span[@class='button-text large'][text()='Enable']"
btn_plus_merchant = "div.Sidebar_header__add_button__aX9rh > button"
btn_create_in_modal_ticket = "//button[@class='btn primary large']/span[text()='Create']"
btn_close_ticket = ".Tickets_close_ticket_modal__5escI"
btn_yes_in_close_ticket = "//span[@class='button-text large'][text()='Yes']"
input_merchant_name = 'input[name="merchantName"]'
input_email = 'identifierId'
input_email_in_apple = "//input[@type='text' and @id='account_name_text_field']"
input_password_in_google = '//input[@aria-label="Enter your password"]'
input_password_in_apple = '//input[@id="password_text_field"]'
btn_rm_merchant_confirm_yes = "//span[@class='button-text large'][text()='Yes']"
rm_merchant_notistack_snackbar = '//div[@id="notistack-snackbar" and contains(., "Your merchant was successfully deleted")]'
invalid_code = "//span[@class='error__description'][text()='Invalid code.']"
snackbar_temporarily_frozen = '//div[@id="notistack-snackbar" and contains(., ' \
                              '"Withdrawals are temporarily blocked, the reason for mail change")]'
snackbar_send_email = "//div[@id='notistack-snackbar' and text()='We will send the file to email']"
snackbar_add_coin = "//div[@id='notistack-snackbar' and text()='Your request has been sent']"
snackbar_pincode_enabled = '//div[@class="SnackbarItem-message" and text()="PIN code set successfully"]'
snackbar_pincode_disabled = '//div[@class="SnackbarItem-message" and text()="PIN code disabled successfully"]'
error_notistack_snackbar = '//div[@id="notistack-snackbar" and contains(., "We can\'t create an order now. Please, try again later")]'
# error_notistack_snackbar = "#notistack-snackbar"
merchant__name = "//span[@class='merchant__name'][text()='111']"
merchant__name_template = "//span[@class='merchant__name'][text()='{}']"
btn_payment_by_link = "//span[@class='control-button__text  '][text()='Payment by link']"
select_type_payment = "//span[@class='InvoiceMethodDropdown_item__name__FmpjD'][text()='Invoice']"
type_payment_static_wallet = "//span[@class='InvoiceMethodDropdown_item__name__FmpjD'][text()='Static wallet']"
type_payment_recurring_payment = "//span[@class='InvoiceMethodDropdown_item__name__FmpjD'][text()='Recurring payment']"
invoice_amount_in_pay = "//span[@class='payment-details__amount'][text()='10']"
invoice_currency_in_pay = "//span[@class='payment-details__amount'][text()='USDT']"
invoice_network_in_pay = "//div[contains(@class,'payment-details__subheading')]/span[contains(text(),'POLYGON')]"
invoice_wallet_address_in_pay = "//span[contains(@class,'share__address') and contains(text(),'0xa499fff7881db5ed170198f425f98b83')]"
invoice_any_wallet_address_in_pay = "//span[@class='share__address']"
wallet_connect_in_pay = "//button[contains(text(),'WalletConnect')]"
pay_via_fiat = "//button[contains(text(),'Pay via fiat')]"
btn_pay_in_pay = '//button[contains(@class, "btn") and contains(@class, "primary") and contains(@class, "large") and text()="Pay"]'
btn_ticket = "a[href='/dashboard/tickets/']"
btn_new_ticket = "//div[@class='add-button__text' and text()='New ticket']"
btn_selector_currency = ".SelectorCurrency_selector__header__ymVZE"
# btn_select_currency_in_pay = "span.css-104rgjn"
btn_select_currency_in_pay = "div.css-veoc3i.e1656iwc8 > svg"
btn_select_currency_invoice = "//div[contains(@class,'title__text')]/span[contains(text(),'Select currency')]"
dropdown_list_network = "div.css-1cqo8tx.e1656iwc9"
dropdown_list_network_fiat = "//div[@data-is_selector='true' and contains(@class, 'css-veoc3i')]"
select_currency_in_static_wallet = '//div[contains(@class, "selector__header") and .//span[text()="Select currency"]]'
select_currency_in_convert_market = '//div[contains(@class, "selector__header") and .//span[text()="Select"]]'
selector_manual_convert_currency = '//span[contains(@class, "SelectorManualConvert_selected") and text()="Select"]'
selector_convert_limit_currency_to = 'div:nth-child(4)>div.Form_input__6\+OIz>div.SelectorManualConvert_selector_manual_convert__Q7G2Y > div.SelectorManualConvert_selector__header__nQTaZ>div.SelectorManualConvert_header__text__rPY21 > span.SelectorManualConvert_selected__Zls21'
selector_convert_limit_expires_in = '.SelectorManualConvert_selected__Zls21'
secret_key_field = '//span[@class="copy__text text__cutted"]'
insert_code2fa_generate_in_modal = '//input[@placeholder="Code"]'
insert_email_code_in_modal = '//input[@placeholder="Enter code"]'
current_email_code_in_change_email = 'div:nth-child(1) > div.ConfirmCodeForm_input__hy3\+H > div > input'
new_email_code_in_change_email = 'div:nth-child(2) > div.ConfirmCodeForm_input__hy3\+H > div > input'
insert_new_email_in_change_email = '//input[@placeholder="Email"]'
insert_new_phone_number = '//input[@placeholder="+1 (102) 123-4567"]'
insert_old_password = '//input[@placeholder="Old password"]'
insert_new_password = '//input[@placeholder="New password"]'
insert_password = '//input[@placeholder="Enter password"]'
insert_promocode = '//input[@placeholder="Enter your promo code"]'
confirm_new_password = '//input[@placeholder="Confirm new password"]'
insert_confirm_code = '//input[@placeholder="Enter code"]'
selector_one_hour = '//li[.//span[text()="1 Hour"]]'
coin_in_add_address = '//div[contains(@class, "title__text") and .//span[text()="Select coin"]]'
btn_receive = '//span[contains(@class, "control-button__text  ")][text()="Receive"]'
btn_generate_new_address = 'button.btn.recreate_btn.secondary.medium'
btn_generate_new_address_in_modal = '//span[@class="button-text large"][text()="Generate new address"]'
btn_order_history = '//span[@class="button-text large"][text()="Order history"]'
expand_in_order_history = '.WalletManualConvertHistoryTableRow_title__icon__eYKZS'
btn_select_crypto_wallet = '//span[@class="css-m5dwgz"][text()="Crypto wallet"]'
wallet_address_in_receive = '//span[@class="copy__text text__cutted"]'
# endregion