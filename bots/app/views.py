from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from app.models import Robot


# Create your views here.

def index(request):
    ctx = {
        'robots': Robot.objects.all()
    }
    return render(request, 'app/index.html', context=ctx)


def add_robot(request):
    if request.method == 'POST':
        robot = Robot()
        robot.name = request.POST.get('name')
        robot.description = request.POST.get('description')
        robot.slug = slugify(robot.name)
        robot.save()

    return redirect('index')


def robot_info(request, robot_id):
    robot = get_object_or_404(Robot, id=robot_id)
    ctx = {
        'robot': robot
    }
    return render(request, 'app/robot_info.html', context=ctx)


def edit_robot(request, robot_id):
    robot = get_object_or_404(Robot, id=robot_id)
    if request.method == 'POST':
        robot.name = request.POST.get('name')
        robot.description = request.POST.get('description')
        robot.save()
    return redirect('robot_info', robot_id=robot_id)


def delete_robot(request, robot_id):
    if request.method == 'POST':
        robot = get_object_or_404(Robot, id=robot_id)
        robot.delete()
    return redirect('index')
