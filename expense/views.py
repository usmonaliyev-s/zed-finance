from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class DashboardTemplateView(TemplateView):
    template_name = 'dashboard.html'

class BudgetsTemplateView(TemplateView):
    template_name = 'budgets.html'

class AnalyticsTemplateView(TemplateView):
    template_name = 'analytics.html'

class TransactionsTemplateView(TemplateView):
    template_name = 'transactions.html'
