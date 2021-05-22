from django.http import JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


@csrf_exempt    
def items(request):
    if request.method == "POST":
        body = json.loads(request.body)
        sample = []
        valid_entries =0
        invalid_entries =0
        
        for i in body['data']:
            if isinstance(i,int) and i>0:
                valid_entries+=1
                sample.append(i)
                
            else:
                invalid_entries+=1
        minimum = min(sample)
        maximum = max(sample)
        average = sum(sample)/len(sample)
        data = {"valid_entries":valid_entries,"invalid_entries":invalid_entries,"min":minimum,"max":maximum,"average":average}
        return JsonResponse(data,safe=False)
    else:
        data = {"sample data":[1, 4, -1, "hello", "world", 0, 10, 7,6,-1,-4,"Akash",50]}
        return JsonResponse(data,safe=False)

@csrf_exempt
def booking(request):

    with open("api/bookings.json", 'r+') as f:
        data = json.load(f)

        def slotcheck(slot,data):
            if len(data[slot-1]['name']) == 2:
                return False
            else:return True
        def addslot(slot,name,data):
            data[slot-1]['name'].append(name)
            f.seek(0)
            json.dump(data,f)
        
        if request.method == "POST":
            body = json.loads(request.body)
            slot = body["slot"]
            name = body['name']
            if slotcheck(slot,data):
                addslot(slot,name,data)
                return JsonResponse({"status":"confirmed"})
            else:
                return JsonResponse({"status": f"slot full, unable to save booking for {name} in slot {slot}"})
        else:
            return JsonResponse(data,safe=False)

@csrf_exempt
def cancelslot(request):
    with open("api/bookings.json", 'r+') as f:
        data = json.load(f)
        body = json.loads(request.body)
        slot = body["slot"]
        name = body['name']
        def slotcheck(slot,name,data):
            if name in data[slot-1]['name']:
                return True
            else:return False
        if request.method == "POST":
                    if slotcheck(slot,name,data):
                        data[slot-1]["name"].remove(name)
                        f.seek(0)
                        f.truncate(0)
                        json.dump(data,f)
                        return JsonResponse({"status": f"canceled booking for {name} in slot {slot}"})
                    else:
                        return JsonResponse({"status": f"no booking for {name} in slot {slot}"})



@csrf_exempt
def plot(request):
    if request.method == "POST":
        body = json.loads(request.body)
        x = [body['x1'],body['x2'],body['x3'],body['x4']]
        y = [body['y1'],body['y2'],body['y3'],body['y4']]
        sample = x
        x=set(x)
        y=set(y)
        if len(x)<3 and len(y)<3:
            return JsonResponse({"status": f"Success ({sample[0]}, {sample[0]}) ({sample[0]}, {sample[2]}) ({sample[2]}, {sample[0]}) ({sample[1]}, {sample[2]})"})
        else:
            return JsonResponse({"status":"no square formed"})
