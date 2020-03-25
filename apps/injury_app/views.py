from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def process_register(request):
    errors = User.objects.regis_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
        if new_user.id == 1:
            new_user.user_level = "S_Admin"
            new_user.save()
            messages.success(request, "Registered Successfully as S_Admin. Log in to continue.")
            return redirect('/signin')
        elif new_user.id == 2:
            new_user.user_level = "Admin"
            new_user.save()
            messages.success(request, "Registered Successfully as Admin. Log in to continue.")
            return redirect('/signin')
        else:
            messages.error(request, "Please speak with admin for login information.")
            return redirect('/signin')
            
def signin(request):
    return render(request, 'signin.html')

def process_signin(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user'] = user.id
            return redirect('/dashboard')
        else:
            messages.error(request, "Wrong password")
            return redirect('/signin')
    else:
        messages.error(request, "Email not registered")
        return redirect('/signin')

def main(request):
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        athletes = Athlete.objects.all().order_by('ath_last_name')
        context = {
            'user' : user,
            'athletes' : athletes,
        }
        print(User.objects.get(id=request.session['user']).user_level)
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/')

def add_athlete(request):
    user = User.objects.get(id=request.session['user'])
    if user.user_level != 'coach':
        user = User.objects.get(id=request.session['user'])
        sports = Athlete.SPORT_CHOICES
        injuries = Athlete.INJURY_CHOICES
        context = {
            'user' : user,
            'sports' : sports,
            'injuries' : injuries,
        }
        return render(request, 'add_athlete.html', context)
    else:
        return redirect('/dashboard')

def process_athlete(request):
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        errors = Athlete.objects.ath_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_athlete')
        else:
            ath_first_name = request.POST['ath_first_name']
            ath_last_name = request.POST['ath_last_name']
            sport = request.POST['sport']
            injury = request.POST['injury']
            desc = request.POST['desc']
            inj_date = request.POST['inj_date']
            poss_return = request.POST['poss_return']
            new_athlete = Athlete.objects.create(ath_first_name=ath_first_name, ath_last_name=ath_last_name, sport=sport, injury=injury, desc=desc, inj_date=inj_date, poss_return=poss_return)
            return redirect('/dashboard')
    else:
        return redirect('/')

def athlete(request, id):
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        athlete = Athlete.objects.get(id=id)
        context = {
            'user' : user,
            'athlete' : athlete,
        }
        return render(request, 'athlete_profile.html', context)
    else:
        return redirect('/')

def ath_update(request, id):
    user = User.objects.get(id=request.session['user'])
    if user.user_level != 'coach':
        user = User.objects.get(id=request.session['user'])
        athlete = Athlete.objects.get(id=id)
        context = {
            'user' : user,
            'athlete' : athlete,
        }
        return render(request, 'update_athlete.html', context)
    else:
        return redirect('/dashboard')

def process_ath_update(request, id):
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        athlete = Athlete.objects.get(id=id)
        errors = Athlete.objects.ath_update_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/athlete/{athlete.id}/update')
        else:
            this_athlete = Athlete.objects.get(id=id)
            this_athlete.ath_first_name = request.POST['ath_first_name']
            this_athlete.ath_last_name = request.POST['ath_last_name']
            this_athlete.desc = request.POST['desc']
            this_athlete.poss_return = request.POST['poss_return']
            this_athlete.save()
            return redirect(f'/athlete/{athlete.id}')
    else:
        return redirect('/')

def cleared(request, id):
    if 'user' in request.session:
        this_athlete = Athlete.objects.get(id=id)
        this_athlete.injured = False
        this_athlete.save()
        return redirect('/dashboard')
    else:
        return redirect('/')

def add_user(request):
    user = User.objects.get(id=request.session['user'])
    if user.user_level != 'coach':
        context = {
            'user' : user,
        }
        return render(request, 'add_user.html', context)
    else:
        return redirect('/dashboard')

def process_user(request):
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        errors = User.objects.regis_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/add_user')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
            messages.success(request, "You successfully added a new user.")
            return redirect('/add_user')
    else:
        return redirect('/')

def user(request, id):
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        context = {
            'user' : user,
        }
        return render(request, 'user_profile.html', context)
    else:
        return redirect('/')

def update_user(request, id):
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        errors = User.objects.pass_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/user/{user.id}')
        else:
            user = User.objects.get(id=request.session['user'])
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user.password = pw_hash
            user.save()
            message.success(request, 'Successfully updated your password.')
            return redirect(f'/user/{user.id}')
    else:
        return redirect('/')

def user_admin(request):
    user = User.objects.get(id=request.session['user'])
    if user.user_level != 'coach':
        users = User.objects.all().order_by('last_name')
        context = {
            'user' : user,
            'users' : users,
        }
        return render(request, 'admin_dash.html', context)
    else:
        return redirect('/dashboard')

def update_user_admin(request, id):
    user = User.objects.get(id=request.session['user'])
    if user.user_level != 'coach':
        user1 = User.objects.get(id=id)
        levels = User.USER_LEVEL_CHOICES
        context = {
            'user' : user,
            'user1' : user1,
            'levels' : levels,
        }
        return render(request, 'update_user_admin.html', context)
    else:
        return redirect('/dashboard')

def update_user_admin_process(request, id):
    if 'user' in request.session:
        user1 = User.objects.get(id=id)
        errors = User.objects.pass_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/user/{user1.id}/admin')
        else:
            if 'submit' in request.POST:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                user1.password = pw_hash
                user1.user_level = request.POST['user_level']
                user1.save()
                messages.success(request, 'Successfully updated user.')
                return redirect('/user/admin')
            elif 'delete' in request.POST:
                user1.delete()
                messages.success(request, 'Successfully deleted a user.')
                return redirect('/user/admin')
    else:
        return redirect('/')

def logout(request):
    if 'user' in request.session:
        request.session.clear()
        messages.success(request, "You have successfully signed out")
        return redirect('/signin')
    else:
        return redirect('/')