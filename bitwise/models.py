from django.db import models

class CalculationEntry(models.Model):
    input_a = models.FloatField()
    input_b = models.FloatField()
    input_c = models.FloatField()
    input_d = models.FloatField()
    input_e = models.FloatField()
    average = models.FloatField()
    is_average_greater_50 = models.BooleanField()
    positive_count = models.IntegerField()
    is_positive_count_even = models.BooleanField()
    sorted_list_gt_10_str = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entry at {self.timestamp} (Avg: {self.average})"

    class Meta:
        db_table = 'calculation_entries'

