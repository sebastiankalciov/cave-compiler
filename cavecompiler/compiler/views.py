from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import subprocess

def home(request):
    
    temp_cpp_file = "temp.cpp"

    with open(temp_cpp_file, "w") as temp_file:
        temp_file.write("#include <iostream> \n using namespace std; int main() {return 69;}")

    run_output = "No result"
    
    try:
        compile_output = subprocess.run(["g++", "-o", "temp", temp_cpp_file], capture_output=True)

        if compile_output.returncode == 0:
            run_output = subprocess.run(["./temp"], capture_output = True, text = True)
    
        run_output = run_output.returncode

    except:
        run_output = compile_output.stderr

    page = loader.get_template("compiler/index.html")
    return HttpResponse(run_output)