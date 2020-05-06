import re

faultname_pattern = re.compile(r':(.*)\(')
faultcode_pattern = re.compile(r'\b0x[0-9A-F]+\b')
s = 'F: MyFaultName(MyFaultCode,0xaEAD1eEF,"This is my fault description.",0,3)'

y = s.split('\"')[2].split(',')[2].split(')')[0].strip()
print(y)