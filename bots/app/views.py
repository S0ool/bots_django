from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from app.models import Robot, Category, Shop_robots


# Create your views here.

def index(request):
    ctx = {
        'robots': Robot.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'app/index.html', context=ctx)


def add_robot(request):
    if request.method == 'POST':
        robot = Robot()
        robot.name = request.POST.get('name')
        robot.description = request.POST.get('description')
        robot.category = Category.objects.get(id=request.POST.get('category'))

        robot.save()

    return redirect('index')


def robot_info(request, robot_id):
    robot = get_object_or_404(Robot, id=robot_id)
    ctx = {
        'robot': robot,
        'categories': Category.objects.all()
    }
    return render(request, 'app/robot_info.html', context=ctx)


def edit_robot(request, robot_id):
    robot = get_object_or_404(Robot, id=robot_id)
    if request.method == 'POST':
        robot.name = request.POST.get('name')
        robot.description = request.POST.get('description')
        robot.category = Category.objects.get(id=request.POST.get('category'))
        robot.save()
    return redirect('robot_info', robot_id=robot_id)


def delete_robot(request, robot_id):
    if request.method == 'POST':
        robot = get_object_or_404(Robot, id=robot_id)
        robot.delete()
    return redirect('index')


def delete_category(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(Category, id=category_id)
        category.delete()
    return redirect('categories')


def delete_shop(request, shop_id):
    if request.method == 'POST':
        shop = get_object_or_404(Shop_robots, id=shop_id)
        shop.delete()
    return redirect('shops')


def categories(request):
    ctx = {
        'categories': Category.objects.all()
    }
    return render(request, 'app/categories.html', context=ctx)


def shops(request):
    ctx = {
        'shops': Shop_robots.objects.all(),
        'robots': Robot.objects.all()
    }
    return render(request, 'app/shops.html', context=ctx)


def category_info(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    ctx = {
        'category': category,
        'robots': category.robots.all()
    }
    return render(request, 'app/category_info.html', context=ctx)


def shop_info(request, shop_id):
    shop = get_object_or_404(Shop_robots, id=shop_id)
    ctx = {
        'shop': shop,
        'robots': shop.robot.all(),
        'all_robots': Robot.objects.all()
    }
    return render(request, 'app/shop_info.html', context=ctx)


def add_category(request):
    if request.method == 'POST':
        category = Category()
        category.name = request.POST.get('name')
        category.save()
    return redirect('categories')


def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.save()
    return redirect('category_info', category_id=category_id)


def add_shop(request):
    if request.method == "POST":
        robots = request.POST.getlist('robots')
        shop = Shop_robots(name=request.POST.get('name'))
        shop.save()
        for robot_id in robots:
            robot = Robot.objects.get(id=robot_id)
            shop.robot.add(robot)
        shop.save()
    return redirect('/shops')


def edit_shop(request, shop_id):
    shop = get_object_or_404(Shop_robots, id=shop_id)
    if request.method == 'POST':
        shop.name = request.POST.get('name')
        shop.robot.set(request.POST.getlist('robots'))
        shop.save()
    return redirect('shop_info', shop_id=shop.id)
