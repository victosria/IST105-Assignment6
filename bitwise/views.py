from django.shortcuts import render
from .forms import DataInputForm
from .models import CalculationEntry

def input_view(request):
    result = None
    if request.method == 'POST':
        form = DataInputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            values = [data['a'], data['b'], data['c'], data['d'], data['e']]
            
            average = sum(values) / len(values)
            is_average_greater_50 = average > 50

            positive_count = sum(1 for v in values if v > 0)
            is_positive_count_even = (positive_count & 1) == 0

            sorted_gt_10 = sorted([v for v in values if v > 10])
            sorted_gt_10_str = ', '.join(map(str, sorted_gt_10))

            entry = CalculationEntry.objects.create(
                input_a=data['a'],
                input_b=data['b'],
                input_c=data['c'],
                input_d=data['d'],
                input_e=data['e'],
                average=average,
                is_average_greater_50=is_average_greater_50,
                positive_count=positive_count,
                is_positive_count_even=is_positive_count_even,
                sorted_list_gt_10_str=sorted_gt_10_str
            )
            result = {
                'average': average,
                'is_average_greater_50': is_average_greater_50,
                'positive_count': positive_count,
                'is_positive_count_even': is_positive_count_even,
                'sorted_list_gt_10_str': sorted_gt_10_str
            }
    else:
        form = DataInputForm()
    
    return render(request, 'bitwise/input_form.html', {'form': form, 'result': result})

def list_entries_view(request):
    entries = CalculationEntry.objects.all().order_by('-timestamp')
    return render(request, 'bitwise/all_entries.html', {'entries': entries})
