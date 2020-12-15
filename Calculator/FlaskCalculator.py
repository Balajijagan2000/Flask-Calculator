import webbrowser
from threading import Timer
import math
from flask import *
import re


obj=Flask(__name__)
global value
value=''
#squareroot funciton:
def squareroot(value):
    _val=value
    for count,j in enumerate(value):
        #print(count)
        if(j=='√'):
            a=count
            #print(value[0:a])
            str1=''
            #print(a)
            for cnt,i in enumerate(value[a:]):
                #print(i)
                if(i!='+' and i!='-' and i!='*' and i!='%' and i!='/'):
                    str1=str1+i
                    #print(str1)
                else:
                    
                    break
                    
            #print(str1)
            #str2=int(str1[1:])
            #print(str2)
            #print(str1[1:])
            str2=str(eval('math.sqrt(float(str1[1:]))'))
            #print(str2)
            _val=_val.replace(str1,str2)
            str1=''
            #val=value[0:a]+str2+value[a+1:]
            
    #return _val      
    #return str1       
    if('^' in _val):
        _val=_val.replace("^","**")
        return _val
    else:
        
        return _val 
    
@obj.route("/")
def view():
    
    
    return render_template("calculator.html")


@obj.route("/calculate",methods=["POST","GET"])
def print():
    if request.method == "POST":
        
        
        if(request.form.get('btn')!='=' and request.form.get('btn')!='C' and request.form.get('btn')!='<'):
            if(request.form.get('txtbx')=='Math Error'):
                
                global value
                value=''
                if(request.form.get('btn')!='='):
                    value=request.form.get('btn')
                    return render_template('calculator.html',val=value)
                else:
                    return render_template('calculator.html',val=value)
            else:
                
                a=str(request.form.get('btn'))
                #global value
                value=str(value)+a
                return render_template('calculator.html',val=value)
        elif(request.form.get('btn')=='='):
            
            if('√' in request.form.get('txtbx')):
                
                    
                _value=request.form.get('txtbx')
                if(re.findall('\+/',_value) or re.findall('\-/',_value) or re.findall('\*/',_value) or re.findall('\+%',_value) or re.findall('\-%',_value) or re.findall('\*%',_value) or re.findall('\%%',_value) or re.findall('\^^',_value) or re.findall('\.\.',_value)):
                        return render_template("calculator.html",val="Math Error")
                else:
                    
                    value=squareroot(_value)
                    try:
                        
                        value=eval(value)
                        return render_template('calculator.html',val=value)
                    except:
                        return render_template('calculator.html',val="Math Error")
            elif('√' not in request.form.get('txtbx')):
                
                
                
                _val=request.form.get('txtbx')
                
                    
                if(re.findall('\+/',_val) or re.findall('\-/',_val) or re.findall('\*/',_val) or re.findall('\+%',_val) or re.findall('\-%',_val) or re.findall('\*%',_val) or re.findall('\%%',_val) or re.findall('\^^',_val) or re.findall('\.\.',_val)):
                    
                    #print(i)
                    return render_template("calculator.html",val="Math Error")
                    
                    
                else:
                    
                    try:
                        
                        _val=_val.replace("^","**")
                        value=eval(_val)
                        return render_template('calculator.html',val=value)
                    except:
                        return render_template('calculator.html',val="Math Error")


        elif(request.form.get('btn')=='C'):
            value=''
            return render_template('calculator.html',val=value)
        elif(request.form.get('btn')=='<'):
            result=request.form.get('txtbx')
            n=len(result)
            value=result[:(n-1)]
            return render_template('calculator.html',val=value)
        #elif(request.form.get('btn')=='√'):
        
        
            
def open_browser():
    webbrowser.open_new('http://127.0.0.1:2000/')
      

        
#@obj.route("/",methods=["POST","GET"])
#def calculate():
    #if request.method=='POST':
        
#@obj.route("/calculate",methods=['POST','GET'])
#def clear():
    
    
 #   if(request.form.get('cbutton'=='C')):
  #      value=''
   #     return render_template('calculator.html',val=value)

if __name__=="__main__":
    
    Timer(1,open_browser).start();
    obj.run(port=2000)
