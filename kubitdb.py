# Eğer proplem olursa discord.gg/4Xpwwz6pgN yazabilirsiniz
# Version: 1.0.0

"""
MIT License

Copyright (c) 2022 kubilay

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

dosyaismi = "database"

try:#Dosya yoksa dosya oluşturur
    open(dosyaismi+".kubitdb", 'r',encoding="utf-8")
except FileNotFoundError:
    with open(dosyaismi+".kubitdb", "w",encoding="utf-8") as f:
        f.write('')
file = open(dosyaismi+".kubitdb", "r",encoding="utf-8").read()

def get(aranacak):
    if aranacak == "": return "false"
    try:
        for x in range(file.count("\n")+1):
            if file.split()[x].split("=")[0] == aranacak:return file.split()[x].split("=")[1]
    except: return "false"

def set(aranacak,deger):
    if deger == "" or aranacak == "": return "false"
    try:
        for x in range(file.count("\n")+1):
           filew = open(dosyaismi+".kubitdb", "w",encoding="utf-8")
           if file.split()[x].split("=")[0] == aranacak:
               filew.write(file.replace(str(file.split()[x]),str(file.split()[x].split("=")[0])+"="+str(deger)))
           else:filew.write(file+"\n"+str(aranacak)+"="+str(deger))
    except:
        filew = open(dosyaismi+".kubitdb", "w",encoding="utf-8")
        filew.write(str(aranacak)+"="+str(deger))

def delete(deger):
    if deger == "": return "false"
    try:
        for x in range(file.count("\n")+1):
            if file.split()[x].split("=")[0] == deger:
                filew = open(dosyaismi+".kubitdb", "w",encoding="utf-8")
                filew.write(file.replace(file.split()[x],"").replace("\n\n","\n"))
    except:return "false"
