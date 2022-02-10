import subprocess
import sys
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   #   Cross Origin Resource Sharing (CORS) handling

#   Run pyinstaller --onefile --noconsole run.py  to pack as .exe to run at background

@app.route("/")
def index():
    return '/run?path=[Executable Path]\nparam=[parameter(optional)] to run local executable.'

#   Read GET request and run executable by reading path and parameters
#   /run?path=[Executable Path]&param=[Parameters]
@app.route("/run", methods=['GET', 'POST'])
def runExec():
    executableFilePath = request.values.get('path')
    parameter = request.values.get('param')
    print("Executable Path: " + str(executableFilePath) + "\n" + "Param: " + str(parameter))
    try:
        if parameter is not None:
            #   Run with parameter
            result = subprocess.run([str(executableFilePath), str(parameter)], stdout=subprocess.PIPE)
            print(result.stdout)
        else:
            #   Run without parameter
            result = subprocess.run([str(executableFilePath)], stdout=subprocess.PIPE)
            print(result.stdout)
    except Exception as e:
        print(str(e))
    return "Success"

#   Default port 2036
if len(sys.argv) != 2:
    app.run(port=2036)
else:
    try:
        #   Custom port
        app.run(port=sys.argv[1])
    except Exception as e:
        print(str(e))