from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

current_file_path = os.path.realpath(__file__)
current_file_dir = os.path.dirname(current_file_path)

@app.route('/')
def hello():
    return 'Hello, Welcome to my app!'

@app.route('/utilization')
def StatusReport():
    path = __file__
    disk_space = subprocess.getoutput('sh ' + current_file_dir + '/' + 'disk_space.sh')
    cpu_utilization = subprocess.getoutput('sh ' + current_file_dir + '/' + 'cpu_utilization.sh')
    final_output = disk_space + '\n' + cpu_utilization

    return render_template('index.html', output=final_output)

@app.route('/service/<port>')
def ServiceRunning(port):
    service_output = subprocess.getoutput('sh ' + current_file_dir + '/' + f'find_service.sh {port}')
    
    return render_template('index.html', output=service_output)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

