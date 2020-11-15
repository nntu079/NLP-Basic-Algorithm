#no edit 0 : s1_1: pop s1, s2_1: pop s2, s3_1: in " "
#replace 1 : s1_1: pop s1, s2_1: pop s2, s3_1: in "R"
#insert  2 : s1_1: in *  , s2_1: pop s2, s3_1: in "I"
#delete  3 : s1_1: pop s1, s2_1: in *  , s3_1: in "D"

def MED(s1,s2):
    s1="#"+s1;
    s2="#"+s2;
    
    l1=len(s1);
    l2=len(s2);
    table=[];

    #tạo mảng ban đầu
    for j in range(0,l1):
        temp=[];
        for i in range(0,l2):
            temp.append(i);
        table.append(temp);
        table[j][0]=j;
    #bảng đường đi    
    for i in range(1,l1):
        for j in range(1,l2):
            if(s1[i]==s2[j]):
                table[i][j]=table[i-1][j-1];
            else:
                table[i][j]=min(table[i][j-1]+1,table[i-1][j]+1,table[i-1][j-1]+2);
    #truy vết
    #current=[[x,y,type];
    rs=[];
    i=l1-1;
    j=l2-1;
    while i>0:
        if j>0:
            temp1=min(table[i-1][j],table[i][j-1],table[i-1][j-1]);
            if temp1==table[i][j-1]:#insert =>type=2
                current=[i,j-1,2];
                rs.insert(0,current);
                j=j-1;
            elif temp1==table[i-1][j-1]: #replace 
                if(temp1)==table[i][j]:  # no edit =>type=0
                    current=[i-1,j-1,0];
                    rs.insert(0,current);
                    i=i-1;j=j-1;
                else:                   #replace =>type = 1
                    current=[i-1,j-1,1];
                    rs.insert(0,current);
                    i=i-1;j=j-1;

            else:  #delete => type=3
                current=[i-1,j,3];
                rs.insert(0,current);
                i=i-1;
        else:
            break;
        
    
    while(1):
        temp=rs[0];
        if temp[0]!=0:
            current=[temp[0]-1,0,3];
            rs.insert(0,current);
        elif temp[1]!=0:
            current=[0,temp[1]-1,2];
            rs.insert(0,current);
        else:
            break;

    #chuỗi hiển thị kết quả
    s1_1="";
    s2_1="";
    s3_1="";
    pos1=1;
    pos2=1;
    for i in range(0, len(rs)):
        temp=rs[i];
        if(temp[2]==0):
            s1_1+=s1[pos1];
            pos1+=1;
            s2_1+=s2[pos2];
            pos2+=1;
            s3_1+=" ";
        elif(temp[2]==1):
            s1_1+=s1[pos1];
            pos1+=1;
            s2_1+=s2[pos2];
            pos2+=1;
            s3_1+="R";
        elif(temp[2]==2):
            s1_1+="*";
            s2_1+=s2[pos2];
            pos2+=1;
            s3_1+="I";
        elif(temp[2]==3):
            s1_1+=s1[pos1];
            pos1+=1;
            s2_1+="*";
            s3_1+="D";
    
    print(s1_1);
    print(s2_1);
    print(s3_1);
    print('R: replace, D: delete, I: insert');

while(1):
    s1=input('Nhập chuỗi s1: ');
    s2=input('Nhập chuỗi s2: ');
    MED(s1,s2);    







    

