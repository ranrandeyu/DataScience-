#建立一个不重复的选项集
def create(dateset):
    c1=[]
    #遍历所有的数据集所有记录中的每一项
    for transaction in dateset:
        for item in transaction:
            #！！！每项元素为单位添加,而非单个字母
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    #用frozenset的不变性作字典的键值使用
    return list(map(frozenset,c1))


#保留所有满足最小支持度的项集
#输入：变量数据集，候选项列表，最小支持度
#输出：大于最小支持度的元素列表
def scan(dateset,ck,minsupport):
    cnt={}
    #遍历所有数据集，候选集
    for t in dateset:
        for can in ck:
            #判断是否为子集
            if can.issubset(t):
                if can not in cnt.keys():
                    cnt[can]=0
                #！计算总数,全记录
                cnt[can]+=1
    numitem=len(dateset)
    #存放大于最小支持度的元素
    reslist=[]
    support_data={}
    #遍历字典中每个键值
    for key in cnt.keys():
        support=cnt[key]/numitem
        if support>=minsupport:
            reslist.append(key)
        support_data[key]=support
    #print("support_data:")
    #print(support_data)
    return reslist,support_data


#根据k-1项集生成k项集
#输入变量：频繁项集lk，项集元素k
#输出变量：每个子集个数k的不重复reslist
def apriori_gen(lk,k):
    reslist=[]
    len_lk=len(lk)
    for i in range(len_lk):
        for j in range(i+1,len_lk):
            if len(lk[i]|lk[j])==k:
                reslist.append(lk[i]|lk[j])
    #删去重复的项
    reslist=set(reslist)
    return reslist


#apriori
#输入：原始数据集dateset，最小支持度minsupport
def apriori(dateset,minsupport=0):
    c1=create(dateset)
    #扫描数据集，map（set，dateset）dateset只用一次，用完后为空
    D=list(map(set,dateset))
    l1,support_data=scan(D,c1,minsupport)
    #构建L列表，第一个元素为l1列表
    L=[l1]
    k=2
    while (len(L[k-2])>0):
        ck=apriori_gen(L[k-2],k)
        lk,support_k=scan(D,ck,minsupport)
        k=k+1
        L.append(lk)
        support_data.update(support_k)
    return L,support_data


#关联规则生成函数
#输入变量：频繁项集列表l，支持数据字典support_data,最小可信度min_conf
#输出变量：可信度的规则列表big_rule_list
def generate_rules(L,support_data,min_conf=0.1):
    big_rule_list=[]
    for i in range(1,len(L)):
        for f in L[i]:
            #print(f)
            h1=[frozenset([item]) for item in f]
            if i>1:
                rules_from_conseq(f,h1,support_data,big_rule_list,min_conf)
            else:
                calc_conf(f,h1,support_data,big_rule_list,min_conf)
    #print(big_rule_list)
    return big_rule_list


#计算规则可信度
#输入变量：频繁项集f，每个频繁项集转换为列表h，支持数据的字典support_data,规则brl
#输出变量：包含可信度的规则列表p_h
def calc_conf(f,h,support_data,brl,min_conf=0.5):
    p_h=[]
    for con in h:
        conf=support_data[f]/support_data[con]
    #print(conf)
    if conf>=min_conf:
        #！！！！三个参数以一个变量输入
        brl.append((f-con,con,conf))
        p_h.append(con)
    #依次输入增加
    #print("brl")
    #print(brl)
    return p_h,conf


#频繁项集中元素多于两个生成关联规则
#输入变量：频繁项集f，转换列表h，字典support_data,关联规则brl
def rules_from_conseq(f,h,support_data,brl,min_conf=0.5):
    m=len(h[0])
    if len(f)>(m+1):
        hmp1=apriori_gen(h,m+1)
        hmp1=calc_conf(f,hmp1,support_data,brl,min_conf)
        if (len(hmp1)>1):
            hmp1=apriori_gen(hmp1,m+1)
            rules_from_conseq(f,hmp1,support_data,brl,min_conf)


dateset = [line.split() for line in open('sleep-mood.dat')]
L,support=apriori(dateset,minsupport=0)
print("支持度conf:")
print(support)
rules=generate_rules(L,support)
print("置信度support:")
print(rules)










