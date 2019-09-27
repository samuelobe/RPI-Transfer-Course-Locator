from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import filedialog

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver.exe',chrome_options = options)
driver.get('https://myproviderhq.com/v3app/a/?6713520D04184E041C0D022C0D140C1C130C11166E1E0A300C0B18584A1F4E2F0C0F42151B110C560D0D7815545D0B50061110795F5D345200435D074717655C000A4345574550580D2659565C56045D0F55321717210C060B00014E5A7900545B175F5311440C0C70594A5D5C53565F127145507A0606085D574A447E5C545D4715471C111C072253232C5F2727344502472362565659585241180C5C55594C5B22445F292C74575E5156275D42470044/&redir=1') 
driver.maximize_window()

