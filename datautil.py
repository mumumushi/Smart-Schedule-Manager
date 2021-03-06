# -*- coding: utf-8 -*-
#
# a special parse data tool set
# #
import json
import time as T
import threading
from request_tts import request_tts


#
# 保存返回结果，并判断请求时候成功，返回result字典
# #
def parse_response(r, queue):
    result = {}
    f = open('temp/result.json','w') #要用try...其实可以不保存的，为了调bug而已
    f.write(r)
    f.close()
    j = json.loads(r)
    if j["desc"] == "success":
        result = parse_data(j, queue)
    return result

#
# 粗提取数据并选择下一步对应的操作，返回result字典
# #
def parse_data(j, queue):
    data = j["data"]
    
    result = {}
    for i in data:
        if i["sub"] == "nlp":  #check if is nlp
            j = i["intent"]
            if (len(j) != 0):  #check if this intent is empty
                intent = j
                
                if "answer" in intent:
                    #answer
                    answer = intent["answer"]   
                    answer = answer["text"]
                    result["answer"] = answer       
                    #获取到答案之后迅速在另一个线程中请求tts
                    task = threading.Thread(target=request_tts, args=(answer, queue,))
                    task.start()

                    ask = intent["text"]
                    result["ask"] = ask
                    
                    if "semantic" in intent:
                        semantic = intent["semantic"]
                        semantic = semantic[0]

                        #intent
                        intent = semantic["intent"]  
                        result["intent"] = intent

                        slots = semantic["slots"]

                        #判断意图intent
                        if intent == "query_schedule_with_time":            #查询行程
                            result["time"] = get_time(slots)
                        elif intent == "query_schedule_without_time":   
                            pass                 
                        elif intent == "query_add_time":   
                            result["time"] = get_time(slots)                   

                        elif intent == "add_schedule_with_time":            #添加行程
                            result["time"] = get_time(slots)
                            result["thing"] = get_thing(slots)
                        elif intent == "add_schedule_without_time":
                            result["thing"] = get_thing(slots)
                        elif intent == "add_add_time":
                            result["time"] = get_time(slots)
                        
                        elif intent == "query_other_schedule_with_time":    #查询别人的行程
                            result["name"] = get_name(slots)
                            result["time"] = get_time(slots)
                        elif intent == "query_other_schedule_without_time":
                            result["name"] = get_name(slots)
                        elif intent == "query_other_add_time":
                            result["time"] = get_time(slots)
                        else:                                               #其它
                            pass
                    else:
                        pass
                   
                else:
                    answer = "不好意思，我好像没听懂。。。"
                    result["answer"] = answer
                    queue.put("DONT_UNDERSTAND")
    if len(result) == 0:
        answer = "不好意思，我好像没听懂。。。"
        result["answer"] = answer
        queue.put("DONT_UNDERSTAND")

    return result


#
# 提取返回结果的time
# 返回时间time为str, 格式有两种，2018-01-01TAM 或2018-01-01T08:00:00
# #
def get_time(slots):
    time = None
    for slot in slots:
        if slot["name"] == "time":
            time = slot["normValue"]
            datetime = time[time.index("datetime")+11:time.index("\",\"suggestDatetime")]
            suggestDatetime = time[time.index("suggestDatetime")+18:time.index("\"}")]
    
            #处理时间格式                               #还有几种编码。。像凌晨，傍晚这些词。。
            n = len(datetime)
            if n == 13:                                #日期带一个上午，一个下午，或者一个晚上的格式
                time = datetime
            elif n == 19:                              #日期带具体时间的形式
                time = datetime
            elif n == 10:                              #只有一个日期，被我在后面加一个TTT伪装成第一种形式
                time = datetime + "TTT"
            elif n == 9 or n == 3:                     #只有一个时间或者一个TAM，TPM等，需要判断，再给他加上个合适的日期
                suggestTime = T.mktime(T.strptime(suggestDatetime,'%Y-%m-%dT%H:%M:%S'))
                curTime = T.time()
                if (suggestTime <= curTime):
                    suggestTime = suggestTime + 86400  #加上24h的秒数，获得明天的时间戳
                    date = T.strftime("%Y-%m-%d", T.localtime(suggestTime)) #转化成日期字符串
                    time = date + datetime
                else :
                    time = suggestDatetime
            elif n == 14:                               #中午TMID，凌晨TEAM 改成中午TMI, 凌晨TEA
                time = suggestDatetime
            else :
                print("Ooooooops somthing wrong!")
            
    return time

#
# 提取返回结果的thing
# #
def get_thing(slots):  
    thing = None
    for slot in slots:
        if slot["name"] == "thing":
            thing = slot["normValue"]
    return thing

#
# 提取返回结果的人名
# #
def get_name(slots):
    name = None
    for slot in slots:
        if slot["name"] == "people":
            name = slot["normValue"]
    return name