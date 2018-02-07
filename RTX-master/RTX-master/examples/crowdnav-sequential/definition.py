# Simple sequantial run of knob values
import random
name = "CrowdNav-Sequential"
arr =[]

execution_strategy = {
    "ignore_first_n_results": 100,
    "sample_size": 100,
    "type": "sequential",
    "knobs": [
        {"route_random_sigma": 0.0},
        {"route_random_sigma": 0.1},
        {"route_random_sigma": 0.2},
        {"route_random_sigma": 0.3},
        {"route_random_sigma": 0.4},
        {"route_random_sigma": 0.5},
        {"route_random_sigma": 0.6},
        {"route_random_sigma": 0.7},
        {"route_random_sigma": 0.8},
        {"route_random_sigma": 0.9},
        {"route_random_sigma": 1.0},
        {"route_random_sigma": 1.1},
        {"route_random_sigma": 1.2},
        {"route_random_sigma": 1.3},
        {"route_random_sigma": 1.4},
        {"route_random_sigma": 1.5},
        {"route_random_sigma": 1.6},
        {"route_random_sigma": 1.7},
        {"route_random_sigma": 1.8},
        {"route_random_sigma": 1.9},
        {"route_random_sigma": 2.0},
        {"route_random_sigma": 2.1},
        {"route_random_sigma": 2.2},
        {"route_random_sigma": 2.3},
        {"route_random_sigma": 2.4},
        {"route_random_sigma": 2.5},
        {"route_random_sigma": 2.6},
        {"route_random_sigma": 2.7},
        {"route_random_sigma": 2.8},
        {"route_random_sigma": 2.9},
        {"route_random_sigma": 3.0},
        {"route_random_sigma": 3.1},
        {"route_random_sigma": 3.2},
        {"route_random_sigma": 3.3},
        {"route_random_sigma": 3.4},
        {"route_random_sigma": 3.5},
        {"route_random_sigma": 3.6},
        {"route_random_sigma": 3.7},
        {"route_random_sigma": 3.8},
        {"route_random_sigma": 3.9},
        {"route_random_sigma": 4.0},
        {"route_random_sigma": 4.1},
        {"route_random_sigma": 4.2},
        {"route_random_sigma": 4.3},
        {"route_random_sigma": 4.4},
        {"route_random_sigma": 4.5},
        {"route_random_sigma": 4.6},
        {"route_random_sigma": 4.7},
        {"route_random_sigma": 4.8},
        {"route_random_sigma": 4.9},
        {"route_random_sigma": 5.0},
        {"route_random_sigma": 5.1},
        {"route_random_sigma": 5.2},
        {"route_random_sigma": 5.3},
        {"route_random_sigma": 5.4},
        {"route_random_sigma": 5.5},
        {"route_random_sigma": 5.6},
        {"route_random_sigma": 5.7},
        {"route_random_sigma": 5.8},
        {"route_random_sigma": 5.9},
        {"route_random_sigma": 6.0},
        {"route_random_sigma": 6.1},
        {"route_random_sigma": 6.2},
        {"route_random_sigma": 6.3},
        {"route_random_sigma": 6.4},
        {"route_random_sigma": 6.5},
        {"route_random_sigma": 6.6},
        {"route_random_sigma": 6.7},
        {"route_random_sigma": 6.8},
        {"route_random_sigma": 6.9},
        {"route_random_sigma": 7.0},
        {"route_random_sigma": 7.1},
        {"route_random_sigma": 7.2},
        {"route_random_sigma": 7.3},
        {"route_random_sigma": 7.4},
        {"route_random_sigma": 7.5},
        {"route_random_sigma": 7.6},
        {"route_random_sigma": 7.7},
        {"route_random_sigma": 7.8},
        {"route_random_sigma": 7.9},
        {"route_random_sigma": 8.0},
        {"route_random_sigma": 8.1},
        {"route_random_sigma": 8.2},
        {"route_random_sigma": 8.3},
        {"route_random_sigma": 8.4},
        {"route_random_sigma": 8.5},
        {"route_random_sigma": 8.6},
        {"route_random_sigma": 8.7},
        {"route_random_sigma": 8.8},
        {"route_random_sigma": 8.9},
        {"route_random_sigma": 9.0},
        {"route_random_sigma": 9.1},
        {"route_random_sigma": 9.2},
        {"route_random_sigma": 9.3},
        {"route_random_sigma": 9.4},
        {"route_random_sigma": 9.5},
        {"route_random_sigma": 9.6},
        {"route_random_sigma": 9.7},
        {"route_random_sigma": 9.8},
        {"route_random_sigma": 9.9}       
    ]
}

