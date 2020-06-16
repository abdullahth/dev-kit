def rmtree_onerror(function, path, exec_info):
    '''
    Onerror Handeller for shutil.rmtree()
    Usage: 
    import shutil
    shutil.rmtree(filepath, onerror=rmtree_onerror)

    Resouce: https://stackoverflow.com/a/2656405/12468930
    '''
    import os 
    import stat

    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)

        function(path)
    

def export_vars(username, path):
    '''
    Writes a shell File with the Important Variable for commands.sh
    Example:

    export USERNAME='Value'
    export DIR='Value'
    '''
    import os

    with open(os.path.join(os.path.dirname(__file__), 'dataset/vars.sh'), 'w') as f:
        f.write(
            "export USERNAME=\"{}\"\nexport DIR=\"{}\"".format(username, path)
        )


def browser():
    '''
    - Creating Selenium browser and return it
    - Create WebDriverWait Object and return it
    return (browser, wait)

    Unpaking:
    browser, wait = Methods.browser() 
    Hint: Replace the undesirable element with _
    '''
    # Importing Statments
    from selenium import webdriver  
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.support.ui import WebDriverWait

    # Browser
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # Wait Object
    wait = WebDriverWait(browser, timeout=10)

    return(browser, wait)

def wait(driver, timeout):
    '''
    Creating Special Wait Object
    '''
    from selenium.webdriver.support.ui import WebDriverWait
    wait = WebDriverWait(driver, timeout)
    return wait
