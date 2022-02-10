# InstantID/TruCredential Background Process Runner

A fairly simlpe Flask application to run in the background to accept HTTP POST/GET request to run executable/process by IID/TruCred workflow call.

- Can work with IID/TruCred with Web service app feature only (Ent edition)
- This is a workaround but not a proper way to integrate
- Use at your own risks

## Installation

The script requires [pyInstaller](https://pyinstaller.readthedocs.io/en/stable) to compile standalone executable.

Install the dependencies
```sh
pip install -r requirements.txt
```

Change code if necessary
Pack the `run.py` into executable (remove `--noconsole` for debugging)
```sh
pyinstaller --onefile --noconsole run.py
```

Run executable
```sh
run.exe [PORT NUMBER (Optional, default 2036)]
```

Add the service in *Data Sources* > *Web Services*.
- Type `Generic`
- Web Service type `REST`
- URL `http://localhost:2036`
- Authentication method `None`

Edit the workflow you want to launch custom application during enrolment runtime.
- Add workflow step *Web Service Interface*
- Configure the path in *Properties*
    - Fields > Advanced > Opeartion: `Write`
    - Write URL `run?path=[your path to executable&param=your parameters]` (parameter optional)
    - Verb `POST`
    - Add a random input field in *Field Connection* and map a random workflow field to save the changes


## Disclaimer
This is just a workaround to those who want to integrate IID/TC software and it is provided on a "AS-IS" basis, with no warranty.
I am not responsible for any loss caused by the application and this is not an offical workaround, use at your own risk and feel free to change the code.