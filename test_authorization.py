import requests as r

SERVER_API_ADDRESS = "http://192.168.1.106:5000/api/"


def login() -> None:
    """emulate login for testing purposes"""
    resp = r.post(
        SERVER_API_ADDRESS + "employee/log-in",
        json={"workbench_no": 1, "employee_rfid_card_no": "0008368511"},
    )
    print(resp.json())


if __name__ == "__main__":
    login()
