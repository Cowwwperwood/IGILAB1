from .models import Manufacturer, Vacation, Review, PickupPoint, Coupon, Product, Sale, ClientData, NewsArticle, FAQ, Order
from django.db.models import Sum
import re
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic import DetailView, ListView
from django.urls import reverse
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.timezone import now
from datetime import date


def index(request):
    num_products = Product.objects.all().count()
    num_manufacturers = Manufacturer.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    total_sales = Sale.objects.aggregate(total=Sum('product_price'))['total'] or 0
    return render(
        request,
        'index.html',
        context={
            'num_products': num_products,
            'num_manufacturers': num_manufacturers,
            'num_visits': num_visits,
            'total_sales': total_sales,
        }
    )


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        order_by = self.request.GET.get('order_by', 'price')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset.order_by(order_by)


class PickupPointListView(ListView):
    model = PickupPoint
    template_name = 'onlineshop/pickup_point_list.html'
    context_object_name = 'pickup_points'


class ProductDetailView(generic.DetailView):
    model = Product


def Contacts_view(request):
   return render(request, 'onlineshop/contacts.html')


def Vacation_view(request):
    vacations = Vacation.objects.all()
    return render(request, 'onlineshop/vacation.html', {'vacations': vacations})


def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, 'onlineshop/reviews.html', {'reviews': reviews})


def privacy_policy(request):
    return render(request, 'onlineshop/privacy_policy.html')


def about(request):
    return render(request, 'onlineshop/about.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'onlineshop/product_detail.html'

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        coupon_code = request.POST.get('coupon', '')
        phone_regex = r'^\+375(29|25|33|44)\d{7}$'
        if not re.match(phone_regex, phone):
            return self.render_to_response({'product': product, 'phone_error': 'Пожалуйста, введите корректный номер телефона.'})
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            return self.render_to_response({'product': product, 'email_error': 'Пожалуйста, введите корректный email.'})

        try:
            coupon = Coupon.objects.get(code=coupon_code, is_active=True)
            discounted_price = float(product.price) * (1 - coupon.discount_percent / 100)
            coupon.delete()
        except Coupon.DoesNotExist:
            discounted_price = product.price
        order = Order.objects.create(
            user=request.user,
            product_name=product.name,
            product_price=discounted_price,
            name=name,
            surname=surname,
            phone=phone,
            address=address
        )

        return redirect('order_list')


class OrderListView(ListView):
    model = Order
    template_name = 'onlineshop/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


def mark_as_completed(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return redirect(reverse('orders'))

    if not order.is_completed:
        sale = Sale.objects.create(
            user=order.user,
            sale_date=order.order_date,
            product_name=order.product_name,
            product_price=order.product_price,
            name=order.name,
            surname=order.surname,
            phone=order.phone,
            address=order.address
        )
        order.delete()
    return redirect(reverse('orders'))


def sales_list(request):
    sales = Sale.objects.all()
    return render(request, 'onlineshop/sales.html', {'sales': sales})


class FullOrderListView(ListView):
    model = Order
    template_name = 'onlineshop/orders.html'
    context_object_name = 'orders'


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    pass


class ManufacturerDetailView(generic.DetailView):
    model = Manufacturer
    pass




matplotlib.use('Agg')


def sales_by_hour(request):
    sales = Sale.objects.all().values('sale_date')
    df = pd.DataFrame(sales)
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df['hour'] = df['sale_date'].dt.hour
    sales_per_hour = df.groupby('hour').size()
    fig, ax = plt.subplots()
    sales_per_hour.plot(kind='bar', ax=ax)
    ax.set_xlabel('Время')
    ax.set_ylabel('Количество продаж')
    ax.set_title('Количество продаж в час')
    image_path = os.path.join(settings.BASE_DIR, 'onlineshop', 'static', 'sales_by_hour2.png')
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    plt.savefig(image_path)
    plt.close()
    return render(request, 'onlineshop/sales_by_hour.html', {'graph_url': 'static/images/sales_by_hour.png'})


def news_list(request):
    articles = NewsArticle.objects.all().order_by('-publication_date')
    return render(request, 'onlineshop/news_list.html', {'articles': articles})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'onlineshop/reviews.html', {'reviews': reviews})


@login_required
def add_review(request):
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        text = request.POST.get('text')
        user = request.user
        review = Review.objects.create(user=user, rating=rating, text=text)
        return redirect('review_list')
    else:
        return redirect('review_list')


def faq_list(request):
    faqs = FAQ.objects.all().order_by('-date_added')
    return render(request, 'onlineshop/faq_list.html', {'faqs': faqs})


@login_required
def add_faq(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        FAQ.objects.create(question=question, answer=answer)
        return redirect('faq_list')
    return render(request, 'onlineshop/add_faq.html')


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
@login_required
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.name = request.POST.get('name')
        order.surname = request.POST.get('surname')
        order.phone = request.POST.get('phone')
        order.address = request.POST.get('address')
        order.save()
        return redirect('order_list')  # Перенаправляем на список заказов

    return render(request, 'edit_order.html', {'order': order})


@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user.is_staff:
        order.delete()
        return redirect('orders')
    else:
        return redirect('orders')


@login_required
def user_sales(request):
    user_sales = Sale.objects.filter(user=request.user)
    return render(request, 'onlineshop/user_sales.html', {'user_sales': user_sales})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        date_birthday = request.POST.get('date_birthday')
        phone_regex = r'^\+375(29|25|33|44)\d{7}$'
        if not re.match(phone_regex, phone_number):
            return render(request, 'onlineshop/register.html', {
                'error_message': 'Пожалуйста, введите корректный номер телефона.'
            })
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            return render(request, 'onlineshop/register.html', {
                'error_message': 'Пожалуйста, введите корректный email.'
            })
        if date_birthday:
            user_birthday = date(*map(int, date_birthday.split('-')))
            age = (now().date() - user_birthday).days // 365
            if age < 18:
                return render(request, 'onlineshop/register.html', {
                    'error_message': 'Вам должно быть не менее 18 лет для регистрации.'
                })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        client_data = ClientData(
            user=user,
            address=address,
            phone_number=phone_number,
            date_birthday=user_birthday
        )
        client_data.save()
        login(request, user)
        return redirect('index')

    return render(request, 'onlineshop/register.html')


def coupon_list(request):
    coupons = Coupon.objects.all()
    return render(request, 'onlineshop/coupon_list.html', {'coupons': coupons})