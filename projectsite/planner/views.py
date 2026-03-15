from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import Task, SubTask, Note, Category, Priority
from .forms import TaskForm, SubTaskForm, NoteForm, CategoryForm, PriorityForm

def dashboard(request):

    total_tasks = Task.objects.count()
    in_progress = Task.objects.filter(status="In Progress").count()
    completed = Task.objects.filter(status="Completed").count()
    total_notes = Note.objects.count()

    # recent tasks
    recent_tasks = Task.objects.order_by('-id')[:5]

    # upcoming deadlines
    upcoming_tasks = Task.objects.filter(
    deadline__gte=now(),
    deadline__isnull=False
).order_by('deadline')[:10]

    high_priority = Task.objects.filter(priority__name="High").count()
    medium_priority = Task.objects.filter(priority__name="Medium").count()
    low_priority = Task.objects.filter(priority__name="Low").count()
    critical_priority = Task.objects.filter(priority__name="Critical").count()

    # completion progress
    progress = 0
    if total_tasks > 0:
        progress = int((completed / total_tasks) * 100)

    context = {
        "total_tasks": total_tasks,
        "in_progress": in_progress,
        "completed": completed,
        "total_notes": total_notes,
        "recent_tasks": recent_tasks,
        "upcoming_tasks": upcoming_tasks,
        "progress": progress,
        "critical_priority": critical_priority,
        "high_priority": high_priority,
        "medium_priority": medium_priority,
        "low_priority": low_priority,
    }

    return render(request, "dashboard.html", context)

def category_list(request):

    categories = Category.objects.all()

    search = request.GET.get('search')

    if search:
        categories = categories.filter(name__icontains=search)

    context = {
        'categories': categories
    }

    return render(request, 'category_list.html', context)


def category_create(request):

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("category_list")

    else:
        form = CategoryForm()

    return render(request, "category_form.html", {"form": form})


def category_update(request, id):

    category = get_object_or_404(Category, id=id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect("category_list")

    else:
        form = CategoryForm(instance=category)

    return render(request, "category_form.html", {"form": form})


def category_delete(request, id):

    category = get_object_or_404(Category, id=id)

    category.delete()

    return redirect("category_list")

def priority_list(request):

    priorities = Priority.objects.all()

    search = request.GET.get("search")

    if search:
        priorities = priorities.filter(name__icontains=search)

    context = {
        "priorities": priorities
    }

    return render(request, "priority_list.html", context)

def priority_create(request):

    if request.method == "POST":
        form = PriorityForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("priority_list")

    else:
        form = PriorityForm()

    return render(request, "priority_form.html", {"form": form})


def priority_update(request, id):

    priority = get_object_or_404(Priority, id=id)

    if request.method == "POST":
        form = PriorityForm(request.POST, instance=priority)

        if form.is_valid():
            form.save()
            return redirect("priority_list")

    else:
        form = PriorityForm(instance=priority)

    return render(request, "priority_form.html", {"form": form})


def priority_delete(request, id):

    priority = get_object_or_404(Priority, id=id)

    priority.delete()

    return redirect("priority_list")

def task_list(request):

    tasks = Task.objects.all()

    search = request.GET.get("search", "")
    status = request.GET.get("status", "")
    category = request.GET.get("category", "")
    priority = request.GET.get("priority", "")
    sort = request.GET.get("sort", "")

    # Search
    if search:
        tasks = tasks.filter(title__icontains=search)

    # Status filter
    if status:
        tasks = tasks.filter(status=status)

    # Category filter
    if category:
        tasks = tasks.filter(category_id=category)

    # Priority filter
    if priority:
        tasks = tasks.filter(priority_id=priority)

    # Sorting
    if sort:
        tasks = tasks.order_by(sort)

    context = {
        "tasks": tasks,
        "categories": Category.objects.all(),
        "priorities": Priority.objects.all(),
        "search": search,
        "status": status,
        "category": category,
        "priority": priority,
        "sort": sort,
    }

    return render(request, "task_list.html", context)

def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_view.html", {"task": task})

def task_create(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")

    else:
        form = TaskForm()

    return render(request, "task_form.html", {"form": form})


def task_update(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("task_list")

    else:
        form = TaskForm(instance=task)

    return render(request, "task_form.html", {"form": form})


def task_delete(request, id):

    task = get_object_or_404(Task, id=id)

    task.delete()

    return redirect("task_list")

def subtask_list(request):

    subtasks = SubTask.objects.all()

    search = request.GET.get('search')
    status = request.GET.get('status')
    sort = request.GET.get('sort')

    # Search
    if search:
        subtasks = subtasks.filter(title__icontains=search)

    # Status filter
    if status:
        subtasks = subtasks.filter(status=status)

    # Sorting
    if sort:
        subtasks = subtasks.order_by(sort)

    context = {
        'subtasks': subtasks
    }

    return render(request, 'subtask_list.html', context)

def subtask_view(request, id):

    subtask = get_object_or_404(SubTask, id=id)

    context = {
        "subtask": subtask
    }

    return render(request, "subtask_view.html", context)


def subtask_create(request):

    if request.method == "POST":
        form = SubTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("subtask_list")

    else:
        form = SubTaskForm()

    return render(request, "subtask_form.html", {"form": form})


def subtask_update(request, id):

    subtask = get_object_or_404(SubTask, id=id)

    if request.method == "POST":
        form = SubTaskForm(request.POST, instance=subtask)

        if form.is_valid():
            form.save()
            return redirect("subtask_list")

    else:
        form = SubTaskForm(instance=subtask)

    return render(request, "subtask_form.html", {"form": form})


def subtask_delete(request, id):

    subtask = get_object_or_404(SubTask, id=id)

    subtask.delete()

    return redirect("subtask_list")

def note_list(request):

    notes = Note.objects.all().select_related("task")

    search = request.GET.get("search")
    created = request.GET.get("created_at")

    if search:
        notes = notes.filter(content__icontains=search)

    if created:
        notes = notes.filter(created_at__date=created)

    context = {
        "notes": notes
    }

    return render(request, "note_list.html", context)

def note_view(request, id):
    note = get_object_or_404(Note, id=id)

    return render(request, "note_view.html", {
        "note": note
    })

def note_create(request):

    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("note_list")

    else:
        form = NoteForm()

    return render(request, "note_form.html", {"form": form})


def note_update(request, id):

    note = get_object_or_404(Note, id=id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect("note_list")

    else:
        form = NoteForm(instance=note)

    return render(request, "note_form.html", {"form": form})


def note_delete(request, id):

    note = get_object_or_404(Note, id=id)

    note.delete()

    return redirect("note_list")