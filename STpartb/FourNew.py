import os

validExtns=["txt","pdf","jpeg","jpg","png","py","cpp","c","java","html","xlsx","psd","docx"]

if __name__ == '__main__':
    inpPath = input("Enter the path to which you want to know the number of files present: ")
    objs = os.listdir(inpPath)
    extensions={}
    for each in objs:
        pos=each.find(".")
        ext=each[(pos+1):]
        if ext not in validExtns:
            continue
        else:
            if(ext not in extensions):
                extensions.update({ext:1})
            else:
                extensions[ext]=extensions[ext]+1
    print ("The files that are present are:")
    count=0
    for i in extensions:
        print(i, extensions[i])
        count+=extensions[i]
    print ("Total =",count)