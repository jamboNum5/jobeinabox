import requests
import timeit

def test_jobe_in_abox(sourcecode):
    url = 'http://127.0.0.1:4000/jobe/index.php/restapi/runs'
    language_id = 'cpp'
    sourcefilename = 'test.cpp'
    data = {
        'run_spec': {
            'language_id': language_id,
            'sourcefilename': sourcefilename,
            'sourcecode': sourcecode
        }
    }

    response = requests.post(url, json=data)
    print(response.text)

sourcecode_hello_world = """
#include <iostream>

int main() {
    std::cout << "Hello world" << std::endl;
}
"""

sourcecode_while_true = """
#include <iostream>

int main() {
    while (true) {  
    }
    std::cout << "Hello world" << std::endl;
}
"""

sourcecode_system_call = """
#include <iostream>
#include <cstdlib>

int main() {
    system("ls");
}
"""

print("Testing hello world")
extime = timeit.timeit(lambda:test_jobe_in_abox(sourcecode_hello_world), number=1)
print("Finished testing hello world", extime)

print("Testing while true")
extime = timeit.timeit(lambda: test_jobe_in_abox(sourcecode_while_true), number=1)
print("Finished testing while true", extime)

print("Testing system call")
extime = timeit.timeit(lambda: test_jobe_in_abox(sourcecode_system_call), number=1)
print("Finished testing system call", extime)