def feedbackStarProvider(arr):
    return max(arr,key=arr.count)


# def primary_data_reducer(state, newData, wf):
#     print("state ",state)
#     # print("arr ",arr)
#     # print("newData ",newData)
#     cnt = state["count"]
#     # arr.append(random.randint(1,5))
#     arr.append(newData["totalTripFeedbackAverage"])
#     # arr[cnt]=random.randint(1,5)
#     state["feedback"]=max(arr,key=arr.count)
#     # state["feedback"]=random.randint(1,5)
#     print("overhead "+newData["overhead"])
#     print("feedback "+newData["totalTripFeedbackAverage"])
#     state["avg_overhead"] = (state["avg_overhead"] * cnt + newData["overhead"]) / (cnt + 1)
#     # if (state["avg_overhead"])
#     state["count"] = cnt + 1
#     return state

def primary_data_reducer(state, newData, wf):
    print("state ",state)
    if(state["count"]==0):
        state["avgFeedback"]=0
    cnt = state["count"]
    state["avg_overhead"] = (state["avg_overhead"] * cnt + newData["overhead"]) / (cnt + 1)
    # arr.append(newData["totalTripFeedbackAverage"])
    # arr.append(newData["feedback"])
    # state["feedback"]=max(arr,key=arr.count)
    state["avgFeedback"] = (state["avgFeedback"] * cnt + newData["feedback"]) / (cnt + 1)
        
    state["count"] = cnt + 1

    # if(sample_size)
    # if(state["avgFeedback"]>3.8):
    #     state["feedback"] = 5
    # if(3.6<=state["avgFeedback"]<=3.8):
    #     state["feedback"] = random.randint(4,5)
    # if(3.55<state["avgFeedback"]<3.6):
    #     state["feedback"] = random.randint(3,4)
    # if(3.4<state["avgFeedback"]<=3.55):
    #     state["feedback"] = random.randint(2,4)
    # if(3.2<state["avgFeedback"]<=3.4):
    #     state["feedback"] = random.randint(2,3)
    # if(state["avgFeedback"]<=3.2):
    #     state["feedback"] = random.randint(1,2)
    # return state

    if(state["avgFeedback"]>3.0):
        state["feedback"] = 5
    if(2.8<state["avgFeedback"]<=3.0):
        state["feedback"] = random.randint(4,5)
    if(2.6<state["avgFeedback"]<=2.8):
        state["feedback"] = random.randint(3,4)
    if(2.5<state["avgFeedback"]<=2.6):
        # if(feedbackStarProvider(arr)>=4):
        if(newData["feedback"]>=4):
            state["feedback"] = 4
        # elif(3<=feedbackStarProvider(arr)<4):
        elif(2<newData["feedback"]<4):
            state["feedback"] = 3
        else:
            state["feedback"] = random.randint(2,3)
    if(state["avgFeedback"]<=2.5):
        # if(feedbackStarProvider(arr)>=4):
        if(newData["feedback"]>=4):
            state["feedback"] = 4
        elif(2<=newData["feedback"]<4):
            state["feedback"] = random.randint(2,3)
        else:
            state["feedback"] = random.randint(1,2)
    # if(state["avgFeedback"]<=2):
    #     state["feedback"] = random.randint(1,2)
    return state


primary_data_provider = {
    "type": "kafka_consumer",
    # "kafka_uri": "kafka:9092",
    "kafka_uri": "localhost:9092",
    "topic": "crowd-nav-trips",
    "serializer": "JSON",
    "data_reducer": primary_data_reducer
}

change_provider = {
    "type": "kafka_producer",
    # "kafka_uri": "kafka:9092",
    "kafka_uri": "localhost:9092",
    "topic": "crowd-nav-commands",
    "serializer": "JSON",
}


def evaluator(resultState, wf):
    resultArr=[]
    resultArr.append(resultState["feedback"])
    resultArr.append(resultState["avg_overhead"])
    # print("resultState[avg_overhead] "+resultState["avg_overhead"])
    ############try dict
    # return resultState["feedback"],resultState["avg_overhead"]
    # return str(resultArr)[1:-1]
    return str(resultArr).strip('[]').strip('"')
    # return (', '.join(map(str, resultArr)))

def state_initializer(state, wf):
    state["count"] = 0
    state["avg_overhead"] = 0
    state["feedback"] = 0
    state["avgFeedback"] = 0
    return state
