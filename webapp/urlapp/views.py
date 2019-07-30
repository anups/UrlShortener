from django.shortcuts import render
from .forms import UrlPostForm
from .models import ShorterUrl
from datetime import datetime
import hashlib
# Create your views here.


# ========================================================================================================
# view for inputting original url and saving it to DB
# ========================================================================================================
def url_form(request):
    url_post = None
    if request.method == 'POST':
        url_post_form = UrlPostForm(data=request.POST)
        if url_post_form.is_valid():
            url_post = url_post_form.save(commit=False)
            url_post.expired_at = expiry_timestamp()
            shorter_url_object = ShorterUrl.objects.filter(original_url=url_post.original_url)
            if shorter_url_object.exists():
                url_post = shorter_url_object[0]
            else:
                url_post.save()
                encoded_url(url_post)
    else:
        url_post_form = UrlPostForm()
    return render(request, 'urlapp/url_form.html', {'url_post': url_post,
                                                    'url_post_form': url_post_form})


# ========================================================================================================
# Encoding scheme : MD5 algorithm
# Input  : url_post object --> An instance of UrlPostForm class
# Output : hashed_url which has been stored in DB
# ========================================================================================================
def encoded_url(url_post):
    hashed_url = hashlib.md5(url_post.original_url.encode())
    hashed_url = hashed_url.hexdigest()
    hashed_url = hashed_url[:6] + str(url_post.id)
    url_post.short_url = hashed_url
    url_post.save()


# ========================================================================================================
# Calculation of expiry time
# Currently expiry time has been hardocded with 1 min i.e. 60 sec
# ========================================================================================================
def expiry_timestamp():
    current_timestamp = datetime.now()
    minute = current_timestamp.strftime("%M")
    minute = int(minute) + 1
    hours = current_timestamp.strftime("%H")
    if minute == 60:
        hours = int(hours) + 1
    seconds = current_timestamp.strftime("%S")
    current_timestamp = current_timestamp.strftime("%Y-%m-%d") + " " + str(hours) \
                        + ":" + str(minute) + ":" + str(seconds)
    return current_timestamp
