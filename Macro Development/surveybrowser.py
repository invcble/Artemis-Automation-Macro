import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Survey Browser")
window.setGeometry(200, 100, 1500, 1000)

browser = QWebEngineView(window)
window.setCentralWidget(browser)

settings = browser.settings()
settings.setAttribute(QWebEngineSettings.PluginsEnabled, False)

profile = browser.page().profile()
profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)

url = QUrl.fromUserInput(sys.argv[1])
browser.setUrl(url)

window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)

window.show()
sys.exit(app.exec_())