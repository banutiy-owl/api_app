import subprocess
import threading

def run_flask_app():
    subprocess.call(["python", "controllers.py"])

def run_tkinter_app():
    subprocess.call(["python", "web.py"])

if __name__ == '__main__':

    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    run_tkinter_app()