def tachTu(path,sen):
    sen=sen.lower();
    sen=sen.lstrip();
    sen=sen.rstrip();
    sen=sen.rstrip('.');
    sen=sen.replace(',','');
    sen=sen.replace('.','');
    sen=sen.replace(';','');
    sen=sen.replace(':','');

    f=open(path,encoding="utf8");

    f1=f.readlines();
    dic=dict();
    for x in f1:
        temp=x.split("\t\t");
        if(len(temp)==2):
            dic[temp[0]]=temp[1];
    sen=sen.split(" ");
    y=[];
    temp=""; # chuổi trước đó
    lenght=len(sen);
    for pos in range(0,lenght):
        if (temp+sen[pos]) in dic:
            temp=temp+sen[pos]+" ";

            if(pos==lenght-1):
                y.append(temp.rstrip());
            
        else:
            y.append(temp.rstrip());
            temp=sen[pos]+" ";
            
            if(pos==lenght-1):
                y.append(temp.rstrip());
    f.seek(0);
    return y;


path ="dictionary.txt"
sen=input('Nhập câu cần tách: ');
rs=tachTu(path,sen)
print('Kết quả tách từ: ',rs)