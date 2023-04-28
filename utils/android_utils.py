import subprocess


def get_device_udid():
    output = subprocess.check_output(["adb", "devices"]).decode().split('\n')
    device = output[1].split("\t")[0]

    return device


def android_get_desired_capabilities():
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "adbExecTimeout": 60000,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "13",
        "resetKeyboard": True,
        "systemPort": 8306,
        "takesScreenshot": True,
        # "udid": get_device_udid(),
        "deviceName": "Pixel 4 API 33",
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
