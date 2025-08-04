import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import SCREENSHOT_DIR

# driver manager
driver_registry = {}
driver_lock = threading.Lock()

def init_driver():
    """
        Init a chrome driver
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920x1080")
    
    return webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=chrome_options
    )

def capture_screenshot(task_id, driver):
    """
        Capture screenshots
    """
    try:
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, total_height)
        # save screenshot
        screenshot_path = str(SCREENSHOT_DIR / f"task_{task_id}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Task_{task_id}: 截图已保存至 {screenshot_path}")
    except Exception as e:
        print(f"Task_{task_id}: 截屏失败 - {str(e)}")