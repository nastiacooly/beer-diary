from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import User, Profile, FriendRequest
from diary.models import BeerReview
from .forms import NewUserForm

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
import random

User = get_user_model()

def register_request(request):
    """
    Функция отображения регистрационной формы
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Registration succesful. You are now logged in as {request.user}.")
            return redirect('index')
        messages.error(
            request, 
            "Unsuccessful registration. Invalid information. Please read the requirements carefully and be sure to complete all the required(*) fields."
            )
    
    form = NewUserForm()
    return render(
        request,
        'register.html',
        context={"register_form": form}
    )


@login_required
def profile_view(request):
    """
    Функция отображения профиля пользователя
    """
    user_info = User.objects.get(username=request.user)

    user_reviews_count = BeerReview.objects.filter(creator=request.user).count()
    user_dark_reviews_count = BeerReview.objects.filter(
        creator=request.user
        ).filter(
        beertype__color__exact='d'
        ).count()
    user_light_reviews_count = BeerReview.objects.filter(
        creator=request.user
        ).filter(
        beertype__color__exact='l'
        ).count()


    p = request.user.profile
    you = p.user
    sent_friend_requests = FriendRequest.objects.filter(from_user=you)
    rec_friend_requests = FriendRequest.objects.filter(to_user=you)
    friends = p.friends.all()

    return render(
        request,
        'profile.html',
        context = {
            'user_info': user_info,
            'reviews': user_reviews_count,
            'dark_reviews': user_dark_reviews_count,
            'light_reviews': user_light_reviews_count,
            'friends_list': friends,
            'sent_friend_requests': sent_friend_requests,   
            'rec_friend_requests': rec_friend_requests,
        },
    )


@login_required
def users_list(request):
    """
    Функция отображения списка пользователей (друзья друзей + рандом)
    """
    users = Profile.objects.exclude(user=request.user)
    sent_friend_requests = FriendRequest.objects.filter(from_user=request.user)
    rec_friend_requests = FriendRequest.objects.filter(to_user=request.user)
    sent_to = []
    received = []
    friends = []

    for user in users:
        friend = user.friends.all()
        for f in friend:
            if f in friends:
                friend = friend.exclude(user=f.user)
        friends+=friend

    my_friends = request.user.profile.friends.all()

    for i in my_friends:
        if i in friends:
            friends.remove(i)

    if request.user.profile in friends:
        friends.remove(request.user.profile)

    random_list = random.sample(list(users), min(len(list(users)), 10))

    for r in random_list:
        if r in friends:
            random_list.remove(r)
    friends+=random_list

    for i in my_friends:
        if i in friends:
            friends.remove(i)

    # to remove duplicates if any
    friends = list(dict.fromkeys(friends))

    for se in sent_friend_requests:
        sent_to.append(se.to_user)

    for rec in rec_friend_requests:
        received.append(rec.from_user)

    return render(
        request, 
        "users_list.html", 
        context = {
        'users': friends,
        'sent': sent_to,
        'received': received
        }
    )

@login_required
def send_friend_request(request, id):
    """
    Функция отображения отправления запроса в друзья
    """
    user = get_object_or_404(User, id=id)
    frequest, created = FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=user)
    return HttpResponseRedirect('/users/profile/{}'.format(user.profile.slug))

@login_required
def cancel_friend_request(request, id):
    """
    Функция отображения отмены запроса в друзья
    """
    user = get_object_or_404(User, id=id)
    frequest = FriendRequest.objects.filter(
            from_user=request.user,
            to_user=user).first()
    frequest.delete()
    return HttpResponseRedirect('/users/profile/{}'.format(user.profile.slug))

@login_required
def accept_friend_request(request, id):
    """
    Функция отображения принятия запроса в друзья
    """
    from_user = get_object_or_404(User, id=id)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    user1 = frequest.to_user
    user2 = from_user
    user1.profile.friends.add(user2.profile)
    user2.profile.friends.add(user1.profile)
    if(FriendRequest.objects.filter(from_user=request.user, to_user=from_user).first()):
        request_rev = FriendRequest.objects.filter(from_user=request.user, to_user=from_user).first()
        request_rev.delete()
    frequest.delete()
    return HttpResponseRedirect(reverse('profile'))

@login_required
def delete_friend_request(request, id):
    """
    Функция отображения удаления запроса в друзья
    """
    from_user = get_object_or_404(User, id=id)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    frequest.delete()
    return HttpResponseRedirect(reverse('profile'))

@login_required
def delete_friend(request, id):
    """
    Функция отображения удаления друга
    """
    user_profile = request.user.profile
    friend_profile = get_object_or_404(Profile, user_id=id)
    user_profile.friends.remove(friend_profile)
    friend_profile.friends.remove(user_profile)
    return HttpResponseRedirect(reverse('profile'))

@login_required
def anyuser_profile_view(request, slug):
    """
    Функция отображения профиля другого пользователя
    """
    p = Profile.objects.filter(slug=slug).first()
    u = p.user

    friends = p.friends.all()

    if u == request.user:
        return redirect('profile')

    # is this user our friend
    button_status = 'none'
    if p not in request.user.profile.friends.all():
        button_status = 'not_friend'

        # if we have sent him a friend request
        if len(FriendRequest.objects.filter(
            from_user=request.user).filter(to_user=p.user)) == 1:
                button_status = 'friend_request_sent'

        # if we have recieved a friend request
        if len(FriendRequest.objects.filter(
            from_user=p.user).filter(to_user=request.user)) == 1:
                button_status = 'friend_request_received'

    # for beer reviews statistics
    u_reviews_count = BeerReview.objects.filter(creator=u).count()
    u_dark_reviews_count = BeerReview.objects.filter(
        creator=u
        ).filter(
        beertype__color__exact='d'
        ).count()
    u_light_reviews_count = BeerReview.objects.filter(
        creator=u
        ).filter(
        beertype__color__exact='l'
        ).count()

    return render(
        request, 
        "profile_view.html", 
        context = {
            'u': u,
            'button_status': button_status,
            'friends_list': friends,
            'reviews': u_reviews_count,
            'dark_reviews': u_dark_reviews_count,
            'light_reviews': u_light_reviews_count
        }
    )

@login_required
def search_users(request):
    query = request.GET.get('q')
    object_list = []
    if query:
        object_list = User.objects.filter(username__icontains=query)

        if object_list:
            messages.success(request, f"Found {object_list.count()} user(s)!")
        else:
            messages.error(request, "No such users found!")
        
    return render(
        request, 
        "search_users.html", 
        context ={
            'users': object_list
        }
    )

# Класс для отображения обзоров другого пользователя/друга
class BeerReviewsByOtherUserListView(LoginRequiredMixin, generic.ListView):
    model = BeerReview
    context_object_name = 'beer_reviews_user_list'
    template_name ='user_beerreviews.html'
    paginate_by = 4
    def get_queryset(self):
        return BeerReview.objects.filter(creator__id=self.kwargs['id']).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Other user
        user = User.objects.get(id=self.kwargs['id'])
        context['user'] = user.username

        # Logged in user and his friends
        p = self.request.user.profile
        friends = p.friends.all().values_list('slug', flat=True)
        
        # Set friends status if other user is a friend of a logged in user
        status = ""
        if user.username.lower() in friends:
            status = "friends"

        context['status'] = status
        return context