

import os
import subprocess
import scipy
import fileinput

start_urls = (
        ['https://tools.keycdn.com/speed?url=seitestes.ml&location=uklo&public=1','londondata.txt'],
        ['https://tools.keycdn.com/speed?url=seitestes.ml&location=frpa&public=1','parisdata.txt'],
        ['https://tools.keycdn.com/speed?url=seitestes.ml&location=sgsg&public=1','singaporedata.txt'],
        ['https://tools.keycdn.com/speed?url=seitestes.ml&location=usny&public=1','nydata.txt'],
        ['https://tools.keycdn.com/speed?url=seitestesml.000webhostapp.com&location=uklo&public=1','londondataN.txt'],
        ['https://tools.keycdn.com/speed?url=seitestesml.000webhostapp.com&location=frpa&public=1','parisdataN.txt'],
        ['https://tools.keycdn.com/speed?url=seitestesml.000webhostapp.com&location=sgsg&public=1','singaporedataN.txt'],
        ['https://tools.keycdn.com/speed?url=seitestesml.000webhostapp.com&location=usny&public=1','nydataN.txt'],
    )

def transform_line(line,url,k):
    if k==0:
        line = line.replace('URLTOSWAP', url)
    else:
        line = line.replace(url, 'URLTOSWAP')
    return line


def run_all():
    input_dir = os.getcwd()
    for url,file2 in start_urls:
        with open('testes\spiders\output.py', "w") as output_file, open("testes\spiders\lucy.py") as input_file:
            output_file.write("".join(transform_line(line,url,0) for line in input_file))
        os.unlink("testes\spiders\lucy.py")
        os.rename('testes\spiders\output.py', "testes\spiders\lucy.py")
        print("C:\Python27\Scripts\scrapy crawl lucy >> {}".format(file2))
        proc = subprocess.Popen("C:\Python27\Scripts\scrapy crawl lucy >> {}".format(file2), shell=True, stdout=subprocess.PIPE)
        proc.wait()
        with open('testes\spiders\output.py', "w") as output_file, open("testes\spiders\lucy.py") as input_file:
            output_file.write("".join(transform_line(line,url,1) for line in input_file))
        os.unlink("testes\spiders\lucy.py")
        os.rename('testes\spiders\output.py', "testes\spiders\lucy.py")


if __name__ == "__main__":
    for i in range(30):
        print('\n\n\n\n\n\n\n')
        print('RUN NUMBER ',i)
        run_all()





