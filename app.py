import subprocess
import threading

def run_flask_app():
    subprocess.call(["python", "api_endpoints.py"])

def run_tkinter_app():
    subprocess.call(["python", "gui.py"])

if __name__ == '__main__':

    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    run_tkinter_app()
