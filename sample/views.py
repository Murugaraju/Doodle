from django.shortcuts import render
from .forms import *
# Create your views here.
def check(request):
    form=TicketForm()

    if request.method=='POST':
        print(request.POST)
        if int(request.POST['age'])<=5:
            error="You are not allowed to book ticket, age should be above 5"
            form=TicketForm(request.POST)
            return render(request,'error.html',{'error':error,'form':form})
        if int(request.POST['lower'][0]) !=0:
            print("I came",request.POST['gender'])
            if request.POST['gender']=='female':
                child=Children()
                form=TicketForm(request.POST)
                print("I came")
                if request.POST['children']=='yes':
                    temp=0
                    error=''
                    c_ob=Coach.objects.get(coach_name=request.POST['coach_name'])
                    if not c_ob.upper>=int(request.POST['upper']):
                        error=error+'upper is not available'
                        temp+=1
                    if not c_ob.lower>=int(request.POST['lower']):
                        error= error+ 'lower is not available'
                        temp+=1

                    if not c_ob.side>=int(request.POST['side']):
                        error= error + 'side is not available'
                        temp+=1

                    if not c_ob.middle>=int(request.POST['middle']):
                        error= error + 'middle is not available'
                        temp+=1
                    if temp==0:
                        tk=form.save()
                        c_ob.upper-=tk.upper
                        c_ob.lower-=tk.lower
                        c_ob.middle-=tk.middle
                        c_ob.side-=tk.side
                        return render(request,'success.html')
                    else:
                        return render(request,'new_error.html',{'error':error,'form':form,'child':child})


                else:    
                    error="Please fill above text field with either yes or no"
                    return render(request,'new_error.html',{'error':error,'form':form,'child':child})
            else:
                if int(request.POST['age'])>60:
                    temp=0
                    error=''
                    c_ob=Coach.objects.get(coach_name=request.POST['coach_name'])
                    
                    if not c_ob.upper>=int(request.POST['upper']):
                        error=error+'upper is not available'
                        temp+=1
                    if not c_ob.lower>=int(request.POST['lower']):
                        error= error+ 'lower is not available'
                        temp+=1

                    if not c_ob.side>=int(request.POST['side']):
                        error= error + 'side is not available'
                        temp+=1

                    if not c_ob.middle>=int(request.POST['middle']):
                        error= error + 'middle is not available'
                        temp+=1
                    if temp==0:
                        tk=form.save()
                        c_ob.upper-=tk.upper
                        c_ob.lower-=tk.lower
                        c_ob.middle-=tk.middle
                        c_ob.side-=tk.side
                        c_ob.save()
                        return render(request,'success.html')
                    else:
                        return render(request,'new2_error.html',{'error':error,'form':form,'child':child})

                else:
                    error="You are not allowed to book lower tickets, please choose other and try"
                    form=TicketForm(request.POST)
                    return render(request,'new2_error.html',{'error':error,'form':form})
        print("hurray")
        temp=0
        error=''
        form=TicketForm(request.POST)
        c_ob=Coach.objects.get(coach_name=request.POST['coach_name'])
        if not c_ob.upper>=int(request.POST['upper']):
            error=error+'upper is not available'
            temp+=1
        if not c_ob.lower>=int(request.POST['lower']):
            error= error+ 'lower is not available'
            temp+=1

        if not c_ob.side>=int(request.POST['side']):
            error= error + 'side is not available'
            temp+=1

        if not c_ob.middle>=int(request.POST['middle']):
            error= error + 'middle is not available'
            temp+=1
        if temp==0:
            tk=form.save()
            c_ob.upper-=tk.upper
            c_ob.lower-=tk.lower
            c_ob.middle-=tk.middle
            c_ob.side-=tk.side
            c_ob.save()
            return render(request,'success.html',{'tk':tk})
        else:
            return render(request,'new3_error.html',{'error':error,'form':form})

            
    print(request.POST)
    return render(request,'random.html',{'form':form})