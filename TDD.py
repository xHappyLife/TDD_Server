# #1
# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')

# assert 'Django' in browser.page_source

#2
from selenium import webdriver
browser = webdriver.Chrome()

# 张三听说有一个在线待办事项的应用
# 他去看了这个应用的首页
browser.get('http://localhost:8000')

# 他注意到网页里包含了“To-Do”这个词
assert 'To-Do' in browser.title, "Browser title was " + browser.title

# 应用有一个输入待办事项的文本输入框

# 他在文本输入框中输入了“Buy flowers”

# 他按下回车键后，页面更新了
# 待办事项表格中显示了“1: Buy flowers”

# 页面中又显示了一个文本输入框，可以输入其他待办事项

# 他输入了“Send a gift to Lisi”，并按下回车键

# 页面再次更新，他的清单中显示了这两个待办事项

# 张三想知道这个网站是否会记住他的清单
# 他看到网站为他生成了一个唯一的URL

# 他访问那个URL，发现待办事项列表还在
# 他很满意地离开了

browser.quit()